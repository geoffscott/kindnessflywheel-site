"""
explore_spiral.py — generates a multi-page exploration PDF showing six
candidate expressions of the Compounding Spiral.

Each candidate is a legitimate design choice with a different feel:
  01. Specimen  — the approved production mark, full plate
  02. Naked     — no terminus dot, pure form
  03. Mono      — monochrome, no accent; how it reads in single-color
  04. Inverted  — light-on-dark, dark mode preview
  05. Open      — terminus extended into an open tail (more dynamic)
  06. Inked     — heavier stroke, more presence at large scale

The page chrome is restrained — engineering plate aesthetic, same as
the original lookbook. Each plate is one decision the designer must
make: do we keep the dot, do we extend the tail, etc.
"""
from __future__ import annotations
from dataclasses import replace
from pathlib import Path
import math
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
from reportlab.lib.colors import HexColor
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont

from spiral import PRODUCTION_SPIRAL, COLORS, Spiral

FONT_DIR = "/mnt/skills/examples/canvas-design/canvas-fonts"
PW, PH = letter

INK = HexColor(COLORS["ink"])
ACC = HexColor(COLORS["accent"])
BG = HexColor(COLORS["ground_warm"])
SUB = HexColor(COLORS["subtle"])
DARK = HexColor(COLORS["ground_dark"])
LIGHT = HexColor(COLORS["ink_dark"])  # warm light, for inverted mark


def register_fonts():
    pdfmetrics.registerFont(TTFont("Bricolage", f"{FONT_DIR}/BricolageGrotesque-Regular.ttf"))
    pdfmetrics.registerFont(TTFont("Bricolage-B", f"{FONT_DIR}/BricolageGrotesque-Bold.ttf"))
    pdfmetrics.registerFont(TTFont("InstSans", f"{FONT_DIR}/InstrumentSans-Regular.ttf"))
    pdfmetrics.registerFont(TTFont("InstSerif", f"{FONT_DIR}/InstrumentSerif-Regular.ttf"))
    pdfmetrics.registerFont(TTFont("InstSerif-I", f"{FONT_DIR}/InstrumentSerif-Italic.ttf"))
    pdfmetrics.registerFont(TTFont("Mono", f"{FONT_DIR}/JetBrainsMono-Bold.ttf"))


# ─────────────────────────────────────────────────────────────────────
# Drawing primitives
# ─────────────────────────────────────────────────────────────────────
def draw_spiral(c, spiral: Spiral, cx, cy, R_max, ink_color, accent_color,
                show_dot: bool = True):
    """Render a configured spiral to the canvas."""
    outer, inner = spiral.offset_curves(cx, cy, R_max)
    p = c.beginPath()
    p.moveTo(*outer[0])
    for x, y in outer[1:]:
        p.lineTo(x, y)
    for x, y in reversed(inner):
        p.lineTo(x, y)
    p.close()
    c.setFillColor(ink_color)
    c.drawPath(p, fill=1, stroke=0)
    if show_dot and spiral.show_terminus_dot:
        (tx, ty), tr = spiral.terminus(cx, cy, R_max)
        c.setFillColor(accent_color)
        c.circle(tx, ty, tr, fill=1, stroke=0)


def draw_open_tail(c, spiral: Spiral, cx, cy, R_max, ink_color, accent_color,
                   extend_deg: float = 25, taper_factor: float = 0.35):
    """
    Draw the spiral with an extended open tail at the terminus — the ribbon
    continues past R_max along the tangent direction, tapering to a point.

    The tail is a triangle from the last ribbon edge points, with the apex
    extended along the local tangent. This reads as a stylus mid-stroke.
    """
    # Draw the main ribbon (no dot)
    draw_spiral(c, spiral, cx, cy, R_max, ink_color, accent_color, show_dot=False)

    # Extend tail
    outer, inner = spiral.offset_curves(cx, cy, R_max)
    pts, _ = spiral.points(cx, cy, R_max)
    # Tangent at the end
    n = len(pts)
    tx = pts[n - 1][0] - pts[n - 2][0]
    ty = pts[n - 1][1] - pts[n - 2][1]
    L = math.hypot(tx, ty) or 1.0
    tx, ty = tx / L, ty / L

    # The local arc length to extend = arc length corresponding to extend_deg
    # in the spiral's outer turn. Approximate as fraction of R_max.
    extend_len = R_max * (extend_deg / 360.0) * 2 * math.pi * 0.4

    # Apex point
    apex = (pts[-1][0] + tx * extend_len, pts[-1][1] + ty * extend_len)

    # Build a tapering tail from outer/inner endpoints to the apex
    p = c.beginPath()
    p.moveTo(*outer[-1])
    p.lineTo(*apex)
    p.lineTo(*inner[-1])
    p.close()
    c.setFillColor(ink_color)
    c.drawPath(p, fill=1, stroke=0)

    # Small accent at the apex
    c.setFillColor(accent_color)
    c.circle(apex[0], apex[1], R_max * 0.025, fill=1, stroke=0)


