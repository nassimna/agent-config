---
name: design-critique
description: Critique an existing UI design from screenshots, Figma frames, or a rendered app, scoring each review point from 0 to 10 and giving evidence, priorities, and practical improvements. Use when asked for design feedback or a visual critique, especially of a dashboard. Keep the review read-only; repeated journey audits belong to ui-ux-loop.
---

# Design Critique

Review as a product designer: explain what the interface communicates, where it
creates friction, and which changes would help most. Judge the design against
the user's task, intended audience, and existing visual direction.

## Establish the target

- Identify the exact screen or frames, available viewport, and requested scope.
  Use the supplied brief and design system. When the audience or primary task
  is unclear, state a working assumption; ask only when it changes the critique.
- Identify the design stage. For concepts and wireframes, emphasize task flow,
  structure, and grouping; assess final styling only when represented or
  requested. For polished mockups, examine visual detail. For working apps,
  assess interaction behavior only where actually exercised.
- Inspect the actual visual before judging layout or styling. Use supplied
  images, accessible Figma renders, or the actual app through available tools.
  Source code alone does not establish the rendered result. If no visual is
  available, ask for a screenshot, frame, or accessible app target rather than
  inventing findings.
- Keep the review read-only. Suggestions do not authorize code edits, Figma
  changes, publication, or actions that alter shared data. If implementation is
  separately requested, follow the applicable development workflow.

## Evaluate the design

Start with the primary task: what should the user notice, understand, and do?
Evaluate and score each lens below within the available evidence. Use them to
find specific strengths and problems; a category does not require a finding.
If the user names additional review points, score those too.

| Lens | Questions that guide the critique |
| --- | --- |
| Visual hierarchy | Does the most important content or action stand out? Do size, weight, placement, and color communicate a clear order? |
| Information architecture and scannability | Are sections, navigation, labels, and groups organized around the task? Can users locate key information without reading everything? |
| Information density and whitespace | Is density appropriate for this audience? Do proximity, similarity, and common region communicate the intended grouping without wasting useful space? |
| Alignment and grid | Are edges, columns, spacing rhythms, and optical alignment coherent? Are exceptions purposeful? |
| Typography | Do size, weight, line length, and line height support readable labels, values, and headings? Does the type scale establish a useful hierarchy? |
| Color and contrast | Does emphasis have a consistent meaning? Are text and controls distinguishable? Is color supplemented by labels or other cues? |
| Consistency and visual coherence | Do components, icons, surfaces, borders, and imagery follow the same visual language and supplied design system? |
| Usability and user control | Does the UI use familiar language, favor recognition over memory, prevent mistakes, and provide understandable cancel, undo, and recovery where applicable and evidenced? |
| Affordance and feedback | Are actions recognizable, labels specific, and selected, disabled, loading, empty, error, and success states understandable where visible or tested? |
| Accessibility and adaptation | What does the evidence show about legibility, focus, keyboard access, zoom, target size, responsive layout, and relevant language or RTL states? |

For dashboards, also examine:

- **Metric meaning:** clear labels, units, date range, comparison period, data
  freshness, and whether a change is beneficial in the metric's context.
- **Data visualization:** appropriate chart types, honest scales and baselines,
  readable axes and legends, consistent encodings, and comparable series.
  Distinguish zero, missing data, and unavailable data where the evidence allows.
- **Filter clarity:** visible active filters and scope, understandable time ranges,
  and a clear relationship between controls and affected charts or totals.
- **Actionability:** whether users can recognize an exception, understand its
  significance, and find the relevant next action or detail.

Use the following references selectively:

- For ambiguous grouping, interaction principles, or examples of grounded
  feedback, read [visual and usability guidance](references/visual-and-usability.md).
- For dashboards, read [dashboard guidance](references/dashboard-review.md),
  including chart perception, monitoring versus analysis, and uncertainty.
- Before reporting a specific accessibility criterion or threshold, read
  [accessibility guidance](references/accessibility.md). It distinguishes
  measurable checks from screenshot-only observations.

## Score each point from 0 to 10

Give every assessed review point an integer score, written as `7/10`, with a
brief evidence-based reason and the most useful improvement. Higher is better.
Apply the same anchors across categories:

