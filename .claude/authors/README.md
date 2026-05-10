# Per-Author Context

This directory holds per-contributor voice profiles, rhetorical references,
and research material that informs AI-assisted authoring.

## Convention

Subdirectories under `.claude/authors/` are gitignored by default. Each
contributor maintains their own `.claude/authors/<their-slug>/` directory on
their fork's `drafts` branch (force-added with `git add -f`). These files
never appear on PR branches submitted upstream.

The CLAUDE.md hook in the project root reads every markdown file in the
contributor's author directory before drafting, so dropping in additional
reference documents (rhetorical forms, source materials, structural
frameworks, etc.) takes effect automatically on the next session.

## Setup

See `CONTRIBUTING.md` → "AI-Assisted Authoring Workflow" for the full
convention. The short version: run `scripts/setup-author.sh` from a clone of
your fork, and it will scaffold everything.

## Why this is private

Voice profiles and research material are working notes, not publishable
content. Keeping them on the contributor's `drafts` branch (and out of PR
branches) means:

- The PR an editor reviews is clean — only the post itself
- Contributors can iterate freely on voice and references without
  signaling intent to publish
- The licensing of research material doesn't have to match CC-BY 4.0
  (only the published posts do)
