---
name: performance-loop
description: Run a measurement-driven performance audit or repeat authorized optimizations against a controlled baseline. Use for performance improvement loops, latency investigations, or bottleneck reviews; use ui-ux-loop for usability and visual design judgments.
---

# Performance Loop

Identify bottlenecks through measurements and verify gains under comparable
conditions. The unit of work is a measured operation, not a speculative rewrite.

## Establish the contract and baseline

- Identify the app/service revision, environment, named pages or operations,
  data/workload, exclusions, and authorized finish stage. Audits are read-only;
  optimize only when requested. Use developer-workflow for code changes and its
  environment gate before starting test or preview services.
- Select metrics that match the complaint: navigation/loading, interaction
  latency, layout shift, request/query latency, resource use, or throughput.
  Use provided targets; otherwise establish a baseline and report opportunities
  without inventing an arbitrary score threshold. Source concerns are hypotheses
  until measured. Do not add a load test to shared services without explicit
  authorization for that workload and target.
- Prefer existing traces, telemetry, tooling, and running services. Fix the
  device/browser, viewport, dataset, workload, cache condition, throttling,
  measurement window, and build mode for comparisons. Record the actual targets.
  Separate cold/warm runs and development/production measurements. Prefer a
  representative production build for local frontend comparisons when available.
  Assign one measurement owner; avoid concurrent audits, builds, or test loads
  affecting the measured target. Do not stop unrelated shared-machine processes.
  For local timings, three comparable runs are initial screening, not proof of
  a gain. Preserve raw samples and report count, median, and spread. When noisy,
  collect more comparable runs within budget and alternate baseline/candidate
  measurements when practical to detect drift. Preserve percentile/window
  definitions for existing production telemetry.
- Use the user's budget; otherwise cap the run at five evaluator rounds.
  Keep a separate task-owned ledger outside the repo or in a verified ignored
  path: contract, baseline/run conditions, bottleneck evidence, changes, results,
  evaluator objections, remaining budget, and next action. Share environment
  identity and resource ownership with UI/UX work, not findings or scores.

## Record coverage explicitly

Use JSON for the ledger. Each required measurement or behavior check records
`id`, `operation`, `criterion`, `status`, `tested_revision`, `conditions`,
`evidence`, and `finding_id`. Start as `untested`; use `passed` for an observed
result satisfying the criterion, `failed` for an evidenced violation linked to
a finding, and `blocked` with the missing capability or authorization. Neither
`blocked` nor `untested` counts as coverage. Preserve original targets and criteria.
Record the build/revision and working diff identity for uncommitted changes;
invalidate affected results after code, workload, or measurement conditions change.

## Measure, isolate, evaluate, repeat

1. Reproduce the slow operation. For web journeys, enter through normal app
   navigation and use the harness's native browser first. Capture available
   performance traces, request waterfalls, or server/query timings. If a tool
   cannot expose the needed measurement, report the limitation and use available
   evidence; do not infer performance from screenshots or code size.
2. Attribute the measured delay to a specific bottleneck before proposing a
   change. Rank opportunities by user impact, measured contribution, and cost
   of change. An audit loops through evidence collection and validation without
   modifying application code or consequential shared state.
3. In authorized optimization mode, change one bottleneck at a time using
   existing infrastructure and contracts. Preserve functionality and freshness;
   faster results obtained by skipping required work are not an improvement.
   Repeat the same operation and comparable measurements, then run affected
   checks. Support claimed gains with traces or attribution evidence showing
   that the identified bottleneck shrank, plus repeated comparable timings.
   A median shift or overlapping ranges alone cannot establish or rule out a
   gain. Investigate noise and drift; if repeat measurements remain inconsistent
   or the apparent gain is small relative to variability, report it inconclusive.
   Do not label three samples statistically conclusive. Investigate regressions
   and retain only changes supported by evidence.
4. When delegation is available and authorized, give a fresh evaluator the
   contract, raw measurements/traces, run conditions, relevant diff, and open
   objections. Have it challenge attribution, comparability, claimed gains,
   and tradeoffs, and reproduce disputed results where permitted. Without an
   independent evaluator, perform a second measurement/review pass and disclose
   the limitation. Update the ledger after each round.
5. Resolve objections or move to the next measured bottleneck. After changes,
   verify the affected user journey still works, including relevant loading,
   error, and data freshness behavior. Use ui-ux-loop for broader experience
   evaluation rather than expanding this loop into a redesign.

## Continue or finish

Check the ledger before handing off. A supported external completion gate should
reject success if required checks are `untested`, `blocked`, lack comparable
current evidence, or have unresolved evaluation objections. An audit may complete
with an evidenced `failed` target linked to an accepted finding; selected
optimization targets and preservation checks must be `passed` before claiming
optimization complete. Without numerical targets, require verified gains on
selected fixes and assessed remaining opportunities. Continue with viable next
actions within budget. If no external gate exists, check these conditions
explicitly and disclose that completion was not enforced by the harness. A skill
alone does not install continuation, stop hooks, or scheduling. Preserve the
ledger across sessions.

Stop incompletely on budget exhaustion, when blockers prevent all remaining
useful authorized work, or after two consecutive rounds with no new evidence or
viable approach. Complete other accessible checks before stopping for a blocker.
Save exact remaining work and do not label stalled or noisy results a success.

Deliver one table of operation/bottleneck, evidence, baseline, result or proposed
fix, run conditions, user-visible tradeoffs, and status. For audits, leave
post-fix results unmeasured. Distinguish local lab results from deployed,
authenticated, real-user, and provider-backed evidence. A local Lighthouse score
or trace does not prove field Core Web Vitals or production capacity. Keep raw
logs/traces local and provide usable supporting evidence in chat.

## Validate changes to this skill

When an app and permitted test target are named, trial the revised skill on an
operation with a known bottleneck and a comparison without that bottleneck.
Keep expected causes separate from the evaluator's initial evidence review.
Check whether the loop attributes the delay, rejects noisy or incomparable
results, and preserves behavior. Refine from observed failures when skill edits
are authorized. Do not introduce load or defects into shared/customer systems.
Without a target, label structural or simulated checks explicitly; they do not
prove bottleneck discovery, verified gains, or production performance.
