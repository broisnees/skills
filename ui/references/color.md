# Color

Color has exact answers: contrast is measurable and ramps are computable. Compute them; never eyeball a value you can calculate.

## OKLCH

Use `oklch(L C H / α)` for new systems. **L** (0-1) is perceived lightness, so equal steps look equal. **C** is chroma (vividness, about 0-0.37). **H** is the hue angle.

- To change contrast, change **L**. Changing the hue barely moves contrast.
- To make a ramp, hold **H** constant, step **L** evenly, and let **C** peak mid-ramp and taper at both ends.
- To theme an accent, swap **H** and keep L and C. The new accent keeps the same contrast.
- To get the same vividness across hues, use the same *fraction* of each hue's maximum chroma, not the same C number (yellow and blue max out at very different C values).
- Gradients use `linear-gradient(in oklab, ...)` to avoid a muddy gray middle. Use `in oklch` for vivid rainbow sweeps.
- For P3, declare the sRGB value first, then override inside `@media (color-gamut: p3)`.

Keep the project's notation. One stray `oklch()` in a hex codebase is worse than consistent hex.

## Structure

- **One neutral ramp** (it carries 80-90% of pixels), **one accent ramp**, and **only the status ramps the product renders**.
- Neutrals: pure gray is a safe default. A trace of the accent hue (C about `0.005-0.01`) makes them feel related. Hold the tint consistent across every step.
- Every step has a role: page bg, subtle bg, component bg, hover, selected, subtle border, border, strong border/focus, solid, solid hover, secondary text, primary text. Don't generate steps nothing uses.
- **Dark mode is its own ramp**, not an inverted light one. Lower chroma, widen the dark end, separate surfaces by lightness (raised surfaces get *lighter*, not shadowed), and remeasure every pair.

## Tokens

Use two tiers. **Primitives** are named by hue and step (`--blue-9`) and never used in components. **Semantics** are named by role (`--text-secondary`, `--bg-raised`, `--border`, `--accent`) and are the only names components use.

- Grammar: `--{role}-{variant}-{state}`, one word per concept: `text`, `bg`, `border`, `accent`.
- Reserve `primary` for "most prominent in its group" (`--text-primary`). The brand color is `accent`.
- Never borrow a token for its value. A border token used as text color breaks when borders change. Add the missing role.
- Use one dark-mode mechanism (`.dark` class or `data-theme`), not mixed with `prefers-color-scheme` in some places.

## Usage

- **One color, one meaning.** If the accent means "interactive", static accent-colored text lies. Hues within about 15° count as the same color.
- **One filled accent action per view.** Peers stay neutral. A filled button reads as primary from across the room.
- **Add an accent.** A UI that is 100% gray reads as unfinished. Spend the accent on the primary action, selection, focus, links and key data, and nowhere else.
- Status hues must be distinguishable from the accent. If the brand is red, danger moves toward crimson and you check them side by side.
- Use alpha-black and alpha-white for borders and overlays so one token works on every surface. **Text is always solid**, so it can be measured.
- Never pure `#000` on `#fff` for large text areas in dark UI. Use about `oklch(0.96 0 0)` text on `oklch(0.16 0 0)`.

## Contrast

| Content | WCAG AA |
| --- | --- |
| Body text under 18.66px bold or 24px regular | **4.5:1** |
| Large text | 3:1 |
| UI components, icons, focus rings, input borders that identify the control | 3:1 |
| Disabled controls, decorative elements | Exempt (keep them legible anyway) |

- Measure the **rendered pair**: the actual background behind the text, including any surface, hover state, or image under a scrim. Measure in light and in dark.
- Placeholder text counts as text if it carries information.
- When a pair fails, change **L**. Report the pair, its ratio and the threshold.
- Quick check: `npx wcag-contrast "oklch(...)" "oklch(...)"`, or compute from OKLCH → linear sRGB → relative luminance.

## Accessibility

- Color is never the only signal: errors get an icon and text, diff lines get `+`/`−`, chart series get labels or patterns.
- `@media (prefers-contrast: more)`: solid backgrounds, stronger borders, no alpha text.
- `@media (forced-colors: active)`: use system colors (`CanvasText`, `Highlight`) and keep focus outlines (`outline-color: Highlight`).

## Before you finish

| Mistake | Fix |
| --- | --- |
| Hex scattered in components | Semantic token |
| `--blue-500` inside a component | Point a semantic token at it |
| Gray-on-gray secondary text at 3:1 | Raise L until `≥4.5:1` |
| Dark mode = inverted light | Separate ramp; lighter = higher |
| Ramp by HSL lightness | OKLCH, even L steps, constant H |
| Two filled primaries | One accent fill; the other goes neutral |
| Red brand plus red danger | Shift danger's hue, check side by side |
