"""
build_raster.py — generate PNG and PDF exports from SVG masters.

PNG sizes are chosen for the common contexts:
  - 1024: hi-res app icons, presentation hero shots
  - 512:  marketplace listings, GitHub social previews
  - 256:  app icons, Slack/Discord avatars
  - 32, 16: favicon raster fallbacks

PDF exports are vector and lossless — for print handoff.

OG image (1200x630) is generated separately because it has unique
composition (mark left, wordmark right, generous whitespace).
"""
from __future__ import annotations
from pathlib import Path
import math
from reportlab.pdfgen import canvas as rl_canvas
from reportlab.lib.colors import HexColor
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from PIL import Image
import cairosvg

from spiral import PRODUCTION_SPIRAL, COLORS


FONT_DIR = "/mnt/skills/examples/canvas-design/canvas-fonts"


def register_fonts():
    pdfmetrics.registerFont(TTFont("Bricolage", f"{FONT_DIR}/BricolageGrotesque-Regular.ttf"))
    pdfmetrics.registerFont(TTFont("Bricolage-B", f"{FONT_DIR}/BricolageGrotesque-Bold.ttf"))


# ─────────────────────────────────────────────────────────────────────
# SVG → PNG raster export
# ─────────────────────────────────────────────────────────────────────
def svg_to_png(svg_path: Path, png_path: Path, target_width: int,
               background: str | None = None):
    """Rasterize an SVG to PNG at the requested width."""
    kwargs = dict(url=str(svg_path), output_width=target_width)
    if background:
        kwargs["background_color"] = background
    cairosvg.svg2png(write_to=str(png_path), **kwargs)


def svg_to_pdf(svg_path: Path, pdf_path: Path):
    """Convert SVG to vector PDF."""
    cairosvg.svg2pdf(url=str(svg_path), write_to=str(pdf_path))


# ─────────────────────────────────────────────────────────────────────
# OG image — purpose-built composition for social cards
# ─────────────────────────────────────────────────────────────────────
def build_og_image(out_path: Path):
    """
    1200x630 Open Graph image. The card needs to:
    - Render the publication name unambiguously
    - Read at thumbnail scale (Twitter shows these small)
    - Use the warm light background, not pure white
    - Have safe margins (Facebook crops slightly)
    """
    register_fonts()
    W, H = 1200, 630
    c = rl_canvas.Canvas(str(out_path), pagesize=(W, H))

    # Background — warm light
    c.setFillColor(HexColor(COLORS["ground_warm"]))
    c.rect(0, 0, W, H, fill=1, stroke=0)

    # Subtle frame rule at top
    c.setStrokeColor(HexColor(COLORS["ink"]))
    c.setLineWidth(0.7)
    c.line(80, H - 80, W - 80, H - 80)

    # Spiral mark — left, sized for the masthead. R_max=130 gives a
    # visible diameter of 260; gap = 0.07 × 260 ≈ 18.
    R_max = 130
    cx, cy = 280, H / 2
    outer, inner = PRODUCTION_SPIRAL.offset_curves(cx, cy, R_max)
    p = c.beginPath()
    p.moveTo(*outer[0])
    for x, y in outer[1:]:
        p.lineTo(x, y)
    for x, y in reversed(inner):
        p.lineTo(x, y)
    p.close()
    c.setFillColor(HexColor(COLORS["ink"]))
    c.drawPath(p, fill=1, stroke=0)

    # Terminus dot
    (tx, ty), tr = PRODUCTION_SPIRAL.terminus(cx, cy, R_max)
    c.setFillColor(HexColor(COLORS["accent"]))
    c.circle(tx, ty, tr, fill=1, stroke=0)

    # Wordmark — B treatment. Both lines at the same point size, bold/regular.
    # Mark visible right edge: cx + R_max = 410. Gap = 0.07 × 260 ≈ 18.
    # Text starts at 410 + 18 = 428.
    # ReportLab y is bottom-up; for a tight two-line stack, baseline-to-
    # baseline distance ≈ font_size × 0.95.
    word_x = 428
    word_size = 84
    line_height = word_size * 0.95   # ~80
    # KINDNESS (top, bold) — baseline above center
    # FLYWHEEL (bottom, regular) — baseline line_height below KINDNESS
    # Optical center the block on H/2
    cap_height = word_size * 0.70
    block_visual = cap_height + line_height
    # Top of cap1 (KINDNESS) sits above H/2 by block_visual/2
    # So KINDNESS baseline = H/2 + block_visual/2 - cap_height
    line1_baseline_y = H / 2 + block_visual / 2 - cap_height
    line2_baseline_y = line1_baseline_y - line_height

    c.setFillColor(HexColor(COLORS["ink"]))
    c.setFont("Bricolage-B", word_size)
    c.drawString(word_x, line1_baseline_y, "KINDNESS")
    c.setFont("Bricolage", word_size)
    c.drawString(word_x, line2_baseline_y, "FLYWHEEL")

    # Subtitle — sits below the FLYWHEEL baseline with breathing room
    c.setFillColor(HexColor(COLORS["subtle"]))
    c.setFont("Bricolage", 22)
    c.drawString(word_x, line2_baseline_y - 40, "Human-centered leadership in the age of AI")

    # Footer URL
    c.setFillColor(HexColor(COLORS["ink"]))
    c.setFont("Bricolage", 18)
    c.drawString(80, 50, "kindnessflywheel.org")

    c.showPage()
    c.save()

    # Rasterize the PDF to PNG at 1200×630 exactly (OG card spec).
    from pdf2image import convert_from_path
    png_path = out_path.with_suffix(".png")
    images = convert_from_path(str(out_path), dpi=300)
    img = images[0].resize((1200, 630), Image.LANCZOS)
    img.save(str(png_path), "PNG", optimize=True)


