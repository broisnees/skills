# House style

The default look when a project has no system of its own: a dense, calm, dark-first tool interface. Neutral surfaces carry about 90% of the screen, one accent marks what matters, type is small and crisp, borders are hairlines, and motion is quick and quiet. It should feel like a precision instrument, not a marketing page.

If the project already has tokens, **use theirs**. Borrow only the parts of this file that fill a gap.

## Character

- **Dark first, light equal.** Design in dark, then verify light with the same care. Both are first-class.
- **Density with air.** Controls are compact (`32px`), and the space *between groups* stays generous. Compactness comes from small type and tight controls, never from cramming groups together.
- **Quiet chrome, loud content.** Sidebars, toolbars and headers recede: low contrast, no fills, no shadows. The user's content gets the contrast.
- **Keyboard first.** Every primary action has a shortcut shown in a `<kbd>`. A command palette (`⌘K`) reaches everything.
- **Instant.** Optimistic updates everywhere, no spinners for anything under `300ms`, and no animation on keyboard actions.

## Tokens (Tailwind v4)

Contrast was measured for every text/background pair listed. Recheck any pair you add.

```css
@import "tailwindcss";

@custom-variant dark (&:where(.dark, .dark *));

:root {
  /* Surfaces */
  --bg: oklch(1 0 0);                 /* page */
  --bg-surface: oklch(0.985 0 0);     /* sidebar, panels */
  --bg-raised: oklch(1 0 0);          /* menus, popovers, dialogs */
  --bg-sunken: oklch(0.97 0 0);       /* inputs, code wells */
  --bg-hover: oklch(0.955 0 0);
  --bg-selected: oklch(0.935 0 0);
  --scrim: oklch(0 0 0 / 0.4);

  /* Text: primary 17.7:1, secondary 7.1:1, tertiary ≥4.6:1 on bg/surface/sunken */
  --text: oklch(0.21 0 0);
  --text-secondary: oklch(0.44 0 0);
  --text-tertiary: oklch(0.52 0 0);   /* metadata only; never on hover or selected rows */
  --text-on-accent: oklch(1 0 0);

  /* Borders */
  --border-subtle: oklch(0 0 0 / 0.06);
  --border: oklch(0 0 0 / 0.1);
  --border-strong: oklch(0 0 0 / 0.18);

  /* Accent (one hue; change the hue, keep L and C) */
  --accent: oklch(0.55 0.2 265);       /* white text on it: 5.1:1 */
  --accent-hover: oklch(0.5 0.2 265);
  --accent-subtle: oklch(0.55 0.2 265 / 0.1);
  --accent-text: oklch(0.5 0.2 265);   /* 6.3:1 on bg */
  --focus: oklch(0.55 0.2 265);

  /* Status: use only what the product ships */
  --danger: oklch(0.55 0.2 27);        /* white text: 5.4:1 */
  --danger-text: oklch(0.52 0.19 27);
  --success-text: oklch(0.5 0.13 155);
  --warning-text: oklch(0.52 0.12 70);

  /* Elevation */
  --elev-sm: 0 1px 2px -1px oklch(0 0 0 / 0.08), 0 0 0 1px var(--border);
  --elev-md: 0 0 0 1px var(--border), 0 4px 8px -2px oklch(0 0 0 / 0.08), 0 2px 4px -2px oklch(0 0 0 / 0.06);
  --elev-lg: 0 0 0 1px var(--border), 0 16px 32px -8px oklch(0 0 0 / 0.16), 0 4px 8px -4px oklch(0 0 0 / 0.08);
}

.dark {
  --bg: oklch(0.16 0 0);
  --bg-surface: oklch(0.185 0 0);
  --bg-raised: oklch(0.235 0 0);
  --bg-sunken: oklch(0.14 0 0);
  --bg-hover: oklch(0.215 0 0);
  --bg-selected: oklch(0.25 0 0);
  --scrim: oklch(0 0 0 / 0.6);

  --text: oklch(0.96 0 0);            /* 17.3:1 */
  --text-secondary: oklch(0.78 0 0);  /* ≥6.7:1 on raised */
  --text-tertiary: oklch(0.66 0 0);   /* ≥4.8:1 on bg, raised, hover */

  --border-subtle: oklch(1 0 0 / 0.05);
  --border: oklch(1 0 0 / 0.08);
  --border-strong: oklch(1 0 0 / 0.14);

  --accent-hover: oklch(0.6 0.2 265);
  --accent-subtle: oklch(0.7 0.15 265 / 0.14);
  --accent-text: oklch(0.74 0.13 265); /* 8.3:1 */
  --focus: oklch(0.7 0.15 265);        /* 7.2:1 */

  --danger-text: oklch(0.72 0.16 25);
  --success-text: oklch(0.76 0.15 155);
  --warning-text: oklch(0.82 0.14 80);

  /* Dark: rings carry the edge; shadows only separate floating layers */
  --elev-sm: 0 0 0 1px var(--border);
  --elev-md: 0 0 0 1px var(--border-strong), 0 8px 16px -4px oklch(0 0 0 / 0.5);
  --elev-lg: 0 0 0 1px var(--border-strong), 0 24px 48px -12px oklch(0 0 0 / 0.6);
  color-scheme: dark;
}

@theme inline {
  --color-bg: var(--bg);
  --color-surface: var(--bg-surface);
  --color-raised: var(--bg-raised);
  --color-sunken: var(--bg-sunken);
  --color-hover: var(--bg-hover);
  --color-selected: var(--bg-selected);
  --color-fg: var(--text);
  --color-fg-secondary: var(--text-secondary);
  --color-fg-tertiary: var(--text-tertiary);
  --color-line-subtle: var(--border-subtle);
  --color-line: var(--border);
  --color-line-strong: var(--border-strong);
  --color-accent: var(--accent);
  --color-accent-hover: var(--accent-hover);
  --color-accent-subtle: var(--accent-subtle);
  --color-accent-text: var(--accent-text);
  --color-danger: var(--danger);
  --color-danger-text: var(--danger-text);
  --color-success-text: var(--success-text);
  --color-warning-text: var(--warning-text);

  --font-sans: "Inter Variable", "Inter", ui-sans-serif, system-ui, -apple-system, "Segoe UI", sans-serif;
  --font-mono: "JetBrains Mono Variable", ui-monospace, "SF Mono", Menlo, monospace;

  /* Type scale: size / line-height */
  --text-2xs: 0.6875rem; --text-2xs--line-height: 1rem;      /* 11: kbd, badges */
  --text-xs: 0.75rem;    --text-xs--line-height: 1rem;       /* 12: metadata */
  --text-sm: 0.8125rem;  --text-sm--line-height: 1.25rem;    /* 13: UI default */
  --text-base: 0.875rem; --text-base--line-height: 1.375rem; /* 14: reading in-app */
  --text-md: 1rem;       --text-md--line-height: 1.5rem;     /* 16: long-form, mobile inputs */
  --text-lg: 1.125rem;   --text-lg--line-height: 1.5rem;     /* 18: section titles */
  --text-xl: 1.375rem;   --text-xl--line-height: 1.75rem;    /* 22: page titles */
  --text-2xl: 1.75rem;   --text-2xl--line-height: 2.125rem;  /* 28 */
  --text-3xl: 2.5rem;    --text-3xl--line-height: 2.75rem;   /* 40: marketing display */

  --radius-xs: 4px;  /* kbd, badges, checkboxes */
  --radius-sm: 6px;  /* buttons, inputs, menu items */
  --radius-md: 8px;  /* cards, menu items inside a p-1 menu */
  --radius-lg: 12px; /* menus and popovers (8 + 4 padding) */
  --radius-xl: 16px; /* sheets, large panels */

  --ease-out: cubic-bezier(0.23, 1, 0.32, 1);
  --ease-in-out: cubic-bezier(0.77, 0, 0.175, 1);
  --ease-drawer: cubic-bezier(0.32, 0.72, 0, 1);

  --shadow-sm: var(--elev-sm);
  --shadow-md: var(--elev-md);
  --shadow-lg: var(--elev-lg);
}

@layer base {
  html { -webkit-font-smoothing: antialiased; -moz-osx-font-smoothing: grayscale; text-rendering: optimizeLegibility; }
  body { @apply bg-bg text-fg font-sans text-sm; font-feature-settings: "cv11", "ss01"; } /* Inter: single-storey a off, open digits */
  :focus-visible { outline: 2px solid var(--focus); outline-offset: 2px; }
  ::selection { background: var(--accent-subtle); }
  * { scrollbar-width: thin; scrollbar-color: var(--border-strong) transparent; }
}
```

