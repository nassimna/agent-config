---
name: developer-workflow
description: Enforce the development lifecycle for a coding feature, bug fix, refactor, or migration of any size, including setup and cleanup of test services. Use for code changes; do not use for read-only questions, routine inspection, or documentation-only edits.
---

# Developer Workflow

## Understand

Identify the current behavior, the expected result, and how to verify it.
If a project map exists (default `.agents/project-map/README.md`), read its
index and the relevant flow entries, then check them against the code.

For substantial work, state the plan, scope, and key choices before editing.
Name the first check that can catch the riskiest regression and what passing
looks like. Run it as soon as that part works and record the observed result.
Fix failures before extending the pattern or building dependent work.

When work spans commits, agents, or sessions, or a file contains someone else's
edits, record the starting revision, task-owned changes, exclusions, and
pre-existing edits in the affected files.

When the task needs runtime proof, side-effecting setup, or several sessions,
read [verification and handoff](references/verification-and-handoff.md).

## Validate

Run the smallest check that can prove the changed behavior works. A focused
test or an isolated probe can cover an internal change. For UI changes, exercise
the affected interaction in the actual app, using agent-browser for web. Inspect
screenshots of the changed state at relevant viewports.

Start at the nearest normal entry point that exercises the change. Include
surrounding steps only when they can expose a regression from the change or the
task or project requires them. When runtime proof is needed for a CLI or service,
run the real command or request and verify the result, including affected stored
data.

Record the observed result and relevant side effects. If a required check is
blocked, say what remains unverified and why.

The implementer's verdict never counts as the `independent-verification`
result, and a verifier never starts another verifier.

## Review

Review the full task-owned diff, including earlier task commits. Check the
result against the requested scope and look for regressions, missing checks,
and security or data-integrity risks. Use `ai-slop-cleanup` when the user asks
or the diff contains duplication or unnecessary complexity worth reviewing.
Fix or report actionable findings and rerun checks affected by any fixes.

Report what changed, how you verified it, and anything still unverified.

## Environment gate

Applies whenever the task starts test or preview services, at any stage.

Before starting:

- List existing containers, including stopped ones, and read the project's
  Compose files and scripts for the services and datastores it expects. Report
  missing capabilities instead of working around them.
- Give the task its own database, user, schema, or key prefix inside the shared
  service, and point destructive tests and migrations only at it. If isolation
  isn't possible, ask before running them.

After testing, including on failure:

- Drop the task's temporary databases, users, and keys; leave shared containers
  and volumes running.
- Stop each task server's whole process tree, not just the parent.
- List every resource left running, and why, in the handoff.
