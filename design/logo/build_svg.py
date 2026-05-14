"""
build_svg.py — generate SVG master files for the logo system.

Produces:
- mark.svg                  mark alone, on transparent ground
- mark-dark.svg             mark alone, dark-mode variant (warm light on dark)
- lockup-horizontal.svg     mark + "THE KINDNESS / FLYWHEEL" set to the right
- lockup-stacked.svg        mark above the wordmark, both centered
- wordmark.svg              wordmark alone
- favicon.svg               square-cropped mark, optimized for 16-32px rendering

All masters use CSS variables (--kf-ink, --kf-accent) so they pick up
the active theme automatically. They also include explicit fill colors
as fallbacks for environments that don't propagate CSS (Twitter cards,
some email clients, design tools).
"""
from __future__ import annotations
import math
from pathlib import Path
from spiral import PRODUCTION_SPIRAL, COLORS


# ─────────────────────────────────────────────────────────────────────
# Building blocks
# ─────────────────────────────────────────────────────────────────────
SVG_NS = 'xmlns="http://www.w3.org/2000/svg"'

def svg_header(width: int, height: int, viewbox: str) -> str:
    return (
        f'<svg {SVG_NS} viewBox="{viewbox}" '
        f'width="{width}" height="{height}" '
        f'role="img" aria-label="The Kindness Flywheel">'
    )


def mark_paths(cx: float, cy: float, R_max: float, dark: bool = False) -> str:
    """Return the mark's <path> elements (ribbon + optional terminus dot).

    Uses explicit fill= attributes (rasterizer-friendly) PLUS a class hook
    (theme-friendly). A stylesheet can override .kf-mark { fill: ... }
    in deployed contexts.
    """
    ink_color = COLORS["ink_dark"] if dark else COLORS["ink"]
    d = PRODUCTION_SPIRAL.svg_path_d(cx, cy, R_max)
    out = f'<path class="kf-mark" fill="{ink_color}" d="{d}"/>'
    if PRODUCTION_SPIRAL.show_terminus_dot:
        # SVG uses y-down convention, so terminus must use y_flip=True
        (tx, ty), tr = PRODUCTION_SPIRAL.terminus(cx, cy, R_max, y_flip=True)
        out += (f'<circle class="kf-accent" fill="{COLORS["accent"]}" '
                f'cx="{tx:.3f}" cy="{ty:.3f}" r="{tr:.3f}"/>')
    return out


# ─────────────────────────────────────────────────────────────────────
# Master generators
# ─────────────────────────────────────────────────────────────────────
def build_mark(dark: bool = False) -> str:
    """Mark alone, on a 240x240 canvas with 20px padding around the spiral."""
    SIZE = 240
    PAD = 20
    cx, cy = SIZE / 2, SIZE / 2
    R_max = (SIZE - 2 * PAD) / 2
    return (
        svg_header(SIZE, SIZE, f"0 0 {SIZE} {SIZE}")
        + "\n  " + mark_paths(cx, cy, R_max, dark=dark)
        + "\n</svg>\n"
    )


def build_favicon() -> str:
    """
    Tighter crop for favicon use.
    """
    SIZE = 64
    PAD = 4
    cx, cy = SIZE / 2, SIZE / 2
    R_max = (SIZE - 2 * PAD) / 2
    return (
        svg_header(SIZE, SIZE, f"0 0 {SIZE} {SIZE}")
        + "\n  " + mark_paths(cx, cy, R_max, dark=False)
        + "\n</svg>\n"
    )


def build_lockup_horizontal(dark: bool = False) -> str:
    """
    Mark on the left, two-line wordmark on the right.

    Treatment "B": KINDNESS in bold, FLYWHEEL in regular weight, same size.

    Geometry (in SVG units):
      - Mark: 240×240 region on the left, spiral within R_max=100 (20px pad)
      - Visible spiral right edge: x = 220
      - Gap: 14 units (0.07 × 200 effective mark size)
      - Text x: 234
      - Font size: 64 units — sized so the two-line stack fits inside 240px
        height with breathing room, not jammed against the spiral edges
      - Line spacing: baseline-to-baseline = font_size × 0.95 (tight)
    """
    PAD = 20
    cx, cy = 120, 120
    R_max = (240 - 2 * PAD) / 2
    visible_mark_size = R_max * 2
    gap = visible_mark_size * 0.07
    text_x = cx + R_max + gap   # 234

    font_size = 64
    # Baseline-to-baseline distance, tight
    line_height = font_size * 0.95
    # Center the two-line block on cy
    # Line 1 baseline sits half a line_height above cy + half-cap correction
    cap_height = font_size * 0.70
    # Block visual height ≈ cap_height + line_height (cap above line2 baseline)
    block_visual = cap_height + line_height
    # Top of cap1 = cy - block_visual / 2; baseline1 = top + cap_height
    line1_baseline_y = cy - block_visual / 2 + cap_height
    line2_baseline_y = line1_baseline_y + line_height

    # Canvas width: text_x + measured KINDNESS bold width (~371) + right pad.
    # Use 410 to give breathing room. If font_size changes, re-measure.
    W = int(text_x + 410)   # 644
    H = 240

    type_color = COLORS["ink_dark"] if dark else COLORS["ink"]
    font_stack = ('"Bricolage Grotesque", "Inter", "Helvetica Neue", '
                  'Arial, sans-serif')

    return (
        svg_header(W, H, f"0 0 {W} {H}")
        + "\n  " + mark_paths(cx, cy, R_max, dark=dark)
        + f'\n  <text class="kf-type" fill="{type_color}" '
        + f'x="{text_x}" y="{line1_baseline_y:.1f}" '
        + f'font-family=\'{font_stack}\' '
        + f'font-size="{font_size}" font-weight="700" '
        + f'letter-spacing="0.01em">KINDNESS</text>'
        + f'\n  <text class="kf-type" fill="{type_color}" '
        + f'x="{text_x}" y="{line2_baseline_y:.1f}" '
        + f'font-family=\'{font_stack}\' '
        + f'font-size="{font_size}" font-weight="400" '
        + f'letter-spacing="0.01em">FLYWHEEL</text>'
        + "\n</svg>\n"
    )


