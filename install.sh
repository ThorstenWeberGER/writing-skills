#!/usr/bin/env bash
# Link this repo's skill and ground rules into ~/.claude so a git pull
# updates every machine. Symlinks, not copies, on purpose.
#
#   ./install.sh            link skill + CLAUDE.md (refuses to clobber)
#   ./install.sh --force    replace an existing CLAUDE.md, backing it up first
#   ./install.sh --status   show what is linked and whether it is current
#   ./install.sh --uninstall remove the links this script made
set -uo pipefail

REPO="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
CLAUDE_DIR="${CLAUDE_CONFIG_DIR:-$HOME/.claude}"
SKILL_SRC="$REPO/skills/clear-writing"
SKILL_DST="$CLAUDE_DIR/skills/clear-writing"
RULES_SRC="$REPO/CLAUDE.md"
RULES_DST="$CLAUDE_DIR/CLAUDE.md"
MODE="${1:-install}"

say() { printf '  %s\n' "$*"; }

status() {
  echo "repo:        $REPO"
  echo "claude dir:  $CLAUDE_DIR"
  echo
  if [ -L "$SKILL_DST" ]; then
    say "skill      linked -> $(readlink "$SKILL_DST")"
  elif [ -e "$SKILL_DST" ]; then
    say "skill      EXISTS but is not a link (a real directory is in the way)"
  else
    say "skill      not installed"
  fi
  if [ -L "$RULES_DST" ]; then
    say "CLAUDE.md  linked -> $(readlink "$RULES_DST")"
  elif [ -e "$RULES_DST" ]; then
    say "CLAUDE.md  EXISTS as a real file, not linked. Use --force to replace it"
  else
    say "CLAUDE.md  not installed"
  fi
  echo
  if [ -d "$REPO/.git" ]; then
    local behind
    behind=$(git -C "$REPO" rev-list --count HEAD..@{u} 2>/dev/null || echo "?")
    if [ "$behind" = "0" ]; then say "git        up to date with upstream"
    elif [ "$behind" = "?" ]; then say "git        no upstream configured"
    else say "git        $behind commit(s) behind upstream. Run: git -C $REPO pull"
    fi
  fi
}

case "$MODE" in
  --status) status; exit 0 ;;
  --uninstall)
    [ -L "$SKILL_DST" ] && rm "$SKILL_DST" && say "removed skill link"
    [ -L "$RULES_DST" ] && rm "$RULES_DST" && say "removed CLAUDE.md link"
    say "done. Any real files left in place were not touched."
    exit 0 ;;
esac

[ -d "$SKILL_SRC" ] || { echo "error: $SKILL_SRC not found. Run this from the repo." >&2; exit 1; }
mkdir -p "$CLAUDE_DIR/skills"

# --- skill ---
if [ -L "$SKILL_DST" ]; then
  ln -sfn "$SKILL_SRC" "$SKILL_DST"; say "skill link refreshed"
elif [ -e "$SKILL_DST" ]; then
  echo "error: $SKILL_DST exists and is not a symlink." >&2
  echo "       Move it aside first; this script will not delete a real directory." >&2
  exit 1
else
  ln -s "$SKILL_SRC" "$SKILL_DST"; say "skill linked"
fi

# --- ground rules ---
# Overwriting someone's existing CLAUDE.md would silently drop rules they rely
# on, so refuse by default and back up on --force.
if [ -L "$RULES_DST" ]; then
  ln -sfn "$RULES_SRC" "$RULES_DST"; say "CLAUDE.md link refreshed"
elif [ -e "$RULES_DST" ]; then
  if [ "$MODE" = "--force" ]; then
    bak="$RULES_DST.backup.$(date +%Y%m%d%H%M%S)"
    mv "$RULES_DST" "$bak"; ln -s "$RULES_SRC" "$RULES_DST"
    say "existing CLAUDE.md backed up to $(basename "$bak"), then linked"
  else
    say "CLAUDE.md already exists and was NOT touched."
    say "Either append the six rules from $RULES_SRC by hand,"
    say "or re-run with --force to back it up and replace it."
  fi
else
  ln -s "$RULES_SRC" "$RULES_DST"; say "CLAUDE.md linked"
fi

echo
say "verify the skill with: $SKILL_SRC/tests/test.sh"
