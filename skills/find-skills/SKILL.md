---
name: find-skills
description: Find and evaluate installable agent skills. Use when the user explicitly asks to find, discover, recommend, or install a skill; do not trigger from an ordinary "how do I" question.
---

# Find Skills

Find a skill only when the user explicitly asks for skill discovery,
recommendations, or installation. Ordinary task requests should be handled
directly with the capabilities already available.

## Workflow

1. Define the requested capability and target harness: Codex, Claude, or both.
2. Check the currently available and locally installed skills first. Do not
   recommend a duplicate under a different name.
3. Search the supported catalog or use `npx skills find <specific query>` when
   that CLI is available. Try one or two precise alternative queries if needed.
4. Inspect promising candidates before recommending them:
   - read the complete `SKILL.md`
   - verify the source and maintenance status
   - inspect scripts, executable instructions, permissions, and external tools
   - check overlap or conflicts with existing global rules and skills
   - treat install counts and repository stars as signals, not proof of quality
5. Present at most three options. For each, state its purpose, source, notable
   risks or dependencies, and why it fits.
6. Install only when the user explicitly asks. Use the supported installer for
   the active harness, preserve existing skills, and avoid blindly executing
   untrusted setup scripts.
7. After installation, validate the skill and confirm that a fresh agent session
   discovers it. Do not claim it works from copied files alone.

## Output

- Lead with the best match or say clearly that no good match was found.
- Use short bullets and include the exact install command only when useful.
- If no suitable skill exists, offer to handle the task directly or create a
  small custom skill when the workflow is genuinely reusable.
