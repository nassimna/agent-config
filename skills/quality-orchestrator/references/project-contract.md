# Project contract fields

Reuse the project's existing private contract/ledger. Record facts and unresolved
items; this checklist is not a source of permissions.

- Identity: repository, coordinator owner, target branch/base, worktree policy.
- Scope: application/roles/flows, pattern references, exclusions, known baseline.
- Authorization: local writes, publication, staging deploy, scoped fixtures,
  automatic merge eligibility, human gates; production excluded unless explicit.
- Environments: local/staging URL, verified deployment/source identity, credential
  file/profile pointers only (never secret values), datastore/object targets.
- Local data: approved source, refresh/init/cleanup commands, refresh triggers,
  snapshot timestamp/revision/manifest, referenced uploads, allowed sanitization,
  neutralized providers/jobs and known consistency limitations.
- Resources: worker/heavy caps, owner/task/run/lease, model/provider/effort settings,
  browser choice, startup/cleanup and state writer.
- Discovery: coverage cursor, fingerprints, reproduction criteria, perf baseline,
  per-pass budget, candidate priorities and no-progress stop conditions.
- Acceptance: actual-app and independent proof, meaningful focused regressions,
  required CI, artifact/target identity, evidence in PR, cleanup and merge gates.
- Continuation: supported worker/PR events, pending operations, health/due-work
  gate and recovery dedupe; report unsupported integration explicitly.
- Reporting: one digest schedule/timezone/thread, covered event IDs, local-date
  delivery claim and already-notified decision fingerprints.

Activation requires one owner handoff, correct schedule bindings and a bounded
pilot. Do not overwrite an active project's state to initialize a new one.
