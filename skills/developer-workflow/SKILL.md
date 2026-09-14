---
name: developer-workflow
description: Complete a substantial implementation, bug fix, refactor, or migration through validation and review. Use for end-to-end software changes; do not use for read-only questions, routine inspection, or tiny edits.
---

# Developer Workflow

Complete substantial development tasks through the stages below. Adapt the depth
of each stage to the task while preserving the sequence and outcome.

## Delegation

Keep planning, scope division, integration, conflict resolution, and the final
completion decision in the primary agent. Use subagents only when the user or
active runtime instructions authorize delegation and it materially improves the
work.

Delegate only when it improves speed, context efficiency, or validation quality:

- Use a read-focused agent for bounded repository investigation.
- Use an implementation agent for a clearly owned code change.
- Use a browser-focused agent for repeated UI flows, screenshots, console or
  network checks, and viewport coverage.
- Use an independent reviewer after implementation and primary validation.

Before substantial exploration or delegation, use the `model-routing` skill at
`~/.agents/skills/model-routing/SKILL.md` for model choices, effort, handoffs,
escalation, and cost controls. Honor explicit user choices and active runtime
constraints. Keep model-specific policy in that skill. If it is unavailable,
use supported capabilities and disclose the missing routing guidance.

Give every subagent a self-contained assignment containing the objective,
relevant paths and context, scope and file ownership, constraints, expected
output, and validation criteria. Keep concurrent assignments non-overlapping.
Use the host agent's supported models, tools, and routing mechanism; do not
assume provider-specific model names or APIs.

If subagents are unavailable or delegation would cost more than it saves,
perform the same checkpoints directly and record any reduced independence in
the final report.

## 1. Understand

Inspect repository instructions, relevant code, existing behavior, tests, and
expected behavior. Resolve important uncertainty before editing. Prefer concise
evidence with file and symbol references over raw search output.

## 2. Plan

Form a concise plan covering implementation, validation, risks, ownership, and
completion criteria. Keep at most one primary step in progress at a time unless
independent work is deliberately parallelized.

## Development and test environments

Apply this procedure whenever starting test or preview services, including small
tasks that do not need the full development workflow.

- Inspect project setup and all existing containers, including stopped ones,
  plus their service versions, ports, and volumes. Reuse the user's shared
  Postgres, Redis, and other service containers across projects. Start an
  identified existing stopped container when needed; do not create a new stack.
- Creating or recreating any container requires explicit user permission.
  Inspect Compose commands, project scripts, and test tools before running them
  so they cannot silently provision containers. If a service is missing or
  incompatible, report the specific requirement and ask before provisioning.
- Isolate parallel work with task-specific databases, users, or schemas inside
  existing services. For Redis, use application-supported key prefixes or
  logical databases and verify that queues and cleanup honor that isolation.
  Never flush/reset a shared service or apply destructive tests or migrations
  to another project's data. If safe isolation is unavailable, ask for direction.
- The primary agent owns setup and cleanup. Assign shared services to subagents
  so they do not independently create duplicate stacks.
- Give temporary resources task-specific names, track their ownership, and use
  appropriate resource limits. Run destructive tests only on disposable data.
- After testing, including failures, remove only confirmed task-owned temporary
  databases, users, keys, and processes that are no longer needed. Keep shared
  containers and volumes intact and running. Clean up separately authorized
  temporary containers only within their approved scope; never broadly prune.
- Keep one preview when the user needs to review it. Provide the verified remote
  URL, exact stop command, and any remaining access uncertainty. Report all
  temporary resources left running and why.

## 3. Execute

Implement the requested outcome completely while respecting project
conventions and the established scope. Preserve unrelated user changes. Divide
independent work into bounded assignments only when it improves throughput.
Inspect and integrate delegated changes before validation.

## 4. Validate

Run checks proportional to the change: focused tests first, then broader tests,
builds, linters, type checks, or end-to-end flows as applicable. Exercise the
affected behavior and resolve failures caused by the implementation.

For UI work, capture final-state screenshots at relevant viewports, including
successful results. Identify the flow and viewport checked. Follow workspace
artifact rules, exclude sensitive data, and deliver inline images or verified
remote links. If capture is blocked, report the blocker and visually unverified
areas; a build or automated test is not a substitute for screenshots.

## 5. Review

Review the final diff for correctness, regressions, unintended changes, missing
validation, security or data-integrity risks, and alignment with the request.
When delegation is authorized and independent review adds meaningful value,
give a reviewer the requirements, final diff, and validation evidence. Resolve
actionable findings and rerun affected checks.

## 6. Complete

Do not claim completion until review is finished and actionable findings are
resolved and revalidated or explicitly reported. Summarize the outcome,
important files changed, validation evidence, and anything unverified or
unresolved.
