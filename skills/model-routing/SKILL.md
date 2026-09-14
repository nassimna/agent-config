---
name: model-routing
description: Choose models and reasoning effort for substantial agent tasks and bounded subagents, or maintain the shared routing policy as models change. Use before substantial exploration or implementation and when planning delegation; skip trivial tasks that need no delegation decision.
---

# Model Routing

This skill is the shared source of truth for model and effort routing. Honor
explicit user choices and higher-priority runtime constraints. Loading this skill
for task execution does not authorize changing machine configuration.

Keep the lead on `gpt-6-astra` at low effort for requirements, architecture,
difficult diagnosis, integration, and final acceptance; use medium when needed.
Use the current tool's supported controls. Do not switch providers or silently
substitute unavailable models. Tiny tasks can stay with the lead when delegation
would add more cost than value.

## Delegation policy

When the tool supports these models, select both model and effort explicitly:

| Work | Model | Effort |
| --- | --- | --- |
| Repo searches, call sites, existing patterns | gpt-5.6-terra | low |
| Clearly specified coding and focused tests | gpt-5.6-sol | medium |
| Implementation with several interacting behaviors | gpt-5.6-sol | high |
| Repetitive extraction or mechanical transformations | gpt-5.6-luna | low |
| Requirements, architecture, difficult diagnosis, final acceptance | gpt-6-astra | low; medium when needed |

- Use Sol medium as the fallback subagent. On other tools, honor supported
  capabilities; report unavailable routing instead of silently substituting.
- Delegate substantial exploration before loading broad source or logs into
  the lead's context. Distinguish locating code from resolving uncertain logic.
- Give workers a compact, self-contained objective, relevant paths, constraints,
  file ownership, acceptance checks, and escalation conditions. Prefer fresh or
  limited context over full-history forks when supported.
- Return concise findings or changes with file references, checks and results,
  and unresolved decisions. Keep raw search output and full passing logs local.
- The lead verifies critical evidence and the final diff without repeating the
  entire investigation. Reuse a worker for follow-ups on the same scope.
- Keep at most two subagents active by default. Avoid recursive delegation and
  overlapping edits; parallelize only independent work with useful payoff.
- Escalate to the lead when requirements conflict, an important invariant is
  unclear, or a failed attempt has no evidence-backed next step. The lead uses
  Astra medium when needed; do not cycle through every model automatically.
- Validate proportionally and stop repeating passing checks unless new evidence
  warrants it. Preserve all required checks and actual-app validation.
- When evaluating routing, measure total parent/child usage, elapsed time,
  corrections, acceptance, and human review effort. Distinguish requested model
  settings from runtime-verified settings. Do not claim savings without data.

## Runtime configuration

Codex needs matching runtime settings in addition to this policy:

- `~/.codex/config.toml`: root `model` and `model_reasoning_effort` select the
  lead defaults. Under `[agents]`, `default_subagent_model` and
  `default_subagent_reasoning_effort` select the fallback, and
  `max_concurrent_threads_per_session` limits worker concurrency.
- `~/.codex/agents/explorer.toml`: repo exploration row above.
- `~/.codex/agents/worker.toml`: clearly specified coding and focused tests.
- `~/.codex/agents/complex-worker.toml`: interacting implementation.
- `~/.codex/agents/bulk-worker.toml`: mechanical transformations.

Set both model and effort in every role. When spawning directly through a tool,
pass both explicitly; use fresh or limited context if overrides require it.
Model-specific Codex TOML roles are not portable Claude agent definitions.
On other tools, use supported capabilities and disclose unavailable routing.

## Updating this policy

When the user requests a routing update:

1. Verify current model availability and supported effort levels using the
   active runtime and official documentation. Preserve explicitly chosen models.
2. Edit the policy here. Keep model lists out of global AGENTS.md and
   developer-workflow; those files should reference this skill.
3. Apply corresponding model, effort, fallback, and concurrency changes to the
   existing Codex runtime files above. Preserve unrelated settings, role
   permissions, instructions, user changes, and account authentication.
4. Check TOML parsing and the client's effective configuration where exposed.
   Verify configured provider homes still resolve the shared files. Do not
   restart active sessions; state when a fresh session is needed.
5. Report configuration validation separately from runtime inference proof and
   measured cost or quality. Do not launch a broad benchmark by default.

Reading or editing Markdown alone does not synchronize Codex's runtime settings.
These maintenance steps keep the policy and runtime settings aligned when a
routing change is requested.
