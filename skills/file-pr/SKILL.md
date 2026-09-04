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
  required migrations. Preserve unrelated changes and keep local evidence,
  reports, screenshots, logs, and audit files out of a code-only PR.
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

## Open the pull request

- Open a non-draft PR unless the user requests a draft.
- Begin the description with the user-visible problem, then briefly explain the
  solution. Do not lead with an implementation inventory.
- Include focused validation, material risks, anything unverified, and linked
  issues when available. Include visual evidence only when requested or required
  by repository rules.
- Do not merge, close, label, assign, or delete the source branch unless the
  user separately asks.

## Verify the remote result

Read the PR back from the hosting service and confirm:

- URL, open state, and draft status
- base and head branches
- title and description
- exact remote file list and commit set
- currently available checks

Correct an in-scope publication mistake when safe; otherwise stop and report
it. Finish with concise bullets containing the PR link, commit, files or scope,
checks run, and any remaining risk.
