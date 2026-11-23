---
name: folio-upload
description: Upload or update an HTML artifact on Folio when the user explicitly asks to send that artifact or revision to Folio.
---

# Folio Upload

Upload the requested artifact as a private Preview by default. Add `--public` only on explicit public-sharing intent. Read [references/folio.md](references/folio.md) for first-time account setup, renames, bundle limits, sync errors and conflicts.

```sh
python3 SKILL_DIR/scripts/upload.py /abs/path/review.html \
  --title 'Design review' --project 'REPO_OR_PROJECT' \
  --thread 'CURRENT_THREAD_ID' --thread-title 'Short thread title'
```

- Pass the project and the stable conversation ID and title; never invent an ID. Add `--root /abs/artifact-folder` for relative assets; the folder holds only the HTML and its assets.
- The helper writes `.folio-sync.json` beside the HTML. Keep it so every revision updates the same URL; never commit or delete it, or create a new artifact per edit.
- Updates preserve the owner's title, project, Keep status and sharing choice. Agents never decide what to keep, clear or share.
- On a revision conflict, never override automatically; follow the reference.
- Report the canonical `url` and whether it was created, updated or unchanged. If sync fails, say so; the hosted page still serves the last successful version. Never share signed asset URLs.
