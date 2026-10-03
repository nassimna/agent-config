---
name: file-pr
description: File a focused pull request from completed local changes. Use when the user asks to file, open, create, or publish a PR; do not use for drafting PR text without publishing it.
---

# File PR

Publish the requested change as a reviewable pull request whose remote contents
match the user's goal exactly.

## Before publishing

- Read the repository instructions and inspect the current branch, worktree,
  remotes, status, and diff against the intended base.
- Check whether a pull request already exists for the branch. Update the
  existing PR instead of creating a duplicate.
- Confirm that the diff contains only the intended implementation, tests, and
  required migrations. Preserve unrelated changes.
- For PRs containing code changes, run `ai-slop-cleanup` on the final task-owned
  diff before committing or pushing, including already committed task changes.
  Pass along the task's editing permission, starting revision, ownership record,
  exclusions, and finish stage. Reuse the `developer-workflow` pass while the
  owned content and relevant callers/contracts are unchanged; committing the
  same content does not require another pass. Review later edits or changed
  invariants and rerun affected checks.
  Fix only confirmed findings within the authorized scope and report unresolved
  ones.
- Never stage, commit, or push screenshots or evidence artifacts (including
  recordings, validation reports, logs, and audit files) into any repository
  unless the user explicitly asks to include those artifacts in the repository.
  A request to file a PR, capture evidence, or attach screenshots does not grant
  that permission. Keep these artifacts outside the repository by default.
- Run the smallest reliable checks for the changed surface. Do not introduce
  broad formatter churn or mislabel an existing baseline failure as a
  regression.
- Inspect staged content for credentials, generated noise, accidental binaries,
  and unrelated files before committing.

## Commit and push

- Follow the repository's commit convention and hooks. Do not bypass a failing
  hook unless the failure is confirmed unrelated, the staged snapshot has been
  verified independently, and bypassing is allowed by the active instructions.
- Write a concise human title that explains why the change matters. Prefer
  `fix(sync): preserve edited room content` over `fix: update files`.
- Push the topic branch without rewriting unrelated remote history. Never push
  directly to a protected integration branch unless explicitly requested.
- Before pushing, inspect the outgoing commit file lists as well as the staged
  diff for unauthorized evidence artifacts. A clean final diff is insufficient
  if earlier outgoing commits contain them. Exclude them from the unpublished
  commits while preserving local copies and unrelated work; if this cannot be
  done safely, stop and report the blocker instead of pushing them.

## Open the pull request

- Open a non-draft PR unless the user requests a draft.
- Begin the description with the user-visible problem, then briefly explain the
  solution. Do not lead with an implementation inventory.
- Include focused validation, material risks, anything unverified, and linked
  issues when available. For UI changes, include image/video attachments in the PR
  body using the requirements below; do not wait for another request for
  screenshots.
- Do not merge, close, label, assign, or delete the source branch unless the
  user separately asks.

## Image and video evidence

- For UI changes, capture the actual app's final state at relevant viewports.
  Include before/after comparisons when useful, and caption each screenshot
  with the flow, state, and viewport shown. Clearly label simulated data.
- Open and inspect every image for readability, correct content, and sensitive
  data before attaching it. Retake blurry, stale, or misleading captures.
- Upload images and videos as GitHub attachments directly in the PR body using
  `gh pr create --attach` or `gh pr edit <pr-url> --attach`. For example:
  `gh pr edit <pr-url> --attach '<screenshot-path>#<alt text>' --attach '<video-path>'`.
  Repeat `--attach` for additional files; do not add alt text to videos.
  Without a body flag, `gh pr edit --attach` preserves the existing body and
  appends the attachments. To position media among captions, pass the complete
  intended description with `--body-file`; local references to attached files
  are rewritten to uploaded asset URLs. Preserve existing relevant PR content.
- Keep captions concise and describe the recorded flow. Do not put evidence in
  a separate comment or commit/push it into the repository. Never use localhost,
  machine-local paths, or Tailscale links as published evidence URLs.
- Check the selected `gh pr` command's help for `--attach` support. If unavailable
  or upload fails, report the exact blocker; do not substitute a repository
  upload. On partial failure, read the PR back and retry only missing attachments.
- Inspect videos as well as images for correct content and sensitive data before
  uploading. Verify the published PR body and rendered attachments are readable
  and accessible to reviewers. Preserve source captures until delivery is
  confirmed, and refresh evidence when later changes make it stale.
- Attachment syntax: https://cli.github.com/manual/gh_pr_edit
- If capture or upload is blocked, state the exact blocker in the PR and handoff
  and mark visual verification incomplete. Do not claim screenshots were added
  or substitute test counts for them.
- For changes with no visual surface, state "Screenshots: not applicable — no UI
  changes" and provide relevant test or source evidence instead of artificial
  screenshots.

## Verify the remote result

Read the PR back from the hosting service and confirm:

- URL, open state, and draft status
- base and head branches
- title and description
- exact remote file list and commit set
- currently available checks
- image/video evidence is attached in the PR body, readable, and accessible to reviewers, or
  explicitly marked blocked or not applicable

Correct an in-scope publication mistake when safe; otherwise stop and report
it. Finish with concise bullets containing the PR link, commit, files or scope,
checks run, and any remaining risk.
