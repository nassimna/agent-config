# Folio agent API

Base origin: `https://folio.devexa.net`. Use a per-user token from **Settings →
Upload tokens**. Keep credentials outside repositories and skills. Send
`Authorization: Bearer YOUR_UPLOAD_TOKEN` from a server-side client; never embed
it in HTML. No Cloudflare credentials are needed for artifact uploads.

## Default workflow

Generate/check → sync a private Preview → return its canonical live URL.
Repeat with the same artifact key after each completed revision. Projects use
`category`; threads use `thread:<stable-id>` and `thread-title:<readable-title>`
tags. Several artifacts may share a thread; each has its own UUID sync key.

The owner chooses **Keep** or **Move to previews**, sharing, restoration, and
cleanup in Folio. Agent content updates preserve all owner metadata and choices.
Kept artifacts continue updating at their original URLs. Existing artifacts from
before this feature remain Kept. New agent artifacts are Previews.

## Authentication and permissions

Tokens can call:

- `GET /api/artifact-sync/:key`: read the small sync record for that user's key.
- `PUT /api/artifact-sync/:key`: create or update content for that user's key.
- `POST /api/artifacts`: legacy creation of a separate artifact on every call.

Keys are UUIDs and scoped by token owner. Tokens cannot list the library, read
private HTML/files, edit metadata, change existing visibility/retention, delete,
restore, invite, or manage accounts/tokens. Those routes require a verified
browser session. For writes, an optional Origin header must exactly match the app origin.
Omit it for server-to-server calls. GET sync lookups do not enforce Origin. Redirects must not forward credentials.

## Stable content sync

Persist a UUID key **before the first request**. Keep it through changes,
renames, retries and resumed work. Do not derive identity from the file contents.

`GET /api/artifact-sync/:key` returns HTTP 200:

```json
{
  "id": "12345678-1234-4234-8234-123456789abc",
  "url": "https://folio.devexa.net/artifacts/12345678-1234-4234-8234-123456789abc",
  "visibility": "private",
  "status": "preview",
  "revision": 1,
  "contentHash": "SHA256_BUNDLE_HASH",
  "project": "Folio",
  "tags": ["thread:THREAD_ID", "thread-title:Artifact workflow"]
}
```

A missing key returns 404. A new key must use expected revision `0`. A known
artifact that was deleted must not be silently recreated.

`PUT /api/artifact-sync/:key` accepts `multipart/form-data`:

| Part | Meaning |
| --- | --- |
| `revision` | Expected integer content revision; 0 for creation. |
| `title` | Required, 1–160 trimmed characters; applied on creation. |
| `description` | Up to 2,000 trimmed characters; applied on creation. |
| `category` | Project name, up to 80 trimmed characters; applied on creation. |
| `tags` | JSON string array; up to 20 tags of 1–100 trimmed characters; applied on creation. |
| `visibility` | `private` by default; `public` only for explicit sharing intent on creation. |
| `entrypoint` | Uploaded relative `.html` or `.htm` path. |
| `paths` | JSON string array aligned with the repeated `files` parts. |
| `files` | Repeated binary parts; up to 100 files and 20 MiB total. |

Send the complete bundle each time, not a patch or ZIP. Whole requests must fit
within 21 MiB. Sync always creates Preview status and preserves existing title,
description, project, tags, retention, and visibility during updates.

Creation returns 201. Updates and exact-content retries return 200 with the same
record shape as GET. Every accepted content change increments `revision` and
updates `updatedAt`; Keep/sharing changes do not count as content revisions.

The server uploads a complete immutable version before atomically changing the
current version. It retains the current version and one previous version for
owner-controlled restoration. Older versions are removed. Relative asset URLs
include the version, and cached page content is keyed by that version.

For hashing, use SHA-256 of UTF-8 JSON with no extra whitespace:
`[entrypoint, [[path, sha256(fileBytes)], ...]]`, in submitted path/file order.
Hash strings use lowercase hex. Only bundle contents and the entrypoint affect
the hash, so owner's metadata changes are preserved. The server computes its
own hash. The uploader skips PUT when the remote hash already matches.

