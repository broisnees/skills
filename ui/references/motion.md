# Motion

Motion exists to explain what happened: where something came from, where it went, and that the interface heard the user. If it does none of those, it is decoration, and decoration repeated a hundred times a day is friction.

## 1. Should it animate at all?

| How often the user sees it | Decision |
| --- | --- |
| 100+ times a day: keyboard shortcuts, command palette, typing, focus moves | **No animation. Ever.** |
| Tens of times a day: hover, list navigation, tab switches in a work tool | Instant, or `≤150ms` on color, background or opacity only |
| Occasionally: menus, dialogs, sheets, toasts | The standard motion below |
| Rarely: onboarding, first load, success moments, empty states | Room for a little delight |

Valid reasons to animate: **spatial continuity** (where it came from and went), **state change** (this became that), **feedback** (I heard you), and **preventing a jarring jump**. "It looks nice" is not a reason on anything seen often.

## 2. Tokens

```css
:root {
  --ease-out: cubic-bezier(0.23, 1, 0.32, 1);     /* entrances, exits, feedback */
  --ease-in-out: cubic-bezier(0.77, 0, 0.175, 1); /* moving or morphing on screen */
  --ease-drawer: cubic-bezier(0.32, 0.72, 0, 1);  /* sheets and drawers */

  --dur-press: 120ms;
  --dur-hover: 150ms;
  --dur-tooltip: 150ms;
  --dur-popover: 200ms;   /* dropdowns, selects, popovers: 150-250ms band */
  --dur-dialog: 250ms;
  --dur-sheet: 300ms;
}
```

**Exits are 20% shorter than enters:** popover `200 → 160ms`, dialog `250 → 200ms`, sheet `300 → 240ms`. The user has already moved on, so don't make them wait for it.

**User-initiated UI never exceeds `300ms`.** If something feels slow, cut the duration before you touch the curve.

### Easing decision

- Entering or exiting → **ease-out**. It starts fast, so it feels responsive at the exact moment the user is watching.
- Already on screen and moving or morphing → **ease-in-out**.
- Color or background on hover → `ease-out` at `150ms`.
- Progress, time or a marquee → `linear`. Nothing else is linear.
- **Never `ease-in`** on UI. It delays the first frame, so the same 200ms feels slower.

## 3. The twenty motion rules