Use `oklch(0 0 0 / α)` and `oklch(1 0 0 / α)` alpha borders so one token works on every surface. Text never uses alpha colors, because its contrast can't be verified.

## Density and sizing

| Thing | Value |
| --- | --- |
| Base spacing grid | `4px` (`gap-1` = 4, `gap-2` = 8, `gap-3` = 12, `gap-4` = 16, `gap-6` = 24) |
| Control height | sm `28px` (`h-7`), **default `32px` (`h-8`)**, lg `36px` (`h-9`) |
| Control height on coarse pointers | `40px` minimum; use `@media (pointer: coarse)` |
| Button padding | `px-3` default, `px-2.5` small; icon side `-2px` |
| Icon size | `16px` in controls and rows, `14px` in dense metadata, `20px` in nav rail |
| Icon stroke | `1.5` (Lucide `strokeWidth={1.5}`); `2` only beside semibold text |
| List row | `32px` tall, `px-2`, `rounded-sm`, `gap-2` between icon and label |
| Sidebar | `240-280px`, resizable, `bg-surface`, separated by a `1px` `border-line` |
| Content measure | `max-w-[65ch]` for prose, `max-w-3xl` for forms and chat columns |
| Page padding | `16px` mobile, `24px` tablet, `32px` desktop |
| Header and toolbar | `44-48px` tall, sticky, `bg-bg/80 backdrop-blur-md` with a bottom hairline that appears only once scrolled |

