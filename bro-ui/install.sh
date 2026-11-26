#!/usr/bin/env bash
# Link this skill into Claude's skills dir. Idempotent. No always-on import:
# bro-ui only runs when I type /bro-ui.
#
#   bash install.sh            # personal:  ~/.claude/skills
#   bash install.sh --project  # this repo: ./.claude/skills

set -euo pipefail

SRC="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
NAME="$(basename "$SRC")"

if [[ "${1:-}" == "--project" ]]; then
  SKILLS_DIR=".claude/skills"
else
  SKILLS_DIR="$HOME/.claude/skills"
fi

mkdir -p "$SKILLS_DIR"
TARGET="$SKILLS_DIR/$NAME"

if [[ -e "$TARGET" || -L "$TARGET" ]]; then
  RESOLVED="$(cd "$TARGET" 2>/dev/null && pwd -P || true)"
  if [[ "$RESOLVED" == "$SRC" ]]; then
    echo "skill: already installed at $TARGET"
  else
    echo "skill: $TARGET exists and points elsewhere ($RESOLVED), leaving it alone" >&2
  fi
else
  ln -s "$SRC" "$TARGET"
  echo "skill: linked $TARGET -> $SRC"
fi

echo
echo "Done. Start a new Claude session, or run /$NAME to load it now."
