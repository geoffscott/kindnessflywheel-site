# Brand

The Kindness Flywheel uses a small, deliberate visual system: one mark, one wordmark, one warm accent against a contemplative dark indigo. The full philosophy is in [`design/PHILOSOPHY.md`](design/PHILOSOPHY.md). This page is for engineers and contributors who need to use the brand correctly without reading the manifesto.

## The mark

A logarithmic spiral — `r = a · exp(0.20 · θ)`, 2.3 revolutions — rendered as a variable-weight ribbon with a small coral period at the terminus. The math is doing real work: the spiral evokes compounding, momentum, patient care over time.

Masters live in [`design/logo/masters/`](design/logo/masters/). Site-deployed copies are in [`assets/images/brand/`](assets/images/brand/).

| File | When to use |
|---|---|
| `mark.svg` | The mark alone, on a light surface |
| `mark-dark.svg` | The mark on a dark surface |
| `lockup-horizontal.svg` | Mark + "THE KINDNESS / FLYWHEEL", set side-by-side |
| `lockup-stacked.svg` | Mark above wordmark, both centered |
| `favicon.svg` | Tighter crop, optimized for 16–32px rendering |
| `og-image.png` | 1200×630 social card |

Always use the SVG masters when possible. PNG exports are derivatives for contexts that can't render vector.

## Colors

| Token | Hex | Role |
|---|---|---|
| `--kf-ink` | `#2A2250` | Mark, body type, rules, primary surface |
| `--kf-accent` | `#D95F3B` | Terminus dot, link hover state, occasional accent |
| `--kf-ground-warm` | `#F8F5F0` | Page background (light mode) |
| `--kf-ground-dark` | `#13102A` | Page background (dark mode) |
| `--kf-subtle` | `#5A5670` | Captions, metadata, muted body |

The accent appears sparingly — never as fill, never as background. If you want more coral, you want more contrast somewhere else.

## Typography

| Face | Role |
|---|---|
| Fraunces | Display, headings, UI chrome, the wordmark |
| Source Serif 4 | Body, long-form posts, italic asides |
| JetBrains Mono | Code, metadata, footers, registration marks |

Both Fraunces and Source Serif 4 are variable fonts with an optical-sizing (`opsz`) axis. Modern browsers default `font-optical-sizing: auto`, so heading-sized type gets the display-optical cut and body-sized type gets the text-optical cut without explicit `font-variation-settings`. Fraunces also carries a `SOFT` axis (0–100) and a `WONK` axis if more characterful weighted display variants are wanted at hero scale.

Hierarchy descends: mark, wordmark, headline, body. Nothing larger than it needs to be.

## Using in the site

Tokens are exposed three ways:

**SCSS / CSS** — import `assets/css/_design-tokens.scss` and use the CSS variables (`var(--kf-ink)`, `var(--kf-type-display)`, etc.). Dark mode is wired in automatically via `prefers-color-scheme` and an explicit `[data-theme="dark"]` override.

**Jekyll templates** — read from `site.data.design` for paths and palette:

```liquid
<img src="{{ site.data.design.logo.lockup_horizontal }}" alt="The Kindness Flywheel">
```

**Python / scripts** — import from `design.logo.spiral`:

```python
from design.logo.spiral import PRODUCTION_SPIRAL, COLORS
```

## Regenerating

After editing `design/tokens.yml` or `design/logo/spiral.py`:

```bash
./design/build.sh
```

This rebuilds every SVG master, every PNG/PDF export, and copies the right subset into `assets/images/brand/`. The script is idempotent — safe to re-run.

## Don't

- Don't hand-edit SVGs in `design/logo/masters/`. They are regenerated. Edit `spiral.py` and rebuild.
- Don't introduce a new color without putting it in `design/tokens.yml` first.
- Don't use the coral accent as a background fill or large surface. It's a period at the end of a sentence, not a paragraph.
- Don't pair the wordmark with a face other than Bricolage Grotesque without checking [`design/PHILOSOPHY.md`](design/PHILOSOPHY.md) first.

## License

All brand assets are CC-BY 4.0. Use them, build on them, just credit the publication.
