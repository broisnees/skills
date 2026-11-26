# The math behind bro-ui

Every formula the rules cite, with a worked number. `scripts/bro_ui.py` computes all of them.

## Weber's law and the type scale (rule 3)

Weber's law: the smallest change a person notices is a fixed fraction of the starting value, ΔS / S = k. A 2px jump is obvious at 12px and invisible at 48px. So sizes that look evenly spaced grow by a ratio, not by a fixed amount:

```
size_n = base × r^n
```

| n | r = 1.2, base 16 | r = 1.25, base 16 |
|---|---|---|
| -2 | 11.11 → 11px | 10.24 → 10px |
| -1 | 13.33 → 13px | 12.80 → 13px |
| 0 | 16px | 16px |
| 1 | 19.20 → 19px | 20px |
| 2 | 23.04 → 23px | 25px |
| 3 | 27.65 → 28px | 31.25 → 31px |
| 4 | 33.18 → 33px | 39.06 → 39px |

```
python3 scripts/bro_ui.py scale --base 16 --ratio 1.2
```

Use 1.2 for dense apps, where many levels sit close together. Use 1.25 to 1.333 for pages, where headings need more jump. More than 5 sizes on one screen and the steps stop being distinguishable.

## WCAG contrast (rule 9)

1. Divide each sRGB channel by 255.
2. Linearize: `c ≤ 0.04045 ? c / 12.92 : ((c + 0.055) / 1.055)^2.4`.
3. Relative luminance: `L = 0.2126 R + 0.7152 G + 0.0722 B`. Green weighs most because the eye is most sensitive to it.
4. Ratio: `(L_lighter + 0.05) / (L_darker + 0.05)`. Range 1:1 to 21:1.

Worked: `#767676` on white. 118 / 255 = 0.4627. Linear = ((0.4627 + 0.055) / 1.055)^2.4 = 0.1812. Ratio = 1.05 / 0.2312 = **4.54:1**, which passes AA. One step lighter, `#777777`, is 4.48:1 and fails.

| Content | WCAG 2.2 AA |
|---|---|
| Body text | 4.5:1 (SC 1.4.3) |
| Large text: 24px and up, or 18.66px and up when bold | 3:1 |
| Control borders, icons, focus rings, chart lines | 3:1 against what is next to them (SC 1.4.11) |
| Disabled controls, logos | no requirement |

```
python3 scripts/bro_ui.py contrast 5d6068 f9fafc a6aab2 1e2024
```

## OKLCH (rule 8)

OKLCH has three axes: lightness L (0 to 1), chroma C (0 to about 0.37), hue H (0 to 360 degrees). Unlike HSL, equal steps in L look equally different, and changing H keeps the brightness the same. HSL yellow and HSL blue at "50% lightness" differ by 8:1 in contrast. In OKLCH they don't.

Conversion goes OKLCH → OKLab (a = C cos H, b = C sin H) → LMS (cube) → linear sRGB (3×3 matrix, Björn Ottosson 2020) → gamma encode. Colors outside sRGB are pulled back by lowering C and keeping L and H.

```
python3 scripts/bro_ui.py ramp 265 --chroma 0.16
python3 scripts/bro_ui.py oklch 4067c8
```

The ramp keeps chroma highest in the middle and low near white and black, because a very light or very dark color with high chroma falls outside the sRGB gamut and gets clipped.

## Fitts's law (rule 13)

Time to hit a target (Shannon form, MacKenzie 1992):

```
MT = a + b × log2(D / W + 1)
```

D is the distance to the target and W is its width along the direction of movement. The log term is the index of difficulty, in bits. Measured b for a mouse falls around 100 to 200 ms per bit. The examples assume 150.

Worked, with D = 600px:
- W = 24px: log2(26) = 4.70 bits, about 705 ms + a.
- W = 48px: log2(13.5) = 3.75 bits, about 563 ms + a. Doubling the width saves about 142 ms per click.

What follows from it:
- Make frequent targets big and close to where the cursor already is.
- Make the whole row clickable, not just the text in it.
- Targets pinned to a screen edge act as if infinitely deep, because the cursor stops at the edge. That is why OS menu bars live at the edge.
- Context menus open at the cursor, so D is close to 0.

```
python3 scripts/bro_ui.py fitts 600 24 48
```

## Hick's law (rule 14)

Time to choose between n equally likely options:

```
RT = a + b × log2(n + 1)
```

7 options = 3 bits. 15 options = 4 bits. Doubling the choices adds a constant amount of time, so the cost is logarithmic. This holds only when people know the options. Scanning an unfamiliar list is linear in n, which is why long lists need search, grouping and a sensible default.

```
python3 scripts/bro_ui.py hick 3 7 15
```

## Working memory (rule 15)

Cowan (2001) puts working memory at about 4 chunks. Miller's "7 ± 2" (1956) is older and overestimates it. What follows from it: never make someone carry a code, a name or a number from one screen to the next. Show it again where it's needed.

## Response time (rule 16)

Miller (1968) and Card, Robertson and Mackinlay (1991), as summarized by Nielsen:

| Delay | Feels like | Show |
|---|---|---|
| under 100 ms | instant, direct manipulation | nothing extra |
| 100 ms to 1 s | a short wait, flow intact | a state change (pressed, spinner in the button) |
| 1 to 10 s | waiting | a skeleton or progress |
| over 10 s | lost attention | percent done, time left, a way to cancel |

## Springs (rule 22)

A UI spring is a damped harmonic oscillator, m x'' + c x' + k x = 0.

```
ω0 = √(k / m)             natural frequency
ζ  = c / (2 √(k m))       damping ratio
overshoot = e^(-ζπ / √(1 - ζ²))   for ζ < 1
settle (2%) ≈ 4 / (ζ ω0)          for ζ < 1
```

| ζ | Overshoot | Use |
|---|---|---|
| 0.5 | 16.3% | games, playful toys |
| 0.7 | 4.6% | visible bounce, rarely right for tools |
| 0.8 | 1.5% | a slight settle, still reads as solid |
| 0.9 | 0.15% | looks like no bounce |
| 1.0 | 0 | critically damped, fastest settle without overshoot |
| over 1 | 0 | overdamped, slower than 1.0 for no gain |

Worked: k = 400, m = 1. ω0 = 20 rad/s. For ζ = 1, c = 2 × √400 = 40. Settles in about 290 ms.

```
python3 scripts/bro_ui.py spring --stiffness 400 --damping 32
```

## Frame budget (rule 23)

1000 / 60 = 16.7 ms per frame at 60 Hz, and 1000 / 120 = 8.3 ms at 120 Hz. The browser needs part of that for style, layout and paint, so keep script work per frame under about 10 ms at 60 Hz. `transform` and `opacity` run on the compositor and skip layout and paint. Animating `width`, `top` or `height` runs layout every frame.

## Nested radius (rule 5)

Two rounded rectangles look concentric when their corner curves share a center:

```
inner radius = outer radius - padding
```

A 16px card with 8px padding holds an 8px button. When padding is equal to or larger than the outer radius, the inner corner goes to 0 or a small fixed radius.

```
python3 scripts/bro_ui.py radius 16 8
```

## Proximity (rule 2)

Gestalt proximity: things that sit closer together read as one group. The gap inside a group has to be clearly smaller than the gap between groups, and a 1:2 ratio is the minimum that reads reliably. For example, 8px between a label and its input, 16 to 24px between fields, 32 to 48px between sections.
