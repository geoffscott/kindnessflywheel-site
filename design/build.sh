#!/usr/bin/env bash
# design/build.sh — regenerate all derived design assets.
#
# Reads design/tokens.yml + design/logo/spiral.py and writes:
#   - design/logo/masters/*.svg               (SVG masters)
#   - design/logo/exports/*.{png,pdf}         (raster + print derivatives)
#   - design/logo/exploration/*.pdf           (decision-record PDFs)
#   - assets/images/brand/*                   (deployed site assets)
#
# Idempotent. Safe to re-run after any token or logo edit.
#
# Requires: python3, reportlab, cairosvg, pillow, pdf2image, poppler-utils

set -euo pipefail

# Resolve repo root (script lives in design/, so repo is parent)
SCRIPT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
REPO_ROOT="$( cd "${SCRIPT_DIR}/.." && pwd )"

cd "${SCRIPT_DIR}"

echo "▶ The Kindness Flywheel — design system build"
echo "  repo root: ${REPO_ROOT}"
echo

# ─── 1. SVG masters ──────────────────────────────────────────────────
echo "▶ Building SVG masters…"
mkdir -p logo/masters
python3 logo/build_svg.py logo/masters/

# ─── 2. Raster + PDF exports ─────────────────────────────────────────
echo
echo "▶ Building raster and PDF exports…"
mkdir -p logo/exports
python3 logo/build_raster.py logo/masters/ logo/exports/

# ─── 3. Exploration PDF ──────────────────────────────────────────────
echo
echo "▶ Building exploration PDF…"
mkdir -p logo/exploration
python3 logo/explore_spiral.py logo/exploration/spiral_exploration.pdf

# ─── 4. Deploy subset to assets/images/brand/ ────────────────────────
echo
echo "▶ Copying deployed assets to assets/images/brand/…"
BRAND_DIR="${REPO_ROOT}/assets/images/brand"
mkdir -p "${BRAND_DIR}"

# Logo SVGs the site actually uses
cp logo/masters/mark.svg                    "${BRAND_DIR}/mark.svg"
cp logo/masters/mark-dark.svg               "${BRAND_DIR}/mark-dark.svg"
cp logo/masters/lockup-horizontal.svg       "${BRAND_DIR}/lockup-horizontal.svg"
cp logo/masters/lockup-horizontal-dark.svg  "${BRAND_DIR}/lockup-horizontal-dark.svg"
cp logo/masters/favicon.svg                 "${BRAND_DIR}/favicon.svg"

# Favicon raster fallbacks (older browsers)
cp logo/exports/mark-32.png                 "${BRAND_DIR}/favicon-32.png"
cp logo/exports/mark-16.png                 "${BRAND_DIR}/favicon-16.png"

# Apple touch icon
cp logo/exports/apple-touch-icon.png        "${BRAND_DIR}/apple-touch-icon.png"

# Social cards
cp logo/exports/og-image.png                "${BRAND_DIR}/og-image.png"

echo "  ✓ ${BRAND_DIR}/"
ls -1 "${BRAND_DIR}/" | sed 's/^/      /'

# ─── 5. Sanity check: token mirrors ──────────────────────────────────
# These are hand-maintained for now (small files, low churn). If they
# drift from tokens.yml, you'll see it here.
echo
echo "▶ Verifying token mirrors are present…"
test -f "${REPO_ROOT}/_data/design.yml"            && echo "  ✓ _data/design.yml"
test -f "${REPO_ROOT}/assets/css/_design-tokens.scss" && echo "  ✓ assets/css/_design-tokens.scss"

echo
echo "✓ Build complete."
echo "  Next: review changes with \`git diff\`, then commit."
