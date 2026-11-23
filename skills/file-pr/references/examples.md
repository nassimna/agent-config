# PR writing examples

These illustrate wording; they are not claims about the current task. Lead with
the effect a reviewer or user can understand. Name implementation choices only
when they explain the fix or a meaningful tradeoff.

**Title — bad:** `fix(catering): map packageNumber into code`

**Title — good:** `fix(catering): restore meal quantities and delivery recording`

**Description — bad:**

> Updated the package projection, adjusted the report action, and added assertions.

**Description — good:**

> Catering reports failed to load for seasons containing packages, preventing staff
> from viewing quantities or recording deliveries. The response now matches the
> existing report contract, so those operations work again.

**Feature journey — good:**

> A guide opens Pilgrim selections and submits a passport number. An admin
> reviews the request, and the guide returns to the same list to see the decision.

**Review focus — good:**

> Can a guide see a pilgrim's details before an admin approves the request?

Keep decisive checks and material limits after that explanation; the example
paragraph alone is not a complete verification receipt. For performance changes,
a title such as `perf(packages): reduce editor loading time` explains the goal.
Include a percentage or timing only when comparable measurements support it.

Adapted from [Theo's tstack file-pr](https://github.com/t3dotgg/tstack/blob/main/skills/file-pr/SKILL.md).
