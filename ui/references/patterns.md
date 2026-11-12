# Patterns

Behaviors that make an app feel fast and trustworthy. Each lists the rule, then the recipe.

## Optimistic updates

Apply the change in the UI immediately, send the request, and reconcile.

- Use it for likes, toggles, renames, reorders, sends, deletes with undo, and status changes: anything that succeeds more than 99% of the time.
- On failure, roll back, show an inline error or toast with "Try again", and keep the user's input. Never silently discard it.
- Pending items look nearly final, maybe `opacity-70` or a small spinner beside them, never a blocking overlay.
- With TanStack Query: `onMutate` snapshots and sets data, `onError` restores, `onSettled` invalidates. With React 19: `useOptimistic`.
- **Delete with undo beats confirm dialogs** for reversible actions: remove the item, show "Deleted · Undo" for `6s`, and commit afterwards.

## Loading states

| Wait | Show |
| --- | --- |
| `< 300ms` | Nothing; showing a spinner causes flicker |
| `300ms-1s` | A subtle inline indicator (button spinner, row shimmer) |
| `1-10s` | A skeleton shaped like the content, or a determinate progress bar |
| `> 10s` | Progress with stage labels, plus the ability to leave and come back |

- Delay showing indicators by about `300ms`. Once shown, keep them visible for at least `500ms` so they don't flash.
- Skeletons match final dimensions exactly. No layout shift on arrival.
- Keep stale data visible while refetching (stale-while-revalidate) and indicate refreshing subtly.
- A spinner that rotates faster feels faster (`600-800ms` per turn).
- **Prefetch** on hover intent (about `100ms` hover) or on the cursor's trajectory, on `focus` for keyboard users, and on `touchstart` for touch. Don't prefetch everything.
- Respond within about `100ms` and finish visible feedback within `400ms` (Doherty threshold).

## Layout stability

See layout.md "Layout shift". Rule: nothing the user is looking at moves unless they caused it.

## Combobox, select, autocomplete

- Use a tested primitive (Radix, Base UI, React Aria, cmdk, Ariakit). Never hand-roll one.
- Input with `role="combobox"`, `aria-expanded`, `aria-controls` and `aria-activedescendant`; listbox with options.
- Arrows move the highlight (the input keeps focus), Enter selects, Esc closes and then clears, Home/End jump, and typing filters.
- Highlight the matched substring in `font-medium`. Show "No results for 'x'" with a create option where relevant.
- Debounce remote search by `150-200ms`, show an inline loading row, and cancel stale requests (`AbortController`).
- The highlight moves instantly; never animate it under keyboard control.

## Command palette

- `⌘K` / `Ctrl+K`. **No open/close animation.** Focus goes to the input on open.
- Fuzzy matching across actions, navigation and recent items. Recent items appear first when the query is empty.
- Each row shows an icon, label, a breadcrumb or group label, and a trailing shortcut.
- Nested pages (for example "Change theme ›") use Backspace on an empty query to go back.

## Progressive disclosure

- Show the 20% of options used 80% of the time, and put the rest behind "Advanced", a disclosure, or a secondary menu.
- Hidden things are signposted: "Show 8 more", a chevron, a peeking scroll edge.
- Prefer inline expansion (accordion, popover) over navigating away.
- Don't hide primary actions in overflow menus to look minimal. Simplicity is not minimalism.

## Shared-element transitions

- When the same object appears in two places (list row → detail view, thumbnail → lightbox, tab underline), morph it with Motion `layoutId` or the View Transitions API.
- Only the shared element morphs. Surrounding content crossfades.
- Use spring `{ duration: 0.35, bounce: 0 }` or `--ease-in-out`, `300ms`.
- View Transitions: give each element a unique `view-transition-name`, set it just before the transition, clear it after, and style `::view-transition-old/new(name)`.

## Toasts

See house-style.md. Use toasts for results of the user's own actions that happen away from the focal point. Inline feedback beats a toast when the change is visible where the user is looking.

## Tables and lists

- Right-align numbers with `tabular-nums`. Left-align text. Headers are aligned like their data.
- Sticky header; row height `32-40px`; hover background on the row; actions revealed on row hover *and* focus-within (and always visible on touch).
- Selection: checkbox column, shift-click range, and a bulk action bar that appears without shifting layout.
- Virtualize past about 200 rows.
- Truncate long cells with a tooltip containing the full value.

## Forms

- Single column, labels above, related fields grouped with spacing, and a primary action at the end of the form flow.
- Accept messy input (Postel's law): trim, allow spaces in card numbers, and parse dates in multiple formats.
- Autosave settings, with a quiet "Saved" status, instead of a Save button where possible.
- Long forms: show progress, save drafts, and keep the user's input across errors.

## Dangerous actions

| Severity | Treatment |
| --- | --- |
| Reversible | Do it, then offer Undo |
| Irreversible, small | Confirm dialog with a verb button |
| Irreversible, large blast radius | Type-to-confirm (the resource's name) |

The danger color is reserved for destructive actions only.

## Laws worth applying

- **Fitts:** frequent and important targets are big and near the cursor's path. Screen edges are infinite targets.
- **Hick:** fewer choices make faster decisions. Group and stage them.
- **Miller:** chunk things into groups of about 4-7 (phone numbers, settings sections).
- **Jakob:** users expect your app to work like the others they use. Break conventions only with proof.
- **Peak-end:** make the end of a flow (success state) and its best moment feel great.
- **Zeigarnik / goal gradient:** show incomplete progress ("3 of 5 steps") to motivate completion.
- **Tesler:** complexity can't vanish, so move it from the user into the system.
- **Von Restorff:** the one different thing gets noticed, so make it the CTA and nothing else.
