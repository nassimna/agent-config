---
name: claude-codex-workflow
description: Split work between Claude (exploring ambiguous or open-ended problems, questioning assumptions, comparing options, creative and product judgment, recommending an approach) and Codex (implementing, integrating, verifying, and fixing the agreed approach). Use when the approach is genuinely unresolved and judgment or creativity is central, such as architecture choices, research synthesis, planning, or writing, or when a consequential decision warrants an independent other-model challenge. Not for routine tasks, clear fixes, simple questions, or straightforward implementation; new UI/UX uses claude-codex-ui-workflow.
---

# Claude/Codex Workflow

Neither model is universally better. Claude leads open-ended judgment; Codex
executes the agreed approach because it is substantially cheaper for
production work. Use the split only where it improves the result.

## When it applies

- **Use** when the approach is genuinely unresolved and judgment or creativity
  is central: ambiguous problems, architecture or design choices, research
  synthesis, planning, product decisions, or writing.
- **Skip** routine tasks, clear fixes, factual or simple questions,
  straightforward implementation with no meaningful open approach, and small UI
  adjustments that follow an established pattern. Global Terra routing for
  bounded jobs is unchanged.
- Do not send all diagnosis, research, or architecture work to Claude by
  default. Most diagnosis is evidence work that stays with the executing agent;
  bring in Claude when the open question is one of judgment.
- New UI and UX work uses `claude-codex-ui-workflow`, which specializes this
  skill.

## Roles

- **Claude** frames the problem, questions assumptions, compares options with
  their trade-offs, and recommends one. Ground recommendations in source, docs,
  or evidence where relevant, and mark what is unverified. Ideas beyond the
  original goal are proposals for the user, not work to implement.
- **Codex** implements the agreed approach: frontend and backend production
  code, integration, migrations, infrastructure, evidence gathering,
  verification, and fixes. When evidence shows an assumption is wrong, it
  challenges it instead of obeying blindly, and it reports needed deviations
  instead of silently reinterpreting the brief.
- Claude's recommendation is input, not final authority. Production safety,
  complex implementation and verification judgment, and release decisions stay
  with the originating primary agent, within the user's authorization.
- When the user chooses Claude to author final text, Claude's text is the
  deliverable; do not route it through Codex for rewriting just for role purity.
- No routine approval gate: settle in-scope choices and continue. Ask the user
  only when a decision is genuinely theirs under the global rules.

## Flow

1. Get focused Claude input first: one bounded exploration ending in a
   recommendation. Scale effort to the uncertainty; a narrow question gets a
   short answer, not a full study.
2. Turn the accepted scope and decisions into a bounded brief: goal, scope and
   exclusions, decisions with rationale, relevant files and evidence, owned
   files, authorized actions, and acceptance criteria. The brief is the
   contract; scope changes go back through the originating agent instead of
   drifting.
3. Within authorized design/implementation work, settle consequential observable
   unknowns with a small runnable prototype when useful, preserving the conditions
   and reason for the choice. Keep read-only investigations read-only and avoid
   automatic alternatives for clear routine work.
4. Codex executes and verifies against the brief.
5. The originating agent follows the global communication standard and
   delegation report: integrate the material recommendation, checked evidence,
   decisions and limits into a few plain sentences. Keep the full record in task
   notes and link the child when useful; do not forward its report unchanged.
   The originating agent retains responsibility.

## Independent challenge

- For a consequential or uncertain decision, when useful, ask the other model
  for one read-only challenge. Require concrete evidence or failure cases, not
  preferences.
- The originating agent validates each finding before acting on it; findings
  do not trigger automatic rewrites. Run another round only for new evidence or
  a material change, never on unchanged evidence or as back-and-forth between
  models.
- Ordinary work does not need both models. A design challenge is not a runtime
  verification verdict; use `independent-verification` for fresh behavioral proof
  when the task warrants it.

## Ownership and delegation

- The originating agent owns the end-to-end deliverables, integrated
  acceptance, and the authorized finish stage, whichever provider it runs on.
  On Codex, it delegates the judgment step to Claude; on Claude, it does that
  step itself and delegates execution to Codex.
- In T3 Code, cross-provider work goes through `delegate_task`. Resolve the
  provider, model, and options from the orchestrator capabilities catalog and
  preserve the user's chosen account and model. Use each provider's primary
  model for these steps; Terra Low/Medium stays for the bounded jobs the global
  rules name. On exhausted quota or a rate limit, follow the shared instructions'
  provider failover rule, preserving the requested model and effort. Other
  unavailable routing must be reported; never substitute silently.
- Outside T3, use only a supported cross-provider delegation mechanism;
  otherwise report the limitation.
- Delegate complete tasks. Delegates get no parent history, so the brief must
  stand alone. Keep one owner for each shared file, browser session, and build
  or dev server.

## Boundaries

- Source-only, review, investigation, and question requests stay read-only,
  including Claude's exploration and any challenge. This workflow never
  authorizes implementation, publication, or external state changes beyond the
  request.
- The global rules still govern `agent-browser`, tests, evidence, dependencies,
  publication, and data changes.
