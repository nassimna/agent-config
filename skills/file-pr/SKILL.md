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
  issues when available. Always include a screenshot-evidence section using the
  requirements below; do not wait for another request for screenshots.
- Do not merge, close, label, assign, or delete the source branch unless the
  user separately asks.

## Screenshot evidence

- For UI changes, capture the actual app's final state at relevant viewports.
  Include before/after comparisons when useful, and caption each screenshot
  with the flow, state, and viewport shown. Clearly label simulated data.
- Open and inspect every image for readability, correct content, and sensitive
  data before attaching it. Retake blurry, stale, or misleading captures.
- Upload screenshots as PR attachments or use an approved durable location
  accessible to reviewers, then embed them in the PR description. Never use
  localhost, machine-local paths, or Tailscale links. Attachments are separate
  from repository contents: never commit or push evidence to make it accessible
  without the user's explicit request to include it in the repository.
- Verify the images and links in the published description, and preserve source
  captures until delivery is confirmed. Refresh evidence when later changes
  make it stale.
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
- screenshot evidence is embedded, readable, and accessible to reviewers, or
  explicitly marked blocked or not applicable

Correct an in-scope publication mistake when safe; otherwise stop and report
it. Finish with concise bullets containing the PR link, commit, files or scope,
checks run, and any remaining risk.
