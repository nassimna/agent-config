# Loop protocol

Shared by `ui-ux-loop` and `performance-loop`. The skill names its unit of work
(journey check or measured operation), its ledger fields, its evaluator focus,
and its report columns; this file covers the rest.

## Budget

Use the user's budget; otherwise cap the run at five evaluator rounds. A round
covers the agreed scope, not one click or one run. Finish earlier when the
completion conditions hold. Don't invent a minimum runtime or finding quota.

## Ledger

- Keep one task-owned JSON ledger outside the repo or in a verified ignored
  path: contract, coverage, findings, evidence, evaluator objections, remaining
  budget, and next action. Keep UI/UX and performance ledgers separate; share
  only environment identity and resource ownership.
- Each required check records `id`, `criterion`, `status`, `tested_revision`,
  `evidence`, and `finding_id`, plus the skill's own fields.
- Start every check as `untested`. Use `passed` only for an observed result
  that meets the criterion, `failed` for an evidenced violation linked to a
  finding, and `blocked` with the missing access, capability, or authorization.
  `blocked` and `untested` never count as coverage.
- Record the build/revision, and the working diff identity when testing
  uncommitted changes. Invalidate affected checks after code, data, workload,
  environment, or measurement conditions change.
- Never weaken criteria or drop checks to reach completion.
- Update the ledger after every round and preserve it across sessions.

## Evaluator step

When a separate agent is available, give a fresh evaluator the contract and the
evidence the skill specifies, have it challenge the results against the
contract, and reproduce disputed results where permitted. It must explain
failures, not just score or praise. On later rounds, carry forward the original
brief, prior findings, responses, and open objections. Without a separate
agent, do an explicit second pass and disclose that it was not independent.
Then resolve objections or move to the next finding.

## Continue or finish

Finish only when every required check has current evidence and no evaluator
objection is open:

- Audit mode: an evidenced `failed` check linked to an accepted finding counts
  as coverage. Finding a defect does not authorize fixing it.
- Fix mode: the selected fixes' checks and preservation checks must be `passed`
  on the final revision.

Otherwise continue with the next viable action within budget. If a harness
completion gate exists, it should reject success on the same conditions; if
not, check them yourself and say completion was not enforced by the harness.
The skill does not install stop hooks or schedulers.

Stop incomplete when the budget runs out, when blockers prevent all remaining
useful work, or after two consecutive rounds with no new evidence or viable
approach. Finish other accessible checks before stopping for a blocker. Report
the reason and exact remaining work; never call stalled, noisy, or partial
results complete, and don't repeat the same failed attempt.

## Report

Deliver one prioritized table with the skill's columns plus status. Include
tested and skipped coverage and evaluation limits. Keep raw logs, traces, and
media local unless publication is requested.
