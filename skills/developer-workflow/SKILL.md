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
When work spans commits, agents, or sessions, or a file contains someone else's
edits, record the starting revision, task-owned changes, exclusions, and
pre-existing edits in the affected files.

When the task needs runtime proof, side-effecting setup, or several sessions,
read [verification and handoff](references/verification-and-handoff.md).

## Validate

Exit when:

- the checks for the changed behavior pass;
- you used the change as the user does, from the normal entry point: open the
  app, sign in, navigate, and act, using agent-browser for web journeys; for a
  CLI, run the real command and check its output and exit code; for a service
  or stored data, send a real request and read back what changed;
- you observed the result, relevant side effects, and relevant loading, empty,
  error, and language states, and wrote what the user sees versus what was
  expected;
- for UI changes, screenshots of the key steps and final state at relevant
  viewports exist and you inspected them.

Passing tests, a build, mocks, or a responding server never replace this. If
the journey is blocked, mark it unverified and say why.

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
