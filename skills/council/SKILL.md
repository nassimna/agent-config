---
name: council
description: Get independent Claude and GPT reviews and reconcile their findings. Use for an explicit council request or a workflow requiring two-model review, not routine checks or publishing an already reviewed PR.
---

# Council

Use exactly two members: one Claude model and one GPT model. Resolve the latest
available suitable flagship in each family from the current model catalog,
respecting named models/accounts and configured provider preferences. When
selecting Sol, default to `gpt-6.2-sol` unless the user requests another version.
Use high reasoning effort where supported. Never substitute a third family. If
a member is unavailable, report the gap; one reply is not a completed council.
Follow the user's same-family quota failover policy without silently changing
models.

## Prepare and delegate

Fix known in-scope defects and run relevant checks before requesting a fresh
review. Freeze the scoped candidate while reviewers read it. Record the intended
base, candidate head/working diff, goal, exclusions and valid proof with its limits.

In T3, resolve capabilities once under current tool rules, then use a new
`delegate_task` for each member and each round. Put effort/settings in
`target.options`, and respect the coordinator's concurrency/resource cap. Run the
two read-only reviews in parallel when capacity permits; otherwise queue them.
Elsewhere use supported native cross-model routing; report unavailable routing.
A delegated child must not spawn reviewers: return the review request to its
parent. Neither reviewer may edit, publish, merge, watch PRs or recruit agents.

Give both members the same self-contained task, exact diff and surrounding
contracts, relevant skills and permitted evidence. Ask each for: APPROVE or
CHANGES, a score out of 10, and evidence-backed findings with stable IDs,
severity, file/line, user impact and a minimal suggested correction. A source
review does not establish actual-app or staging verification.

## Reconcile and bound the loop

Inspect results against source and actual evidence. Accept real defects in scope;
explain rejected or out-of-scope findings rather than fixing every suggestion.
Keep one finding ledger; do not edit the candidate until both reviews stop.

Default maximum: three rounds. First round reviews the full scoped diff; later
rounds review changed behavior and unresolved findings, carrying forward valid
unchanged evidence. Request a fresh delegate for each member whose prior verdict
no longer covers the candidate. Retain a still-valid verdict without inventing a
new score. Do not run another round for rejected nits or wording-only changes.
Stop once both members accept the current behavior diff and no actionable finding
remains. Scores are feedback, not a voting threshold or a substitute for proof.
Budget exhaustion, silence, provider failure or disputed evidence is not approval:
record the exact open issue and stop that gate while independent work continues.

## Record

For a PR, put the useful outcome and actual scores in its description, not a
separate comment. Use actual model names; write `no score` when one was not
provided. For example (illustrative only):

| Member | Round 1 | Round 2 | Current verdict |
| --- | --- | --- | --- |
| Claude | 7/10 | 9/10 | APPROVE |
| GPT | 8/10 | 9/10 | APPROVE |

Distinguish new reviews from carried-forward verdicts, and retain disagreements,
accepted fixes and proof limits in the private receipt. Follow the global concise
reporting rule; a maintenance coordinator includes the outcome in its daily
digest. A council grants no implementation, publication or merge permission.

Adapted from [Theo's tstack council](https://github.com/t3dotgg/tstack/blob/main/skills/council/SKILL.md).