# ─────────────────────────────────────────────────────────────────────
# Page chrome
# ─────────────────────────────────────────────────────────────────────
def draw_frame(c, bg, ink, spec_no, title_kicker, geom_label):
    c.setFillColor(bg)
    c.rect(0, 0, PW, PH, fill=1, stroke=0)
    c.setStrokeColor(ink)
    c.setLineWidth(0.4)
    c.line(54, PH - 54, PW - 54, PH - 54)
    c.setFillColor(ink)
    c.setFont("InstSans", 7.5)
    c.drawString(54, PH - 46, "THE KINDNESS FLYWHEEL  ·  SPIRAL EXPLORATION")
    c.setFont("Mono", 7.5)
    c.drawRightString(PW - 54, PH - 46, spec_no)
    c.setFont("InstSerif-I", 11)
    c.drawString(54, PH - 78, title_kicker)
    c.line(54, 60, PW - 54, 60)
    c.setFont("Mono", 6.5)
    c.drawString(54, 48, geom_label)
    c.drawRightString(PW - 54, 48, "kindnessflywheel.org")
    # Corner ticks
    c.setLineWidth(0.3)
    for (x, y) in [(54, PH - 54), (PW - 54, PH - 54), (54, 60), (PW - 54, 60)]:
        c.line(x - 4, y, x + 4, y)
        c.line(x, y - 4, x, y + 4)


def draw_caption_block(c, name, num_label, concept_lines, ink, accent, sub):
    cap_x = 360
    cap_y = PH - 110

    c.setFillColor(accent)
    c.setFont("Mono", 7)
    c.drawString(cap_x, cap_y, f"▍ CANDIDATE  {num_label}")

    c.setFillColor(ink)
    c.setFont("Bricolage-B", 22)
    c.drawString(cap_x, cap_y - 28, name)

    c.setStrokeColor(ink)
    c.setLineWidth(0.4)
    c.line(cap_x, cap_y - 40, PW - 54, cap_y - 40)

    c.setFillColor(sub if sub else ink)
    c.setFont("InstSerif", 10.5)
    cur_y = cap_y - 60
    for line in concept_lines:
        c.drawString(cap_x, cur_y, line)
        cur_y -= 14
    return cur_y


# ─────────────────────────────────────────────────────────────────────
# Page builders — six candidates
# ─────────────────────────────────────────────────────────────────────
def page_specimen(c):
    """01 — The approved production mark."""
    draw_frame(c, BG, INK, "01 / 06",
               "The approved mark — variable-weight ribbon, coral terminus.",
               "GEOM   b=0.20   ·   REVS=2.3   ·   TERMINUS  coral dot")

    # Plate
    c.setFillColor(HexColor("#F1ECE3"))
    c.roundRect(74, PH/2 - 130, 252, 320, 4, fill=1, stroke=0)

    draw_spiral(c, PRODUCTION_SPIRAL, 200, PH/2 + 30, 95, INK, ACC)

    # Construction rings
    c.setStrokeColor(INK)
    c.setLineWidth(0.2)
    c.setDash(1, 3)
    for r in [30, 60, 90]:
        c.circle(200, PH/2 + 30, r, fill=0, stroke=1)
    c.setDash()

    # Favicon row
    sizes_y = PH/2 - 100
    c.setFillColor(INK)
    c.setFont("Mono", 6)
    c.drawString(94, sizes_y + 28, "FAVICON  ·  32px      16px")
    draw_spiral(c, PRODUCTION_SPIRAL, 110, sizes_y, 13, INK, ACC)
    draw_spiral(c, PRODUCTION_SPIRAL, 150, sizes_y, 7, INK, ACC)

    draw_caption_block(c, "Specimen", "production",
        ["The mark as it currently stands. Variable-weight",
         "ribbon, ~2.3 revolutions, coral period at the terminus.",
         "Reads as compounding, momentum, patient care.",
         "",
         "Use this if the brief is satisfied as-is."],
        INK, ACC, SUB)
    c.showPage()


