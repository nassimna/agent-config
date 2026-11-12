---
name: enforce-lessons
description: Investigate repeated, evidenced agent mistakes and turn an authorized correction into the smallest enforceable constraint. Use for recurring review failures or repeated corrections, not one-off style preferences or broad unsolicited refactors.
---

# Enforce Lessons

Replace recurring correction effort with an enforceable constraint when the
record supports it. Investigation and recommendation are read-only unless the
user asks for implementation; naming this skill alone does not authorize edits.

## Find a real recurring class
Read only the relevant task history, commits, review comments and source. Count
independent occurrences, not inherited fork messages or several comments about
one incident. Require at least two evidenced occurrences for a recurring class.
For a single incident, report the finding without inventing a universal rule.
Preserve legitimate variants and trust-boundary validation.

For each class, identify the failed invariant, concrete harm, current rule and
any existing enforcer. Check existing checks before proposing new ones. A written
rule is policy, not proof of enforcement. An allegedly repeated rule may already
be enforced; inspect the actual paths and report that instead of adding a layer.

## Choose the smallest constraint
Prefer a boundary, single source of truth or domain structure that removes the
invalid state. Otherwise consider types, an existing lint/runtime guard, or a
small check with an error naming the supported path. Avoid abstractions that add
more indirection than the demonstrated problem warrants. Docs are appropriate
for judgment that cannot be encoded. Do not add duplicate instructions when an
existing rule only needs a concrete example or a corrected trigger.

Implement only within the authorized task. Follow developer-workflow, preserve
other work and ask before new dependencies. Add or update relevant tests and run
focused checks under the user's standing test authorization; respect explicit
task restrictions. Do not commit, publish or modify CI
or shared/customer state merely because upstream does so.

## Prove and report
In isolated task-owned state, show an authorized enforcer rejecting the real
past mistake or a faithful broken variant and accepting legitimate behavior.
Keep temporary probes outside product commits. Never weaken assertions or the
invariant to pass; distinguish a bad model/check from a product defect. If code
changes are not authorized, propose this proof and say it was not run.

Return a compact rule-to-enforcer mapping: class and independent occurrences,
source evidence, chosen level and why a stronger level was unnecessary or did
not fit, existing/proposed enforcer, rejection/acceptance evidence and limits.
Keep it in the existing task record. Persist only durable, authorized guidance
in the project's source of truth; do not append a global rule for every incident.

For pstack adaptations and license, see [sources](references/sources.md).
