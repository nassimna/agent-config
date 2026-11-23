---
name: performance-loop
description: Run a measurement-driven performance audit or repeat requested optimizations against a controlled baseline. Use for performance improvement loops, latency investigations, or bottleneck reviews; use ui-ux-loop for usability and visual design judgments.
---

# Performance Loop

The unit of work is a measured operation, not a speculative rewrite.

At loop start, read
[../ui-ux-loop/references/loop-protocol.md](../ui-ux-loop/references/loop-protocol.md)
for the budget, ledger, evaluator, finish, and stop rules.

## Set the contract and baseline

- Identify the revision, environment, named pages or operations, data/workload,
  exclusions, and finish stage.
- Pick metrics that match the complaint: loading, interaction latency, layout
  shift, request/query latency, resource use, or throughput. Use given targets;
  otherwise baseline and report opportunities without inventing a score
  threshold. Source concerns are hypotheses until measured. Never load-test a
  shared service without explicit approval for that workload and target.
- Prefer existing traces, telemetry, tooling, and running services. Fix the
  device/browser, viewport, dataset, workload, cache state, throttling, window,
  and build mode; record the actual targets. Separate cold/warm and dev/prod
  runs; prefer a production build for local frontend comparisons. One
  measurement owner; no concurrent builds, audits, or loads on the target.
- Three local runs are screening, not proof. Keep raw samples; report count,
  median, and spread. When noisy, collect more runs within budget and alternate
  baseline/candidate to detect drift. Keep existing telemetry's percentile and
  window definitions.
- Reuse a proven measurement recipe from the project skill or task evidence
  (operation, data prep, timing boundaries, build/cache, repetitions, error and
  work counts); report changed conditions. Never infer a speedup from faster
  failed requests.
- Ledger checks add `operation` and `conditions`.

## Measure, isolate, evaluate, repeat

1. Reproduce the slow operation. For web journeys, enter through normal
   navigation, preferably with `agent-browser`. Capture traces, request
   waterfalls, or server/query timings. If a tool can't expose a measurement,
   say so; never infer performance from screenshots or code size.
2. Attribute the delay to a specific bottleneck before proposing a change. Rank
   by user impact, measured contribution, and cost. Audits don't modify app code
   or shared state.
3. For requested optimizations, change one bottleneck at a time with existing
   infrastructure. Results that skip required work or lose freshness are not
   gains. Repeat the same measurements and run affected checks. A gain needs
   traces or attribution showing the bottleneck shrank plus repeated comparable
   timings; a median shift or overlapping ranges alone prove nothing. Report
   inconsistent or small-versus-noise results as inconclusive; never call three
   samples statistically conclusive. Keep only evidenced changes.
4. Evaluator: give it the contract, raw measurements/traces, run conditions,
   diff, and open objections; have it challenge attribution, comparability,
   claimed gains, and tradeoffs.
5. After changes, verify the affected journey still works, including loading,
   error, and data freshness. Leave broader experience review to ui-ux-loop.

Without numerical targets, completion needs verified gains on selected fixes
and assessed remaining opportunities.

## Report

Table columns: operation/bottleneck, evidence, baseline, result or proposed fix,
run conditions, user-visible tradeoffs, status. Audits leave post-fix results
unmeasured. Separate local lab results from deployed, authenticated, real-user,
and provider-backed evidence; a local Lighthouse score or trace doesn't prove
field Core Web Vitals or production capacity.

To change this skill, see [references/maintenance.md](references/maintenance.md).
