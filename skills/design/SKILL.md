---
name: design
description: >-
  Design rules and methods for any UI work: building or changing screens and components,
  proposing design samples or directions, building marketing or company websites, and
  critiquing an existing design. Use whenever a task creates, changes, or reviews UI;
  ui-ux-loop owns repeated journey evaluations.
hooks:
  Stop:
    - hooks:
        - type: command
          command: 'for f in ${CLAUDE_SKILL_DIR:+"$CLAUDE_SKILL_DIR/scripts/gate.mjs"} ${CLAUDE_PLUGIN_ROOT:+"$CLAUDE_PLUGIN_ROOT/scripts/gate.mjs" "$CLAUDE_PLUGIN_ROOT/skills/taste-skill/scripts/gate.mjs"} ${CLAUDE_PROJECT_DIR:+"$CLAUDE_PROJECT_DIR/.claude/skills/design/scripts/gate.mjs" "$CLAUDE_PROJECT_DIR/.agents/skills/design/scripts/gate.mjs"} ${HOME:+"$HOME/.claude/skills/design/scripts/gate.mjs" "$HOME/.agents/skills/design/scripts/gate.mjs"}; do if [ -f "$f" ]; then exec node "$f" --hook claude; fi; done; if [ -d .taste-skill ]; then printf "%s gate.mjs not found; CLAUDE_PLUGIN_ROOT=%s CLAUDE_PROJECT_DIR=%s HOME=%s\n" "$(date -u +%Y-%m-%dT%H:%M:%SZ)" "${CLAUDE_PLUGIN_ROOT-}" "${CLAUDE_PROJECT_DIR-}" "${HOME-}" > .taste-skill/gate-hook-missing.txt 2>/dev/null; fi; for d in .taste-skill */.taste-skill; do if [ -f "$d/build.json" ]; then echo "tasteskill gate: gate.mjs not found (CLAUDE_PLUGIN_ROOT=${CLAUDE_PLUGIN_ROOT-}); the build in $d is not checked" >&2; break; fi; done; exit 0'
          timeout: 600
---

# Design

Apply these rules to all UI work. They override `website.md` and `critique.md`
where they conflict. Pass this skill to workers doing UI work.

- For multiple samples, variants, or design directions, first research and
  inspect internet references. Link them per direction and say what you
  adapted. If internet access is blocked or excluded, say the designs are not
  reference-backed.
- Avoid unless asked: cream or off-white backgrounds, italic accent words in
  headings, "01 / 02 / 03" section labels, monospace labels, pill buttons.
- Fit controls to the task and data volume: dialogs for short decisions, room
  for complex editing, lists and pickers tested with realistic item counts.
- Make UI specific to the product: approved brand assets, real product screens
  where they explain the feature, one clear idea per visual.
- Size containers to their content and rebalance after removals. Keep work
  screens compact and readable; give marketing content room.
- Align comparable headings, values, fields, and actions; check long labels and
  uneven content so wrapping doesn't misalign actions.
- Keep nearby controls steady through wrapping and hover, focus, selection,
  loading, and active states. Use motion only to clarify feedback or transitions.

## By task

- **Marketing or company website** (landing, product, shop, studio, SaaS,
  game; static HTML/CSS or an existing frontend project): read
  [website.md](website.md), the tasteskill 2.5.1 build process with its
  checker and finish gate.
- **Review of an existing design** (screenshots, Figma frames, a rendered app):
  read [critique.md](critique.md). Reviews stay read-only.
- **App screens and components:** the rules above are enough; follow the
  product's existing design system.
