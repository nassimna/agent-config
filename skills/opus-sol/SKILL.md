---
name: opus-sol
description: Orchestrate a coding task where Sol Medium implements and tests, Sol Extra High reviews, and you only plan, brief and judge. Use when the user says "opus-sol" or asks for Opus to orchestrate with Sol implementing and reviewing. For Sol review of your own edits, use sol-loop.
---

# opus-sol

You orchestrate; Sol does all repository work. The user normally runs you on
Opus 5.5 Extra High.

| Role | Model | Owns |
|---|---|---|
| Orchestrator (you) | session model | scope, owner questions, briefs, judging findings, final report |
| Implementer | latest Sol, Medium | code, tests, checks, browser validation, screenshots, recordings, cleanup |
| Reviewer | latest Sol, Extra High | independent review and runtime validation, no edits |

- Never edit repo files, run builds or tests, or fix a finding yourself,
  however small. This overrides the T3 rule to fix small review findings
  yourself. Reading code and live state to write briefs is fine.
- Requests for a video, screenshots or a demo of the change also go to an
  implementer delegate.

## 1. Set up

1. Call `orchestrator_capabilities`. Use the latest Sol model unless the user
   names a version. Use the provider instance the user names (for example
   "rize provider" means `codex_rize`); otherwise use the default Codex
   instance and say which. Set effort through the option id it lists (Codex:
   `reasoningEffort`). If Sol or either effort is missing, stop and say so.
2. Read the request, the repo's AGENTS.md files and the code involved. Ask the
   user only decisions that are theirs: product behavior and scope. If they
   asked for proposals or samples first, make them and wait for a pick.
3. Delegates use the thread's checkout (default `isolation`). Put its absolute
   path in every brief.

## 2. Implement

Start a new `delegate_task` with `role: "implementation"`, Sol, effort
`medium`, and a title naming the work. Children get no history, so the brief
holds:

- Goal, done criteria, and behavior before and after.
- Where things stand: checkout path, branch, base commit, uncommitted work to
  build on.
- Owner decisions, numbered.
- Rules: the repo's AGENTS.md files, simplest code, reuse what exists. No
  commit, push or PR unless the user asked.
- Checks to run and the browser journey to verify, including the language,
  mobile and error states that matter. Artifacts go outside the repo.
- Cleanup: test data to restore, servers to stop, ports to confirm free.
- Report: changed files by purpose, checks pass/fail, screenshot paths with
  what each proves, unverified items, risks.

Wait for the completion notice; don't poll. Open every screenshot it reports
before accepting the result. Send missing checks or evidence the brief asked
for back to a new implementer delegate.

## 3. Review

Start a new `delegate_task` every round with `role: "review"`, Sol, effort
`xhigh`. The brief holds:

- Review only: no edits, reverts, commits or PR comments. Artifacts outside
  the repo. Stop any server it starts.
- Checkout, base commit, and the diff: `git diff <base>` plus untracked files.
- What the change must do, numbered, and owner decisions not to flag.
- Run the app and test the risky paths that apply: permissions and tenant
  isolation, existing data and old clients, RTL and translations, mobile.
- Reply format: `VERDICT: APPROVE` or `VERDICT: CHANGES`, then one line per
  finding: `[blocker|important|nit] file:line claim · evidence · smallest fix`,
  then what it ran and what it skipped.

From round 2, add the ledger (each earlier finding `fixed` or
`declined: <reason>`) and ask for those findings and the files the latest fix
report changed only.

## 4. Judge and loop

1. Check every finding against the code. A finding outside the requested
   behavior (another path, a rare case, style) is a nit, whatever its label.
2. Send accepted blockers and importants to a new implementer delegate with
   the finding, its evidence, the smallest fix and the checks to re-run.
   Decline the rest in one line each.
3. Re-review after each fix round. Stop when a review has no open blocker or
   important.
4. If blockers or importants are still open after 3 review rounds on the same
   piece of work, show the user each open item in 2-3 lines and ask whether
   to continue.
5. A failed, interrupted or silent delegate is not approval. Start a new
   delegate once with the same brief; if that fails too, stop and tell the
   user.
6. New scope from the user mid-flow runs the same cycle: implement, then
   review.

## 5. Report

- Lead with the outcome and what changed for the user, with the implementer's
  screenshots or video.
- Checks pass/fail, review rounds and final verdict, declined findings and
  nits, and anything unverified.
- Confirm the delegates stopped the servers they started and freed their
  ports.
