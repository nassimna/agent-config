---
name: astra-orchestration
description: Run a substantial task with GPT-6 Astra as a hands-on lead that reads, edits, and verifies directly at low effort, raises to medium only for hard decisions, and delegates only bounded parallel chunks or long validation runs with one brief and one report. Use before substantial exploration or implementation and whenever delegation is being considered; skip questions and one-file edits.
---

# Astra Orchestration

Keep the lead on `gpt-6-astra` at low effort and let it do the work itself.
Astra solves tasks in the fewest steps and output tokens of any available
model, so its cost is driven by call count, not by output. Every extra call
re-reads the whole context. Raise to medium only for a hard decision, an
ambiguous requirement, or a failed attempt with no evidence-backed next step;
never use xhigh, max, or ultra. Take worker models and efforts from the
`model-routing` skill at `~/.agents/skills/model-routing/SKILL.md`; this skill
governs behavior. Honor explicit user choices and runtime constraints.

## Do the work directly

The lead searches, reads, edits, tests, and checks the browser itself. Read
what the change needs, not the whole repository. Batch related reads and
edits into few calls; avoid one-line probes, sleeps, and polling. Do not
delegate to save tokens: a worker plus the lead's briefing, waiting, and
correction calls costs more than the lead doing the same bounded work.

## Delegation gate

Delegate only when it buys parallelism or frees the lead from a long wait:

- Two or more independent chunks with clear file ownership that can run at
  the same time while the lead continues on its own chunk.
- A long test suite, browser flow, or build that would otherwise leave the
  lead idle, or an independent review of the final diff.
- The user asks for delegation or names a model.

Do not delegate a single sequential task, a search the lead can run in one
command, or any work the lead must then re-read to judge. If subagents are
unavailable, do the work directly and say so.

## One brief, one report

- Brief workers once with a compact, self-contained objective, relevant paths,
  constraints, file ownership, acceptance checks, and escalation conditions.
  Spawn with `fork_turns: none` so the worker never inherits the lead's
  history; on tools without that control, use the freshest context offered.
- End every brief with: "Return a compact report: short bullets with file
  references, the checks run with their results, and unresolved decisions. Do
  not include raw search output, full file contents, or full logs."
- Wait for the report once. Do not send follow-up messages, nudges, or
  clarifications while the worker runs, and do not interrupt a running worker
  to relay a new user message; let it finish, then brief the change as a new
  bounded task or do it directly.
- Keep at most two subagents active. No recursive delegation, no overlapping
  edits, no Astra workers unless the user asks.
- On a worker report that fails acceptance, the lead fixes it directly if the
  fix is bounded; otherwise send one corrected brief. Do not iterate through
  many rounds with the same worker.
- Verify the final diff and critical checks in the lead. Validate
  proportionally and stop repeating passing checks unless new evidence warrants
  it. Preserve all required checks and actual-app validation.

## Worker selection

Use the roles and the model table from `model-routing`:

- Explorer (Terra low) for a broad, parallel repository survey the lead does
  not need to read itself.
- Complex worker (Sol high) for implementation chunks with real logic.
- Worker (Sol medium) for simple, fully specified bounded edits and focused
  test runs, and as the fallback for anything unclassified.
- Do not use Luna. Below max effort it does not solve real tasks, and at max
  it takes several times more steps than Sol, which keeps the lead waiting.
- Never use the `ultra` effort; it enables automatic delegation at maximum
  reasoning.

## Reporting

Report per the global AGENTS.md: what changed, what was tested, and what
remains uncertain. Name which work was delegated and which model and effort
were requested for each worker. Distinguish requested settings from
runtime-verified settings. Measure total parent and child usage when
evaluating this skill; do not claim savings without data.
