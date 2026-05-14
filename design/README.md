# `design/`

This directory is the **design workshop** for The Kindness Flywheel. It contains:

- The brand philosophy (`PHILOSOPHY.md`)
- The canonical design tokens (`tokens.yml`)
- The logo source code and master SVG files (`logo/`)
- The exploration PDFs documenting design decisions (`logo/exploration/`)

**This directory is not built by Jekyll.** It's the workshop. Built outputs are mirrored to:

- `_data/design.yml` — Jekyll-readable token mirror
- `assets/css/_design-tokens.scss` — CSS variables for stylesheets
- `assets/images/brand/` — deployed logo files (SVG + PNG)

---

## Quick start

To regenerate everything from source:

```bash
cd design
./build.sh
```

This script:
1. Reads `tokens.yml`
2. Writes `_data/design.yml` and `assets/css/_design-tokens.scss`
3. Runs `logo/build_svg.py` → writes masters to `logo/masters/`
4. Runs `logo/build_raster.py` → writes PNGs/PDFs to `logo/exports/`
5. Copies the right subset of files into `assets/images/brand/`

The script is idempotent. Run it after any token or logo change.

---

## Editing the logo

The spiral mark is generated from `logo/spiral.py`. The single configuration that defines the production mark is the `PRODUCTION_SPIRAL` constant near the bottom of that file.

To change the mark:

1. Edit `PRODUCTION_SPIRAL` in `logo/spiral.py`
2. Optionally edit `tokens.yml` if colors are changing
3. Run `./build.sh`
4. Visually verify by opening `logo/masters/mark.svg` and `logo/exports/og-image.png`
5. Commit all changes together (source + outputs) so the repo is always consistent

Always change the source. Never hand-edit the generated SVGs in `logo/masters/` — they will be overwritten.

---

## Exploring alternatives

`logo/explore_spiral.py` generates a multi-page PDF showing six candidate expressions of the production spiral. These are the legitimate alternatives — naked (no terminus dot), monochrome, inverted, open-tail, heavy-stroke.

```bash
python logo/explore_spiral.py logo/exploration/spiral_exploration.pdf
```

To propose a different production variant, modify `PRODUCTION_SPIRAL` and re-run the exploration to see how it lives in the family.

---

## Why this structure?

**`design/` is the source.** `_data/`, `assets/`, and any built artifacts are derivative. If `design/` and the derivatives ever disagree, `design/` wins and the build script reconciles them.

**The spiral is code.** Logos drawn in Illustrator drift. Logos generated from a parameter set don't. Every spiral on every surface comes from the same six numbers — growth rate, revolutions, phase, stroke start, stroke end factor, dot factor. Change one, regenerate everything, ship.

**SVG is the master format.** Vector, resolution-independent, version-control-friendly, browser-native. PNGs and PDFs are derivatives generated from the SVG.

**Tokens are the contract.** Templates, stylesheets, and Python all read from the same `tokens.yml` (via mirrors). Changing a color in one place changes it everywhere.

---

## File map

```
design/
├── README.md                  ← this file
├── PHILOSOPHY.md              ← Considered Warmth — the brand compass
├── tokens.yml                 ← canonical design tokens (colors, type, spacing)
├── build.sh                   ← regenerate all derived outputs
└── logo/
    ├── spiral.py              ← spiral geometry library (single source of truth)
    ├── build_svg.py           ← SVG master generator
    ├── build_raster.py        ← PNG and PDF export generator
    ├── explore_spiral.py      ← multi-candidate exploration PDF
    ├── masters/               ← generated SVG masters (committed)
    │   ├── mark.svg
    │   ├── mark-dark.svg
    │   ├── favicon.svg
    │   ├── lockup-horizontal.svg
    │   ├── lockup-horizontal-dark.svg
    │   ├── lockup-stacked.svg
    │   ├── lockup-stacked-dark.svg
    │   ├── wordmark.svg
    │   └── wordmark-dark.svg
    ├── exports/               ← generated PNG and PDF (committed)
    │   ├── mark-{16,32,64,256,512,1024}.png
    │   ├── mark-dark-{256,512,1024}.png
    │   ├── lockup-{horizontal,stacked}-{600,1200}.png
    │   ├── lockup-{horizontal,stacked}.pdf
    │   ├── apple-touch-icon.png
    │   ├── og-image.pdf
    │   └── og-image.png
    └── exploration/           ← decision-record PDFs (committed)
        └── spiral_exploration.pdf
```

---

## License

All design assets are CC-BY 4.0. Use them, build on them, just credit the publication.
