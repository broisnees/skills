---
name: ui
description: The complete interface skill for building, polishing and reviewing web UI. Use it for any component, screen or design system; motion and animation (easing, duration, springs, stagger, gestures, shared-element transitions); typography, color, layout, spacing, surfaces and icons; accessibility; interface copy; or a review of how an interface looks, moves and feels. It ships a dense, calm, dark-first house style for tool-grade apps and exact values for every rule. Trigger on "build a UI", "make this look good", "polish", "redesign", "animate", "review the UI", "design system", "tokens", "feels off", "dark mode", or any frontend task where the result should feel crafted.
---

# UI

Great interfaces come from hundreds of small decisions that are each correct. Users never notice them one at a time. They notice that the product feels fast, calm and trustworthy. This skill gives you those decisions, each with an exact value.

**Three laws, in priority order:**

1. **Usable before pretty.** Keyboard, focus, contrast, hit areas, readable text. A beautiful control nobody can operate is a defect.
2. **The project's system before this one.** Reuse the project's existing tokens, components, density and motion. Use the house style only where the project has no system, or when the user asks for it.
3. **Exact values, not vibes.** Every number here is chosen on purpose. `0.97` is not `0.95`, and `cubic-bezier(0.23, 1, 0.32, 1)` is not `ease-out`. Use what is written.

## Pick the mode