## Weights

`400` body, `500` for UI labels, buttons and active nav, `600` for headings. Avoid `700`+ in app UI; it looks shouty at small sizes.

## Component recipes

Use with `cn()` (clsx + tailwind-merge). Adapt to the project's primitives (Radix, Base UI, React Aria).

### Button

```tsx
const button = cva(
  "inline-flex items-center justify-center gap-1.5 whitespace-nowrap rounded-sm text-sm font-medium select-none " +
  "transition-[background-color,color,box-shadow,scale] duration-150 ease-out " +
  "active:not-disabled:scale-[0.97] active:duration-[120ms] " +
  "disabled:opacity-50 disabled:pointer-events-none " +
  "focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-[var(--focus)] " +
  "[&_svg]:size-4 [&_svg]:shrink-0",
  {
    variants: {
      variant: {
        primary: "bg-accent text-white hover:bg-accent-hover shadow-[inset_0_1px_0_oklch(1_0_0/0.15)]",
        secondary: "bg-raised text-fg shadow-sm hover:bg-hover",
        ghost: "text-fg-secondary hover:bg-hover hover:text-fg",
        danger: "bg-danger text-white hover:brightness-110",
      },
      size: { sm: "h-7 px-2.5 text-xs", md: "h-8 px-3", lg: "h-9 px-4", icon: "size-8" },
    },
    defaultVariants: { variant: "secondary", size: "md" },
  },
);
```

- **Loading:** keep the label in the DOM with `invisible`, overlay a spinner centered, and set `aria-busy`. The width never changes.
- **Icon-only:** `size="icon"`, an `aria-label`, and a tooltip with the label plus its shortcut.

### Input

```tsx
"h-8 w-full rounded-sm bg-sunken px-2.5 text-sm text-fg placeholder:text-fg-tertiary " +
"shadow-[inset_0_0_0_1px_var(--border)] hover:shadow-[inset_0_0_0_1px_var(--border-strong)] " +
"focus-visible:outline-2 focus-visible:outline-offset-0 focus-visible:outline-[var(--focus)] " +
"aria-invalid:shadow-[inset_0_0_0_1px_var(--danger)] " +
"max-sm:text-md transition-[box-shadow] duration-150"
```

The label sits above at `text-xs font-medium text-fg-secondary`, `mb-1.5`. Help or error text sits below at `text-xs`, `mt-1.5`.

### Menu, popover, select

```tsx
// content
"min-w-48 rounded-lg bg-raised p-1 shadow-lg origin-[var(--radix-dropdown-menu-content-transform-origin)] " +
"data-[state=open]:animate-[pop-in_200ms_var(--ease-out)] data-[state=closed]:animate-[pop-out_160ms_var(--ease-out)]"
// item: inner radius = 12 - 4 = 8
"flex h-8 items-center gap-2 rounded-md px-2 text-sm text-fg outline-none cursor-default " +
"data-[highlighted]:bg-hover data-[disabled]:opacity-50 [&_svg]:size-4 [&_svg]:text-fg-secondary"
// shortcut on the right
"ms-auto text-xs text-fg-tertiary tabular-nums"
```

