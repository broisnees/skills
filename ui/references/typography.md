# Typography

Most of an interface is text. Get the scale, spacing and rendering right, and half the design is done.

## Scale and roles

- Use one small scale with semantic use: about 7-9 sizes. App UI defaults to **13px**, in-app reading to **14px**, long-form to **16px**, captions and metadata to **12px**, and nothing below **11px** (kbd and badges only).
- Build hierarchy from **size + weight + color together**, not size alone. A `13px 500` primary line over a `12px 400 text-secondary` meta line beats two sizes 4px apart.
- Heading levels descend visually: an h3 never outweighs its h2. Pick the element for semantics and the size in CSS.
- Weights: `400` body, `500` labels and buttons, `600` headings. Stay at `≥400` below 18px; thin weights (`<300`) are for display sizes of `28px`+ only.
- At most two families: a sans, plus a mono for code. A third (a display serif) only on marketing surfaces.

## Spacing

| Role | `line-height` | `letter-spacing` |
| --- | --- | --- |
| Display, 32px+ | `1.05-1.1` | `-0.02em` to `-0.03em` |
| Headings, 18-28px | `1.2-1.25` | `-0.01em` |
| UI text, 12-14px | `1.4-1.55` | `0` |
| Long-form body | `1.5-1.6` | `0` |
| Small uppercase labels | `1.3` | `+0.06em` |

- Use unitless line-height. Any text that wraps to 3+ lines needs `≥1.4`.
- **Tracking** is size-specific: negative as text grows and positive on small caps. A single global `letter-spacing` is wrong somewhere.
- **x-height** matters more than point size. A font with a large x-height (Inter, SF) reads bigger at 13px than a small-x-height serif at 15px, so compare rendered sizes, not numbers. When swapping fonts, match the x-height with `font-size-adjust: from-font` or by eye.
- **Leading** follows size inversely: tight on large text, looser on small text.

## Measure

Cap long-form text at **`65ch`** (60-75 characters). UI columns like chat and docs use `max-w-3xl`. A paragraph spanning a 1440px screen is unreadable.

## Wrapping

- `text-wrap: balance` on headings and short centered text, so lines come out even with no ragged one-word tail.
- `text-wrap: pretty` on paragraphs and descriptions, which prevents **widows** (a lone word on the last line).
- `overflow-wrap: anywhere` where URLs, IDs or file paths can overflow.
- `white-space: nowrap` on buttons, badges, tabs and kbd.
- `hyphens: auto` with a `lang` attribute for narrow justified columns, and only there. Don't justify UI text.
- For a manual break, use `&nbsp;` between a number and its unit (`16&nbsp;px`) and between the last two words of a headline.

## Numbers

- `font-variant-numeric: tabular-nums` (Tailwind `tabular-nums`) on **every changing or aligned number**: prices, counters, timers, tables, charts, percentages, line numbers. Proportional digits jitter as values update, which is layout shift.
- `slashed-zero` for IDs and codes where 0 and O might be confused.
- `oldstyle-nums` only in long-form prose.
- Right-align numeric table columns, with the header aligned to match.
- Format with `Intl.NumberFormat` and `Intl.DateTimeFormat`; never concatenate units by hand.

## Kerning and features

- **Kerning** stays on (`font-kerning: normal`, the default). Never turn it off for "performance". Use `text-rendering: optimizeLegibility` on headings.
- Use properties over raw tags: `font-weight: 550`, not `font-variation-settings: "wght" 550`; `font-optical-sizing: auto`, not `"opsz"`. Raw `font-feature-settings` only for stylistic sets (`"ss01"`, `"cv11"`) that have no property.
- Load the real weights and italics you use. Synthesized bold and italic distort the face (`font-synthesis: none` once you've confirmed every needed face loads).
- Serve `.woff2`, use variable fonts where possible, `font-display: swap`, and preload the one or two faces above the fold. Match the fallback metrics (`size-adjust`, `ascent-override`) so the swap doesn't shift layout.

## Rendering

- `-webkit-font-smoothing: antialiased` and `-moz-osx-font-smoothing: grayscale` **once on the root**.
- Text on translucent or blurred surfaces needs a heavier weight (`+100`) and higher contrast than on solid ones.

## Typographic details

- Curly quotes `“ ”` and apostrophes `’` in prose, straight in code. Use an en dash for ranges (`2020–2024`), an em dash for breaks, a single `…` character, `×` for dimensions, and `−` (minus) in numbers. <!-- ai-tells: ignore -->
- Store copy in natural case and style it with `text-transform`.
- Links: `text-underline-offset: 0.2em`, `text-decoration-thickness: from-font`, `text-decoration-skip-ink: auto`. Use a dotted underline for "has a definition" hints.
- Truncation: `truncate` for one line and `line-clamp-N` for several. **The full value must stay reachable** through a tooltip, expand control or detail view.
- Keep text selectable. Use `user-select: none` only on drag handles and gesture surfaces.
- Set `lang` on `<html>`. Wrap mixed-direction user content in `<bdi>`.

## Inputs on mobile

iOS zooms on focus when an input's text is under 16px. Use `text-base sm:text-sm` (or the house `max-sm:text-md`). Never disable zoom in the viewport meta.

## Before you finish

| Mistake | Fix |
| --- | --- |
| Lopsided two-line headline | `text-wrap: balance`, `max-width` in `ch` |
| Single word on the last line | `text-wrap: pretty` |
| Counter or price jitters | `tabular-nums` |
| One `letter-spacing` everywhere | Per-role tracking table |
| `leading-none` on wrapping text | `≥1.4` |
| 300-weight 13px text | `≥400` below 18px |
| Mono used for "technical vibe" | Mono only for code, IDs and kbd |
| Random italics or gradient words | One emphasis per view, or none |
