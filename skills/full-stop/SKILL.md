---
name: full-stop
description: Carry authorized implementation through a verified PR ready for human review, then stop before merging. Use for a full-stop request or an end-to-end workflow with this finish state; not publish-only work, read-only review or an explicit merge request.
---

# Full Stop

Own the authorized task through a reviewable PR, and leave it open and unmerged.
Use existing scope, repository rules and actual publication/deployment permission;
selecting this skill alone grants none. This is self-contained and does not load
full-send or inherit its merge, force-push or blanket testing permissions.

## Finish state

The final candidate has relevant proof, accepted independent review, passing
required checks, decisive PR evidence, no owned unresolved blocker, and the
required project staging acceptance. Then leave it ready for the user to review.
Never merge, enable auto-merge, enter a merge queue, push directly to the target
branch, bypass protection or delegate those actions. This mode overrides an older
general automatic-merge preference for this task. Inspect task-owned PR auto-merge
and queue state before work/push and handoff; disable/remove automatic merging if
necessary and authorized by this full-stop task. If that cannot be done, hold
publication/readiness rather than risk merging. Preserve unrelated PRs.

## Work to the gate

1. Use developer-workflow for the smallest complete correction. Reproduce the
   reported failure, preserve the requested target branch and public contracts,
   and verify the changed behavior through its normal actual-app entry point.
   Reuse valid unchanged checks and evidence; refresh affected proof after edits.
   Run ai-slop-cleanup on the final owned diff.
2. Use council for independent Claude/GPT source review. Resolve real in-scope
   findings with minimal edits. Complete separately required runtime/independent
   verification; council scores do not replace app, permission or staging proof.
3. Use file-pr to publish or update one focused PR with concise problem/change,
   decisive checks, council outcome and accessible sanitized evidence. Publishing
   needs user/standing task authorization. Respect project draft gates rather
   than opening ready merely to trigger review bots. Do not install or require
   full-send, sol-loop or a second PR-writing skill.
4. Own CI/review follow-through. In T3, the parent handles existing findings,
   registers one watch_pull_request and ends the turn for real events; children
   never watch. On a wake, validate new feedback against source, fix actual scoped
   defects through a bounded job, and refresh affected checks/review/evidence.
   Never poll, add a second watcher, post unchanged status or wait for optional
   bots as though they were required gates. Outside T3, use an existing supported
   event watcher; do not invent a polling loop when no watcher is available.
5. Complete required staging deployment/verification within the existing task
   authorization. If the project requires exact-candidate staging acceptance,
   keep draft until meaningful affected behavior and independent hosted proof
   pass. Never substitute local tests or a healthy endpoint. Performance claims
   require comparable hosted measurements. Keep secrets/customer records private
   while putting decisive sanitized proof in the PR.

When a parent orchestrator uses this skill, it owns the lifecycle and delegates
bounded implementation/review/runtime stages. Children complete only their given
stage and return actual results; they do not recursively invoke council, merge,
watch, edit the canonical ledger or contact the user. A partial child result does
not establish the complete full-stop gate.

## Handoff

Refresh the live head/base/checks/reviews, mergeability and automatic-merge state.
Passing evidence must cover the current behavior diff and relevant base changes.
Mark ready only when the required gates pass. Keep incomplete/failed gates draft;
name the concrete next action and continue authorized work without routine
'continue' prompts. A genuine required human review is waiting for approval, not
an agent failure. Budget expiry or missing proof is not approval.

Unwatch before a terminal handoff or user-only question under current T3 rules.
Record URL, exact head, ready/waiting/blocked result, decisive evidence, review
outcomes, cleanup and material limits. State that the PR remains open/unmerged.
If another actor merged it, report the observed state instead of claiming this
workflow merged it. Maintenance outcomes go to the coordinator's daily digest;
interrupt only under the established urgent/user-only policy.

Adapted from [Theo's tstack full-stop](https://github.com/t3dotgg/tstack/blob/main/skills/full-stop/SKILL.md) and its delivery workflow, with the user's narrower permissions and two-member council.
