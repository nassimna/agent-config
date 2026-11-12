---
name: developer-workflow
description: Enforce the development lifecycle for a coding feature, bug fix, refactor, or migration of any size. Use for code changes; do not use for read-only questions, routine inspection, or documentation-only edits.
---

# Developer Workflow

Every code change passes these gates in order. Scale the effort in each gate to
the change, but do not skip one. If a later gate exposes a problem, return to the
gate that owns it.

## Own the task through its finish line

Select and read the relevant skills yourself as the task reaches their trigger;
the user describes the goal, not the skill sequence. Use current skill discovery
and preserve the user's model/browser choices. Keep clear fixes lightweight.

| Task or stage | Apply when relevant |
| --- | --- |
| Runtime validation | The project's existing verification skill or recipe, plus agent-browser for web journeys |
| Unresolved architecture or product judgment | claude-codex-workflow; new UI/UX uses claude-codex-ui-workflow |
| Performance measurement or optimization | performance-loop |
| Requested fresh check or consequential behavior | independent-verification |
| Recurring evidenced correction | enforce-lessons; investigate before proposing a structural fix |
| Substantial skill change or verifier self-check | evaluate-agent-skills |
| Final task-owned code review | ai-slop-cleanup |
| Explicit PR publication request | file-pr; otherwise stop at the authorized local finish stage |

A skill handoff is an internal step, not a reason to ask the user to pick a skill
or send the next prompt. Delegate a complete job with its goal, relevant skill
references, authorization and checks. Inspect the returned evidence and continue
within scope. Follow the host's event-driven continuation protocol when a child
or PR is running; do not add polling or bypass its required yield.

Carry the work from implementation through affected validation, scoped repairs,
review and cleanup. Reuse valid evidence. Do not stop at a plan, passing build or
worker report when required work remains, or offer to perform the next already
authorized step. If a required check is blocked, complete independent useful
work, then report the exact missing input and resume point without claiming done.
After repeated failures, inspect the cause and change the approach; do not loop
unchanged or relax the finish condition.

## 1. Understand

Exit when you can state the current behavior, the expected behavior, and the
files and contracts the change touches, backed by the code, tests, or running
app.

If a project feature map exists, read its index and only the flow entries needed
for this task before retracing the source. The default index is
`.agents/project-map/README.md`; respect any project-defined map location.
Check relevant claims against current code. For requested map generation or
refresh, use `map-project`; do not regenerate maps on every coding task or edit
them during a read-only review.

Record the starting revision, task-owned files or hunks, exclusions, and any
pre-existing edits affecting them. Keep that ownership record through commits
and resumes so final review includes committed task changes and preserves other
work. A small task can keep the record in its existing plan or handoff.

## 2. Plan

Exit when these are explicit, from the prompt, the code, or the user's global
defaults:

- the finish line: the observable result and the checks that must pass;
- what is out of scope;
- any screenshot, design, chart, log, or error the task describes but didn't
  attach.

Resolve observable facts from the workspace, current access and standing
permissions. Ask in one concise message only for genuinely missing user input
or authorization; batch known blockers where practical. Missing optional detail
uses a conventional reversible default with its reason. New approval needs may
still appear later; never treat silence or elapsed time as permission. Report the
brief and key choices with reasons before substantial work; update it when scope
changes.

For readiness, evidence validity, maintenance and resumption, use
[verification and handoff](references/verification-and-handoff.md) when the task
needs runtime proof, side-effecting setup, delegation or multiple sessions.
Keep the receipt short even for a small change; do not create a separate ledger
unless the existing task notes cannot hold it.

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
Match proof to the surface: UI journey and visible result, real CLI output/exit,
service response, storage read-back or queue state. Verify relevant side effects.
Use `independent-verification` for the global risk triggers or a requested fresh
check. Keep the implementer's evidence available, but do not treat its verdict
as the independent result. Never start a nested verifier from inside a verifier.

## 5. Review

Before completing this gate, run `ai-slop-cleanup` on the final task-owned diff,
including task commits since the recorded start. Pass the task's editing
permission, ownership record, exclusions, and authorized finish stage to it.
Apply its evidence requirements, make the smallest authorized simplifications or
repairs, and rerun affected checks. Keep this pass within the current workflow
and preserve unrelated work. Report the pass and any unresolved findings in the
handoff.

Exit when the final diff has been reviewed for correctness, regressions,
unintended changes, missing validation, security or data-integrity risks, and
code that could be simpler or shorter, and every actionable finding is fixed
and revalidated or explicitly reported.

## 6. Complete

Do not claim completion before gates 1–5 have passed. Follow the global
"How to communicate with me" standard: answer first in plain words, include
material verification evidence, cleanup result and unverified or unresolved
behavior. Name files when they help the user act or were requested. Keep full
checklists and logs in task notes rather than turning them into reply sections.
Preserve required proof and deliverables. Record the exact resume point if work
is incomplete; reuse results only while their relevant inputs remain unchanged.

## Environment gate

Applies whenever the task starts test or preview services, at any stage.

Before starting:

- Check existing containers, including stopped ones, and reuse a compatible
  service. Inspect Compose/project scripts and actual datastore targets first.
  Start task-owned local services or containers under the user's standing local
  validation authorization; preserve pre-existing data and configuration. Report
  missing capabilities; ask only for actions outside that authorization.
- The task has its own database, user, schema, or key prefix inside the shared
  service, and destructive tests or migrations target only that. If isolation
  isn't possible, ask before running.

After testing, including on failure:

- Task-owned temporary databases, users, keys, and processes are removed;
  shared containers and volumes stay running.
- Stop task-owned server process trees and confirm exit and released ports.
  Leave a preview running only when explicitly requested, with its verified URL
  and exact stop command.
- The report lists every resource left running and why.
