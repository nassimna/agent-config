---
name: independent-verification
description: Independently verify a consequential change or challenge implementation claims using actual runtime evidence. Use for requested fresh verification and high-risk behavior; not routine small fixes, visual design critique or automatic shipping.
---

# Independent Verification

Verify the requested behavior without adopting the author's verdict. Default to
read-only inspection and safe task-owned local execution. A pass is evidence,
not permission to commit, publish, merge, deploy or change customer data.

## Establish independence and scope
The verifier must be a different agent from the implementer. If invoked by the
implementer, delegate one complete verification job through the existing routing
rules. A verifier does the job itself, without recursively spawning verifiers.
If independent routing cannot run, report the limitation and label any self-check
as non-independent; never manufacture a fresh verdict.

Read the original goal, exclusions, accepted decisions and authorized finish
stage. Identify the exact diff, starting/base revision and current working state;
uncommitted task changes count. Preserve unrelated edits. The author's report is
a claim to investigate, not the oracle. Use the relevant project verification
skill if available; do not replace the user's feature map or browser tooling.

## Observe the real behavior
- Check target/build identity, access, meaningful data, resource ownership and
  side effects before driving. Unknown identity or missing data stays explicit.
- Choose the smallest decisive checks for the changed contract and likely
  regressions. Compare parent/base and changed behavior when available; without
  a runnable base, distinguish the current failure from its attribution.
- Use normal user entry points. For web work use agent-browser and its own named
  session; for CLI use the real command and output/exit; for storage/services/
  queues inspect actual responses and state within the allowed target.
- Capture trigger and stable result, relevant negative/empty/error/persistence
  behavior and side effects when in scope. A green build, mock, internal setter
  or cached screenshot alone cannot establish the real path.
- Reproduce suspected defects with a command or concrete user sequence and
  compare observed versus required output. Source-only concerns remain labeled
  concerns rather than reproduced bugs. No findings is a valid result.
- Add or update relevant tests and run focused checks under the user's standing
  test authorization; respect explicit task restrictions. Use safe temporary
  probes when sufficient; never inject defects into shared data.

## Validity and handoff
Bind each result to its revision/diff, build if known, relevant base/dependencies,
environment/data conditions, operation, command/steps and evidence. Rerun checks
whose inputs changed; a matching patch fingerprint alone does not prove the
base, environment or build stayed equivalent. Do not rerun unrelated valid checks.

Report verified, failed, blocked or unverified for each requested flow. Include
exact observed failures, evidence checked, dismissed claims with reasons,
remaining uncertainty and cleanup of task-owned resources. Never treat a blocked
required check as an overall pass. The main agent reviews the evidence, reports
accepted/rejected conclusions and retains integrated ownership.

For pstack adaptations and license, see [sources](references/sources.md).