def page_naked(c):
    """02 — No terminus dot, pure form."""
    draw_frame(c, BG, INK, "02 / 06",
               "Without the period — geometry alone, no accent.",
               "GEOM   b=0.20   ·   REVS=2.3   ·   TERMINUS  none")

    c.setFillColor(HexColor("#F1ECE3"))
    c.roundRect(74, PH/2 - 130, 252, 320, 4, fill=1, stroke=0)

    naked = replace(PRODUCTION_SPIRAL, show_terminus_dot=False)
    draw_spiral(c, naked, 200, PH/2 + 30, 95, INK, ACC)

    sizes_y = PH/2 - 100
    c.setFillColor(INK)
    c.setFont("Mono", 6)
    c.drawString(94, sizes_y + 28, "FAVICON  ·  32px      16px")
    draw_spiral(c, naked, 110, sizes_y, 13, INK, ACC)
    draw_spiral(c, naked, 150, sizes_y, 7, INK, ACC)

    draw_caption_block(c, "Naked", "no-dot",
        ["The terminus dot removed. The mark is pure form,",
         "all geometry, no decoration. The taper does the",
         "work the dot was doing.",
         "",
         "More austere. Less warmth. Easier to engrave,",
         "embroider, or render in single-color contexts.",
         "Stronger at small sizes — one less detail to lose."],
        INK, ACC, SUB)
    c.showPage()


def page_mono(c):
    """03 — Monochrome, terminus as a small uncolored circle."""
    draw_frame(c, BG, INK, "03 / 06",
               "Single-color — terminus rendered in ink, not accent.",
               "GEOM   b=0.20   ·   REVS=2.3   ·   TERMINUS  ink (mono)")

    c.setFillColor(HexColor("#F1ECE3"))
    c.roundRect(74, PH/2 - 130, 252, 320, 4, fill=1, stroke=0)

    draw_spiral(c, PRODUCTION_SPIRAL, 200, PH/2 + 30, 95, INK, INK)

    sizes_y = PH/2 - 100
    c.setFillColor(INK)
    c.setFont("Mono", 6)
    c.drawString(94, sizes_y + 28, "FAVICON  ·  32px      16px")
    draw_spiral(c, PRODUCTION_SPIRAL, 110, sizes_y, 13, INK, INK)
    draw_spiral(c, PRODUCTION_SPIRAL, 150, sizes_y, 7, INK, INK)

    draw_caption_block(c, "Mono", "ink-only",
        ["The mark in a single color. Terminus dot is",
         "still present but rendered in the ink color,",
         "so it reads as part of the form, not an accent.",
         "",
         "This is the version that ships everywhere coral",
         "can't go: faxes, photocopies, engravings, embossed",
         "stationery, anything one-color."],
        INK, ACC, SUB)
    c.showPage()


def page_inverted(c):
    """04 — Dark mode preview."""
    draw_frame(c, DARK, LIGHT, "04 / 06",
               "Dark-on-light inverted to light-on-dark — readable both ways.",
               "GEOM   b=0.20   ·   REVS=2.3   ·   GROUND  dark indigo")

    # Plate on the dark background — slightly lighter than ground
    c.setFillColor(HexColor("#1A1638"))
    c.roundRect(74, PH/2 - 130, 252, 320, 4, fill=1, stroke=0)

    draw_spiral(c, PRODUCTION_SPIRAL, 200, PH/2 + 30, 95, LIGHT, ACC)

    sizes_y = PH/2 - 100
    c.setFillColor(LIGHT)
    c.setFont("Mono", 6)
    c.drawString(94, sizes_y + 28, "FAVICON  ·  32px      16px")
    draw_spiral(c, PRODUCTION_SPIRAL, 110, sizes_y, 13, LIGHT, ACC)
    draw_spiral(c, PRODUCTION_SPIRAL, 150, sizes_y, 7, LIGHT, ACC)

    # Caption block on dark ground
    cap_x = 360
    cap_y = PH - 110
    c.setFillColor(ACC)
    c.setFont("Mono", 7)
    c.drawString(cap_x, cap_y, "▍ CANDIDATE  dark-mode")
    c.setFillColor(LIGHT)
    c.setFont("Bricolage-B", 22)
    c.drawString(cap_x, cap_y - 28, "Inverted")
    c.setStrokeColor(LIGHT)
    c.setLineWidth(0.4)
    c.line(cap_x, cap_y - 40, PW - 54, cap_y - 40)
    c.setFillColor(LIGHT)
    c.setFont("InstSerif", 10.5)
    for i, line in enumerate([
        "The mark on a dark indigo ground, with the spiral",
        "rendered in warm light. The coral terminus reads",
        "more vividly against the dark.",
        "",
        "This is the dark-mode variant that ships alongside",
        "the primary. The site stylesheet swaps to this",
        "automatically via prefers-color-scheme."]):
        c.drawString(cap_x, cap_y - 60 - i * 14, line)
    c.showPage()


