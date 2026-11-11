---
name: claude-codex-ui-workflow
description: Route new UI and UX work between Claude (design, product, and interaction judgment) and Codex (production implementation, integration, and fixes). Use when a task creates or improves an interface or user flow, or raises an ambiguous product decision inside a UI task. Specializes claude-codex-workflow. Not for backend-only work or small mechanical fixes that follow an established design.
---

# Claude/Codex UI Workflow

Claude designs; Codex builds. Codex is substantially cheaper for production
code, so Claude's output is a design and decisions, not the shipped
implementation.

## Roles

- **Claude** owns creative, product, interaction, and visual design for new UI
  and UX improvements, and helps settle ambiguous product decisions within the
  original goal. Ideas beyond that goal are proposals for the user, not work to
  implement. Claude may supply prototype code when it communicates the design
  better than prose; Codex treats it as reference, not production code.
- **Codex** implements the agreed design plus backend, contracts, integration,
  verification, and fixes. It reuses existing components, styling, i18n, and
  RTL behavior, and reports any needed deviation from the design instead of
  silently reinterpreting it.
- Routine design and product choices need no human approval; ask the user only
  when a choice is genuinely theirs under the global rules.

## Ownership and delegation

Follow the ownership, delegation, brief, and boundary rules in
[claude-codex-workflow](../claude-codex-workflow/SKILL.md). For UI, the
originating agent delegates design to Claude when it runs on Codex, and
production implementation to Codex when it runs on Claude.

## Multiple UI samples or sets

When the user requests multiple UI samples, sets, variants, or design
directions, research internet references before designing the alternatives.
Carry this requirement into the delegated design brief. Inspect actual screens
or images; search snippets and remembered examples do not establish visual
research. Prefer references relevant to the product, journey, and constraints.

For each direction, include source links and a short explanation of the layout,
hierarchy, or interaction patterns adapted from them. Make alternatives
meaningfully distinct; color swaps alone do not establish different directions.
Adapt references to the existing product and the user's requested scope.
Honor explicit no-internet instructions. If access is blocked, disclose which
references could not be inspected and label any resulting designs as unresearched.

## Design handoff

Claude's handoff must be actionable for implementation without follow-up:

- Goal, scope, and the existing screen or component used as the reference.
- Layout and hierarchy, interactions, and navigation.
- Responsive behavior and language/RTL behavior.
- Relevant loading, error, and empty states.
- Copy, phrased for the translation files.
- Acceptance criteria Codex can verify in the actual app.
- A visual or prototype only when it clarifies something the text cannot.

For new or substantially changed forms, onboarding, signup, pricing,
upgrade, and cancellation journeys, include:

- The user's goal and earliest useful outcome.
- Which inputs are required now and which can wait.
- Proposed defaults, their source, and how users change them.
- How entered work survives back navigation, errors, and authentication.
- What progress, availability, price, and consequence claims rely on.

Reduce unnecessary decisions using verified context. Keep consent and
paid extras unselected. Count only meaningful completed work as progress.
Provide useful results before optional commitments when access, cost,
and abuse controls allow. Explain consequences factually, provide neutral
exits, and compare prices using matching periods and total costs.

Apply only the relevant points; do not add steps or customization merely
to create investment. Label prototype data so it cannot be mistaken for
verified production claims.

The actual app, not the prototype, is the implementation preview.

## Review

- For substantial UI work, after Codex implements, run one bounded Claude design
  review of actual-app screenshots against the handoff. Codex fixes confirmed
  deviations. Re-review only when the UI materially changed; do not re-review
  unchanged work or bounce between models automatically.
- Small mechanical fixes that follow the established design stay with Codex
  without a Claude pass.
- Any other cross-model challenge follows `claude-codex-workflow`; do not add
  one to routine work.
