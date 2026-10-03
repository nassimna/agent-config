---
name: developer-workflow
description: Enforce the development lifecycle for a coding feature, bug fix, refactor, or migration of any size. Use for code changes; do not use for read-only questions, routine inspection, or documentation-only edits.
---

# Developer Workflow

Every code change passes these gates in order. Scale the effort in each gate to
the change, but do not skip one. If a later gate exposes a problem, return to the
gate that owns it.

## 1. Understand

Exit when you can state the current behavior, the expected behavior, and the
files and contracts the change touches, backed by the code, tests, or running
app.

## 2. Plan

Exit when the finish line is explicit: the observable result, the checks that
must pass, and what is out of scope.

## 3. Implement

Exit when the change meets the finish line and the diff contains nothing outside
the scope.

## 4. Validate

Exit when:

- the checks for the changed behavior pass; other failures are noted, not
  investigated;
- the affected behavior has been exercised through the actual app or entry
  point;
- for UI changes, final-state screenshots at relevant viewports exist and the
  user can view them. A passing build or test does not replace them.

If a check or capture is blocked, record exactly what remains unverified.

## 5. Review

Before completing this gate, run `ai-slop-cleanup` on the final task-owned diff.
Apply its evidence requirements, make the smallest authorized simplifications or
repairs, and rerun affected checks. Keep this pass within the current workflow
and preserve unrelated work. Report the pass and any unresolved findings in the
handoff.

Exit when the final diff has been reviewed for correctness, regressions,
unintended changes, missing validation, security or data-integrity risks, and
code that could be simpler or shorter, and every actionable finding is fixed
and revalidated or explicitly reported.

## 6. Complete

Do not claim completion before gates 1–5 have passed. The final report starts
with anything needed from the user, then the outcome, files changed, validation
evidence, and anything unverified or unresolved.

## Environment gate

Applies whenever the task starts test or preview services, at any stage.

Before starting:

- Existing containers, including stopped ones, have been checked and a
  compatible one is reused. A missing or incompatible service is reported to the
  user before anything is provisioned.
- Compose files, project scripts, and test tools have been checked so they
  cannot create or recreate containers without the user's permission.
- The task has its own database, user, schema, or key prefix inside the shared
  service, and destructive tests or migrations target only that. If isolation
  isn't possible, ask before running.

After testing, including on failure:

- Task-owned temporary databases, users, keys, and processes are removed;
  shared containers and volumes stay running.
- At most one preview stays running, only when the user needs to review it, and
  the report gives its verified URL and exact stop command.
- The report lists every resource left running and why.
