# Performance (rules 25-27)

## Core Web Vitals

Google's thresholds, measured at the 75th percentile of real page loads:

| Metric | Measures | Good | Poor |
|---|---|---|---|
| LCP, Largest Contentful Paint | when the main content shows | ≤ 2.5 s | > 4 s |
| INP, Interaction to Next Paint | delay from a click or key to the next frame | ≤ 200 ms | > 500 ms |
| CLS, Cumulative Layout Shift | how much content jumps around | ≤ 0.1 | > 0.25 |

## Measure (rule 34)

```bash
# lab numbers for one page
npx lighthouse http://localhost:3000 --only-categories=performance,accessibility \
  --output=json --output-path=./lh.json --chrome-flags="--headless"
node -e 'const r=require("./lh.json").audits;for(const k of ["largest-contentful-paint","cumulative-layout-shift","total-blocking-time"])console.log(k, r[k].displayValue)'
```

Lighthouse can't measure INP, because it needs a real interaction. Use Total Blocking Time as the lab stand-in (under 200 ms is good), or record a click in the browser's Performance panel and read the interaction's duration. In production, the `web-vitals` npm package reports real values.

## Stop layout shift (rule 26)

| Cause | Fix |
|---|---|
| Image without dimensions | `width` and `height` attributes, or `aspect-ratio` |
| Web font swap changes line width | `font-display: optional`, or `size-adjust` on the fallback `@font-face` |
| Banner or ad injected above content | reserve its height, or put it in an overlay |
| Spinner replaced by content of a different size | skeleton with the final dimensions |
| Button text changes to "Saving..." and widens the button | fixed `min-width`, or put a spinner over the label |

## Keep interactions fast

- Long tasks over 50 ms block input. Split them with `await scheduler.yield()` (or `setTimeout(0)`), or move them to a Web Worker.
- Debounce search input by 150-250 ms. Never block typing on a network call.
- Virtualize lists over a few hundred rows (rule 27): render only what's visible, plus a buffer. Libraries: TanStack Virtual, react-window. Or use `content-visibility: auto` with `contain-intrinsic-size` for simple long pages.
- Ship less JavaScript. Parse and execute time on a mid-range phone is several times slower than on a dev laptop, so measure with CPU throttling at 4x in DevTools.

## Perceived speed

- Prefetch on hover or on pointer down. The gap between hovering a link and clicking it is usually a few hundred milliseconds, enough to start the request.
- Render the shell first, then stream data in.
- Optimistic updates (interaction.md) turn a 300 ms round trip into 0 ms on screen.
