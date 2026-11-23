---
name: ui-ux-loop
description: Run repeated, evidence-backed UI and UX evaluations across named user journeys, or verify requested usability fixes. Use when the user requests a UI/UX improvement loop or a systematic experience review; use dogfood for exploratory bug hunting and performance-loop for measured speed improvements.
---

# UI/UX Loop

The unit of work is a user journey, not a screenshot or source file.

At loop start, read [references/loop-protocol.md](references/loop-protocol.md)
for the budget, ledger, evaluator, finish, and stop rules.

## Set the contract

- Identify the app URL/revision, roles, journeys, exclusions, design references,
  and finish stage. For broad requests, start with 3–5 important journeys;
  don't multiply every state combination.
- Follow existing data ownership rules when exercising interactions, even in
  an audit.
- Define observable acceptance criteria per journey before evaluating. Judge
  visuals against supplied design guidance and existing app patterns. Separate
  reproducible defects from UX hypotheses that need user validation.
- Ledger checks add `journey` and `state`.

## Explore, evaluate, repeat

1. Enter through normal navigation and attempt the user's actual task, using
   `agent-browser` by preference. Reuse an approved signed-in session and the
   existing dev stack. One browser owner at a time; hand it over between
   exploration and evaluator passes.
2. Check discoverability, hidden prerequisites, labels, progress and success
   feedback, recovery, and preservation of input across relevant mobile/desktop,
   keyboard/focus, loading, empty, error, and language states. Record concrete
   friction: extra steps, repeated input, unclear outcomes, lost work. A polished
   screen doesn't prove the task is usable; agent timings and preferences are not
   human usability measurements.
3. Reproduce suspected defects with minimal steps, expected/actual behavior,
   user impact, role/viewport, and screenshots or runtime evidence. Read code to
   explain a demonstrated problem, never as proof of usability. Deduplicate
   shared causes; separate environment failures, defects, and proposals.
4. Evaluator: give it the user's task, unchanged criteria, app access, and
   design references first. It exercises the journeys and records its own
   observations before seeing prior findings, coverage, or proposed fixes; then
   reconcile both passes and exercise disputed or missed interactions. If it saw
   findings or fixes before its first pass, use a fresh one or disclose the lost
   independence. Calibrate with supplied good/bad UI examples.
5. For requested fixes, make the smallest change, run affected checks, and
   repeat the same journey; a finding is resolved only with verification
   evidence. Keep existing visual conventions unless redesign is in scope. Run a
   focused performance check when a change could affect loading or
   responsiveness; leave broader optimization to performance-loop.

For each applicable journey, also verify:

- Defaults match their stated source and stay editable.
- Optional inputs don't block the earliest useful outcome.
- Back navigation, recoverable errors, and login preserve appropriate work.
- Progress and availability reflect actual state.
- Prices disclose billing periods and total commitments.
- Declining, cancelling, or leaving uses clear, neutral actions.

Exercise these interactions; screenshots alone can't prove them. Report
conversion and usability gains as hypotheses unless measured.

## Report

Table columns: finding, user impact, evidence, smallest proposed change,
acceptance criteria, status. Label UX hypotheses and simulations.

To change this skill, see [references/maintenance.md](references/maintenance.md).
