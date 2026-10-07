---
name: ui-ux-loop
description: Run repeated, evidence-backed UI and UX evaluations across named user journeys, or verify requested usability fixes. Use when the user requests a UI/UX improvement loop or a systematic experience review; use dogfood for ordinary exploratory bug hunting and performance-loop for measured speed improvements.
---

# UI/UX Loop

Improve confidence in usability through actual-app exploration and independent
evaluation. The unit of work is a user journey, not a screenshot or source file.

## Establish the contract

- Identify the app URL/revision, roles, journeys, exclusions, design references,
  and authorized finish stage from the request. For broad requests, start with
  3–5 important journeys; avoid multiplying every possible state combination.
- Audits and reviews are read-only. Implement only requested fixes. Use the
  developer-workflow skill for code changes and its environment gate before
  starting test or preview services. Follow existing data ownership rules when
  exercising interactions, including during an audit.
- Define observable acceptance criteria per journey before evaluation. Use
  supplied design guidance and existing app patterns for visual judgments.
  Distinguish reproducible defects from UX hypotheses that need user validation.
- Use the user's budget. Otherwise cap the run at five evaluator rounds; a
  round covers the agreed journeys, not one click. Finish earlier when the
  completion criteria are satisfied. Do not invent a minimum runtime or bug quota.
- Keep a task-owned ledger outside the repo or in a verified ignored path:
  contract, coverage, finding IDs/status, evidence, evaluator objections,
  remaining budget, and next action. Keep it separate from performance findings.

## Record coverage explicitly

Use JSON for the ledger so a harness can inspect completion. Each required check
records `id`, `journey`, `state`, `criterion`, `status`, `tested_revision`,
`evidence`, and `finding_id`. Start checks as `untested`; use `passed` only for
an observed result satisfying the criterion, `failed` for a reproduced violation
linked to a finding, and `blocked` with the missing access or authorization.
Neither `blocked` nor `untested` counts as covered. Record the app build/revision
and the working diff identity when testing uncommitted changes. Invalidate
affected checks after code, relevant data, or environment changes. Preserve the
original criteria; do not weaken them or drop checks to obtain completion.

## Explore, evaluate, repeat

1. Enter the app through normal navigation and attempt the user's actual task.
   Prefer the active harness's native browser. In T3, check preview status and
   open the preview if necessary before selecting a fallback. Reuse an approved
   authenticated session and existing dev stack when available. Assign one
   browser owner and hand it over between exploration and evaluator passes;
   do not drive the same tab concurrently.
2. Check action discoverability, hidden prerequisites, understandable labels,
   progress/success feedback, recovery, and preservation of user input. Cover
   relevant mobile/desktop, keyboard/focus, loading, empty, error, and language
   states. Record concrete friction: unnecessary steps, repeated input, hidden
   prerequisites, unclear outcomes, and lost work. A polished screen does not
   establish that the task is usable. Agent task timings or preference judgments
   are not measurements of human usability. Mark unavailable states `blocked`
   or `untested` rather than claiming coverage.
3. Reproduce suspected defects and capture minimal steps, expected/actual
   behavior, user impact, role/viewport, and screenshots or runtime evidence.
   Inspect code to explain a demonstrated problem; source inspection alone
   does not establish actual usability. Deduplicate shared causes and separate
   environment failures, defects, and subjective proposals.
4. When delegation is available and authorized, give a fresh evaluator the
   user's task, unchanged acceptance criteria, app access, and supplied design
   references first. Let it exercise the scoped journeys and record its own
   observations before revealing prior findings, coverage, or proposed fixes.
   Then reconcile both passes, share evidence and unresolved objections, and
   exercise disputed or missed interactions. On later review rounds, carry the
   original brief and prior findings, responses, and open objections forward.
   If a reviewer already saw proposed fixes or findings before its first pass,
   use a fresh reviewer for that pass or disclose the loss of independence.
   Use supplied acceptable/problematic UI examples to calibrate judgment. The
   evaluator must explain failures against the contract, not simply assign a
   score or praise the result. Without independent evaluation, perform an
   explicit second pass and disclose that it is not independent.
5. Resolve specific objections in the app and update the ledger. For authorized
   fixes, make the smallest change, run affected checks, and repeat the same
   journey. A finding is resolved only with verification evidence. Preserve
   existing visual conventions unless redesign is within scope. Run a focused
   performance check when a UI change could affect loading or responsiveness;
   move broader optimization work to performance-loop.

## Continue or finish

Before handing off, check the contract and ledger. A supported external
completion gate should reject success if a required check is `untested`,
`blocked`, lacks current evidence, or has unresolved evaluation objections.
In audit mode, an evidenced `failed` check linked to an accepted finding counts
as coverage; discovering a defect does not authorize fixing it. In fix mode,
the selected fixes' acceptance checks must be `passed` on the final revision.
Continue with the next viable action while coverage or objections remain within
budget. If no external gate exists, check the same conditions explicitly and
disclose that completion was not enforced by the harness. Do not claim the skill
installed a stop hook or scheduler. Preserve the ledger across context handoffs.

Require accepted coverage from independent review when available, otherwise the
disclosed second pass. Stop incompletely at the budget limit, when blockers
prevent all remaining useful authorized work, or after two consecutive rounds
without new evidence or a viable new approach. Complete other accessible checks
before stopping for a blocker. Report the reason and exact remaining work;
do not call it complete or repeat the same failed interaction.

Deliver one prioritized table with finding, user impact, evidence, smallest
proposed change, acceptance criteria, and status. Include tested/skipped coverage
and evaluation limitations. Label UX hypotheses and simulations explicitly.
Keep reports and media local unless publication is requested; present usable
evidence in chat through native images or verified links.

## Validate changes to this skill

When a suitable app and permitted test environment are named, trial the revised
skill on a small journey with known defects and an acceptable comparison. Keep
the expected issues separate from the evaluator's first-pass brief. Compare
discovered/missed issues, unsupported findings, and coverage against that record.
Do not seed defects into shared or customer systems. Refine instructions from
observed misses when skill edits are authorized. Without an app target, report
structural or simulated validation as such; it does not prove real-app discovery.
