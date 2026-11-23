---
name: html-artifact
description: Create and verify portable HTML plans, design explorations, code explainers, and reviews. Use when asked for an HTML artifact or visual document.
---

# HTML Artifact

Turn the user's material into a browser-readable document that helps them inspect decisions and give feedback. Match the artifact to the task; a short plan does not need a dashboard.

## Establish the content

Read the supplied material and relevant code before describing current behavior. When converting an existing plan, keep its scope, constraints, decisions and open questions. Distinguish observed facts, proposals, assumptions and illustrative examples; cite sources near claims.

Default to one HTML file; use linked pages only when separate explorations and a final plan need their own space. Reuse the current conversation's artifact folder. Never create a framework project for a document.

## Make a plan reviewable

For implementation plans, cover what the reader must decide and what an implementer must execute, scaled to the task:

- Problem, outcome, scope and constraints.
- Current vs. proposed behavior, with a concrete example.
- Alternatives and tradeoffs for open decisions.
- Interface mockups, architecture or data-flow diagrams, short code or contract examples.
- Ordered steps, affected components and acceptance checks.
- Risks, open questions, migration or rollback when relevant.

Label mockups and proposed snippets; never imply a prototype is connected to a real backend. Keep decisions readable in the HTML source so another agent can recover them without operating the UI.

## Build the document

- Self-contained HTML: inline CSS and SVG, JavaScript only for useful interactions. No external fonts, CDNs or runtime fetches; use relative paths for necessary assets.
- Semantic headings, anchor navigation for long documents, tables for comparisons, diagrams for relationships. Code goes in escaped `pre`/`code` blocks.
- Keyboard access, visible focus, sufficient contrast, readable diagram labels. Essential content works without JavaScript; print styles reveal collapsed or tabbed content.
- Use controls only when they aid a real decision. Editable choices get a copy/export action producing text usable in a follow-up prompt, with selectable text as a clipboard fallback. Say whether edits persist.

## Visual quality

- Centered reading area with a maximum width; 24–40px desktop and 16–20px phone page gutters; 24–40px between sections; 16–24px inside panels. Text never touches a panel edge.
- Body text 14–16px, line-height 1.5–1.7; table cells 12–16px padding with clear row grouping.
- On phones, stack wide comparisons or scroll only the table. Long paths and labels wrap without widening the page.
- No decorative metrics, gradients, repeated cards or controls added for show.
- Provide a light/dark palette without network requests; match the host theme for inline delivery.
- If the inline renderer requires a transparent background and zero outer padding, keep spacing inside sections, and keep a separate portable layout with page gutters for the portable file.

## Verify

Open the actual file in a browser (prefer `agent-browser`) at desktop and phone widths. Exercise navigation and every interaction; check overflow, clipped labels, broken links, missing assets and console errors, and print rendering when it matters. Judge the screenshots for gutters, padding, heading rhythm and density, for both the inline and the portable version when delivering both. Fix problems before delivery.

## Deliver

Return the portable HTML file or show it inline as requested. Use `folio-upload`
only when the user explicitly asks to send this artifact or revision to Folio.

Briefly report what the artifact contains, what was checked and open decisions. Before later implementation or verification, read the approved artifact and its linked context.
