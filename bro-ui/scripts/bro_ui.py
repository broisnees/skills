#!/usr/bin/env python3
"""bro-ui calculator. Standard library only.

  python3 bro_ui.py contrast FG BG [FG BG ...]   WCAG 2.2 contrast ratio and pass/fail
  python3 bro_ui.py scale [--base 16] [--ratio 1.25] [--down 2] [--up 5]
  python3 bro_ui.py ramp HUE [--chroma 0.15] [--steps 11]   OKLCH ramp as hex, with contrast
  python3 bro_ui.py oklch HEX [HEX ...]          hex to oklch()
  python3 bro_ui.py spring [--stiffness 400] [--damping 40] [--mass 1]
  python3 bro_ui.py fitts DISTANCE WIDTH [WIDTH ...] [--b 150]
  python3 bro_ui.py hick N [N ...] [--b 150]
  python3 bro_ui.py radius OUTER PADDING

Every formula is in references/math.md.
"""
import argparse
import math
import sys


# ---------- color ----------

def hex_to_rgb(h):
    h = h.strip().lstrip("#")
    if len(h) == 3:
        h = "".join(c * 2 for c in h)
    if len(h) != 6:
        raise ValueError(f"not a hex color: #{h}")
    return tuple(int(h[i:i + 2], 16) / 255 for i in (0, 2, 4))


def rgb_to_hex(rgb):
    return "#" + "".join(f"{round(max(0, min(1, c)) * 255):02x}" for c in rgb)


def to_linear(c):
    return c / 12.92 if c <= 0.04045 else ((c + 0.055) / 1.055) ** 2.4


def to_gamma(c):
    return 12.92 * c if c <= 0.0031308 else 1.055 * c ** (1 / 2.4) - 0.055


def luminance(rgb):
    r, g, b = (to_linear(c) for c in rgb)
    return 0.2126 * r + 0.7152 * g + 0.0722 * b


def contrast(a, b):
    la, lb = luminance(a), luminance(b)
    hi, lo = max(la, lb), min(la, lb)
    return (hi + 0.05) / (lo + 0.05)


def oklch_to_linear_rgb(L, C, H):
    a = C * math.cos(math.radians(H))
    b = C * math.sin(math.radians(H))
    l_ = (L + 0.3963377774 * a + 0.2158037573 * b) ** 3
    m_ = (L - 0.1055613458 * a - 0.0638541728 * b) ** 3
    s_ = (L - 0.0894841775 * a - 1.2914855480 * b) ** 3
    return (
        4.0767416621 * l_ - 3.3077115913 * m_ + 0.2309699292 * s_,
        -1.2684380046 * l_ + 2.6097574011 * m_ - 0.3413193965 * s_,
        -0.0041960863 * l_ - 0.7034186147 * m_ + 1.7076147010 * s_,
    )


def in_gamut(lin, eps=1e-6):
    return all(-eps <= c <= 1 + eps for c in lin)


def oklch_to_srgb(L, C, H):
    """Clamp to sRGB by lowering chroma (binary search), keeping L and H."""
    lin = oklch_to_linear_rgb(L, C, H)
    if not in_gamut(lin):
        lo, hi = 0.0, C
        for _ in range(30):
            mid = (lo + hi) / 2
            if in_gamut(oklch_to_linear_rgb(L, mid, H)):
                lo = mid
            else:
                hi = mid
        C = lo
        lin = oklch_to_linear_rgb(L, C, H)
    return tuple(to_gamma(max(0.0, min(1.0, c))) for c in lin), C


def srgb_to_oklch(rgb):
    r, g, b = (to_linear(c) for c in rgb)
    l_ = (0.4122214708 * r + 0.5363325363 * g + 0.0514459929 * b) ** (1 / 3)
    m_ = (0.2119034982 * r + 0.6806995451 * g + 0.1073969566 * b) ** (1 / 3)
    s_ = (0.0883024619 * r + 0.2817188376 * g + 0.6299787005 * b) ** (1 / 3)
    L = 0.2104542553 * l_ + 0.7936177850 * m_ - 0.0040720468 * s_
    A = 1.9779984951 * l_ - 2.4285922050 * m_ + 0.4505937099 * s_
    B = 0.0259040371 * l_ + 0.7827717662 * m_ - 0.8086757660 * s_
    C = math.hypot(A, B)
    H = math.degrees(math.atan2(B, A)) % 360 if C > 1e-4 else 0.0
    return L, C, H


def grade(ratio):
    if ratio >= 7:
        return "AAA text"
    if ratio >= 4.5:
        return "AA text"
    if ratio >= 3:
        return "large text / UI only"
    return "FAIL"


def cmd_contrast(a):
    if len(a.colors) % 2:
        sys.exit("contrast takes pairs: FG BG [FG BG ...]")
    for fg, bg in zip(a.colors[::2], a.colors[1::2]):
        r = contrast(hex_to_rgb(fg), hex_to_rgb(bg))
        print(f"{fg:>9} on {bg:<9} {r:5.2f}:1  {grade(r)}")


def cmd_oklch(a):
    for h in a.colors:
        L, C, H = srgb_to_oklch(hex_to_rgb(h))
        print(f"{h:>9}  oklch({L * 100:.1f}% {C:.3f} {H:.1f})")


