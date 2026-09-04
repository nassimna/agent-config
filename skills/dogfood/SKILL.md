---
name: dogfood
description: Perform exploratory QA of a web app and return evidence-backed bug findings. Use when the user asks to dogfood, bug-hunt, exploratory-test, or broadly QA a site; do not use for a focused verification of one known change.
metadata:
  hermes:
    tags: [qa, testing, browser, web, dogfood]
    related_skills: []
---

# Dogfood

Explore a real web application as a user, find reproducible problems, and
report useful evidence. The goal is discovery and diagnosis, not merely proving
that pages load.

## Establish the scope

- Confirm the target URL, important flows, authenticated roles, relevant
  viewports, and whether the user wants findings in chat or a saved report.
- Treat ordinary QA as read-only. Do not create accounts, submit consequential
  forms, change shared data, purchase anything, or test destructive actions
  unless the user authorized that exact behavior.
- If credentials are already available through an approved local mechanism,
  use them without printing or copying them into reports.

## Choose the browser

- In T3 Code, use its attached preview/browser tools first.
- Otherwise use the active harness's product-native browser when available.
- Use `agent-browser` only when the user requests it or no suitable native
  browser is available. Load its current CLI instructions before operating it.
- Reuse an existing authenticated session when allowed; do not assume a fresh
  browser profile shares the user's cookies.

## Explore

1. Map the reachable surface and prioritize the flows that matter most.
2. Exercise navigation, forms, state transitions, loading and empty states,
   refresh/back behavior, validation, and failure recovery where applicable.
3. Check console and network behavior around suspicious interactions when the
   browser exposes those signals.
4. Cover relevant responsive sizes and input methods without multiplying
   redundant passes.
5. Compare actual behavior with visible product intent, supplied requirements,
   existing patterns, and accessibility expectations. Do not invent a defect
   from personal taste alone.

## Record findings

For each real issue, capture:

- concise title and severity
- exact URL, role, viewport, and prerequisites
- minimal reproduction steps
- expected and actual behavior
- screenshot or recording when it materially clarifies the issue
- relevant console or network evidence
- confidence and any remaining uncertainty

Verify a finding twice when practical. Merge duplicate symptoms that share one
cause, distinguish product defects from environment failures, and avoid padding
the report with trivial observations.

Use [references/issue-taxonomy.md](references/issue-taxonomy.md) when severity
or category labels are needed. Use
[templates/dogfood-report-template.md](templates/dogfood-report-template.md)
only when producing a saved report.

## Deliver

- Lead with the highest-impact findings and state what was tested and skipped.
- Prefer concise bullets and direct evidence.
- Follow the current workspace's artifact rules. Do not create a report folder
  when the user only needs an answer in chat.
- Do not modify application code or file issues unless separately requested.
