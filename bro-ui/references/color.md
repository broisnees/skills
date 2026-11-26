# Color (rules 8-12)

## Build the palette

1. Pick one accent hue in OKLCH (H in degrees). Blue is about 265, green about 150, red about 25.
2. Generate an 11 step ramp: `python3 scripts/bro_ui.py ramp 265 --chroma 0.16`.
3. Generate neutrals on the same hue with almost no chroma: `ramp 265 --chroma 0.014`. That tint is rule 10, and it is why the greys look chosen.
4. Map steps to tokens by measured contrast, not by step number. Run `contrast` on every text and background pair.

## Token roles

| Token | Light (from 265 ramps) | Dark | Checked against |
|---|---|---|---|
| `--bg` | `#f9fafc` | `#0d0d0f` | |
| `--surface` | `#ffffff` | `#1e2024` | |
| `--fg` | `#1e2024` 15.62:1 | `#f9fafc` 18.59:1 | 4.5:1 |
| `--fg-muted` | `#5d6068` 6.02:1 | `#a6aab2` 8.33:1 | 4.5:1 |
| `--border` | `#dcdfe4` | `#31343a` | decorative, no minimum |
| `--border-control` | `#8d9199` 3.16:1 | `#747881` 3.69:1 | 3:1 (SC 1.4.11) |
| `--accent` | `#4067c8` 5.26:1 | `#6994f9` 6.66:1 | 4.5:1 when used as text |
| `--on-accent` | `#ffffff` 5.26:1 | `#0d0d0f` 6.66:1 | 4.5:1 |

All of it is ready to paste in `examples/tokens.css`.

## Rules in practice

- **One accent.** It marks the primary action, the selection and links. A second brand color fights the first for attention.
- **Semantic colors carry state.** Red = destructive or failed, amber = needs attention, green = done. Each still needs an icon or a word (rule 11), because about 1 in 12 men has red-green color vision deficiency.
- **Dark mode is a separate design (rule 12).** Elevation goes up by making the surface lighter, since shadows barely show on dark backgrounds. Lower the chroma of saturated colors a little, or they glow. Never use pure `#000` for the background behind text, because pure white on pure black at 21:1 can blur and glow (halation) for readers with astigmatism. 18:1 is plenty.
- **States derive from tokens.** Hover = surface plus or minus about 0.03 L in OKLCH. Pressed = about 0.06. In CSS: `background: oklch(from var(--surface) calc(l - 0.03) c h)`.
- **Translucent overlays** take on the color of whatever sits under them. Measure contrast on the composited color, which `scripts/verify.mjs` does.

## Common failures

| Smell | Fix |
|---|---|
| Placeholder text at 2:1 | Use `--fg-muted`. A placeholder is still text people read. |
| Muted text on a tinted card fails while it passes on the page | Measure against the card, not the page. |
| Accent text on an accent-tinted background | Use `--fg` on the tint, or darken the accent one step. |
| Input border at 1.3:1 | `--border-control`, 3:1. |
| Focus ring the same color as the button | Add a 2px offset so the ring sits on the page background. |
