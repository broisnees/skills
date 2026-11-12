# Layout

Position, space and alignment communicate hierarchy before a single word is read.

## Spacing

- **4px grid.** Everything is a multiple of 4: 4, 8, 12, 16, 24, 32, 48, 64.
- **Proximity:** the gap between groups is **at least 2×** the gap within one (8 within, 16-24 between). If the groups and their contents have the same spacing, the grouping disappears.
- **Group with space first**, background second, and lines last. Most cards, dividers and boxes exist only because the spacing was wrong. Unbox them.
- **Internal ≤ external:** padding inside a card is less than or equal to the space around it.
- Prefer a parent's `gap` over margins on children. No `margin-top` on the first child.

## Alignment

- Choose a few alignment edges and stay on them. Every stray edge is noise.
- **Align by eye, not pixels.** Geometric centering often looks wrong:
  - Icon + text buttons: the icon side's padding is 2px less (`ps-3 pe-2.5` with a trailing icon).
  - Play triangles shift about 2px toward the point.
  - Text next to an icon centers on the x-height, not the line box. Nudge by `1px` when the cap height makes it look low.
  - Large quotes and bullets hang outside the text edge (`hanging-punctuation: first`, or a negative indent).
  - Circles and triangles look smaller than squares of the same size, so draw them about 5-10% larger.
- **Optical centre.** The visual center of a frame sits slightly *above* the geometric center. Place a lone centered element (empty state, login card) about 5-10% above true center: `padding-bottom: 10vh` on the centering container.
- Baseline-align mixed sizes in a row (`items-baseline`), not `items-center`.

## Hierarchy

- **Enlarge the main feature.** One focal element per view, about 2-3× the visual weight of the next. If everything is emphasized, nothing is.
- **Order by importance:** most important at the top and leading edge, reading flows top to bottom and leading to trailing.
- **Emphasize the CTA:** the one primary action is the highest-contrast element, and secondary actions are visibly quieter.
- **Progressive disclosure:** show the common path, and put advanced options one level deeper. Every hidden thing needs a visible cue: "Show 12 more", a chevron, or a peek of the next item `16-32px` past the scroll edge.
- **Affordance:** controls must look operable. A background, border or consistent placement distinguishes a button from text. Links are underlined or accent-colored *and* nothing else uses that treatment.

## Responsiveness

- Breakpoints come from content: break where the layout stops fitting, not at 768 because a preset says so. Collapse late.
- **Container queries** for components (`@container`), media queries for page chrome.
- Survive **320px** width and **200%** zoom with no horizontal scroll.
- No fixed widths or heights on text containers; translated strings grow 30-200%. Use `min-height`, `max-width` and wrapping.
- `min-w-0` on flex children that contain truncating text.
- Use `100dvh`, not `100vh`, on mobile so the URL bar doesn't clip content.

## Safe area

```html
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
```

```css
.bottom-bar { padding-bottom: max(12px, env(safe-area-inset-bottom)); }
.app { padding-inline: max(16px, env(safe-area-inset-left)) max(16px, env(safe-area-inset-right)); }
```

Content and backgrounds bleed to the edges, while controls and text stay inside the safe area and the margins. Fixed bottom actions never sit under the home indicator.

## Layout shift (CLS)

- Give images and embeds `width`/`height` or `aspect-ratio`.
- Skeletons match final content dimensions.
- `scrollbar-gutter: stable` on scroll containers, so content doesn't jump when the scrollbar appears.
- `tabular-nums` on changing numbers.
- Reserve space for async banners, error text (keep a `min-h` for the message line) and lazy-loaded UI.
- Button loading states keep their width: hide the label with `invisible`, don't remove it.
- Font swaps use metric-matched fallbacks.
- Never insert content above what the user is reading. Show a "N new items" pill instead.

## Logical properties

Use `ms/me/ps/pe/start/end/inset-inline` instead of left and right. Directional icons (arrows, chevrons) flip in RTL with `rtl:-scale-x-100`. Clocks, media controls and logos do not flip.

## App shells

- Sidebar and main: the sidebar is a fixed `240-280px` and resizable. The main area scrolls on its own (`overflow-auto` on main, not on body), with `min-w-0`.
- Sticky headers float above content with a translucent background (`bg-bg/80 backdrop-blur`). The bottom hairline appears only when content scrolls under (use a scroll-driven animation or IntersectionObserver).
- Overscroll: `overscroll-behavior: contain` on panels and modals so the page behind doesn't scroll.
- Primary actions live in stable chrome (a sticky footer or header), never at the bottom of a clip-prone scroll area.

## Before you finish

| Mistake | Fix |
| --- | --- |
| Same gap within and between groups | 2× rule |
| Cards inside cards inside cards | Remove boxes; use space |
| `margin-left` in localizable UI | `ms-*` |
| Centered card at true center looks low | Shift up 5-10% |
| Truncated text in flex overflows | `min-w-0` on the child |
| `100vh` mobile layout clipped | `100dvh` |
| Content jumps when data loads | Reserve space; size skeletons exactly |
