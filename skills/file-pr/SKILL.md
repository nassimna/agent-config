---
name: file-pr
description: File a focused pull request from completed local changes. Use when the user asks to file, open, create, or publish a PR; do not use for drafting PR text without publishing it.
---

# File PR

Publish the requested change as a reviewable pull request whose remote contents
match the user's goal exactly.

## Before publishing

- Reuse repository instructions and task notes already in context; load missing
  or changed guidance. Refresh the current branch, worktree, remotes, status,
  and diff against the intended base before publishing.
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
- Reuse passing checks and actual-app evidence while the relevant code,
  configuration, dependencies, runtime, and verification target are unchanged.
  Committing or pushing unchanged content does not invalidate those results.
- When validation is missing, stale, failed, or incomplete, choose and run the
  smallest reliable checks needed to verify the affected behavior. Do not ask
  the user to select routine checks. Respect their test-suite and test-file
  restrictions, preserve required hooks and CI gates, and keep unrelated
  failures separate. Do not introduce broad formatter churn.
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

- Open a non-draft PR unless the user or project requires draft status.
  Honor required staging/evidence gates before promoting a draft.
- Start with the user-visible change in concise, plain language. For a bug,
  describe what went wrong, when it happened, and what happens now. For a
  feature, walk through the normal user journey from entry point to outcome.
  Identify who does each step when the journey spans roles. Include technical
  details that help the reviewer understand the change or a tradeoff.
- Write from the final diff and recorded verification. Follow required
  repository templates and body validators. A simple change can use a short
  opening paragraph and a verification note.
- Describe verification briefly. Say what was checked, where it ran, what
  happened, and what remains unverified or blocked. Include supporting evidence
  and link the issue when available. Attach UI evidence in the body as described
  below.
- Add **Review focus** when a reviewer has a meaningful decision or a risky
  behavior to check, such as permissions, an import, or a migration. Give one
  concrete question or check. Add rollout details when the merge has
  operational consequences.
- Do not merge, close, label, assign, or delete the source branch unless the
  user separately asks.

### Bad and good PR writing

These examples illustrate wording; they are not claims about the current task.
Lead with the effect a reviewer or user can understand. Name implementation
choices only when they explain the fix or a meaningful tradeoff.

**Title — bad:** `fix(catering): map packageNumber into code`

**Title — good:** `fix(catering): restore meal quantities and delivery recording`

**Description — bad:**

> Updated the package projection, adjusted the report action, and added assertions.

**Description — good:**

> Catering reports failed to load for seasons containing packages, preventing staff
> from viewing quantities or recording deliveries. The response now matches the
> existing report contract, so those operations work again.

**Feature journey — good:**

> A guide opens Pilgrim selections and submits a passport number. An admin
> reviews the request, and the guide returns to the same list to see the decision.

**Review focus — good:**

> Can a guide see a pilgrim's details before an admin approves the request?

Keep decisive checks and material limits after that explanation; the example
paragraph alone is not a complete verification receipt. For performance changes,
a title such as `perf(packages): reduce editor loading time` explains the goal.
Include a percentage or timing only when comparable measurements support it.
Never turn an illustrative example into a fabricated result.

## Image and video evidence

- For each changed UI screen or flow, embed actual-app screenshots under
  separate, visible **Desktop** and **Mobile** headings in the PR body.
- When a prior UI exists, show labeled **Before** and **After** screenshots
  under each viewport. Capture the same screen and comparable conditions for
  each pair. For a brand-new screen, include **After** in both sections.
- Show states that demonstrate the change, such as a failed import row with its
  reason or a list with the new statuses. Caption each screenshot with the
  flow and state. Use synthetic records and identify them in the evidence.
  Label simulated behavior.
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
it. For a publish-only request, return the PR link promptly once the remote
contents and required evidence are verified. Report the current CI state;
do not wait for CI completion or start a new CI/review repair cycle solely
because a PR was filed. If the user also requested monitoring, merge readiness,
or a merge, continue that authorized work and follow the environment's watch
instructions. Pending checks must not be described as passing, and required
merge checks must not be bypassed.

Finish with concise bullets containing the PR link, commit, files or scope,
checks performed or reused, and any remaining risk.

PR writing examples adapted from [Theo’s tstack file-pr](https://github.com/t3dotgg/tstack/blob/main/skills/file-pr/SKILL.md); existing local publication and evidence rules remain in force.
