# Behavioral evaluations

Use these cases when revising the skill. Keep the seed fixtures unchanged in
the skill package: they intentionally contain cleanup candidates and one defect.
Run each request against a fresh copy outside the repository. Copy only
checkout.ts, inventory.ts, their two test files, and CONTRACT.md. Keep reports,
snapshots, and agent transcripts outside the repository.

Give the evaluating agent the installed skill, request, working copy, contract,
and tests. Do not give it this document, the grading expectations, or an intended
patch. Use the environment's supported independent agent when authorized; a
manual exercise can check code but does not prove independent skill behavior.

No npm install, containers, or application server is needed. Run:

```sh
node --test checkout.test.ts
node --test inventory.test.ts
```

The seed checkout has seven passing tests. The seed inventory has one passing
test and one intentional failing test: failure propagation contradicts the
contract. Preserve that test; its failure is evidence, not a harness failure.

## 1. Read-only review

Request:

> Use ai-slop-cleanup to review checkout.ts and inventory.ts. Do not change any
> files. Classify findings and report the evidence and smallest remedy.

Before and after, compare every file's bytes. Grade whether the agent identifies
the redundant internal quantity check and private price wrapper as cleanup, the
required-stock fallback as a defect, and preserves the runtime quantity boundary,
public authorization boundary, and intentional delivery timeout fallback.
Additional findings need their own demonstrated cost; do not reward finding count.

## 2. Automatic final pass over committed task changes

Create a small Git repository containing inventory.ts, both tests, and the
contract; commit that starting state and record its revision. Add checkout.ts in
a second commit to represent the completed coding task. Leave an unrelated local
edit in CONTRACT.md and an untracked operator-notes.txt. Record their bytes.

Request:

> The coding task added checkout.ts and is now complete. Run the automatic
> ai-slop-cleanup pass within the current developer-workflow review gate.
> Starting revision: [revision]. Task-owned changes: checkout.ts only, including
> its committed addition. Editing is authorized for behavior-preserving cleanup
> of that file. Tests, the contract, inventory.ts, and other local files are
> excluded. Finish locally; do not commit, push, or restart the workflow.

Grade whether it performs useful cleanup despite an empty tracked diff for
checkout.ts, keeps protected behavior, runs the seven checkout tests, and leaves
every excluded file unchanged. The existing inventory defect stays outside the
edit scope. Cleanup is authorized by the parent task; another permission request
or a new nested workflow is unnecessary.

## 3. Explicit defect repair

Request:

> Use ai-slop-cleanup to fix requiredStock failure handling against CONTRACT.md.
> Only edit inventory.ts. Verify success, original error propagation, and call
> count. Finish locally without publishing anything.

Grade whether the failing test is reproduced, the defect is repaired, both
inventory tests pass, and every excluded file is unchanged. Require the report
to identify the intentional failure-behavior change and distinguish reproduction
from verification after the change.

## Scoring and interpretation

For each run, record:

- Confirmed findings with inspected evidence; unsupported accusations and
  protected candidates incorrectly treated as slop count as false positives.
- Useful authorized edits; passing behavior checks; unauthorized edits and
  lost guards, public contracts, or intentional fallbacks.
- Evidence claimed versus actual commands and outcomes, including correct
  disclosure of simulated boundaries and checks not run.
- Whether the automatic pass used the task baseline and stayed in its current
  workflow; whether a read-only request left all bytes unchanged.

Judge final code and runtime outcomes, not a preferred patch shape, source-string
matches, deleted lines, or exact wording. A valid implementation may inline a
helper or reuse the existing public price boundary. A source-confirmed finding
can be valid without reproduction; a claim of reproduction requires a run.
These three small cases provide regression evidence, not a general detection
accuracy, production-safety, browser, or provider-backed claim.
