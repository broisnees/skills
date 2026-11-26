# Verify pass (rules 28-34)

The verify pass is what separates "looks done" from "works". Run every step, fix what fails, run it again. Report each rule as PASS or FAIL with its number.

## 1. Build clean (rule 28)

Run the project's own build, typecheck and lint. All three must have zero errors. Warnings get fixed or explained.

## 2. Automated sweep (rules 13, 28, 30, 31, 32)

```bash
npm i -D playwright && npx playwright install chromium   # once
node scripts/verify.mjs http://localhost:3000/page --out ./bro-ui-shots
```

For each of 3 widths (320, 768, 1440) times 2 themes (light, dark), the script checks:

| Check | Rule | Fails when |
|---|---|---|
| Console and network | 28 | any `console.error`, `console.warn`, uncaught exception or failed request |
| Overflow | 30 | the page scrolls sideways. It names the widest elements |
| Contrast | 31 | text under 4.5:1, or under 3:1 for large text, on its composited background |
| Hit targets | 13 | a control under 24 × 24px. Links inside running text are exempt |
| Focus | 32 | Tab lands on something with no outline and no box-shadow |

It also saves 6 screenshots. **Look at every one of them.** The script can't see overlap, clipped text, wrong alignment or ugly breaks. Exit code 0 means PASS.

Limits: it skips text on images and gradients, and it misses focus styles drawn only by a border or background change. Check those by eye.

## 3. Click everything (rule 29)

Use every control on the screen once, including the edge cases:
- Submit each form empty, with bad input, and with good input.
- Double-click every submit button. It should send one request.
- Open and close every menu, dialog and popover, with the mouse and then with Esc.
- Paste a 200 character string into every text field and check what happens to the layout.

Every action has to produce a visible result within 100 ms (rule 16).

## 4. Force the states (rule 33)

| State | How to force it |
|---|---|
| Empty | point the API at an empty fixture, or clear the data |
| Loading | DevTools Network panel, throttle to "Slow 3G" |
| Error | DevTools, right-click the request, "Block request URL", or return a 500 from a mock |
| Offline | DevTools Network panel, "Offline" |
| Long content | names with 60 characters, numbers with 9 digits, a list of 1,000 rows |

Each one has to look designed, not broken.

## 5. Keyboard only (rule 32)

Put the mouse away and complete the main task with Tab, Enter, Space, Esc and the arrow keys. Focus order follows the visual order, focus is always visible, and dialogs return focus to their trigger.

## 6. Measure one number (rule 34)

Run Lighthouse (performance.md) and record LCP, CLS and TBT. Compare them with rule 25.

## Report format

```
bro-ui verify: <page or component>
28 build/console    PASS  0 errors, 0 warnings
29 click-through    PASS  12 controls, 3 forms
30 widths           FAIL  320px: table overflows 140px -> wrapped in overflow-x container, re-run PASS
31 themes/contrast  PASS  lowest pair 4.8:1 (muted on card, dark)
32 keyboard         PASS
33 states           PASS  empty, loading, error, offline, long content
34 vitals           PASS  LCP 1.4 s, CLS 0.02, TBT 90 ms
```

A screen is done when every line says PASS.
