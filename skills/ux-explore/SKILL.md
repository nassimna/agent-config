---
name: ux-explore
description: Use when explicitly asked to explore alternative UX journeys. Compare three reference-backed concepts in a local prototype. Use ui-ux-loop to evaluate an existing journey.
disable-model-invocation: true
---

# UX Explore

1. **Frame the job.** Identify the user, their goal, and the constraints that must hold. Treat the current layout and sequence as open choices.
2. **Get independent designs.** Select the latest Claude Opus and GPT Sol from the live delegation catalog (`orchestrator_capabilities` on T3). Give both the same scenario, data, and constraints in separate briefs. Ask one to explore how the operator makes the choice and the other what the system could prepare or decide. Opus leads visual design. Request extra-high effort for both unless the user specifies otherwise. Ask before substituting an unavailable model or setting. Label each result with its exact model ID and effort.
3. **Ground each idea.** Have each designer inspect a real interaction, link the source with the date inspected, and explain what they adapted. Look outside the product’s industry for similar decisions.
4. **Show three directions.** Preserve both originals and explain any convergence. Add a third that changes a decision or action. Use `html-artifact` for one local interactive comparison unless the user requests another format. Label simulated behavior.
5. **Help the user choose.** Run the same scenario in each design with a meaningful tradeoff or changed condition. Compare whether the user can understand what changed, recover, and verify the outcome. Recommend a direction and give one user test that could change the recommendation. Stop at the prototype.
