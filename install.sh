#!/usr/bin/env bash
set -euo pipefail

repo_dir="$(cd -- "$(dirname -- "${BASH_SOURCE[0]}")" && pwd)"
user_home="${HOME:?HOME is not set}"

link_path() {
  local source_path="$1"
  local target_path="$2"
  local target_dir

  target_dir="$(dirname -- "$target_path")"
  mkdir -p -- "$target_dir"

  if [[ -L "$target_path" ]] &&
    [[ "$(readlink -f -- "$target_path")" == "$(readlink -f -- "$source_path")" ]]; then
    printf 'ok      %s\n' "$target_path"
    return
  fi

  if [[ -e "$target_path" || -L "$target_path" ]]; then
    printf 'refusing to overwrite %s\n' "$target_path" >&2
    return 1
  fi

  ln -s -- "$source_path" "$target_path"
  printf 'linked  %s\n' "$target_path"
}

link_path "$repo_dir/AGENTS.md" "$user_home/.codex/AGENTS.md"
link_path "$repo_dir/CLAUDE.md" "$user_home/.claude/CLAUDE.md"

for skill_path in "$repo_dir"/skills/*; do
  [[ -d "$skill_path" ]] || continue
  link_path "$skill_path" "$user_home/.claude/skills/$(basename -- "$skill_path")"
done

printf 'Agent configuration is installed.\n'
