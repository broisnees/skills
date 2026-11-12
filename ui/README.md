# ui

My interface skill. It covers building, polishing and reviewing web UI, with one
exact value for every rule instead of a range to eyeball: motion, typography,
color, layout, surfaces, icons, accessibility and interface copy.

I built it by merging the UI skills I was already running (better-*, the motion
and design-engineering ones, the interface wiki) into one source of truth. Where
they disagreed I picked one number and wrote it down: press scale is `0.97`,
popovers start at `0.95`, list rows stagger by `30ms`, exits run 20% shorter than
entrances, and everyday UI never bounces.

It also carries my house style for when a project has no design system yet: a
dense, calm, dark-first tool look with Tailwind v4 tokens in OKLCH, contrast
measured on every text pair, and recipes for buttons, inputs, menus, dialogs,
tooltips, sidebar items, toasts, empty states and skeletons. A project's own
tokens always win over it.

## What's inside

| File | Covers |
|---|---|
| `SKILL.md` | Modes (build, polish, review, motion, vocabulary), recon, the non-negotiables, a quick audit, the 20 point polish pass, the done checklist |
| `references/house-style.md` | Default tokens and component recipes |
| `references/motion.md` | When to animate, easing and duration tokens, the 20 motion rules, springs, gestures, performance, reduced motion |
| `references/typography.md` | Scale, tracking, leading, measure, wrapping, tabular numbers |
| `references/color.md` | OKLCH, ramps, semantic tokens, contrast |
| `references/layout.md` | Spacing, optical alignment, hierarchy, responsiveness, safe area, layout shift |
| `references/surfaces.md` | Concentric radius, elevation, materials, icons |
| `references/accessibility.md` | Semantics, focus, keyboard, touch targets, forms, live regions |
| `references/writing.md` | Labels, headlines, errors, empty states |
| `references/patterns.md` | Optimistic updates, loading, combobox, command palette, shared element transitions |
| `references/glossary.md` | The vocabulary, so I can name an effect and ask for it |
| `references/review.md` | Review procedure, severity, output format |

## Install

```bash
git clone https://github.com/broisnees/skills.git ~/src/claude-skills
bash ~/src/claude-skills/ui/install.sh
```

It loads on demand for any UI task, or with `/ui`.
