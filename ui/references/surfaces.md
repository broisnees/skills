# Surfaces, depth and icons

## Concentric radius

`outer radius = inner radius + padding`

```tsx
<div className="rounded-[14px] p-1.5"> {/* 8 + 6 = 14 */}
  <div className="rounded-lg">...</div>   {/* 8 */}
</div>
```

- Applies whenever an inner surface sits inside an outer one with an even, visible inset: menus and their items, segmented controls and their thumbs, cards with an inset image, input groups.
- Past `24px` of padding, the layers read as separate surfaces, so choose each radius independently.
- The radius scales with size. Small things get small radii (badges `4px`, buttons `6px`, cards `8-12px`, dialogs `12-16px`). One radius on everything makes buttons look like pills or dialogs look sharp.
- `corner-shape: squircle` (where supported) for a smoother, iOS-like corner on large surfaces.

## Elevation

Shadows signal elevation. Borders signal structure.

| Use a shadow | Use a border |
| --- | --- |
| Raised: cards on a busy bg, dropdowns, popovers, dialogs, toasts | Dividers between list rows, table cells |
| Bordered buttons (shadow-as-border adapts to any bg) | Sidebar and panel separation |
| Hover lift | Input outlines (they identify the control) |

- **Layered shadows:** one `0 0 0 1px` ring for the edge, one tight contact shadow, and one soft ambient shadow. Use low-alpha black (`oklch(0 0 0 / 0.04-0.16)`), never pure black at high opacity and never a gray hex.
- The shadow's size matches the elevation: menus are smaller than dialogs, and dialogs are smaller than sheets.
- Light comes from above, so the y offset is positive and x is `0`.
- **Dark mode:** shadows barely show. Raise surfaces by making them *lighter* (raised `0.235` over bg `0.16`) and use a white alpha ring (`oklch(1 0 0 / 0.08)`). Keep a dark ambient shadow only on floating layers.
- A `1px` inset highlight at the top of filled buttons (`inset 0 1px 0 oklch(1 0 0 / 0.15)`) gives a subtle physical edge.
- Animate shadow changes on a pseudo-element's `opacity`, not on `box-shadow` itself.

```css
.card {
  box-shadow: 0 0 0 1px oklch(0 0 0 / 0.06), 0 1px 2px -1px oklch(0 0 0 / 0.06), 0 2px 4px oklch(0 0 0 / 0.04);
}
.dark .card { box-shadow: 0 0 0 1px oklch(1 0 0 / 0.08); }
```

## Materials (translucency)

- Use translucent chrome for headers, toolbars and floating bars over scrolling content: `bg-bg/75 backdrop-blur-md backdrop-saturate-150`.
- Never stack translucent on translucent; legibility collapses.
- Text on glass gets `+100` weight and higher contrast.
- `@media (prefers-reduced-transparency: reduce)` makes it solid.
- Prefer a fade mask where content meets sticky chrome over a hard divider.

## Image outlines

```tsx
<img className="outline outline-1 -outline-offset-1 outline-black/10 dark:outline-white/10" />
```

Use pure black or white at 10%, never a tinted gray; it reads as dirt on the edge. Use `outline`, not `border`, because outline doesn't affect layout.

## Icons

- **One library per product** (Lucide, Phosphor, Heroicons: pick one). Never mix.
- **One stroke width:** `1.5` beside regular text, `2` beside semibold. Match the icon's optical weight to its label.
- **Sizes:** `14` in dense metadata, `16` in controls and rows, `20` in nav, `24` maximum in app UI.
- **Outline by default, filled for the active or selected state.** Never mix styles otherwise.
- `currentColor` everywhere. Hover, disabled and selected come from CSS color or opacity, never from separate assets.
- Icons in a row with text are the same color as the text, or one step quieter (`text-fg-secondary`).
- Fix optical centering in the SVG where possible. Otherwise use `translate-x-px`.
- Directional icons flip in RTL.
- Decorative icons get `aria-hidden="true"`. Icon-only buttons get an `aria-label`.
- **No icon garnish:** an icon inside every card title, beside every heading, or in every bullet is embellishment. Icons earn their place by aiding scanning or recognition.

## Cursors

`cursor: pointer` on links only; buttons in an app keep `default` (native platform behavior) unless the project already uses pointer, in which case stay consistent. `cursor: grab`/`grabbing` on draggables, `col-resize` on resizers, `text` on editable regions, `not-allowed` only alongside a visible disabled style.

## Scrollbars

Thin and neutral: `scrollbar-width: thin; scrollbar-color: var(--border-strong) transparent`. Use `scrollbar-gutter: stable` on containers whose content changes length.
