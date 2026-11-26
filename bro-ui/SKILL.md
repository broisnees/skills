---
name: bro-ui
description: Build or fix UI so it ships polished and actually works. Rules come from perception science and measurable math, then a verify pass proves it. Use on /bro-ui, "make this UI goated", "polish this", or any screen that has to feel like a finished product.
disable-model-invocation: true
---

# Bro UI

Build the UI, apply every rule below, then run the verify pass. A screen is done when the verify pass is clean, not when it looks done.

Rule numbers are stable ids. A removed rule leaves a gap.

## Layout and type

1. Space on a 4px grid: 4, 8, 12, 16, 24, 32, 48, 64. No other values.
2. Proximity (Gestalt). Space inside a group is smaller than space between groups. Keep the ratio at 1:2 or more.
3. Type scale is geometric, because perception follows Weber's law (ΔI / I = k): size_n = base × r^n. Use base 14 to 16px, r = 1.2 for dense apps, 1.25 to 1.333 for pages. At most 5 sizes.
4. Line length 45 to 75 characters (`max-width: 65ch`). Line height 1.5 for body, 1.1 to 1.25 for headings.
5. Nested corners: inner radius = outer radius - padding. Never inner > outer.
6. Numbers that line up use `font-variant-numeric: tabular-nums`.
7. Align optically. Circles and triangles overshoot their box by about 3 to 5% to look the same size as squares. A play icon shifts right to look centered.

## Color

8. Build palettes in OKLCH. It is perceptually uniform, so equal steps in L look like equal steps. Step L evenly, hold H, lower C near white and black.
9. Contrast is computed, not eyeballed. Relative luminance L = 0.2126 R + 0.7152 G + 0.0722 B on linearized sRGB. Ratio = (L1 + 0.05) / (L2 + 0.05). Body text at least 4.5:1, large text and icons and borders of controls at least 3:1 (WCAG 2.2).
10. Neutrals carry a slight tint of the accent hue (OKLCH chroma 0.005 to 0.02). Pure grey looks unfinished.
11. Color means state. One accent, plus semantic red, amber, green. Never color as the only signal: pair it with an icon or text.
12. Define every color as a token for light and dark. Dark mode is its own design: elevation goes up by lightening the surface, not by adding shadow.

## Interaction

13. Fitts's law: time = a + b × log2(D / W + 1). Big targets close to the cursor are fast. Hit area at least 24×24px (WCAG 2.5.8), 44×44px on touch. Screen edges count as infinite width.
14. Hick's law: time = b × log2(n + 1). Fewer choices per step. Group long lists and put a search box on anything over about 10 items.
15. Working memory holds about 4 chunks (Cowan, 2001). Never ask people to remember something from a previous screen.
16. Response limits (Nielsen): 100ms feels instant, 1s keeps flow, 10s loses attention. Under 100ms, show nothing. 100ms to 1s, show a state change. Over 1s, show progress.
17. Optimistic updates for anything that rarely fails. Offer undo instead of "Are you sure?".
18. Every interactive component has all 8 states: default, hover, active, focus-visible, disabled, loading, empty, error. A missing state is a bug.
19. Everything works by keyboard. Visible focus ring, logical tab order, Esc closes, Enter submits.

## Motion

20. Duration 100 to 300ms. Small things faster, large things slower. Exits run about 20% faster than entries.
21. Enter with ease-out, for example `cubic-bezier(0.2, 0, 0, 1)`. Never linear for UI movement.
22. Springs are damped oscillators with damping ratio ζ = c / (2√(k m)). Use ζ = 1 for no bounce, 0.7 to 0.85 for a small settle. Higher ζ never overshoots.
23. Animate only `transform` and `opacity`. The frame budget is 16.7ms at 60Hz and 8.3ms at 120Hz. Layout properties blow it.
24. Respect `prefers-reduced-motion`: swap movement for a short fade.

## Performance

25. Hit Core Web Vitals: LCP at most 2.5s, INP at most 200ms, CLS at most 0.1.
26. Reserve space for anything that loads late (images, embeds, fonts) so nothing shifts. Use skeletons that match the final layout.
27. Lists over a few hundred rows are virtualized.

## Verify pass

Run all of it. Report each item as pass or fail with the number. Fix fails and run again.

28. Build and lint pass with zero errors. The console shows zero errors and zero warnings during use.
29. Click every control and fill every form, including bad input. Every action has a visible result.
30. Check widths 320, 768 and 1440px. No horizontal scroll, no clipped text, no overlap.
31. Check light and dark themes. Measure the contrast of body text, muted text and borders against rule 9.
32. Do a keyboard-only pass through the whole flow.
33. Force each state from rule 18 (empty data, slow network, server error) and look at it.
34. Measure at least one number from rule 25 with Lighthouse or the browser performance panel.
