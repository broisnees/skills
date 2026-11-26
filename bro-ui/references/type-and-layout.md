# Type and layout (rules 1-7)

## Spacing scale

4, 8, 12, 16, 24, 32, 48, 64. Nothing in between. The 4px base divides cleanly at 1x, 1.5x, 2x and 3x pixel densities, so edges land on whole device pixels.

| Space | Use |
|---|---|
| 4 | icon to its label, tight chips |
| 8 | label to input, items inside a row |
| 12 | padding in small controls |
| 16 | card padding, gap between form fields, page gutter on phones |
| 24 | gap between cards, padding in dialogs |
| 32-48 | gap between page sections |
| 64 | above a major heading on long pages |

Proximity check (rule 2): for any group, the outer gap is at least 2x the inner gap. If the label sits 16px from its input and 16px from the field above, the eye can't tell which field it belongs to.

## Type

| Role | Size (16 × 1.2^n) | Weight | Line height | Letter spacing |
|---|---|---|---|---|
| Page title | 28-33px | 600-700 | 1.2 | -0.02em |
| Section heading | 19-23px | 600 | 1.25 | -0.01em |
| Body | 16px (14-15px in dense apps) | 400 | 1.5 | 0 |
| Secondary, metadata | 13px | 400-500 | 1.4 | 0 |
| Caption, overline | 11-12px | 500-600 | 1.3 | +0.04em, uppercase only here |

- Body text measures 45 to 75 characters per line: `max-width: 65ch`. Longer lines make the eye lose its place on the jump back to the left margin.
- Headings get `text-wrap: balance`, paragraphs get `text-wrap: pretty`.
- Large text needs tighter tracking and line height. Small text needs looser. Variable fonts with `font-optical-sizing: auto` do part of this for free.
- Numbers in tables, timers and prices use `font-variant-numeric: tabular-nums` so the digits don't shift as values change (rule 6).
- 2 weights per family are usually enough: regular and semibold. Bold plus a size change is redundant emphasis.

## Alignment

- Pick one left edge per column and put everything on it. Count the distinct left edges on a screen. Fewer is calmer.
- Align text baselines across a row, not box tops.
- Optical corrections (rule 7, a rule of thumb, not a law): circles and triangles drawn 3 to 5% larger than squares look the same size. A play triangle shifts about 1/12 of its width right to look centered. Text in a button looks low by a pixel when the font has tall ascenders, so check it at 2x zoom.

## Radius

Inner = outer - padding (rule 5). One radius per nesting level. A screen that uses 6 different radii looks assembled from different kits.

| Element | Radius |
|---|---|
| Page-level cards, dialogs | 12px |
| Buttons, inputs, menus | 8px |
| Chips inside a card with 4px padding | 4px |
| Avatars, toggles, pills | 9999px |

## Responsive

- Check 320, 768 and 1440px (rule 30). 320 is the narrowest phone still in common use.
- Use fluid sizes for big headings: `font-size: clamp(28px, 4vw + 12px, 40px)`.
- Flex and grid children that hold text get `min-width: 0`, or long words push the layout wider than the screen.
- Only tables, code and diagrams may scroll sideways, each inside its own `overflow-x: auto` box.