def page_open(c):
    """05 — Open tail extension, more dynamic."""
    draw_frame(c, BG, INK, "05 / 06",
               "Open tail — the spiral continues past the terminus, mid-stroke.",
               "GEOM   b=0.20   ·   REVS=2.3   ·   TAIL  +25° tangent extension")

    c.setFillColor(HexColor("#F1ECE3"))
    c.roundRect(74, PH/2 - 130, 252, 320, 4, fill=1, stroke=0)

    draw_open_tail(c, PRODUCTION_SPIRAL, 200, PH/2 + 30, 95, INK, ACC)

    sizes_y = PH/2 - 100
    c.setFillColor(INK)
    c.setFont("Mono", 6)
    c.drawString(94, sizes_y + 28, "FAVICON  ·  32px      16px")
    draw_open_tail(c, PRODUCTION_SPIRAL, 110, sizes_y, 13, INK, ACC)
    draw_open_tail(c, PRODUCTION_SPIRAL, 150, sizes_y, 7, INK, ACC)

    draw_caption_block(c, "Open", "tail-extension",
        ["The terminus extends along the tangent, tapering",
         "to a point with a small accent at the apex. The",
         "mark reads as mid-stroke — still being drawn.",
         "",
         "More kinetic. Less contained. Says \"in progress\"",
         "more loudly than the closed version. Risks: less",
         "stable at small sizes; the tail can disappear."],
        INK, ACC, SUB)
    c.showPage()


def page_inked(c):
    """06 — Heavier stroke for poster/billboard presence."""
    draw_frame(c, BG, INK, "06 / 06",
               "Heavier stroke — for poster and large-format presence.",
               "GEOM   b=0.20   ·   REVS=2.3   ·   STROKE  end_factor=0.11")

    c.setFillColor(HexColor("#F1ECE3"))
    c.roundRect(74, PH/2 - 130, 252, 320, 4, fill=1, stroke=0)

    inked = replace(PRODUCTION_SPIRAL,
                    stroke_start=1.2,
                    stroke_end_factor=0.11)
    draw_spiral(c, inked, 200, PH/2 + 30, 95, INK, ACC)

    sizes_y = PH/2 - 100
    c.setFillColor(INK)
    c.setFont("Mono", 6)
    c.drawString(94, sizes_y + 28, "FAVICON  ·  32px      16px")
    draw_spiral(c, inked, 110, sizes_y, 13, INK, ACC)
    draw_spiral(c, inked, 150, sizes_y, 7, INK, ACC)

    draw_caption_block(c, "Inked", "heavy-stroke",
        ["A heavier-weight version of the mark — same",
         "geometry, thicker ribbon (~50% more mass at",
         "the outer terminus).",
         "",
         "For posters, book covers, conference signage —",
         "any large-format context where the lighter mark",
         "feels under-weighted against ambient noise. Use",
         "the production weight for screen, this for print."],
        INK, ACC, SUB)
    c.showPage()