| The request | Mode | Do |
| --- | --- | --- |
| Build a new screen, component or app | **Build** | Recon, then [house-style.md](references/house-style.md), then the domain references the work touches |
| "Make it better", "polish", "feels off" | **Polish** | Recon, run the [quick audit](#quick-audit), then fix it in place, cheapest fix first |
| "Review", "audit", "what's wrong" | **Review** | [review.md](references/review.md). Read-only unless asked to fix |
| "Animate this" or "how should this move" | **Motion** | [motion.md](references/motion.md), starting with "should it animate at all" |
| "What's it called when..." | **Vocabulary** | [glossary.md](references/glossary.md) |

## Recon first (every mode)

Spend two minutes before writing a line:

- **Stack:** framework, styling (Tailwind v3 or v4, CSS modules, vanilla), component library (Radix, Base UI, shadcn, React Aria, custom), and motion library (`motion` or `framer-motion` in `package.json`, or none).
- **System:** existing tokens (`@theme`, `:root` variables, `tailwind.config`), the type scale, radii, spacing, and the dark-mode mechanism (`.dark` class, `data-theme`, or `prefers-color-scheme`).
- **Written rules:** `CLAUDE.md`, `AGENTS.md`, `CONTRIBUTING.md`, design-system docs, Storybook.
- **Neighbours:** read two or three sibling components and match their idiom exactly.

Write every fix in the project's own idiom. Never add a dependency to fix a detail. Never mix `motion/react` and `framer-motion` imports.

## The non-negotiables

These hold in every project, every mode. Details and recipes live in the references.

### Interaction and motion: [motion.md](references/motion.md)
- **Should it animate?** Anything triggered 100+ times a day, and every keyboard-initiated action, gets **no animation**. Hover and list navigation get at most a `≤150ms` color or opacity change.
- **Easing:** entrances and exits use `--ease-out: cubic-bezier(0.23, 1, 0.32, 1)`. On-screen moves use `--ease-in-out: cubic-bezier(0.77, 0, 0.175, 1)`. Only progress uses `linear`. **Never use `ease-in` on UI.**
- **Duration:** press `120ms`, hover `150ms`, tooltip `150ms`, dropdown or popover `200ms` (the range is 150-250ms), dialog `250ms`, sheet `300ms`. User-initiated UI never exceeds `300ms`. **Exits are 20% shorter than enters.**
- **Press:** `scale: 0.97` on `:active`. **Popovers start at `scale: 0.95` + `opacity: 0`**, never `scale(0)`.
- **Enter from the trigger, exit to the trigger** (`transform-origin` at the anchor). Modals are the exception: they stay centered.
- **No bounce on everyday UI.** Use `bounce: 0`. Reserve overshoot for momentum the user threw (flick or release).
- **Interruptible:** use CSS transitions or springs for state, never keyframes. **Don't tween while held:** a drag or slider tracks 1:1 with `transition: none`.
- **Stagger list rows by `30ms`**, capped so the whole cascade ends within `300ms`.
- Animate only `transform`, `opacity`, `filter` and `clip-path`. Name the properties; never `transition: all`.
- **`prefers-reduced-motion`** turns movement into an opacity crossfade. Motion is never the only signal of a state change.

### Typography: [typography.md](references/typography.md)
- Body `line-height` is `1.5`, headings `1.1-1.25`. Large type gets negative tracking (`-0.02em` at 32px+). Small uppercase labels get positive tracking (`+0.06em`).
- Put `font-variant-numeric: tabular-nums` on every number that changes or sits in a column.
- Use `text-wrap: balance` on headings and `text-wrap: pretty` on paragraphs (no widows). Long-form text is capped at `65ch`.
- Weight `≥400` below 18px. Inputs are `16px` on touch so iOS does not zoom. Apply `antialiased` once, at the root.

### Color: [color.md](references/color.md)
- `oklch()` for new systems. Primitives are named by hue, semantic tokens by role, and components use **only** the semantic tokens.
- One accent, and only the status colors the product actually uses. **One filled primary action per view.**
- Measure contrast on the rendered pair: `4.5:1` for text, `3:1` for UI and large text. Never estimate it.
- Color is never the only signal; pair it with an icon or label.

### Layout and surfaces: [layout.md](references/layout.md) · [surfaces.md](references/surfaces.md)
- Use a 4px spacing grid. **The gap between groups is at least 2× the gap within a group.** Group with space first, background second, and a line last.
- **Concentric radius:** `outer = inner + padding`.
- Shadows show elevation and borders show structure. Use layered, low-alpha shadows, never pure black at high opacity.
- Use logical properties (`ps-`, `pe-`, `ms-`, `inset-inline-*`). Respect `env(safe-area-inset-*)`. Prefer container queries.
- **No layout shift:** reserve space for images, async content, scrollbars (`scrollbar-gutter: stable`) and changing numbers.
- Correct optical alignment by eye: use `pe` 2px less on the icon side of a button, and nudge play triangles right.

### Accessibility: [accessibility.md](references/accessibility.md)
- Use native elements first: `<button>`, `<a href>`, `<label>`, `<dialog>`. No ARIA beats bad ARIA.
- A visible `:focus-visible` ring on everything focusable (`2px`, offset `2px`). Never `outline: none` without a replacement.
- Every pointer action has a keyboard path. Esc closes, arrows move within a widget, Tab moves between widgets.
- **Touch targets:** 24px minimum, 44px on touch and 40px on desktop where density allows. Extend the target with a pseudo-element.
- Every icon-only button has an `aria-label`. Errors use `aria-invalid` + `aria-describedby`, and focus goes to the first invalid field.

### Writing: [writing.md](references/writing.md)
- Buttons start with a verb and name the outcome ("Delete project", not "OK"). Use sentence case everywhere.
- Errors say what happened and how to fix it, next to the field. No "Oops", no exclamation marks, no blame.
- Empty states say what goes here, why it matters, and offer one next action.

### Patterns: [patterns.md](references/patterns.md)
Optimistic updates, skeletons and layout stability, combobox, command palette, progressive disclosure, shared-element transitions, toasts, forms, tables, perceived performance.

## Quick audit

When polishing, sweep for these first. They cover about 80% of what makes UI feel off:

| Smell | Fix |
| --- | --- |
| `transition: all`, or keyframes on toggles | Name properties; use a transition |
| `ease-in`, default `ease`, or `> 300ms` on UI | `--ease-out`, durations from the motion table |
| `scale(0)` entrances, popovers growing from the center | `scale(0.95)` + opacity, `transform-origin` at the trigger |
| Hover and keyboard actions that animate | Remove the motion; keep an instant color change |
| Nested radii that match | `outer = inner + padding` |
| Gray borders everywhere for depth | Layered shadow on raised surfaces; borders only for structure |
| Jumping numbers or layout | `tabular-nums`, reserved space, skeletons sized like the content |
| Lopsided headings, orphan words | `text-wrap: balance` / `pretty` |
| Two or more filled buttons competing | One primary; the rest neutral or ghost |
| Missing focus ring, `div` buttons, unlabeled icons | `:focus-visible` ring, `<button>`, `aria-label` |
| Hover styles stuck on touch | `@media (hover: hover) and (pointer: fine)` |
| Theme toggle smears colors | Disable transitions for one frame during the swap |
| Raw hex and one-off sizes | Semantic tokens and the type and spacing scales |
| "Oops! Something went wrong." | "Unable to save. Check your connection and try again." |
| Empty, loading and error states missing | Design all four: empty, loading, error, ideal |

## The polish pass (remove the slop)

Generated and template UI fails in the same twenty ways. Run this pass on every landing page, marketing surface, dashboard or screen you build, in this order. Subtract first, then sharpen, then add.

**Subtract**
1. **Delete filler badges.** "New", "AI-powered" or "Beta" pills that say nothing, and sparkle icons on every heading. A badge must carry real state or it goes.
2. **Drop redundant labels.** A "Search" label above a search field with a magnifier and placeholder, "Email:" beside `name@example.com`, or section headings that repeat the nav. Keep the label only if removing it leaves an input with no accessible name; use `sr-only` in that case.
3. **Unitalicize random words.** Use italics and gradient-text emphasis at most once per view, on the one word that carries the meaning. Never decorate a word just because it's a keyword.
4. **Mono only where needed.** Monospace is for code, IDs, hashes, keyboard shortcuts and aligned numerals. It is never for headings, labels or body text "to look technical".
5. **Remove embellishments.** Decorative gradients, glows, blobs, grain, glassmorphism on everything, rotating borders, icons inside every card, emoji bullets. If it doesn't explain, group or give feedback, delete it.

**Sharpen**
6. **Use a design system.** Every color, size, radius, space and shadow comes from a token ([house-style.md](references/house-style.md) when the project has none). Five near-identical grays mean one system is missing.
7. **Group with spacing.** Use the 2× rule before borders and cards: related items sit `8px` apart and groups sit `24px`+ apart. Unbox things that only needed space.
8. **Make headlines specific.** "Ship reviewed code in half the time" beats "The future of development". Say what it does, for whom, and the outcome, with no adjectives a competitor could also claim.
9. **Wrap headlines properly.** `text-wrap: balance`, tight `line-height: 1.1`, negative tracking, and a max width so a headline breaks into two even lines. Never leave one word on its own line.
10. **Improve text contrast.** Light-gray-on-white "elegance" fails. Secondary text must still pass `4.5:1`. Measure it.
11. **Use tabular nums.** Prices, stats, tables, timers and counters all get `tabular-nums`.
12. **Keep icons consistent.** One icon library, one stroke width (`1.5` at regular weight), one size per context (`16px` inline, `20px` for nav), and `currentColor`. Never mix outline and filled icons, except filled for the active state.
13. **Inner radius = outer − padding.** Nested rounded surfaces are concentric.
14. **Align by eye, not pixels.** Optically center icons, play glyphs and quotation marks. Hang punctuation in pull quotes. Nudge until it looks centered.

**Add**
15. **Show the actual product.** Use a real screenshot, a live embed or an interactive demo, not abstract 3D shapes or stock illustration. If the product isn't ready, show the real flow with real-looking data.
16. **Enlarge the main feature.** One hero element dominates, at 2-3× the visual weight of anything else. If everything is the same size, nothing is important.
17. **Emphasize the CTA.** One filled accent button per view, verb-first ("Start free trial"), with secondary actions as ghost or link. It should be the highest-contrast element on the screen.
18. **Add an accent colour.** A fully neutral UI reads as unfinished. Pick one accent and spend it only on the primary action, selection, focus and key data.
19. **Add loading states.** Skeletons shaped like the content, button spinners that keep the label width, optimistic updates and progress for anything over `1s`. Never a blank screen or layout jump.
20. **Animate useful feedback.** Press scale, success pulse, origin-aware popovers and an icon crossfade on state change. Motion confirms that something happened. It never decorates.

## Before you say done

- [ ] Every state exists: default, hover, active, focus-visible, disabled, loading, empty, error, and selected where it applies.
- [ ] Light and dark both checked, plus `prefers-reduced-motion`.
- [ ] Checked at 320px width, at 200% zoom, with long strings, and with keyboard only.
- [ ] No layout shift on load, hover or data update.
- [ ] Every value comes from a token or a scale. Raw numbers have a written reason.
- [ ] Motion replayed at 10% speed in the browser's Animations panel when it matters. Anything you could not check is reported as **Not verified**, never as done.

When a browser is available (Deck browser, preview tools or Playwright), look at the rendered result before claiming it is right. Source alone cannot prove a visual.
