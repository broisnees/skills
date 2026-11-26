# bro-ui

My short UI rulebook: 34 numbered rules in one 65 line file. Every rule is a
number, a formula or a named source, so a screen can be checked instead of
eyeballed. The last 7 rules are a verify pass. A screen is done when that pass
is clean, not when it looks done.

`ui` is the long reference with recipes and a house style. `bro-ui` is the
checklist I run when I want a screen finished and working.

## What's inside

| Group | Rules | Built on |
|---|---|---|
| Layout and type | 1-7 | 4px grid, Gestalt proximity, geometric type scale from Weber's law (`size = base × r^n`), 45-75 character lines, nested radius math |
| Color | 8-12 | OKLCH ramps, the WCAG 2.2 contrast formula (4.5:1 text, 3:1 controls), tinted neutrals, separate dark theme |
| Interaction | 13-19 | Fitts's law and 24/44px targets, Hick's law, about 4 chunks of working memory (Cowan 2001), Nielsen's 0.1s / 1s / 10s limits, 8 required component states |
| Motion | 20-24 | 100-300ms durations, ease-out entries, spring damping ratio `ζ = c / (2√(km))`, 16.7ms frame budget, reduced motion |
| Performance | 25-27 | Core Web Vitals: LCP ≤ 2.5s, INP ≤ 200ms, CLS ≤ 0.1 |
| Verify pass | 28-34 | Zero console errors, every control clicked, 320/768/1440px, both themes, keyboard only, forced error and empty states, one Lighthouse number |

Rule numbers are stable ids. A removed rule leaves a gap, so other skills and
notes can cite `bro-ui 13` and keep meaning the same thing.

## Install

```bash
git clone https://github.com/broisnees/skills.git ~/src/claude-skills
bash ~/src/claude-skills/bro-ui/install.sh
```

It only runs when I type `/bro-ui` (`disable-model-invocation: true`).