# ─────────────────────────────────────────────────────────────────────
# Cover page
# ─────────────────────────────────────────────────────────────────────
def page_cover(c):
    c.setFillColor(BG)
    c.rect(0, 0, PW, PH, fill=1, stroke=0)

    c.setStrokeColor(INK)
    c.setLineWidth(0.4)
    c.line(54, PH - 54, PW - 54, PH - 54)
    c.setFillColor(INK)
    c.setFont("InstSans", 7.5)
    c.drawString(54, PH - 46, "THE KINDNESS FLYWHEEL  ·  SPIRAL EXPLORATION")
    c.setFont("Mono", 7.5)
    c.drawRightString(PW - 54, PH - 46, "INDEX")
    c.setLineWidth(0.3)
    for (x, y) in [(54, PH - 54), (PW - 54, PH - 54), (54, 60), (PW - 54, 60)]:
        c.line(x - 4, y, x + 4, y)
        c.line(x, y - 4, x, y + 4)

    # Title
    c.setFillColor(INK)
    c.setFont("Bricolage-B", 60)
    c.drawString(54, PH - 210, "Spiral.")

    c.setFillColor(SUB)
    c.setFont("InstSerif-I", 18)
    c.drawString(54, PH - 245, "Six expressions of one mark.")

    # Body
    c.setFillColor(INK)
    c.setFont("InstSerif", 11.5)
    intro = [
        "Each candidate is a legitimate version of the Compounding Spiral.",
        "Same growth rate, same revolutions, same geometric DNA. What",
        "varies: the terminus, the color treatment, the stroke weight,",
        "the question of whether the tail closes or stays open.",
        "",
        "These are decisions, not failed experiments. Pick the one",
        "that fits the surface it's living on — or pick a primary",
        "and let the others serve specific use cases.",
    ]
    y = PH - 280
    for line in intro:
        c.drawString(54, y, line)
        y -= 16

    # Index — six small thumbnails
    candidates = [
        ("01", "Specimen", "Production mark, full color.", "spec"),
        ("02", "Naked", "No terminus dot, pure form.", "naked"),
        ("03", "Mono", "Single-color, no accent.", "mono"),
        ("04", "Inverted", "Light-on-dark, dark mode.", "inv"),
        ("05", "Open", "Tangent tail, mid-stroke.", "open"),
        ("06", "Inked", "Heavier stroke for poster scale.", "ink"),
    ]
    y_index = PH - 460
    c.setStrokeColor(INK)
    c.setLineWidth(0.4)
    c.line(54, y_index + 20, PW - 54, y_index + 20)

    for i, (num, name, blurb, kind) in enumerate(candidates):
        row_y = y_index - 18 - i * 48

        c.setFillColor(INK)
        c.setFont("Mono", 9)
        c.drawString(54, row_y + 8, num)
        c.setFont("Bricolage-B", 16)
        c.drawString(94, row_y + 10, name)
        c.setFillColor(SUB)
        c.setFont("InstSerif-I", 10.5)
        c.drawString(94, row_y - 6, blurb)

        # Thumbnail
        tx = PW - 130
        ty = row_y + 5
        if kind == "spec":
            draw_spiral(c, PRODUCTION_SPIRAL, tx, ty, 18, INK, ACC)
        elif kind == "naked":
            draw_spiral(c, replace(PRODUCTION_SPIRAL, show_terminus_dot=False),
                        tx, ty, 18, INK, ACC)
        elif kind == "mono":
            draw_spiral(c, PRODUCTION_SPIRAL, tx, ty, 18, INK, INK)
        elif kind == "inv":
            # Need dark patch for this thumbnail
            c.setFillColor(DARK)
            c.rect(tx - 24, ty - 22, 48, 44, fill=1, stroke=0)
            draw_spiral(c, PRODUCTION_SPIRAL, tx, ty, 18, LIGHT, ACC)
        elif kind == "open":
            draw_open_tail(c, PRODUCTION_SPIRAL, tx, ty, 18, INK, ACC)
        elif kind == "ink":
            draw_spiral(c,
                replace(PRODUCTION_SPIRAL, stroke_start=1.2, stroke_end_factor=0.11),
                tx, ty, 18, INK, ACC)

        c.setStrokeColor(INK)
        c.setLineWidth(0.25)
        c.line(54, row_y - 14, PW - 54, row_y - 14)

    # Footer
    c.setLineWidth(0.4)
    c.line(54, 60, PW - 54, 60)
    c.setFillColor(INK)
    c.setFont("Mono", 6.5)
    c.drawString(54, 48, "GROWTH SCIENCE  /  GEOFF SCOTT  ·  CC-BY 4.0")
    c.drawRightString(PW - 54, 48, "kindnessflywheel.org")
    c.showPage()


# ─────────────────────────────────────────────────────────────────────
# Build
# ─────────────────────────────────────────────────────────────────────
def main(out_path: Path):
    register_fonts()
    c = canvas.Canvas(str(out_path), pagesize=letter)
    c.setTitle("The Kindness Flywheel — Spiral Exploration")
    c.setAuthor("Growth Science / Geoff Scott")
    page_cover(c)
    page_specimen(c)
    page_naked(c)
    page_mono(c)
    page_inverted(c)
    page_open(c)
    page_inked(c)
    c.save()
    print(f"Wrote {out_path}")


if __name__ == "__main__":
    import sys
    out = Path(sys.argv[1]) if len(sys.argv) > 1 else Path("spiral_exploration.pdf")
    main(out)