## Retry and conflict handling

Retry an interrupted sync with the **same key and bundle**. If the first attempt
succeeded, GET/hash comparison or the server's duplicate-content check resolves
it without another artifact or revision. A different bundle with a stale
revision returns 409, including a race during upload. Partial/stale uploads do
not replace the live version.

Reconcile conflicting work before explicitly accepting the current revision.
Do not automatically overwrite newer content, discard the manifest, create a
replacement artifact, or claim a failed sync changed the hosted page.

The helper persists `.folio-sync.json` beside the HTML and excludes it locally
from Git. It uses a folder lock to avoid concurrent manifest updates. Pass
`--artifact-key ORIGINAL_IDENTITY` after renaming (the original filename is the
default). `--revision N` explicitly accepts a reconciled remote revision.
`FOLIO_CONFIG_PATH` supports a separate private configuration for isolated tests.

## Legacy creation

`POST /api/artifacts` uses the same multipart fields except `revision`, and
returns `{id,url,visibility,status,revision}` with HTTP 201. It creates a new ID
on every call. Bearer uploads start as Preview; browser uploads may choose Kept.
Do not automatically retry an ambiguous legacy POST; it has no stable key.
Use the sync endpoint for the default agent workflow.

## Paths and previews

Paths must be unique, relative, nonempty and at most 240 characters. No absolute
paths, traversal (`.`/`..`), empty segments, control characters, or
`\\ ? # % " < >`. The entrypoint must occur in `paths` and match an uploaded file.
Folders must contain only the artifact and supporting assets, never credentials,
application source or logs. Prefer bundled relative assets.

HTML runs in an opaque sandbox. Inline JS and HTTPS scripts/styles/images/fonts
can load. API/network requests, forms, nested frames and same-origin access are
blocked. File responses also apply the sandbox policy. Private asset capabilities
expire within 15 minutes, and an old version can become unavailable sooner after
later updates; never share those URLs. Return `/artifacts/:id` instead.

Private canonical URLs ask the owner to sign in. Public URLs work anonymously.
Changing public to private blocks new anonymous asset/page requests even when
content was cached; previously downloaded copies cannot be recalled.

## Owner-only controls

The authenticated browser session can list `GET /api/artifacts`, edit metadata
with `PATCH /api/artifacts/:id`, set retention with
`PATCH /api/artifacts/:id/status` (`{"status":"kept"}` or `preview`), restore
with `POST /api/artifacts/:id/restore` (`{"revision":N}` using the current content
revision), and delete with
`DELETE /api/artifacts/:id`. Metadata PATCH requires a title and defaults omitted
legacy metadata fields; use the dedicated retention endpoint for Keep actions.

Restoration swaps the current and previous content versions and increments the
content revision. It preserves the owner's metadata, sharing and Keep status.

Preview cleanup uses DELETE with `?previewBefore=MILLISECONDS`, limited to the
confirmed selection. The server atomically checks Preview status and last
content-update time when removing the record. Artifacts kept or updated after
the selection are left alone (409). Cleanup never runs automatically.

## Errors

Application errors return `{"error":"message"}`. Provider failures may differ.

| HTTP | Action |
| --- | --- |
| 400 | Correct metadata, paths, expected revision or file count. |
| 401 | Set up a valid token privately, or sign in for owner-only actions. |
| 403 | Correct an untrusted Origin, supply a token when Origin is absent, or refresh expired signed capabilities. |
| 404 | Missing sync key/artifact/file, or another user's private resource. |
| 409 | Reconcile changed/deleted content or a preview kept/updated before cleanup. |
| 413 | Reduce the bundle to fit the file/request limits. |
| 500/timeout | Report failure; retry keyed sync with its unchanged manifest. |

A passing upload response does not prove the artifact's browser interactions.
Verify through the actual viewer with an authorized session before claiming it.
