# bro-ui

My UI rulebook: 37 numbered rules, each one a number, a formula or a named
source, so a screen can be checked instead of eyeballed. Rules 28-34 are a
verify pass. A screen is done when that pass is clean, not when it looks
done.

`ui` is the long reference with recipes and a house style. `bro-ui` is the
checklist I run when I want a screen finished and working, with a calculator
for every number and a Playwright script that exits 1 when a check fails.

## What's inside

| Group | Rules | Built on |
|---|---|---|
| Layout and type | 1-7 | 4px grid, Gestalt proximity, geometric type scale from Weber's law (`size = base × r^n`), 45-75 character lines, nested radius math |
| Color | 8-12 | OKLCH ramps, the WCAG 2.2 contrast formula (4.5:1 text, 3:1 controls), tinted neutrals, separate dark theme |
| Interaction | 13-19 | Fitts's law and 24/44px targets, Hick's law, about 4 chunks of working memory (Cowan 2001), Nielsen's 0.1s / 1s / 10s limits, 8 required component states |
| Motion | 20-24 | 100-300ms durations, ease-out entries, spring damping ratio `ζ = c / (2√(km))`, 16.7ms frame budget, reduced motion |
| Performance | 25-27 | Core Web Vitals: LCP ≤ 2.5s, INP ≤ 200ms, CLS ≤ 0.1 |
| Verify pass | 28-34 | Zero console errors, every control clicked, 320/768/1440px, both themes, keyboard only, forced error and empty states, one Lighthouse number |
| Copy | 35-37 | Buttons name the action, errors say how to fix, empty states give the first step |

## Files

| File | What it is |
|---|---|
| `SKILL.md` | The 37 rules and how to run them |
| `references/math.md` | Every formula with a worked number: Weber, WCAG contrast, OKLCH, Fitts, Hick, Cowan, Nielsen, springs, frame budget, nested radius |
| `references/type-and-layout.md` | Spacing scale, type roles, alignment, radius, responsive |
| `references/color.md` | Building the palette in OKLCH, token roles with measured contrast, common failures |
| `references/interaction.md` | Target sizes, the 8 states, feedback timing, optimistic updates, keyboard map |
| `references/motion.md` | Duration and easing tables, spring presets, reduced motion, CSS recipes |
| `references/performance.md` | Core Web Vitals, measuring, layout shift fixes, fast interactions |
| `references/verify.md` | The full verify procedure and report format |
| `scripts/bro_ui.py` | Calculator: `contrast`, `ramp`, `oklch`, `scale`, `spring`, `fitts`, `hick`, `radius`. Standard library only |
| `scripts/verify.mjs` | Playwright sweep over 3 widths and 2 themes: console errors, overflow, contrast, target size, focus rings, screenshots |
| `examples/tokens.css` | Starter tokens for projects with no system, every text pair measured |

Rule numbers are stable ids. A removed rule leaves a gap, so other skills and
notes can cite `bro-ui 13` and keep meaning the same thing.

## Install

```bash
git clone https://github.com/broisnees/skills.git ~/src/claude-skills
bash ~/src/claude-skills/bro-ui/install.sh
```

It only runs when I type `/bro-ui` (`disable-model-invocation: true`).
