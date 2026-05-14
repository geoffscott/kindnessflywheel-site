# Geoff Scott — Author Context for Kindness Flywheel

This directory is private authoring context for the Kindness Flywheel publication. It lives at `.claude/authors/geoff-scott/` on the `drafts` branch of my fork of [`kindnessflywheel-site`](https://github.com/kindnessflywheel/kindnessflywheel-site). The site repo's `CLAUDE.md` hook auto-loads files from this directory when I'm authoring.

Post markdown files do **not** live here. Drafts and published posts both live in the site repo's `_posts/` on the `drafts` branch (see CONTRIBUTING.md). This directory holds only the durable context that informs how those posts get written.

## How to use these files when authoring a post

1. **Read `voice.md` first** — every time. Authoritative reference for how posts should read. The closest published voice example is "The Race to the Mean" in `_posts/` on the drafts branch.
2. **Check `personas/`** to confirm who the post is being written for (audience archetypes).
3. **Check `people/`** for real named individuals or organizations that might appear in the post (case studies, quoted sources, story subjects).
4. **Pull from `research/`** when a claim needs a source. Don't invent statistics; everything here has provenance.
5. **Cross-check the thesis in `context/core-thesis.md` and `context/positioning.md`** — every post should land somewhere on that map.
6. **Use `context/rhetorical-structure.md`** for the structural template (classical + Rogerian + Toulmin hybrid).
7. **Look in `ideation/`** for raw seeds and unfinished thinking that might feed the next post.

## Layout

```
geoff-scott/
├── voice.md                ← authoritative voice reference; read first
├── README.md               ← this file
│
├── context/                ← durable cross-cutting authoring context
│   ├── manifesto.md
│   ├── content-strategy.md         ← cadence, formats, channels, lenses
│   ├── core-thesis.md              ← the central claim, in plain language
│   ├── positioning.md              ← strategic positioning and differentiation
│   ├── implementation.md           ← how the flywheel applies operationally
│   ├── golden-circle.md            ← why/how/what for the publication
│   ├── rhetorical-structure.md     ← KF house style — classical + Rogerian + Toulmin
│   ├── publishing-hashtags.md      ← the five lenses and how to tag posts
│   ├── cheat-sheet.md              ← one-pager of key stats and framings
│   ├── visual-style-guide.md       ← brand visual style (colors, type) — not writing voice
│   └── feedback-on-inaugural-post.md  ← editorial notes from inaugural post v5 review
│
├── personas/               ← audience archetypes (who I'm writing FOR)
│   ├── target-personas.md          ← umbrella — primary and secondary readers
│   ├── investor.md
│   └── celebrity-contributor.md
│
├── people/                 ← real named individuals and organizations referenced in the writing
│   ├── entities.md                 ← roster: Paul Oran, Dan Morena, Geoff Scott; OneEleven, Cohere, Saranam, etc.
│   └── greg-reynolds.md            ← deep dossier; canonical for biographical facts
│
├── research/               ← cross-cutting research, by topic; cite specifically when used
│   ├── ai-adoption.md
│   ├── commoditization-breadth.md
│   ├── content-landscape.md
│   ├── coordination-tax.md         ← fact-check of Reynolds' coordination-tax claims
│   ├── empires-conquest-giving.md
│   ├── extractive-practices.md
│   ├── gene-keys-human-design.md
│   ├── geo-strategy.md
│   ├── human-capital-ai-era.md
│   ├── kindness-comprehensive.md
│   ├── moats-ai.md
│   ├── moats-summary.md
│   ├── moats-readme.md             ← index for the moats research bundle
│   ├── stress-pfc-system2.md
│   ├── zen-motorcycle.md
│   ├── synthesis.md
│   ├── verification-data-points.md ← stat-by-stat fact checks
│   ├── companies.md
│   ├── competitive-landscape.md
│   ├── market-research-summary.md
│   ├── skeptical-executive-review.md  ← steel-man critique of the thesis
│   ├── report.pdf
│   └── references/                 ← external articles and reference materials
│       ├── motherless-article.md
│       └── zyro-hive-living-income-gap.md
│
├── ideation/               ← raw, pre-post thinking; seeds for future posts
│   ├── inbox-2026-03-28.md         ← thinking session, dated
│   ├── inbox-2026-03-30.md
│   ├── narrative-threads.md        ← reusable story arcs
│   └── brand-positioning-spec.md
│
└── assets/                 ← visual prompts and asset references
    └── logo-prompts.md
```

## Single source of truth — biographical facts

For any person who has a file in `people/`, that file is canonical. Other files (research, references, context) reference it rather than restate biographical facts. Reynolds is the current example: his bio lives in `people/greg-reynolds.md`; `research/coordination-tax.md` and `research/references/zyro-hive-living-income-gap.md` link back to it.

## Adding new material

- **New ideation** → `ideation/`. Inbox files for raw sessions are dated; standalone seeds get their own filename.
- **New research** → `research/<topic>.md`. Keep filenames short and topic-focused; drop redundant date suffixes.
- **External articles or excerpts to cite** → `research/references/`.
- **Persona refinement** → update files in `personas/`. The umbrella is `target-personas.md`.
- **New named person or organization** → add a row to `people/entities.md` with role + narrative thread. Promote to a standalone `people/<slug>.md` when the entry warrants a deeper dossier.
- **Voice refinement** → edit `voice.md`. Keep it the single source of truth; if a rule belongs anywhere, it belongs there.

## What's intentionally not here

- **Post drafts and published posts.** They live in the site repo's `_posts/` on the `drafts` branch.
- **CLAUDE.md.** That belongs at the repo root of the site fork, not under `.claude/authors/geoff-scott/`.
- **Anything public-facing.** This directory is gitignored upstream and only force-pushed to my fork's `drafts` branch.

## A note on context cost

The site repo's CLAUDE.md hook reads files from this directory automatically. Heavy research files (some 30–60 KB) load every session. If load cost matters, the candidates to thin first are the largest files in `research/` — most are background reference, not load-bearing voice context.