def build_lockup_stacked(dark: bool = False) -> str:
    """
    Mark above the wordmark, both centered. B treatment.
    Used in square contexts: avatars, OG cards where stacked is preferred.
    """
    PAD = 20
    R_max = (240 - 2 * PAD) / 2
    visible_mark_size = R_max * 2
    cx_mark = 200  # half of canvas width (set below)
    cy_mark = 120

    font_size = 56
    line_height = font_size * 0.95
    cap_height = font_size * 0.70

    # Wordmark baselines, stacked below the mark with a small gap
    wordmark_top = cy_mark + R_max + visible_mark_size * 0.10
    line1_y = wordmark_top + cap_height
    line2_y = line1_y + line_height
    H = int(line2_y + 24)   # bottom padding

    # Canvas width: needs to fit KINDNESS bold at 56pt (~325 units measured)
    # plus margin on both sides
    W = 400

    type_color = COLORS["ink_dark"] if dark else COLORS["ink"]
    font_stack = ('"Bricolage Grotesque", "Inter", "Helvetica Neue", '
                  'Arial, sans-serif')

    cx_mark = W / 2  # recenter now that we know W

    return (
        svg_header(W, H, f"0 0 {W} {H}")
        + "\n  " + mark_paths(cx_mark, cy_mark, R_max, dark=dark)
        + f'\n  <text class="kf-type" fill="{type_color}" '
        + f'x="{W/2}" y="{line1_y:.1f}" text-anchor="middle" '
        + f'font-family=\'{font_stack}\' '
        + f'font-size="{font_size}" font-weight="700" letter-spacing="0.01em">'
        + 'KINDNESS</text>'
        + f'\n  <text class="kf-type" fill="{type_color}" '
        + f'x="{W/2}" y="{line2_y:.1f}" text-anchor="middle" '
        + f'font-family=\'{font_stack}\' '
        + f'font-size="{font_size}" font-weight="400" letter-spacing="0.01em">'
        + 'FLYWHEEL</text>'
        + "\n</svg>\n"
    )


def build_wordmark(dark: bool = False) -> str:
    """Wordmark alone, no mark. B treatment."""
    font_size = 64
    line_height = font_size * 0.95
    cap_height = font_size * 0.70
    # Block visual height = cap + line_height (covers cap1 + descender room)
    block_visual = cap_height + line_height

    H = int(block_visual + 32)  # generous vertical pad
    line1_y = (H - block_visual) / 2 + cap_height
    line2_y = line1_y + line_height

    # Width: bold KINDNESS at 64pt ≈ 371 units measured, plus padding
    W = 410

    type_color = COLORS["ink_dark"] if dark else COLORS["ink"]
    font_stack = ('"Bricolage Grotesque", "Inter", "Helvetica Neue", '
                  'Arial, sans-serif')
    return (
        svg_header(W, H, f"0 0 {W} {H}")
        + f'\n  <text class="kf-type" fill="{type_color}" '
        + f'x="0" y="{line1_y:.1f}" '
        + f'font-family=\'{font_stack}\' '
        + f'font-size="{font_size}" font-weight="700" letter-spacing="0.01em">'
        + 'KINDNESS</text>'
        + f'\n  <text class="kf-type" fill="{type_color}" '
        + f'x="0" y="{line2_y:.1f}" '
        + f'font-family=\'{font_stack}\' '
        + f'font-size="{font_size}" font-weight="400" letter-spacing="0.01em">'
        + 'FLYWHEEL</text>'
        + "\n</svg>\n"
    )


# ─────────────────────────────────────────────────────────────────────
# Build orchestration
# ─────────────────────────────────────────────────────────────────────
def main(out_dir: Path):
    out_dir.mkdir(parents=True, exist_ok=True)
    files = {
        "mark.svg": build_mark(dark=False),
        "mark-dark.svg": build_mark(dark=True),
        "favicon.svg": build_favicon(),
        "lockup-horizontal.svg": build_lockup_horizontal(dark=False),
        "lockup-horizontal-dark.svg": build_lockup_horizontal(dark=True),
        "lockup-stacked.svg": build_lockup_stacked(dark=False),
        "lockup-stacked-dark.svg": build_lockup_stacked(dark=True),
        "wordmark.svg": build_wordmark(dark=False),
        "wordmark-dark.svg": build_wordmark(dark=True),
    }
    for name, body in files.items():
        (out_dir / name).write_text(body)
        print(f"  ✓ {name}  ({len(body)} bytes)")


if __name__ == "__main__":
    import sys
    out = Path(sys.argv[1]) if len(sys.argv) > 1 else Path("masters")
    main(out)
