---
name: file-pr
description: File a focused pull request from completed local changes. Use when the user asks to file, open, create, or publish a PR; do not use for drafting PR text without publishing it.
---

# File PR

Publish the requested change as a reviewable pull request whose remote contents
match the user's goal exactly.

## Before publishing

- Refresh the branch, worktree, remotes, status, and diff against the intended
  base. If a PR already exists for the branch, update it instead of opening a
  duplicate.
- Confirm the diff contains only the intended implementation, tests, and
  required migrations.
- For code changes, run `ai-slop-cleanup` on the final task-owned diff before
  committing or pushing; reuse an earlier pass while that content is unchanged.
- Never stage, commit, or push screenshots, recordings, validation reports,
  logs, or audit files unless the user explicitly asks for them in the
  repository. A request to file a PR or attach screenshots is not that request.
- Reuse passing checks and app evidence while the code, configuration,
  dependencies, and target are unchanged; committing or pushing doesn't
  invalidate them. When validation is missing, stale, or failed, run the
  smallest checks that verify the affected behavior. No broad formatter churn.
- Inspect staged content for credentials, generated noise, accidental binaries,
  and unrelated files.

## Commit and push

- Follow the repository's commit convention and hooks. Bypass a failing hook
  only when the failure is confirmed unrelated and the staged snapshot is
  verified another way.
- Write a concise title that says why the change matters:
  `fix(sync): preserve edited room content`, not `fix: update files`.
- Push the topic branch without rewriting unrelated remote history. Never push
  directly to a protected integration branch unless explicitly requested.
- Before pushing, check the file lists of every outgoing commit, not only the
  final diff, for evidence artifacts. Remove them from unpublished commits while
  keeping local copies; if that can't be done safely, stop and report it.

## Open the pull request

Read `references/examples.md` when drafting the title and body.

- Open a non-draft PR unless the user or project requires draft. Honor required
  staging or evidence gates before promoting a draft.
- Lead with the user-visible change in plain language. For a bug: what went
  wrong, when, and what happens now. For a feature: the normal journey from
  entry point to outcome, naming who does each step when roles differ. Add
  technical detail only when it explains the fix or a tradeoff.
- Write from the final diff and recorded verification. Follow required
  repository templates and body validators. A simple change can be a short
  paragraph plus a verification note.
- Verification: what was checked, where, the result, and what remains
  unverified or blocked. Link the issue when available. Never present an
  illustrative example or pending check as a result.
- Add **Review focus** with one concrete question when a reviewer must decide
  something or check risky behavior (permissions, imports, migrations). Add
  rollout notes when merging has operational consequences.
- Do not merge, close, label, assign, or delete the branch unless separately
  asked.

## UI evidence

- For each changed UI screen or flow, embed actual-app screenshots in the PR
  body under **Desktop** and **Mobile** headings, with **Before** and **After**
  pairs when a prior UI exists (**After** only for a new screen). Show the
  states that demonstrate the change and caption each with flow and state.
- Follow `references/media.md` to capture, inspect, and upload images and
  videos.
- If capture or upload is blocked, state the exact blocker in the PR and
  handoff and mark visual verification incomplete. Never claim screenshots were
  added or substitute test counts for them.
- With no visual surface, write "Screenshots: not applicable — no UI changes"
  and give test or source evidence instead.

## Verify the remote result

Read the PR back from the host and confirm:

- URL, open state, and draft status
- base and head branches
- title and description
- exact remote file list and commit set
- currently available checks
- UI evidence attached, readable, and accessible to reviewers, or marked
  blocked or not applicable

Fix an in-scope publication mistake when safe; otherwise stop and report it.
For a publish-only request, return the PR link once contents and evidence are
verified and report the current CI state; don't wait for CI or start a repair
cycle. If monitoring, merge readiness, or a merge was also requested, continue
that work. Never call pending checks passing or bypass required merge checks.

Finish with bullets: PR link, commit, files or scope, checks run or reused, and
remaining risk.
