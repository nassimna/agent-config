---
name: ai-slop-cleanup
description: Identify and resolve coding AI slop through evidence-based review and scoped simplification. Use when asked to audit or clean up AI slop, remove unnecessary abstractions or defensive code, or simplify an overengineered diff. Preserve required behavior and repository conventions; review requests stay read-only.
---

# AI Slop Cleanup

Find code that increases maintenance cost without serving the requested behavior,
or that creates the appearance of correctness while concealing failures. Replace
confirmed problems with the simplest readable implementation that meets the
existing contract. Assess the code; do not guess whether AI wrote it.

## Choose the mode and scope

- **Review / identify / investigate:** inspect and explain; do not edit files.
- **Clean up / simplify:** make scoped changes that preserve observable behavior.
- **Fix / resolve:** repair confirmed in-scope defects against the intended
  contract. Identify intentional behavior changes and verify them.
- Invoking the skill alone does not authorize edits. Default to review.

Follow named files, exclusions, and finish stage literally. Otherwise start with
the current task's diff, including relevant new files. Check branch, working
tree, and the base before choosing a comparison; do not invent a base branch or
assume all uncommitted changes belong to this task. If no target can be inferred,
ask for it. Read neighboring code and callers to understand the target without
expanding the edit scope. Preserve unrelated work and publication permissions.

When editing, use the available developer-workflow skill and repository checks.
If it is unavailable, apply the understand, plan, implement, validate, and review
steps here without blocking on that dependency.

## Establish the contract before judging the code

Read applicable instructions, the diff, nearby implementations, relevant tests,
callers, exports, and configuration. Identify normal inputs, trust boundaries,
outputs, errors, side effects, and compatibility obligations.

Search for an existing component, helper, or library feature before proposing a
replacement. Inspect actual dependency versions and API contracts when needed;
plausible method names are not evidence that an API exists.

Read [the pattern catalog](references/patterns.md) for candidates and reasons to
keep apparently suspicious code. Read [the research notes](references/sources.md)
when explaining the evidence behind this approach; ordinary cleanup needs no
new web research unless an API or factual claim requires verification.

## Require evidence for each finding

For each candidate, establish:

1. **Location and pattern:** a file and line or symbol, with the relevant shape.
2. **Concrete cost:** duplicated policy, extra indirection, unreachable logic,
   obscured failure, misleading verification, or another demonstrated problem.
3. **Context:** inspected callers or invariants that show why this code is
   unnecessary or incorrect, including any reason it might need to stay.
4. **Smallest remedy and check:** what to change and what proves the required
   behavior still holds.

Prioritize correctness and hidden failures, then maintenance costs. Treat
unproven candidates as questions or leave them unchanged; style preferences,
file counts, line counts, and complexity scores do not establish a defect.
Say that no actionable slop was found when that is the result.

## Simplify without creating new slop

Prefer deleting redundant logic, using an established implementation, or making
an existing function clearer. Keep changes coherent and reviewable. Avoid new
frameworks, generic helpers, knobs, dependencies, and broad formatting churn.
Do not replace understandable code with dense expressions to save lines.

Before removing a guard, prove its invariant is enforced on every relevant path.
Types or assertions alone do not validate network, storage, environment, or user
input. Preserve authorization, tenancy, validation at trust boundaries,
transaction handling, cancellation, resource cleanup, and required telemetry.

Before deleting a symbol, inspect exports, registries, reflection, framework
discovery, external consumers, and documentation as relevant. A text search with
no local callers is insufficient for a public API or dynamically loaded code.
Keep generated and vendor files out unless explicitly included; edit their
source when authorized.

Preserve success and failure behavior, call ordering, async semantics, and side
effects in cleanup mode. Repairing a swallowed error, narrowing a fallback, or
changing retries can change behavior: flag the defect and proposed contract
change, then implement only when the request authorizes that repair. Continue
with independent authorized simplifications while any required decision waits.

## Verify and finish

Use focused existing tests and checks for the affected behavior. Add or adjust a
small number of meaningful tests only where needed. Assert independently known
outputs, errors, or side effects; do not copy the implementation into the test.
Do not remove assertions, skip failures, or blanket-update snapshots to get green.

Exercise the affected normal entry point when practical, including relevant
error and UI states. Follow the environment gate before starting services;
do not provision dependencies or shared infrastructure without authorization.
State exactly what source inspection or isolated tests leave unverified.

Review the final diff against the original contract. Stop when the confirmed
in-scope findings are addressed and relevant checks pass; do not keep hunting
for optional rewrites or chase a deletion percentage.

Report a compact findings/results table when multiple items exist:

| Location | Evidence and cost | Remedy / status | Verification |
| --- | --- | --- | --- |

Include material behavior changes, unresolved candidates, and blocked checks.
For a single small change, a short paragraph is enough. Separate local evidence
from deployed or provider-backed proof.
