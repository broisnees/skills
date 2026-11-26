# Interaction (rules 13-19)

## Hit targets

| Context | Minimum | Source |
|---|---|---|
| Pointer, AA | 24 × 24px, or 24px of clear spacing around a smaller target | WCAG 2.2 SC 2.5.8 |
| Pointer, AAA | 44 × 44px | WCAG 2.2 SC 2.5.5 |
| iOS | 44 × 44pt | Apple HIG |
| Android | 48 × 48dp | Material |

A small icon can keep its visual size and get a bigger hit area through padding or a `::before` with negative inset.

## The 8 states (rule 18)

Every interactive component is designed in all of these before it counts as done:

| State | What it looks like |
|---|---|
| default | resting |
| hover | surface shift about 0.03 L. Desktop only: wrap in `@media (hover: hover)` so phones don't get stuck hovers |
| active / pressed | about 0.06 L, or `transform: scale(0.97)` |
| focus-visible | 2px ring, 2px offset, 3:1 against the background |
| disabled | 40-50% opacity or muted tokens, `cursor: not-allowed`, and the reason in a tooltip when it isn't obvious |
| loading | spinner inside the control, same width (no layout shift), `aria-busy="true"`, clicks ignored |
| empty | what will appear here, plus the one action that fills it |
| error | what went wrong and how to fix it, next to the field, `aria-invalid` and `aria-describedby` |

## Feedback timing (rule 16)

- Under 100 ms: just update the UI.
- Over 100 ms: change the control right away (pressed, spinner in the button). People click twice when nothing changes.
- Over 1 s: a skeleton in the shape of the result.
- Over 10 s: progress with a number, and a cancel button.

## Optimistic updates (rule 17)

When the server rejects under about 1% of requests, show success right away and reconcile later:

```js
async function toggleDone(item) {
  const prev = item.done;
  setItem({ ...item, done: !prev });        // UI changes in the same frame
  try {
    await api.update(item.id, { done: !prev });
  } catch (err) {
    setItem({ ...item, done: prev });       // roll back
    toast.error("Couldn't save. Check your connection and try again.");
  }
}
```

Undo beats confirmation. "Delete? Are you sure?" costs every user a click on every delete, and people learn to click through it. An undo toast for about 5 seconds costs nothing until someone needs it. Keep real confirmations for actions that can't be undone, and make them type-to-confirm when the damage is large.

## Keyboard (rule 19)

| Key | Does |
|---|---|
| Tab / Shift+Tab | next and previous control, in visual order |
| Enter | submit the form, open the focused item |
| Space | toggle a checkbox or press a button |
| Esc | close the top layer (menu, dialog, popover), then return focus to what opened it |
| Arrow keys | move inside one widget (menu items, tabs, list rows, radio group) |
| Cmd/Ctrl+K | command menu, when the app has one |

- Dialogs trap focus inside while they are open, and give it back when they close.
- Use `:focus-visible`, not `:focus`, so mouse clicks don't flash rings.
- Never `outline: none` without a replacement.
- Use real elements: `<button>` for actions and `<a href>` for navigation. A `div` with `onClick` has no keyboard support, no role and no focus.

## Copy in controls

- Buttons say what happens: "Save changes", "Delete project". Not "OK" or "Submit".
- Errors say what went wrong and what to do: "Password needs 12 or more characters." Not "Invalid input."
- Empty states say what will appear and give the first step: "No invoices yet. Create one to bill a client."
