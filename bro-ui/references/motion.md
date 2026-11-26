# Motion (rules 20-24)

Motion explains a change: where something came from, where it went, what caused it. When it explains nothing, cut it. Things people do 100 times a day (opening the command menu, switching tabs) get no animation or under 150 ms.

## Duration

| Element | Enter | Exit |
|---|---|---|
| Hover color, press | 100-150 ms | same |
| Tooltip, small popover | 150 ms | 100 ms |
| Dropdown, menu | 150-200 ms | 120-150 ms |
| Dialog, sheet | 200-250 ms | 150-200 ms |
| Page-level transition | 250-300 ms | 200 ms |

Bigger things travel farther, so they get more time. Exits run about 20% faster than entries, because once someone dismisses a thing they're done with it.

## Easing

| Token | Curve | Use |
|---|---|---|
| `--ease-out` | `cubic-bezier(0.2, 0, 0, 1)` | entering, anything responding to input |
| `--ease-in` | `cubic-bezier(0.4, 0, 1, 1)` | leaving the screen for good |
| `--ease-in-out` | `cubic-bezier(0.4, 0, 0.2, 1)` | moving from one place on screen to another |
| linear | | progress bars, spinners, color fades only |

Ease-out starts fast, so the UI looks like it responded the moment it was touched.

## Springs

Use springs for things that follow the finger or can be interrupted mid-motion (drag, swipe, sheet), because a spring keeps its velocity when its target changes. A CSS duration restarts from zero.

| Feel | Stiffness | Damping | Mass | ζ | Overshoot |
|---|---|---|---|---|---|
| Snappy, no bounce | 400 | 40 | 1 | 1.0 | 0 |
| Slight settle | 400 | 32 | 1 | 0.8 | 1.5% |
| Soft sheet | 200 | 28 | 1 | 0.99 | 0 |

Check any config: `python3 scripts/bro_ui.py spring --stiffness 400 --damping 32`.

## Performance

- Animate only `transform` and `opacity` (rule 23). For size changes, animate `transform: scale()` and correct the content, or use the FLIP technique: measure First and Last, Invert with a transform, then Play.
- `will-change: transform` only during the animation. Left on permanently, it holds GPU memory for every element.
- Animating `height: auto` works in Chromium 129+ with `interpolate-size: allow-keywords`. Otherwise use `grid-template-rows: 0fr → 1fr`.

## Reduced motion (rule 24)

```css
@media (prefers-reduced-motion: reduce) {
  *, *::before, *::after {
    animation-duration: 1ms !important;
    animation-iteration-count: 1 !important;
    transition-duration: 1ms !important;
    scroll-behavior: auto !important;
  }
}
```

Swap movement for a short opacity fade rather than removing all feedback. Parallax, zoom and large slides are what make people with vestibular disorders feel sick.

## Recipes

```css
/* popover: scale from the trigger, not the center */
.popover {
  transform-origin: var(--radix-popover-content-transform-origin, top center);
  animation: pop-in 150ms var(--ease-out);
}
@keyframes pop-in {
  from { opacity: 0; transform: scale(0.95); }
}

/* button press */
.button:active { transform: scale(0.97); transition: transform 100ms var(--ease-out); }

/* list stagger: 30 ms per item, capped so long lists don't wait */
.item { animation: fade-up 200ms var(--ease-out) both; animation-delay: calc(min(var(--i), 8) * 30ms); }
@keyframes fade-up { from { opacity: 0; transform: translateY(4px); } }
```