# ─────────────────────────────────────────────────────────────────────
# Build orchestration
# ─────────────────────────────────────────────────────────────────────
def main(masters_dir: Path, exports_dir: Path):
    exports_dir.mkdir(parents=True, exist_ok=True)

    # Mark raster exports — multiple sizes, transparent and on-warm
    mark_svg = masters_dir / "mark.svg"
    for size in [1024, 512, 256, 64, 32, 16]:
        svg_to_png(mark_svg, exports_dir / f"mark-{size}.png", size)
        print(f"  ✓ mark-{size}.png")

    # Dark variant
    mark_dark_svg = masters_dir / "mark-dark.svg"
    for size in [1024, 512, 256]:
        svg_to_png(mark_dark_svg, exports_dir / f"mark-dark-{size}.png", size)
        print(f"  ✓ mark-dark-{size}.png")

    # Lockup exports
    for variant in ["lockup-horizontal", "lockup-stacked"]:
        for size in [1200, 600]:
            svg_to_png(masters_dir / f"{variant}.svg",
                       exports_dir / f"{variant}-{size}.png", size)
            print(f"  ✓ {variant}-{size}.png")
        # PDF for print
        svg_to_pdf(masters_dir / f"{variant}.svg",
                   exports_dir / f"{variant}.pdf")
        print(f"  ✓ {variant}.pdf")

    # Apple touch icon — 180x180, on warm background (Apple wants opaque)
    svg_to_png(mark_svg, exports_dir / "apple-touch-icon.png", 180,
               background=COLORS["ground_warm"])
    print(f"  ✓ apple-touch-icon.png")

    # OG image
    build_og_image(exports_dir / "og-image.pdf")
    print(f"  ✓ og-image.pdf + og-image.png")


if __name__ == "__main__":
    import sys
    masters = Path(sys.argv[1]) if len(sys.argv) > 1 else Path("masters")
    exports = Path(sys.argv[2]) if len(sys.argv) > 2 else Path("exports")
    main(masters, exports)
