#!/usr/bin/env bash
# scripts/setup-author.sh
#
# One-time setup for contributors using AI-assisted authoring.
# See CONTRIBUTING.md "AI-Assisted Authoring Workflow" for the convention.
#
# What this does:
#   1. Verifies you're in a fork (not upstream)
#   2. Adds `upstream` remote if missing
#   3. Creates a `drafts` branch off the latest main
#   4. Scaffolds your public author bio in _authors/<slug>.md
#   5. Scaffolds your private voice profile in .claude/authors/<slug>/voice.md
#   6. Force-adds the voice profile (it's gitignored by default)
#   7. Pushes drafts to your fork
#   8. Sets drafts as your fork's default branch via `gh repo edit`

set -euo pipefail

UPSTREAM_REPO="kindnessflywheel/kindnessflywheel-site"
UPSTREAM_URL="https://github.com/${UPSTREAM_REPO}.git"

if ! command -v git >/dev/null 2>&1; then
  echo "Error: git is required." >&2
  exit 1
fi

if ! command -v gh >/dev/null 2>&1; then
  echo "Error: GitHub CLI ('gh') is required." >&2
  echo "Install: https://cli.github.com/" >&2
  exit 1
fi

if ! git rev-parse --git-dir >/dev/null 2>&1; then
  echo "Error: not inside a git repository." >&2
  exit 1
fi

ORIGIN_URL=$(git remote get-url origin 2>/dev/null || echo "")
if [[ -z "$ORIGIN_URL" ]]; then
  echo "Error: no 'origin' remote set." >&2
  exit 1
fi

if [[ "$ORIGIN_URL" == *"${UPSTREAM_REPO}"* ]]; then
  echo "Error: 'origin' points at the upstream repo." >&2
  echo "Fork the repo on GitHub first, then clone your fork." >&2
  exit 1
fi

if ! git remote get-url upstream >/dev/null 2>&1; then
  echo "Adding 'upstream' remote → ${UPSTREAM_URL}"
  git remote add upstream "${UPSTREAM_URL}"
fi

echo
read -r -p "Your name (e.g., 'Geoff Scott'): " AUTHOR_NAME
read -r -p "Your slug for filenames (e.g., 'geoff-scott'): " AUTHOR_SLUG

if [[ -z "${AUTHOR_NAME}" || -z "${AUTHOR_SLUG}" ]]; then
  echo "Error: name and slug are required." >&2
  exit 1
fi

if [[ ! "${AUTHOR_SLUG}" =~ ^[a-z0-9-]+$ ]]; then
  echo "Error: slug must contain only lowercase letters, digits, and hyphens." >&2
  exit 1
fi

echo
echo "Fetching upstream..."
git fetch upstream

if git show-ref --verify --quiet refs/heads/drafts; then
  echo "Branch 'drafts' already exists; checking it out."
  git checkout drafts
else
  echo "Creating 'drafts' branch off upstream/main..."
  git checkout -b drafts upstream/main
fi

AUTHOR_FILE="_authors/${AUTHOR_SLUG}.md"
if [[ ! -f "${AUTHOR_FILE}" ]]; then
  mkdir -p "$(dirname "${AUTHOR_FILE}")"
  cat > "${AUTHOR_FILE}" <<EOF
---
name: ${AUTHOR_NAME}
role:
---

A few sentences about who you are, what you're working on, and what you're
learning. This gives readers context for your stories.

Links to your work, GitHub, LinkedIn, or personal site are welcome.
EOF
  echo "Created ${AUTHOR_FILE}"
fi

VOICE_DIR=".claude/authors/${AUTHOR_SLUG}"
VOICE_FILE="${VOICE_DIR}/voice.md"
mkdir -p "${VOICE_DIR}"
if [[ ! -f "${VOICE_FILE}" ]]; then
  cat > "${VOICE_FILE}" <<EOF
# Voice Profile: ${AUTHOR_NAME}

This directory holds agent guidance for drafting in your voice. Add
reference documents (rhetorical forms, structural frameworks, source
material) as additional markdown files here — the CLAUDE.md hook reads
every file in this directory automatically before drafting.

## Canonical reference posts

List your published posts here as the agent's reference points for tone:

- (Add posts as you publish them.)

## Voice rules

Replace this section with rules specific to your writing. Useful categories:
sentence rhythm, argument structure, tone guardrails, endings, bold/italics
conventions, first-person usage.

## First-draft self-check

List patterns you want the agent to scan for and rewrite before showing you
a draft.
EOF
  echo "Created ${VOICE_FILE}"
fi

git add "${AUTHOR_FILE}" 2>/dev/null || true
git add -f "${VOICE_FILE}"

if ! git diff --cached --quiet; then
  git commit -m "setup: bootstrap ${AUTHOR_NAME}'s drafts branch"
fi

echo
echo "Pushing 'drafts' to your fork..."
git push -u origin drafts

FORK_REPO=$(gh repo view --json nameWithOwner -q .nameWithOwner)
echo
echo "Setting '${FORK_REPO}' default branch to 'drafts'..."
gh repo edit "${FORK_REPO}" --default-branch drafts

cat <<EOF

Setup complete.

Next steps:
  1. Edit ${VOICE_FILE} with your voice rules.
  2. Add any reference documents (research, rhetorical forms, source
     material) into ${VOICE_DIR}/ — the agent will read them automatically.
  3. Start drafting on the 'drafts' branch.

When you're ready to submit a post, see CONTRIBUTING.md →
"Submitting a post".
EOF
