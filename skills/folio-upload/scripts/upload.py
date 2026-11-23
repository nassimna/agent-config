#!/usr/bin/env python3
"""Sync an HTML artifact to one stable Folio URL without exposing credentials."""
import argparse
import hashlib
import json
import mimetypes
import os
from pathlib import Path
import secrets
import stat
import subprocess
import sys
import urllib.error
import urllib.parse
import urllib.request
import uuid


class NoRedirect(urllib.request.HTTPRedirectHandler):
    def redirect_request(self, req, fp, code, msg, headers, newurl):
        return None


def api_request(config, route, method='GET', body=None, content_type=None):
    headers = {'Authorization': 'Bearer ' + config['token'], 'User-Agent': 'Folio/2.0'}
    if content_type:
        headers['Content-Type'] = content_type
    request = urllib.request.Request(config['url'] + route, data=body, headers=headers, method=method)
    try:
        with urllib.request.build_opener(NoRedirect).open(request, timeout=90) as response:
            return json.load(response)
    except urllib.error.HTTPError as error:
        if method == 'GET' and error.code == 404:
            return None
        try:
            message = json.loads(error.read()).get('error', f'HTTP {error.code}')
        except (ValueError, UnicodeDecodeError):
            message = f'HTTP {error.code}'
        raise ValueError(f'Sync failed (HTTP {error.code}): {message}') from None


def write_manifest(path, value):
    temporary = path.with_name(path.name + '.new')
    temporary.write_text(json.dumps(value, ensure_ascii=False, indent=2) + '\n')
    temporary.replace(path)


