# Attaching images and videos

## Capture and inspect

- Capture the same screen under comparable conditions for each Before/After
  pair. Use synthetic records and say so in the caption; label simulated
  behavior.
- Open every image and video before uploading. Check readability, correct
  content, and sensitive data. Retake blurry, stale, or misleading captures.

## Upload

- Upload as GitHub attachments in the PR body with `gh pr create --attach` or
  `gh pr edit <pr-url> --attach`, for example:
  `gh pr edit <pr-url> --attach '<screenshot-path>#<alt text>' --attach '<video-path>'`.
  Repeat `--attach` per file; no alt text on videos. Syntax:
  https://cli.github.com/manual/gh_pr_edit
- Without a body flag, `gh pr edit --attach` keeps the existing body and appends
  the attachments. To place media among captions, pass the complete intended
  body with `--body-file`; local references to attached files are rewritten to
  uploaded asset URLs. Preserve existing relevant PR content.
- Check the chosen command's help for `--attach` support. If it's missing or
  upload fails, report the exact blocker; never fall back to committing the
  files. On partial failure, read the PR back and retry only missing files.
- Never put evidence in a separate comment, and never publish localhost,
  machine-local paths, or Tailscale links as evidence URLs.

## After upload

- Confirm the published body renders the attachments readably for reviewers.
- Keep source captures until delivery is confirmed, and refresh evidence when
  later changes make it stale.
