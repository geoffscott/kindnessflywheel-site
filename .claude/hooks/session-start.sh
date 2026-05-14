#!/bin/bash
set -euo pipefail

if [ "${CLAUDE_CODE_REMOTE:-}" != "true" ]; then
  exit 0
fi

# Activate the versioned pre-commit hook that rejects _posts/*.md files
# with a blank line before front matter (Jekyll silently breaks on those).
git -C "$CLAUDE_PROJECT_DIR" config core.hooksPath .githooks
