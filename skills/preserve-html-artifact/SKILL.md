---
name: preserve-html-artifact
description: Automatically upload new and revised HTML review artifacts to Folio and keep each artifact at one stable URL. Use after generating or changing an HTML artifact, or when asked to preserve one. Private Preview by default; explicit local-only or public instructions take precedence.
---

# Sync HTML artifacts to Folio

Folio is this user's default delivery location for HTML artifacts. The standing
workflow authorizes private uploads and content updates after each completed
revision. Honor explicit instructions such as “local only,” “don't upload,” or
public sharing. This applies to review artifacts, not application source pages
or unrelated files.

## Account

The helper privately loads `~/.config/artifact-library/upload.json` (mode `0600`):

```json
{"url":"https://folio.devexa.net","token":"YOUR_UPLOAD_TOKEN"}
```

Create tokens in **Settings → Upload tokens** after signing in and verifying
email. Use a private secret-input tool or local editor for setup; never request,
print, or inspect tokens in chat. Preserve the existing account configuration.
Agents need no Wrangler, Cloudflare, or Resend credentials. For an isolated
account or local validation, `FOLIO_CONFIG_PATH` can point to another private
configuration file without changing the normal configuration.

## Generate, check, sync

1. Create or revise the HTML using `html-artifact`. Check its layout and relevant
   interactions using the available native browser before delivery.
2. Identify the project and current conversation. Use the repository/project
   name as the category, the stable conversation ID as `--thread`, and a short
   readable conversation title as `--thread-title`. If an ID is unavailable,
   use a stable conversation label; do not invent an ID or mix unrelated threads.
3. Inspect the dedicated artifact folder. Send only the HTML and required
   assets; exclude credentials, source repositories, logs and review evidence.
4. Resolve this skill's installed directory, then run its helper:

```sh
python3 SKILL_DIR/scripts/upload.py /absolute/path/review.html \
  --title 'Design review' --project 'Folio' \
  --thread 'CURRENT_THREAD_ID' --thread-title 'Artifact workflow'
```

For relative assets, add `--root /absolute/path/artifact-folder`. It includes
all non-hidden regular files within that root. Read [the API reference](references/api.md)
for file limits, preview restrictions, direct integrations and errors.

The helper saves `.folio-sync.json` beside the HTML and adds local Git ignore
rules when inside a repository. Keep this manifest through revisions; do not
commit it, delete it to resolve errors, or create a new artifact after every edit.
Use the same working file on subsequent calls. When renaming, move its manifest
with it and pass `--artifact-key` with the original local identity (the original
filename by default). Several artifacts in a thread have separate identities.
The helper infers a project from the current repository and a thread from
`T3_THREAD_ID` or `CODEX_THREAD_ID` when available, but explicit context is preferred.

New artifacts become **private Previews**. Add `--public` only for explicit
public-sharing intent. Subsequent syncs replace content at the same URL and
preserve the owner's title, project, tags, Keep status and sharing choice.
Kept artifacts keep receiving content updates. Agents do not decide which
artifacts deserve to be kept or cleared.

## Deliver and recover

Report the full canonical `url` from the helper in chat, plus whether it was
created, updated or unchanged. Use that Folio URL as the review link. A private
URL requires the owner's login. Never deliver signed asset URLs; they are
short-lived capabilities. Keep local files as the working source.

Sync after each completed, reviewable change, not every keystroke. Unchanged
bundles skip upload. The persistent key and server content hash make retrying
an interrupted sync safe: rerun with the same manifest. Do not claim a hosted
page was updated when sync failed; it still serves the last successful version.

A revision conflict means another agent or the owner changed the content.
Inspect the hosted result and reconcile changes before using `--revision N`
to explicitly accept the current revision. Never automatically override a
conflict or recreate a deleted artifact. An interrupted process can leave an
empty `.folio-sync.lock` directory; verify no uploader is running before
removing that task-owned lock. Preserve the manifest.

Tokens can create artifacts and read/update the sync record identified by its
saved key. They cannot list the library, read private HTML/files, edit metadata,
change sharing/retention, delete artifacts, restore versions, or manage accounts.
Use the owner's authenticated UI for those actions within the user's authorization.
Each sync retains the current content and one previous version; older versions
are removed. The canonical URL remains stable.
