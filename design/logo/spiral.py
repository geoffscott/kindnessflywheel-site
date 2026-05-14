"""
spiral.py — logo geometry library for The Kindness Flywheel.

Single source of truth for the Compounding Spiral mark. Produces:
- SVG path data (for masters)
- ReportLab-rendered specimens (for exploration PDFs)
- High-DPI PNG exports (for OG cards and rasterized assets)

The spiral is a logarithmic spiral, r = a · exp(b · θ), drawn as a
variable-width ribbon. All parameters are exposed; defaults match the
approved design (b=0.20, 2.3 revolutions).

To retune the production mark, edit the PRODUCTION_SPIRAL constant
below and rerun `python -m brand.build_all`.
"""
from __future__ import annotations
from dataclasses import dataclass, field
import math
from typing import Sequence, Tuple

Point = Tuple[float, float]


@dataclass(frozen=True)
class Spiral:
    """Configuration for a single spiral mark."""
    # Geometry
    growth_b: float = 0.20            # logarithmic growth rate
    revolutions: float = 2.3          # number of full turns
    start_phase_deg: float = 180.0    # rotation offset (180 = opens to the right)

    # Stroke
    stroke_start: float = 0.6         # inner-end stroke width (in spiral-units)
    stroke_end_factor: float = 0.075  # outer-end stroke width = R_max * this

    # Render quality
    samples: int = 700                # path resolution

    # Terminus dot
    show_terminus_dot: bool = True
    terminus_dot_factor: float = 0.55  # dot radius = end_stroke_width * this

    def points(self, cx: float, cy: float, R_max: float,
               y_flip: bool = False) -> Tuple[list, list]:
        """
        Return (centerline_points, half_widths) for the spiral fit inside R_max.

        Centerline is sampled along the spiral; half_widths is the
        ribbon half-width at each sample (for offset curve construction).

        y_flip: if True, flips the y-axis convention (use for SVG, where
        y increases downward; PDF/reportlab use y-up).
        """
        theta_max = self.revolutions * 2 * math.pi
        a = R_max / math.exp(self.growth_b * theta_max)
        phi = math.radians(self.start_phase_deg)

        end_stroke = R_max * self.stroke_end_factor
        pts: list[Point] = []
        widths: list[float] = []
        sy = -1.0 if y_flip else 1.0
        for i in range(self.samples + 1):
            t = i / self.samples
            theta = t * theta_max
            r = a * math.exp(self.growth_b * theta)
            x = cx + r * math.cos(theta + phi)
            y = cy + sy * r * math.sin(theta + phi)
            pts.append((x, y))
            w = self.stroke_start + (end_stroke - self.stroke_start) * t
            widths.append(w / 2)
        return pts, widths

    def offset_curves(self, cx: float, cy: float, R_max: float,
                      y_flip: bool = False) -> Tuple[list, list]:
        """Return (outer_curve, inner_curve) — parallel offsets of the centerline."""
        pts, hw = self.points(cx, cy, R_max, y_flip=y_flip)
        N = len(pts) - 1
        outer: list[Point] = []
        inner: list[Point] = []
        for i, (x, y) in enumerate(pts):
            if i == 0:
                tx, ty = pts[1][0] - pts[0][0], pts[1][1] - pts[0][1]
            elif i == N:
                tx, ty = pts[N][0] - pts[N - 1][0], pts[N][1] - pts[N - 1][1]
            else:
                tx, ty = pts[i + 1][0] - pts[i - 1][0], pts[i + 1][1] - pts[i - 1][1]
            L = math.hypot(tx, ty) or 1.0
            nx, ny = -ty / L, tx / L
            outer.append((x + nx * hw[i], y + ny * hw[i]))
            inner.append((x - nx * hw[i], y - ny * hw[i]))
        return outer, inner

    def terminus(self, cx: float, cy: float, R_max: float,
                 y_flip: bool = False) -> Tuple[Point, float]:
        """Return (point, radius) for the terminus dot."""
        pts, hw = self.points(cx, cy, R_max, y_flip=y_flip)
        end_stroke = R_max * self.stroke_end_factor
        r = max(1.4, end_stroke * self.terminus_dot_factor)
        return pts[-1], r

    def svg_path_d(self, cx: float, cy: float, R_max: float) -> str:
        """Return the `d` attribute for the ribbon as a closed SVG path.
        Uses SVG y-down convention automatically."""
        outer, inner = self.offset_curves(cx, cy, R_max, y_flip=True)
        parts: list[str] = []
        parts.append(f"M {outer[0][0]:.3f} {outer[0][1]:.3f}")
        for x, y in outer[1:]:
            parts.append(f"L {x:.3f} {y:.3f}")
        for x, y in reversed(inner):
            parts.append(f"L {x:.3f} {y:.3f}")
        parts.append("Z")
        return " ".join(parts)


# ─────────────────────────────────────────────────────────────────────
# PRODUCTION CONFIGURATION
# This is the approved spiral. Edit here and rebuild everything to retune.
# ─────────────────────────────────────────────────────────────────────
PRODUCTION_SPIRAL = Spiral(
    growth_b=0.20,
    revolutions=2.3,
    start_phase_deg=180.0,
    stroke_start=0.6,
    stroke_end_factor=0.075,
    samples=700,
    show_terminus_dot=True,
    terminus_dot_factor=0.55,
)


# ─────────────────────────────────────────────────────────────────────
# BRAND COLORS — single source of truth, mirrored in tokens.yml
# ─────────────────────────────────────────────────────────────────────
COLORS = {
    "ink": "#2A2250",       # deep indigo — primary mark and type
    "accent": "#D95F3B",    # warm coral — terminus dot and accents
    "ground_warm": "#F8F5F0",   # warm light — primary background
    "ground_white": "#FFFFFF",
    "ground_dark": "#13102A",   # very dark indigo — dark mode ground
    "ink_dark": "#F8F5F0",      # warm light — mark on dark backgrounds
    "subtle": "#5A5670",        # muted text
}