| Score | Meaning within the inspected scope |
| --- | --- |
| 0 | The represented design fundamentally fails this criterion and prevents the relevant task. |
| 1–2 | Severe problems; substantial changes are needed. |
| 3–4 | Weak; major clarity or usability problems remain. |
| 5–6 | Workable, with noticeable problems that affect the task. |
| 7–8 | Good; mostly effective, with specific improvements remaining. |
| 9 | Excellent; only minor refinements are supported by the evidence. |
| 10 | Exemplary for the stated task and stage, with enough evidence to justify the rating and no material issue found within scope. |

- Scores are reasoned design judgments, not measurements of human usability or
  proof of accessibility conformance. Tie deductions to evidence and the brief;
  do not grade against an invented ideal or deduct for a personal style preference.
- Use **Not assessed** when evidence is insufficient and **Not applicable**
  when a point does not apply. Neither means zero. Do not award a high score
  simply because no problem was visible.
- For partial evidence, narrow the point's label and state the limitation, for
  example `Accessibility — visible presentation only`. Leave interaction,
  screen-reader, and unseen breakpoint checks unassessed until tested.
- Keep the quality score separate from issue severity and confidence. A
  category can score well and still contain one consequential defect. Do not
  invent an overall score unless requested; if requested, explain its basis
  and exclude unassessed or inapplicable points.

## Make defensible findings

- Name the precise element and observed issue, explain the likely user impact,
  and propose the smallest useful change. Use design terms to clarify the cause;
  avoid vague verdicts such as "make it cleaner" or "it feels off."
- Anchor significant visual findings to a frame, exact label, crop, or marked
  region when tools permit. Verify that any annotation actually identifies the
  element discussed. Do not invent coordinates or require image editing to
  deliver an otherwise clear critique.
- Separate observed problems, UX hypotheses, and aesthetic preferences. Give
  preferences a reason tied to the brief. Preserve effective patterns; do not
  impose a redesign, extra whitespace, or a fashionable style without cause.
- A screenshot supports visible observations. It does not prove interaction
  behavior, keyboard support, screen-reader output, responsive behavior, or
  unseen states. Record those as untested. Claim numerical contrast or spacing
  violations only with reliable measurements and an applicable criterion.
- Prioritize by consequence: **High** impedes the primary task or risks a
  materially wrong decision; **Medium** causes meaningful ambiguity or friction;
  **Low** is a minor consistency or polish issue. Qualify uncertain impact and
  combine findings with the same underlying cause.
- State confidence separately where it matters: **Observed** for an inspected
  property or tested behavior, **Likely** for a supported inference, and
  **Needs validation** for a hypothesis. Observing a layout does not establish
  that its predicted effect on users has been measured.

Example of a hypothetical finding:

> **Medium — Scannability, KPI row:** The three totals omit units and a date
> range, making them hard to interpret or compare. Add units beside each value
> and a shared period label above the row. Check that each metric can be read
> with its unit and period without opening another view.

## Deliver the critique

Lead with a short verdict tied to the primary task, the inspected stage and
scope, and what is worth preserving. Always include a scorecard:

| Review point | Score /10 | Evidence and reason | Best improvement |
| --- | --- | --- | --- |

Include one row for each general lens and, for dashboards, each dashboard lens.
Use the assessment labels above where a numeric score cannot be justified.
For a requested narrow review, include just the requested points. A point that
already works can say `Preserve` in the improvement column.

After the scorecard, explain the highest-priority findings with location,
severity, confidence, user impact, proposed change, and how to check the result.
Avoid repeating every scorecard row. Include only supported, distinct findings;
do not fill a quota.
Reference exact labels, frame names, or screenshot regions so each item can be
located. Show relevant visual evidence through native images or verified links
when available, without publishing private material. Finish with the first
changes to make and any material limits on what was inspected. Follow a user's
requested output format instead when supplied.

## Calibrate future revisions

When validating changes to this skill, use a small set of permitted designs
with known issues and acceptable alternatives. Compare supported findings,
missed issues, unsupported criticism, and the rationale behind scores. Include
a screenshot-only case to check that unseen behavior remains unassessed.
The reference examples are hypothetical writing examples, not real-design
validation. Do not claim behavioral validation without an actual trial.
