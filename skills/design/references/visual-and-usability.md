# Visual and usability guidance

Use these principles to explain a concrete observation. They do not establish
that users experienced the predicted problem.

## Grouping and emphasis

- **Proximity:** items placed close together appear related. Check whether a
  label is closer to its value than to a neighboring value, and whether a
  filter appears attached to the content it actually controls.
- **Similarity:** matching appearance suggests matching meaning or behavior.
  Check for unrelated actions sharing the same strongest emphasis and for
  identical meanings encoded differently.
- **Common region:** a containing surface or boundary creates a group. Check
  whether card boundaries imply an inaccurate scope or separate content that
  needs to be compared. Do not prescribe cards for every group.

## Usability principles

Apply the relevant Nielsen heuristics to visible affordances and tested
behavior: system status, familiar language, control and freedom, consistency,
error prevention, recognition over recall, efficient use, relevant content,
error diagnosis and recovery, and help when needed.

For example, distinguish an observed missing unit from a hypothesis that users
will misunderstand the metric. Do not infer broken undo, lost input, or missing
keyboard access from a static mockup. Do not penalize a wireframe for styling
that is intentionally unspecified.

## Hypothetical critique examples

**Problem:** An "All metrics" date filter sits inside the Revenue card.

> Medium; placement observed, user confusion needs validation. Common region
> suggests the filter affects only Revenue. Place it above the affected metric
> group or clarify its scope. Check that users can identify which metrics it
> affects without explanation.

**Acceptable alternative:** A dense operations table puts related fields
together, aligns comparable values, and retains readable labels.

> Preserve the compact layout for the stated expert monitoring task. Extra
> whitespace is not automatically an improvement; identify an actual reading
> or interaction problem before recommending more spacing.

These examples demonstrate reasoning, not predetermined scores. Assign a score
only after inspecting enough of the relevant design and context.

## Sources

Paraphrased guidance, checked 4 November 2026:

- [NN/g: Derailed Design Critiques](https://www.nngroup.com/articles/derailed-design-critiques/), 30 May 2021 — appropriate scope and stage; hypothetical scenarios are not user evidence.
- [NN/g: 10 Usability Heuristics](https://www.nngroup.com/articles/ten-usability-heuristics/), reviewed 30 January 2024.
- [NN/g: Proximity Principle](https://www.nngroup.com/articles/gestalt-proximity/), 2 August 2020 — grouping through placement, with related principles discussed.
- [Duan et al.: Visual Prompting with Iterative Refinement for Design Critique Generation](https://arxiv.org/abs/2412.16829), revised 22 May 2025 — research on visually grounded comments and region refinement. This supports trying visual anchors; it does not validate this skill or its score scale.