1. **Ease-out for entrances.** `--ease-out`, `150-250ms`.
2. **Dropdowns at 150-250ms.** Default `200ms` in and `160ms` out.
3. **Stagger list rows by `30ms`.** Cap the cascade at about 10 items (`300ms`) and show the rest together. Never block interaction while it plays.
4. **Scale to `0.97` on press.** `transition: scale 120ms var(--ease-out)`; `:active { scale: 0.97 }`. Applies to anything pressable; offer a `static` opt-out for big surfaces.
5. **Stretch moving knobs about 12%.** While a toggle or slider thumb is pressed or travelling, widen it along the axis of travel (`scaleX: 1.12`, anchored to the trailing edge). It reads as squash and stretch, so the thumb feels physical.
6. **Stagger as details settle.** On a staged entrance (hero, success, a panel's first load), reveal semantic chunks one after another: title, then meta, then body, then actions, `60-100ms` apart, each with `opacity` + `translateY(8px)` + `blur(4px) → 0`.
7. **Arcs for object movement.** Things that travel diagonally move on a curve, not a straight line. Give X and Y different easings (X `--ease-out`, Y `--ease-in-out`), or use `offset-path`.
8. **Pulse to confirm success.** One pulse, never a loop: `scale 1 → 1.04 → 1` over `300ms`, or a ring expanding from `0` to `8px` while fading. Pair it with a color or icon change that stays.
9. **Ease-in-out for moves.** Reordering, a tab indicator sliding, a panel resizing: `--ease-in-out`, `200-300ms`.
10. **Start popovers at `0.95`.** `opacity: 0; scale: 0.95` to `1`. Never `scale(0)`; nothing appears from nothing.
11. **Enter from the trigger.** `transform-origin` sits at the anchor: Radix `var(--radix-popover-content-transform-origin)`, Base UI `var(--transform-origin)`, or computed from the trigger's rect. **Modals are exempt** and scale from the center.
12. **Exit to the trigger.** Same origin and same path in reverse. A panel that slides in from the right leaves to the right.
13. **No bounce on everyday UI.** Springs use `bounce: 0` (critically damped). Bounce only when the user's gesture carried momentum (a flick, a throw, a drag release), and then at most `0.15-0.25`.
14. **Don't tween while held.** During a drag, a slider scrub or a resize, the element follows the pointer 1:1 with `transition: none`. Hand off to a spring on release.
15. **Make exits 20% shorter.** See tokens.
16. **Overlap old and new states.** When content swaps (a tab panel, a step change, a number), crossfade with an overlap of the outgoing `opacity → 0` and the incoming `opacity → 1`, rather than waiting for one to finish (`AnimatePresence mode="popLayout"`, not `"wait"`, which doubles the duration).
17. **Masks for reveals and colour.** Reveal with `clip-path: inset()` rather than height or opacity. For tab color changes, duplicate the tab list in its active style and clip it to the active tab, so color transitions are perfect.
18. **Crossfade icons with blur.** Icon swaps (copy → check, play → pause): `opacity 0 → 1`, `scale 0.25 → 1`, `blur(4px) → 0`, using spring `{ duration: 0.3, bounce: 0 }`. Without a library, stack both icons and crossfade with CSS.
19. **Rubber band past bounds.** Past an edge, the element keeps following with rising resistance: `offset = (x·d·0.55) / (d + 0.55·|x|)`. It springs back on release.
20. **Reuse the same `layoutId`.** Shared-element transitions (a tab underline, a card expanding to a detail view, a selected pill) use one `layoutId` so the element morphs from A to B instead of fading out and back in.

## 4. Recipes

### Press

```css
.pressable { transition: scale var(--dur-press) var(--ease-out); }
.pressable:active:not(:disabled) { scale: 0.97; }
```

```tsx
<motion.button whileTap={{ scale: 0.97 }} transition={{ type: "spring", duration: 0.2, bounce: 0 }} />
```

### Popover with `@starting-style` (no library)

```css
.popover {
  transform-origin: var(--transform-origin, top);
  transition: opacity 200ms var(--ease-out), scale 200ms var(--ease-out),
              display 200ms allow-discrete, overlay 200ms allow-discrete;
  &:not(:popover-open) { opacity: 0; scale: 0.95; transition-duration: 160ms; }
  @starting-style { &:popover-open { opacity: 0; scale: 0.95; } }
}
```

### Toggle knob stretch (rule 5)

```css
.switch-thumb {
  transition: translate 200ms var(--ease-in-out), width 120ms var(--ease-out);
  width: 16px;
}
.switch:active .switch-thumb { width: 18px; } /* ≈ +12% */
.switch[aria-checked="true"] .switch-thumb { translate: 14px 0; }
.switch[aria-checked="true"]:active .switch-thumb { translate: 12px 0; } /* grow toward the travel side */
```

### Staged entrance (rule 6)

```tsx
const container = { show: { transition: { staggerChildren: 0.08 } } };
const item = {
  hidden: { opacity: 0, y: 8, filter: "blur(4px)" },
  show: { opacity: 1, y: 0, filter: "blur(0px)", transition: { duration: 0.35, ease: [0.23, 1, 0.32, 1] } },
};
```

### List stagger (rule 3)

```css
.row { animation: row-in 200ms var(--ease-out) both; animation-delay: calc(min(var(--i), 10) * 30ms); }
@keyframes row-in { from { opacity: 0; translate: 0 4px; } }
```

Set `style="--i: {index}"`. Only on first load of the list, never on every re-render or filter.

### Success pulse (rule 8)

```css
@keyframes pulse-once { 50% { scale: 1.04; } }
.confirm { animation: pulse-once 300ms var(--ease-in-out); }
```

### Icon crossfade without a library (rule 18)

```tsx
<span className="relative inline-grid [&>*]:[grid-area:1/1] [&>*]:transition-[opacity,scale,filter] [&>*]:duration-300 [&>*]:ease-[cubic-bezier(0.2,0,0,1)]">
  <CopyIcon className={copied ? "opacity-0 scale-[0.25] blur-[4px]" : ""} />
  <CheckIcon className={copied ? "" : "opacity-0 scale-[0.25] blur-[4px]"} />
</span>
```

### Shared element (rule 20)

```tsx
{tabs.map(t => (
  <button key={t.id} onClick={() => setActive(t.id)} className="relative px-3 h-8">
    {active === t.id && (
      <motion.span layoutId="tab-indicator" className="absolute inset-0 rounded-sm bg-selected"
        transition={{ type: "spring", duration: 0.3, bounce: 0 }} />
    )}
    <span className="relative">{t.label}</span>
  </button>
))}
```

Wrap separate trees in `<LayoutGroup>`. Use `layout="position"` on text that shouldn't stretch. Without Motion, use the View Transitions API with a unique `view-transition-name` per element, removed after the transition.

### Height auto

Use `interpolate-size: allow-keywords` (Chromium) with `transition: height 250ms var(--ease-in-out)`, or a `grid-template-rows: 0fr → 1fr` wrapper. Measure with `ResizeObserver` only for libraries. Animate the inner content's opacity with a short delay so the text doesn't squish.

## 5. Springs and gestures

- **Use springs for anything the user touches or can interrupt.** They start from the current value and carry velocity. Default `{ type: "spring", duration: 0.3-0.4, bounce: 0 }`.
- **Feedback on pointer-down**, not on click. Commit on pointer-up. Allow cancel by dragging away.
- **Drag:** use `setPointerCapture`, keep the grab offset (don't snap to the center), wait for a `~10px` threshold before locking direction, and ignore additional touches mid-drag.
- **Release:** hand the pointer's velocity to the spring. Choose the target by **projecting momentum**: `end = pos + (v / 1000) · 0.998 / (1 − 0.998)`, then snap to the nearest point. Dismiss on a flick when `|distance| / ms > 0.11`, regardless of distance.
- **Reverse cleanly:** animate from the live on-screen value, never from the logical target.

## 6. Performance

- Animate only `transform` (or the individual `translate`, `scale` and `rotate` properties), `opacity`, `filter` and `clip-path`. Never `width`, `height`, `top`, `left`, `margin` or `padding`. The one exception is height-auto via the recipe above.
- Name the properties: `transition-property: opacity, scale`. Never `all`.
- `will-change: transform` only when you see first-frame jank, and remove it afterwards.
- Keep blur `≤ 20px`; Safari pays heavily for large blurs and big `backdrop-filter` areas.
- Under load, CSS and WAAPI stay smooth while rAF-driven JS stutters. Use CSS for predetermined motion and springs for gestures.
- Set transforms on the element directly; don't update a CSS variable on a parent with many children.

## 7. Quiet details

- `AnimatePresence initial={false}` so toggles don't animate on page load (but keep intentional hero entrances).
- Disable all transitions for one frame when switching theme (`next-themes`: `disableTransitionOnChange`).
- Tooltips: delay the first one, then show adjacent ones instantly with no animation.
- Toasts and stacked items: transitions, not keyframes, so rapid additions retarget smoothly.
- Hover effects go behind `@media (hover: hover) and (pointer: fine)`.
- One focal animation at a time. Two things moving at once compete.
- Slow-motion test at 10% in DevTools → Animations. Check the origin, sync between properties, and that there are no double-image crossfades (add `blur(2px)` during the crossfade to blend them).

## 8. Reduced motion

```css
@media (prefers-reduced-motion: reduce) {
  *, *::before, *::after { animation-duration: 0.01ms !important; animation-iteration-count: 1 !important; scroll-behavior: auto !important; }
  .popover, .dialog, .sheet { transition-property: opacity !important; translate: none !important; scale: none !important; }
}
```

```tsx
const reduce = useReducedMotion(); // Motion
<MotionConfig reducedMotion="user">...</MotionConfig>
```

Reduced means gentler, not nothing. Keep short opacity and color crossfades. Remove movement, parallax, autoplay and loops.
