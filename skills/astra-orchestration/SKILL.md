---
name: astra-orchestration
description: Run a substantial task with GPT-6 Astra as an orchestrator-only lead that plans, briefs cheaper workers, integrates their compact reports, and accepts the result without searching, reading broadly, implementing, or testing itself. Use before substantial exploration or implementation and whenever delegation is being planned; skip questions and one-file edits.
---

# Astra Orchestration

Keep the lead on `gpt-6-astra` at low effort; use medium only when a decision
needs it. The lead's context is the scarce resource. Keep it to decisions,
worker briefs, compact worker reports, and the specific evidence needed for
acceptance. Take models and efforts for workers from the `model-routing` skill
at `~/.agents/skills/model-routing/SKILL.md`; this skill governs behavior.
Honor explicit user choices and higher-priority runtime constraints.

## Delegation gate

Delegate when the task touches several files, modules, or services; needs
repository exploration before editing; needs tests, a browser flow, or an
independent review; or when the user asks for delegation. Then spawn a worker
before doing any of that work; do not simulate delegation.

The lead answers questions and makes decisions directly only from information
already in its context. A single-file edit the lead can specify fully without
reading the repository may go to a worker or be done directly, whichever costs
less. If subagents are unavailable, the lead does the work directly and reports
the reduced separation.

## Lead responsibilities

The lead owns the user's goal, architecture, decomposition, worker briefs,
conflict resolution between findings, integration, final acceptance, and the
report to the user. Workers provide evidence and bounded execution; they never
own direction.

- Route every repository search, file read beyond a few lines, implementation
  step, test run, and browser check to a worker.
- Brief workers with a compact, self-contained objective, relevant paths,
  constraints, file ownership, acceptance checks, and escalation conditions.
  Spawn with `fork_turns: none` so the worker never inherits the lead's
  history; on tools without that control, use the freshest context offered.
- Require every brief to end with: "Return a compact report: short bullets
  with file references, the checks run with their results, and unresolved
  decisions. Do not include raw search output, full file contents, or full
  logs." Raw output stays with the worker.
- Verify through workers: have a worker or an independent reviewer check the
  final diff and rerun critical checks, then read only the evidence needed for
  acceptance. Do not repeat the investigation in the lead.
- Reuse a worker for follow-ups on the same scope instead of re-briefing.
- Keep at most two subagents active by default. Avoid recursive delegation and
  overlapping edits; parallelize only independent work with useful payoff.
- On escalation from a worker (conflicting requirements, an unclear invariant,
  or a failed attempt with no evidence-backed next step), decide from the
  worker's evidence, at medium effort when needed, and send a corrected brief.
  Do not reopen the repository in the lead or cycle through every model.
- Validate proportionally and stop repeating passing checks unless new
  evidence warrants it. Preserve all required checks and actual-app validation.

## Worker selection

Use the roles and the model table from `model-routing`, with these rules:

- Explorer (Terra low) for locating code, call sites, and existing patterns.
- Worker (Sol medium) is the default for clearly specified coding and focused
  tests and the fallback for anything unclassified.
- Complex worker (Sol high) only when the brief names several interacting
  behaviors or the user asks for it. It is an escalation, not a default.
- Bulk worker (Luna low) for repetitive extraction or mechanical
  transformations. The current Codex catalog tags Luna as multi-agent `v1`
  while the lead runs `v2`, so Codex may reject it as a spawned model. If a
  spawn is rejected, run that work on Terra at low effort and report it.
- Never use the `ultra` effort; it enables automatic delegation at maximum
  reasoning. Do not spawn Astra workers unless the user asks.

## Reporting

Report per the global AGENTS.md: what changed, what was tested, and what
remains uncertain. Name which work was delegated and which model and effort
were requested for each worker. Distinguish requested settings from
runtime-verified settings. Measure total parent and child usage when
evaluating this skill; do not claim savings without data.
