# Accessibility

Most accessibility comes free with the platform: native elements bring keyboard support, real labels announce themselves, and a focus ring is one CSS rule. When unsure, use the native element and remove ARIA rather than adding it.

Two walks verify a flow. **Keyboard only:** every task completes, every stop shows focus. **Screen reader:** every control announces a name, a role and its state.

## Semantics

- `<button>` for actions, `<a href>` for navigation (it must support Cmd/Ctrl/middle-click), `<label>` for inputs, `<dialog>` or a tested library for modals. Never `<div onClick>`.
- One `<h1>`; headings nest without skipping. A `<main>` landmark, plus `<nav>` and `<header>` where real. A skip link comes first when chrome precedes main.
- Disabled: native `disabled` when truly unavailable. Use `aria-disabled="true"` when it must stay focusable, for example to show a tooltip explaining why, and block activation in code.

## Focus

```css
:focus-visible { outline: 2px solid var(--focus); outline-offset: 2px; }
@media (forced-colors: active) { :focus-visible { outline-color: Highlight; } }
```

- Style `:focus-visible`, not `:focus`. Never `outline: none` without a replacement.
- The ring has `3:1` contrast against everything it touches.
- Modals: move focus in on open, trap it (`inert` on the background), return it to the trigger on close, and use `overscroll-behavior: contain`.
- After deleting an item, move focus to the next item, or the previous one if it was last, never to `<body>`.
- Anchored headings get `scroll-margin-top` equal to the sticky header's height.

## Keyboard

- Every pointer interaction has a keyboard path. Esc closes overlays, Enter and Space activate, Tab moves between widgets, and arrows move within composite widgets (menus, tabs, listboxes, grids, radio groups) with a roving `tabindex`.
- Only `tabindex="0"` and `-1`. Never positive values.
- Shortcuts: show them in tooltips and menus, don't hijack browser and OS shortcuts, and don't fire single-key shortcuts while typing in an input.
- **No animation on keyboard-initiated actions.**

## Touch target

| Floor | Value |
| --- | --- |
| WCAG 2.5.8 AA | `24×24px` (or 24px spacing) |
| Recommended touch | `44×44px` |
| Recommended desktop | `40×40px` where density allows; `32px` controls are fine in dense tools with spacing |

Extend small visuals with a pseudo-element on the button or label (not on `<input>`):

```tsx
<button className="relative size-6 after:absolute after:-inset-2.5 after:content-['']">...</button>
```

- Extended areas must never overlap.
- Decorative overlays (glows, gradients) get `pointer-events-none` and `aria-hidden`.
- A checkbox and its label form one target with no dead gap.
- `touch-action: manipulation` on controls; `touch-action: none` only on custom gesture surfaces.
- Gate hover: `@media (hover: hover) and (pointer: fine)`. On touch, hover sticks after a tap.

## Names and labels

- Icon-only buttons get an `aria-label` describing the action ("Copy link", not "copy icon"). Visible text must be part of the accessible name.
- A placeholder is never a label. Visually hidden labels use `sr-only`.
- Inputs get `type`, `inputmode`, `autocomplete` and `name`. Never block paste.
- Images: decorative get `alt=""`, informative describe the meaning, functional describe the action.
- `aria-hidden` never goes on a focusable element.

## Forms and errors

- Keep submit enabled. Validate on submit (and on blur for fields already touched), never on every keystroke while the user is still typing.
- Invalid fields get `aria-invalid="true"` and `aria-describedby` pointing at the error. Focus the first invalid field.
- While submitting: disable the button, keep the label, add a spinner and `aria-busy`.

## Live regions

- `role="status"` (polite) for toasts, result counts and saved states. Render the empty region at mount, then change its text.
- `role="alert"` only for urgent errors.
- Toasts with actions or errors stay until dismissed.

## Motion, zoom, color

- Respect `prefers-reduced-motion` (see motion.md §8), `prefers-reduced-transparency` and `prefers-contrast`.
- Works at 200% zoom and 320px width. Use `min-height` rather than `height` on text containers. Never `maximum-scale=1` or `user-scalable=no`.
- Color is never the only signal. Contrast is measured (color.md).
- Autoplaying media needs a pause control. Nothing flashes more than 3 times per second.

## Before you finish

| Mistake | Fix |
| --- | --- |
| `<div onClick>` | `<button type="button">` |
| Icon button with no name | `aria-label` |
| `outline: none` | `:focus-visible` ring |
| Submit disabled until valid | Enabled; validate on submit |
| Tooltip on a `disabled` button | `aria-disabled` + explanation |
| `assertive` for routine toasts | `role="status"` |
| 16px icon button with no padding | Pseudo-element target to 24-44px |
