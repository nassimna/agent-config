---
name: ai-slop-cleanup
description: Identify and resolve coding AI slop through evidence-based review and scoped simplification. Use for the final cleanup pass of a coding task, or when asked to audit AI slop, remove unnecessary complexity, or simplify a diff. Review requests stay read-only; runtime proof belongs to independent-verification.
---

# AI Slop Cleanup

Find code that adds maintenance cost without serving the requested behavior, or
that looks correct while hiding failures, and replace it with the simplest code
that meets the existing contract. Judge the code, not whether AI wrote it.

## 1. Choose the mode

- **Review / audit / investigate (default):** inspect and report; don't edit.
- **Clean up / simplify:** edit while preserving observable behavior.
- **Fix / resolve:** also repair confirmed in-scope defects against the intended
  contract; name and verify each deliberate behavior change.

When a workflow calls this skill (developer-workflow, file-pr), take
its editing permission, starting revision, owned files or hunks, exclusions, and
finish stage. Simplify within that scope; repair only defects the task covers,
including regressions it introduced; report other behavior changes. Stay inside
the caller's review step; don't start a nested workflow.

## 2. Fix the scope

- Use named files and exclusions literally. Otherwise review the task's own
  changes since its starting revision, including task commits and new files. An
  empty working tree doesn't mean there is nothing to review.
- Exclude pre-existing edits and other authors' changes, even in the same file.
  Without a recorded baseline, reconstruct ownership from task commits and
  session context; leave code of uncertain ownership unchanged and say so.
- Check branch, working tree, and base before choosing a comparison; don't
  invent a base branch. If no target can be inferred, ask.

## 3. Establish the contract

Read the diff, tests, callers, exports, and configuration without widening the
edit scope. Identify inputs, trust boundaries, outputs, errors, side effects,
and compatibility obligations. Before proposing a replacement, look for an
existing helper or library feature and check actual dependency versions; a
plausible method name doesn't prove an API exists.

Read [the pattern catalog](references/patterns.md) for candidates and reasons to
keep suspicious-looking code. Read [the research notes](references/sources.md)
only when explaining the evidence behind this approach.

## 4. Classify each candidate

- **Cleanup:** demonstrated unnecessary complexity.
- **Defect:** behavior contradicts the intended contract.
- **Uncertain:** necessity, behavior, or ownership is unproven; say what
  evidence is missing and leave it.

A finding needs a location; a concrete cost (duplicated policy, needless
indirection, unreachable logic, hidden failure, misleading test); the callers or
invariants that show it is unnecessary or wrong; and the smallest remedy with a
check that proves behavior holds. Rank correctness and hidden failures first.
Style preferences, line counts, and complexity scores are not findings. If
nothing qualifies, say "no actionable slop found."

## 5. Simplify safely

- Prefer deleting redundant logic or reusing an existing implementation. Add no
  frameworks, generic helpers, options, dependencies, or formatting churn; don't
  compress readable code into dense expressions.
- Remove a guard only after proving its invariant holds on every path. Types and
  assertions don't validate network, storage, environment, or user input. Keep
  authorization, tenancy, boundary validation, transactions, cancellation,
  resource cleanup, and required telemetry.
- Delete a symbol only after checking exports, registries, reflection, framework
  discovery, and external consumers; no local callers is not enough for public
  or dynamically loaded code. Leave generated and vendor files out unless
  included.
- In cleanup mode, keep success and failure behavior, call order, async
  semantics, and side effects. Fixing a swallowed error, narrowing a fallback,
  or changing retries is a behavior change: report it and apply it only when the
  request or task covers it. Continue other simplifications meanwhile.

## 6. Verify and report

For each edit, name the behavior that must stay true (output, error identity,
call count and order, async behavior, state, authorization, cleanup) and run a
check that would catch a violation. Never use the implementation as its own
oracle, skip failures, or blanket-update snapshots. Follow developer-workflow's environment
gate before starting services.

Do one pass after focused validation; stop when confirmed in-scope findings
are addressed and checks pass. Reuse the pass while the reviewed code, callers,
and contracts are unchanged; a commit alone doesn't invalidate it.

Add a short cleanup result to the task handoff, in the format in
[the report reference](references/report.md).
