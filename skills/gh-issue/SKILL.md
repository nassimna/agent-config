---
name: gh-issue
description: "Draft or file concise GitHub issues with current behavior, expected behavior, and available evidence. Use when asked to write or open a GitHub issue, or turn findings into GitHub tickets."
---

# GitHub Issue

Write a short issue that a reader can understand and act on without the chat history.
Draft requests stay in chat. Requests to open, file, or create an issue authorize
publishing it; creating this skill does not authorize publishing issues.

## Prepare

- Identify the intended repository from the request or current Git remote. Ask
  only when the destination or desired outcome cannot be inferred reliably.
- When a repository is known, follow its issue instructions and required
  template fields. Before publishing, search existing issues for the same
  problem. If a matching issue exists, return its link instead of creating a
  duplicate or changing it without authorization.
- Use supplied information and relevant source or evidence. Keep investigation
  proportional to the request; do not invent behavior, causes, or test results.

## Write

- Use a specific title: `Area: observed problem` for bugs, or `Area: desired
  capability` for features.
- Aim for 80–150 words, with 1–3 short bullets per section. Include essential
  context when needed; avoid nested lists and debugging history.
- Choose each heading freely to suit the issue's context and the section's role.
  Follow repository-required headings when present.
- Explain the problem or current state and its impact.
  For bugs, add the shortest known reproduction sequence as a bullet. Include
  role, version, or environment only when it helps explain the issue.
- Describe expected behavior or desired outcomes that also serve as completion
  criteria. Add an implementation proposal only when requested.
- Support the issue with available screenshots, recordings, short relevant logs,
  test results, or GitHub source permalinks, with a brief caption explaining what
  each proves. Distinguish reproduced behavior, source findings, and user reports
  with concise wording. If a bug has not been reproduced, say so briefly.
- Omit the section for evidence when nothing useful is available. Remove all
  placeholders and unsupported optional bullets before delivering the issue.

## Publish with gh

- Use the confirmed repository explicitly: `gh issue create --repo owner/repo
  --title 'Specific title' --body-file issue.md`. Preserve actual Markdown
  newlines. Apply only requested or repository-required labels and assignments.
- For available image or video evidence, check `gh issue create --help` for
  `--attach` support, inspect the media for sensitive content, and upload it as
  GitHub attachments. Repeat `--attach` for multiple files. Local image
  references in the body are rewritten when the referenced file is attached.
  Never commit evidence or publish machine-local, localhost, or Tailscale links.
  If uploading is blocked, report the missing attachment accurately.
- A failed attachment upload can still create the issue. Check the returned URL
  and remote state before retrying; do not create a second issue blindly.
- Read the issue back with `gh issue view`, verify its saved title and body, and
  check that attached evidence is accessible to repository readers. Return the
  issue URL and any material publication or evidence limitation.

Sources: [GitHub issue guidance](https://docs.github.com/en/communities/using-templates-to-encourage-useful-issues-and-pull-requests/syntax-for-issue-forms)
and [gh issue create](https://cli.github.com/manual/gh_issue_create).
