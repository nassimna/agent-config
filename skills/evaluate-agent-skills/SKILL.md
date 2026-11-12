---
name: evaluate-agent-skills
description: Evaluate a new or changed agent skill or verification recipe through scoped behavioral trials and observable outcomes. Use for requested skill evaluations, verifier self-checks and substantial workflow changes; structural validation alone is not behavioral proof.
---

# Evaluate Agent Skills

Check whether the skill works on its intended jobs before relying on it broadly.
Preserve the user's scope, test restrictions, browser/model choices and data
boundaries. Evaluation authorizes only the agreed tasks and targets. Relevant
tests follow the user's standing test authorization and explicit task restrictions;
new dependencies, external messages and shared/customer writes need authorization.

## Choose the claim and trial
State the skill/variant, intended behavior, representative tasks, observable
acceptance criteria, permitted targets/actions, trial budget and stopping rule
before running. Inspect current skill sources and existing evidence. Ask only
for missing authorization, not for facts available in the workspace.

Use structural validation for frontmatter/references and discovery. For behavior,
include a realistic success case, a failure or misleading-proof case, and an
applicable authorization boundary. A small first pass is a smoke trial, not a
measured general improvement. Reuse current passing evidence after narrow edits.

For a verification recipe, run its actual launch/readiness/drive/evidence/cleanup
instructions once, verify evidence survives, and challenge an important check
with a known-bad case in isolated task-owned state. Restore the starting state
and confirm legitimate behavior is accepted. Do not create a new project journey
framework or replace the user's existing skill just to evaluate it.

## Compare variants only when comparison is warranted
Keep task inputs, environment, data, model, reasoning effort and tool access
comparable; record unavoidable differences. Separate candidate directories and
resource ownership. Give each candidate the same ordinary request plus its own
skill version, without telling it the expected answer, rubric or other variant.
Use neutral labels for independent judging and keep hidden scoring material
outside candidate-visible directories. If the harness leaks evaluation context,
report limited blinding rather than claiming a blinded study.

Grade final files/state, actual command output and accessible evidence, supported
by tool traces when available. Do not grade skill adherence from self-report
alone. One neutral judge should use the same criteria across variants; the main
agent checks the artifacts and adjudicates disputed findings. A different model
family can reduce shared bias when available; disclose when it is unavailable.
Use repeated trials within budget when estimating reliability, cost or latency.
One pair cannot establish general superiority. No difference or inconclusive is
an acceptable verdict. Never hide failed trials or keep sampling just to win.

## Decide and maintain
Report task-level outcomes, failures, evidence, conditions/model, count, blinding
limits and effort/cost only when actually measured. Separate structural checks,
isolated smoke behavior, comparative results and live production evidence.
Recommend retain/revise/reject/inconclusive without expanding scope. If findings
justify an authorized edit, make the smallest correction and rerun only affected
trials; otherwise leave the skill unchanged and report the recommendation.

Use a short record in existing task notes with the current skill fingerprint,
covered behaviors, result and evidence. Inspect instruction drift, harness failure
and product regression separately; never weaken the target behavior to pass.
Report real regressions separately and clean only resources the trial created.

For pstack adaptations and license, see [sources](references/sources.md).
