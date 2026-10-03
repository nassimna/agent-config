# Research basis

Checked on **2026-10-03**. Searched the web for coding AI slop, unnecessary
abstractions and defenses, code duplication, maintainability, and code
simplification. Consulted original research, the authors of review guidance,
and a tool author's pattern catalog. The workflow and safeguards are a synthesis;
they are not a validated classifier of AI authorship or an implementation of TRIM.

## Primary research

- [TRIM: Reducing AI-Generated CodeSlop via Agent Trajectory Minimization](https://arxiv.org/html/2607.18161v1)
  — Mathai et al., **2026-07-20**, arXiv preprint. Defines CodeSlop in agent
  repairs as residual edits that can be removed while retaining the working
  solution. Connects it to exploratory changes left in the final patch and
  evaluates a trajectory-based minimization algorithm. Supports inspecting
  abandoned approaches and verifying candidate removals. This skill uses a
  broader practical quality lens and does not promise the paper's benchmark
  reductions or reproduce its algorithm. Passing selected tests is evidence,
  not proof of full equivalence.
- [Human-Written vs. AI-Generated Code: A Large-Scale Study of Defects, Vulnerabilities, and Complexity](https://arxiv.org/abs/2508.21634)
  — Cotroneo, Improta, and Liguori, **2025-08-29**; abstract reports acceptance
  at ISSRE 2025. In its Python/Java comparison, generated code is generally
  less structurally complex but more repetitive, with unused constructs and
  debug leftovers. This limits the claim that AI code is always overengineered;
  findings concern those models and samples, not every current agent or repo.
- [“An Endless Stream of AI Slop”: How Developers Discuss the Burden of AI-Assisted Software Development](https://arxiv.org/abs/2603.27249)
  — Baltes, Cheong, and Treude, first submitted **2026-03-28**, latest listed
  revision **2026-08-28**. Qualitative analysis of developer discussions connects
  slop to review and maintenance burdens. Evidence of reported experiences,
  rather than a measured defect rate or proof of causal effects.
- [The Maintainability Gap: AI Code Quality in 2026](https://www.gitclear.com/the_ai_code_quality_maintainability_gap)
  — GitClear, **2026 report**; exact publication date not displayed on the
  inspected landing page. Reports duplication, error masking, and declining
  reuse signals in its longitudinal data. Commercial observational research;
  the public landing page was inspected, not the gated full report. Trends
  alone do not establish the cause of a particular repository's problems.

## Original guidance and practical patterns

- [Google: What to look for in a code review](https://google.github.io/eng-practices/review/reviewer/looking-for.html)
  — living guidance, publication date not displayed; accessed **2026-10-03**.
  Grounds review in current requirements, design, complexity, testing, and
  useful comments. Supports judging unnecessary generality in context.
- [GitHub: Review AI-generated code](https://docs.github.com/en/copilot/tutorials/review-ai-generated-code)
  — living documentation, publication date not displayed; accessed
  **2026-10-03**. Covers intent, repository fit, invented APIs/dependencies, and
  deleted or skipped tests. Supports checking actual contracts and evidence.
- [Anthropic: Code Simplifier agent](https://github.com/anthropics/claude-plugins-official/blob/main/plugins/code-simplifier/agents/code-simplifier.md)
  — living source, accessed **2026-10-03**. Supports scoped simplification,
  behavior preservation, and readability over compression. Its particular
  language/style rules and proactive-edit policy are not adopted here;
  repository conventions and the user's requested mode govern those choices.
- [scanaislop: 20 AI Slop Code Examples](https://scanaislop.com/blog/ai-slop-code-examples/)
  — tool author's pattern guide, **2026-07-22**. Practical prompts around hidden
  errors, thin layers, repetitive validation, and weak tests. Useful candidate
  patterns, not empirical proof that those shapes are always wrong.

## Limits

There is no universal style signature that proves AI authorship. Some sources
define slop narrowly as unnecessary patch residue; others include unreliable
code and verification. Here, a finding needs local evidence of wasted complexity
or a defect. The catalog adds context checks to prevent simplification from
removing legitimate requirements. No detection accuracy or production safety
claim follows from the literature or the skill's isolated validation examples.