```css
@keyframes pop-in  { from { opacity: 0; scale: 0.95; } }
@keyframes pop-out { to   { opacity: 0; scale: 0.95; } }
```

Open/close here is keyframes because the library unmounts. Context menus get **no entrance animation**, only the exit. Menu item highlight is instant, never transitioned.

### Dialog

- Scrim `bg-[var(--scrim)]`, fading in over `250ms`.
- Panel: `max-w-md rounded-xl bg-raised p-6 shadow-lg`, centered, entering from `scale: 0.96` + `opacity: 0` + `translateY(8px)` over `250ms` with `--ease-out`. It exits in `200ms`.
- Title `text-lg font-semibold`, description `text-sm text-fg-secondary mt-1.5`. Actions sit at the end, `gap-2`, with the primary last (trailing).
- Destructive: the confirm button repeats the verb ("Delete project"). For irreversible actions with a large blast radius, ask the user to type the name.

### Tooltip

`rounded-sm bg-fg text-bg text-xs px-2 py-1` (inverted). Delay `500ms` on first show, then `0ms` with no animation for adjacent tooltips within `300ms`. Content is the label plus `<kbd>`.

### Kbd

```tsx
"inline-flex h-5 min-w-5 items-center justify-center rounded-xs px-1 font-mono text-2xs text-fg-secondary " +
"bg-surface shadow-[inset_0_-1px_0_var(--border),0_0_0_1px_var(--border)]"
```

Show platform glyphs: `⌘ ⇧ ⌥ ⌃` on macOS, `Ctrl Shift Alt` elsewhere.

### Sidebar nav item

```tsx
"flex h-8 items-center gap-2 rounded-sm px-2 text-sm text-fg-secondary " +
"hover:bg-hover hover:text-fg aria-[current=page]:bg-selected aria-[current=page]:text-fg aria-[current=page]:font-medium"
```

Sections are labelled `text-xs font-medium text-fg-tertiary px-2 mb-1 mt-4`. Counts sit trailing with `tabular-nums text-fg-tertiary`.

### Badge and status

`inline-flex h-5 items-center gap-1 rounded-xs px-1.5 text-2xs font-medium`. Status always pairs a `6px` dot or an icon with text. Tint the background with the status color at `/0.12` and use the `*-text` token for the label.

### Toast

Bottom-right on desktop and top-center on mobile, `max-w-sm rounded-lg bg-raised p-3 shadow-lg`. It enters from `translateY(100%)` and exits the same way. Auto-dismiss after `4s`, or `6s` with an action. It pauses on hover and while the tab is hidden. Errors and toasts with actions stay until dismissed. Announce through a persistent `role="status"` region.

### Empty state

Centered in its region, `max-w-sm`, `py-12`. A `20px` icon in `text-fg-tertiary` (no illustration in app UI), a title `text-sm font-medium`, one line of `text-sm text-fg-secondary`, and one button. Search empty states name the query and offer "Clear filters".

### Skeleton

`rounded-sm bg-hover`, with a shimmer (`linear-gradient` sweeping at `1.5s linear infinite`) disabled under reduced motion. Each skeleton matches the final content's exact height and line count, so nothing jumps when data arrives.

### Code and diffs

Font `font-mono text-[12.5px] leading-5`, block `bg-sunken rounded-md p-3`, with `tabular-nums` line numbers in `text-fg-tertiary`. Additions get a green tint at `/0.12`, deletions red at `/0.12`, with a `+` or `−` gutter glyph so color isn't the only signal.

## Marketing surfaces (when the app needs a site)

Keep the same tokens and fonts so the site and the product feel like one thing. Hero: a `text-3xl` (or `clamp(2.5rem, 5vw, 4rem)`) headline with `font-semibold`, `tracking-[-0.03em]`, `leading-[1.05]` and `text-balance`, `max-w-[18ch]`. Under it, one sentence at `text-md text-fg-secondary max-w-[48ch]`, then one primary CTA and one ghost CTA. Then **a real product screenshot**, with an image outline and the large shadow. No blobs, no gradient text, no fake logos.