def cmd_ramp(a):
    white, black = (1, 1, 1), (0, 0, 0)
    n = a.steps
    names = [50, 100, 200, 300, 400, 500, 600, 700, 800, 900, 950] if n == 11 else list(range(1, n + 1))
    print(f"OKLCH ramp, hue {a.hue}, peak chroma {a.chroma}")
    print(f"{'step':>5}  {'L':>5}  {'C':>5}  {'hex':<8} {'vs white':>9} {'vs black':>9}")
    for i in range(n):
        t = i / (n - 1)
        L = a.light - (a.light - a.dark) * t
        # chroma peaks mid-ramp and falls toward white and black (rule 8)
        C = a.chroma * max(0.08, 4 * t * (1 - t)) ** 0.6
        rgb, C_used = oklch_to_srgb(L, C, a.hue)
        print(f"{names[i]:>5}  {L:5.3f}  {C_used:5.3f}  {rgb_to_hex(rgb):<8} "
              f"{contrast(rgb, white):8.2f}:1 {contrast(rgb, black):8.2f}:1")


def cmd_scale(a):
    print(f"type scale: base {a.base}px x {a.ratio}^n (rule 3)")
    for n in range(a.up, -a.down - 1, -1):
        size = a.base * a.ratio ** n
        lh = 1.2 if n >= 2 else 1.5
        print(f"  n={n:+d}  {size:7.2f}px  use {round(size):>3}px  line-height {lh}")


def cmd_spring(a):
    k, c, m = a.stiffness, a.damping, a.mass
    w0 = math.sqrt(k / m)
    z = c / (2 * math.sqrt(k * m))
    print(f"stiffness k={k}  damping c={c}  mass m={m}")
    print(f"natural frequency w0 = sqrt(k/m) = {w0:.2f} rad/s")
    print(f"damping ratio zeta = c / (2 sqrt(km)) = {z:.3f}")
    if z < 1:
        os = math.exp(-z * math.pi / math.sqrt(1 - z * z)) * 100
        print(f"underdamped: overshoot {os:.2f}%  ({'fine for UI' if os < 2 else 'visible bounce'})")
        settle = 4 / (z * w0)
    elif abs(z - 1) < 1e-9:
        print("critically damped: no overshoot, fastest settle without bounce")
        settle = 5.8 / w0
    else:
        print("overdamped: no overshoot, slower than zeta = 1")
        settle = 4 / (w0 * (z - math.sqrt(z * z - 1)))
    print(f"settle time (within 2%) about {settle * 1000:.0f} ms")
    crit = 2 * math.sqrt(k * m)
    print(f"for zeta=1 use damping {crit:.1f}; for zeta=0.8 use {0.8 * crit:.1f}")


def cmd_fitts(a):
    print(f"Fitts: MT = a + b log2(D/W + 1), b = {a.b} ms/bit, D = {a.distance}px")
    base = None
    for w in a.widths:
        idx = math.log2(a.distance / w + 1)
        t = a.b * idx
        extra = "" if base is None else f"  ({base - t:.0f} ms faster than W={a.widths[0]:g})"
        base = t if base is None else base
        print(f"  W={w:>4}px  ID={idx:.2f} bits  ~{t:.0f} ms + a{extra}")


def cmd_hick(a):
    print(f"Hick: RT = a + b log2(n + 1), b = {a.b} ms/bit")
    for n in a.counts:
        bits = math.log2(n + 1)
        print(f"  n={n:>3}  {bits:.2f} bits  ~{a.b * bits:.0f} ms + a")


def cmd_radius(a):
    inner = a.outer - a.padding
    print(f"inner radius = {a.outer} - {a.padding} = {max(0, inner)}px"
          + ("  (padding exceeds radius: use 0 or a small fixed radius)" if inner <= 0 else ""))


def main():
    p = argparse.ArgumentParser(description="bro-ui calculator")
    sub = p.add_subparsers(dest="cmd", required=True)

    s = sub.add_parser("contrast"); s.add_argument("colors", nargs="+"); s.set_defaults(f=cmd_contrast)
    s = sub.add_parser("oklch"); s.add_argument("colors", nargs="+"); s.set_defaults(f=cmd_oklch)
    s = sub.add_parser("ramp"); s.add_argument("hue", type=float)
    s.add_argument("--chroma", type=float, default=0.15); s.add_argument("--steps", type=int, default=11)
    s.add_argument("--light", type=float, default=0.97); s.add_argument("--dark", type=float, default=0.25)
    s.set_defaults(f=cmd_ramp)
    s = sub.add_parser("scale"); s.add_argument("--base", type=float, default=16)
    s.add_argument("--ratio", type=float, default=1.25); s.add_argument("--down", type=int, default=2)
    s.add_argument("--up", type=int, default=5); s.set_defaults(f=cmd_scale)
    s = sub.add_parser("spring"); s.add_argument("--stiffness", type=float, default=400)
    s.add_argument("--damping", type=float, default=40); s.add_argument("--mass", type=float, default=1)
    s.set_defaults(f=cmd_spring)
    s = sub.add_parser("fitts"); s.add_argument("distance", type=float); s.add_argument("widths", type=float, nargs="+")
    s.add_argument("--b", type=float, default=150); s.set_defaults(f=cmd_fitts)
    s = sub.add_parser("hick"); s.add_argument("counts", type=int, nargs="+")
    s.add_argument("--b", type=float, default=150); s.set_defaults(f=cmd_hick)
    s = sub.add_parser("radius"); s.add_argument("outer", type=float); s.add_argument("padding", type=float)
    s.set_defaults(f=cmd_radius)

    a = p.parse_args()
    a.f(a)


if __name__ == "__main__":
    main()
