---
name: html-artifact
description: Create readable, portable HTML artifacts for implementation plans, design explorations, code explainers, and reviews. Use when the user asks for an HTML plan or artifact, or a visual document with diagrams and mockups. Do not replace explicitly requested Markdown, build a production app, or deploy a site merely to deliver a document.
---

# HTML Artifact

Turn the user's material into a browser-readable document that helps them inspect decisions and give useful feedback. Match the artifact to the task; a short plan does not need a dashboard.

## Source and approach

Inspired by Thariq Shihipar's May 20, 2026 Anthropic article, [Using Claude Code: The unreasonable effectiveness of HTML](https://claude.com/blog/using-claude-code-the-unreasonable-effectiveness-of-html).

The article advocates visual documents for exploring alternatives, developing specifications, and carrying context into implementation and verification. Use mockups, diagrams, relevant code, and optional controls where they improve review. Related pages can preserve exploration alongside the selected plan. Editable artifacts should export the reader's choices back into usable text.

The practical delivery and validation guidance below adapts that approach for this environment; it is not a claim that the article prescribes these rules.

## Establish the content

Read the supplied material and relevant code before describing current behavior. Preserve the user's scope, constraints, decisions, and unresolved questions when converting an existing plan. Distinguish observed facts, proposals, assumptions, and illustrative examples. Cite sources near claims and identify inspected files or revisions when useful.

Choose the smallest useful deliverable: one HTML file by default, or linked pages when separate explorations and a final plan genuinely need their own space. Follow workspace artifact-location rules and reuse the current conversation's folder. Do not create a framework project for a document.

## Make a plan reviewable

For implementation planning, cover what the reader needs to decide and what a later implementer needs to execute:

- Problem, intended outcome, scope, and constraints.
- Current behavior and proposed behavior, with a concrete example where useful.
- Alternatives and tradeoffs when a decision remains open.
- Relevant interface mockups, architecture or data-flow diagrams, and short code or contract examples.
- Ordered implementation steps, dependencies, affected components, and acceptance checks.
- Material risks, open questions, and migration or rollback considerations when applicable.

Scale these elements to the task rather than forcing every heading. Label mockups and proposed snippets clearly. Never imply a prototype is connected to a real backend. Keep the plan actionable as text so another agent can read the HTML source and recover the decisions without operating the UI. Planning alone does not authorize implementation.

## Build the document

Prefer self-contained HTML with inline CSS, inline SVG, and only the JavaScript needed for useful interactions. Avoid external fonts, CDNs, and runtime fetches by default so the file remains portable. Use relative paths when supporting assets are necessary.

Use semantic headings, readable typography, a restrained palette, and a clear reading order. Add anchor navigation for long documents; use tables for comparisons and diagrams for relationships. Keep code in escaped `pre`/`code` blocks, never executable script tags. Ensure narrow-screen layouts, keyboard access, visible focus, sufficient contrast, and readable diagram labels. Keep essential content available without JavaScript and include print styles that reveal collapsed or tabbed content.

Use controls only when they aid a real decision. For editable selections or parameters, offer a copy/export action containing the current choices and enough context for a follow-up prompt. Provide selectable text if clipboard access fails. Explain whether edits persist; never imply changes update project files or external systems.

## Verify and deliver

Open the actual file in the available built-in browser, otherwise use agent-browser. Inspect desktop and narrow-screen rendering, exercise navigation and every added interaction, and check for overflow, clipped labels, broken links, missing assets, and console errors. Check print rendering when print support matters. Capture readable final-state screenshots and provide evidence the user can open. If browser verification is blocked, state what remains unverified.

Deliver the artifact through the environment's attachment or preview capability when available. In a remote session, a host-local path alone is insufficient: use a verified existing remote delivery route or explain the access limitation. Follow environment procedures before starting any preview service. Do not publish, upload to a third party, commit, or push without authorization.

Briefly report what the artifact contains, what was checked, and any unresolved decisions. When implementation or verification is subsequently requested, read the approved artifact and its linked context before proceeding.
