# Cleanup report

Add this to the task handoff even when nothing changed; announcing a pass is not
a review.

- **Found:** confirmed findings or "no actionable slop found," with the reviewed
  revision and owned files.
- **Changed:** simplifications and authorized repairs, or "none."
- **Checked:** checks run and their results, and what remains unverified.

Label each claim:

- *source-confirmed*: the inspected paths support it;
- *reproduced*: an observed run shows it;
- *verified after change*: named checks passed on the final code.

A proposed check is not a run, and passing selected tests does not prove full
equivalence. Keep local evidence separate from deployed or provider-backed proof.

For several findings, use a table:

| Location / category | Evidence and cost | Remedy / status | Verification |
| --- | --- | --- | --- |