def project_name():
    result = subprocess.run(['git', 'config', '--get', 'remote.origin.url'], capture_output=True, text=True)
    remote = result.stdout.strip().rstrip('/')
    return (remote.rsplit('/', 1)[-1].removesuffix('.git') if remote else Path.cwd().name)[:80]


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('html', type=Path)
    parser.add_argument('--root', type=Path)
    parser.add_argument('--title', required=True)
    parser.add_argument('--project', '--category', dest='project')
    parser.add_argument('--description', default='')
    parser.add_argument('--tags', default='')
    parser.add_argument('--thread')
    parser.add_argument('--thread-title')
    parser.add_argument('--artifact-key', help='Persistent local identity; keep this when renaming the HTML file.')
    parser.add_argument('--revision', type=int, help='Accept this remote revision after reviewing a conflict.')
    parser.add_argument('--public', action='store_true', help='Create a public artifact only when explicitly requested.')
    args = parser.parse_args()
    config_path = Path(os.environ.get('FOLIO_CONFIG_PATH', Path.home() / '.config/artifact-library/upload.json'))
    if not config_path.is_file():
        raise ValueError('Configure ~/.config/artifact-library/upload.json with your Folio URL and token first.')
    if stat.S_IMODE(config_path.stat().st_mode) & 0o077:
        raise ValueError('Upload configuration must be private (mode 0600).')
    config = json.loads(config_path.read_text())
    parsed = urllib.parse.urlsplit(config['url'])
    if parsed.scheme != 'https' and not (parsed.scheme == 'http' and parsed.hostname in ('localhost', '127.0.0.1')):
        raise ValueError('Use HTTPS for the Folio URL.')
    if parsed.username or parsed.password or parsed.query or parsed.fragment or parsed.path not in ('', '/'):
        raise ValueError('The Folio URL must be an origin without credentials, path, query or fragment.')
    config['url'] = config['url'].rstrip('/')
    entry = args.html.resolve(strict=True)
    if entry.suffix.lower() not in ('.html', '.htm') or not entry.is_file():
        raise ValueError('Choose an HTML file.')
    root = args.root.resolve(strict=True) if args.root else entry.parent
    entrypoint = entry.relative_to(root).as_posix()
    files = sorted(p for p in root.rglob('*') if p.is_file() and not any(part.startswith('.') for part in p.relative_to(root).parts)) if args.root else [entry]
    if any(p.is_symlink() or not p.resolve().is_relative_to(root) for p in files):
        raise ValueError('Artifact folders must not contain symlinks.')
    paths = [p.relative_to(root).as_posix() for p in files]
    if entrypoint not in paths or not files or len(files) > 100 or sum(p.stat().st_size for p in files) > 20 * 1024 * 1024:
        raise ValueError('Include the HTML entrypoint, at most 100 files, and at most 20 MiB total.')
    if any(any(char in path for char in '\\\r\n\x00?#%"<>') or len(path) > 240 for path in paths):
        raise ValueError('File paths contain unsupported characters or exceed 240 characters.')
    contents = [p.read_bytes() for p in files]
    bundle = [entrypoint, [[path, hashlib.sha256(data).hexdigest()] for path, data in zip(paths, contents)]]
    content_hash = hashlib.sha256(json.dumps(bundle, ensure_ascii=False, separators=(',', ':')).encode()).hexdigest()
    manifest_path = entry.parent / '.folio-sync.json'
    lock = entry.parent / '.folio-sync.lock'
    try:
        lock.mkdir(mode=0o700)
    except FileExistsError:
        raise ValueError('Another sync is running in this folder. Wait for it to finish; inspect any stale .folio-sync.lock before removing it.') from None
    try:
        manifest = json.loads(manifest_path.read_text()) if manifest_path.exists() else {}
        identity = args.artifact_key or entry.name
        artifacts = manifest.setdefault(config['url'], {})
        record = artifacts.get(identity)
        if record is None:
            thread = args.thread or os.environ.get('T3_THREAD_ID') or os.environ.get('CODEX_THREAD_ID')
            if not thread:
                raise ValueError('Pass --thread with the current conversation ID or a stable thread label.')
            tags = [tag.strip() for tag in args.tags.split(',') if tag.strip()]
            tags.append('thread:' + thread)
            if args.thread_title:
                tags.append('thread-title:' + args.thread_title)
            if len(tags) > 20 or any(len(tag) > 100 for tag in tags):
                raise ValueError('Use at most 20 tags with at most 100 characters each, including thread tags.')
            record = {'key': str(uuid.uuid4()), 'revision': 0, 'project': args.project or project_name(), 'tags': list(dict.fromkeys(tags))}
            artifacts[identity] = record
            write_manifest(manifest_path, manifest)
        # Keep the identity outside commits in whichever repository contains the artifact.
        exclude = subprocess.run(['git', '-C', str(entry.parent), 'rev-parse', '--path-format=absolute', '--git-path', 'info/exclude'], text=True, capture_output=True)
        if exclude.returncode == 0:
            path = Path(exclude.stdout.strip())
            rules = path.read_text() if path.exists() else ''
            for rule in ('**/.folio-sync.json', '**/.folio-sync.json.new', '**/.folio-sync.lock/'):
                if rule not in rules.splitlines():
                    with path.open('a') as file:
                        file.write('\n' + rule + '\n')
        route = '/api/artifact-sync/' + record['key']
        remote = api_request(config, route)
        if remote and args.public and remote['visibility'] != 'public':
            raise ValueError('Change availability in Folio before syncing. Updates preserve the existing sharing choice.')
        expected = record['revision'] if args.revision is None else args.revision
        if remote and remote['contentHash'] == content_hash:
            result = remote
            action = 'unchanged'
        else:
            if (remote['revision'] if remote else 0) != expected:
                raise ValueError(f'Remote content changed after your last sync. Review {remote["url"] if remote else "the deleted artifact"}; use --revision only after accepting its current revision. Keep the manifest to preserve identity.')
            boundary = 'folio-' + secrets.token_hex(16)
            fields = {'revision': str(expected), 'visibility': 'public' if args.public else 'private', 'title': args.title, 'description': args.description, 'category': record['project'], 'tags': json.dumps(record['tags'], ensure_ascii=False), 'entrypoint': entrypoint, 'paths': json.dumps(paths, ensure_ascii=False)}
            parts = []
            for name, value in fields.items():
                parts.append(f'--{boundary}\r\nContent-Disposition: form-data; name="{name}"\r\n\r\n{value}\r\n'.encode())
            for path, data in zip(paths, contents):
                mime = mimetypes.guess_type(path)[0] or 'application/octet-stream'
                parts.append(f'--{boundary}\r\nContent-Disposition: form-data; name="files"; filename="{path}"\r\nContent-Type: {mime}\r\n\r\n'.encode() + data + b'\r\n')
            body = b''.join(parts) + f'--{boundary}--\r\n'.encode()
            result = api_request(config, route, 'PUT', body, 'multipart/form-data; boundary=' + boundary)
            action = 'updated' if remote else 'created'
        record.update(revision=result['revision'], id=result['id'], url=result['url'])
        write_manifest(manifest_path, manifest)
        print(json.dumps({**result, 'sync': action}, ensure_ascii=False))
    finally:
        lock.rmdir()


if __name__ == '__main__':
    try:
        main()
    except (ValueError, KeyError, OSError, urllib.error.URLError) as error:
        print(f'Error: {error}', file=sys.stderr)
        sys.exit(1)
