<!-- ai-tells: ignore-file (describes what each skill bans) -->

# skills

My Claude skills. One directory per skill, each self-contained with its own
`SKILL.md`.

| Skill | What it does |
|---|---|
| [me](me/) | Whose voice it is. Docs, comments, commit bodies, PRs and specs come out in my own first person instead of tutorial voice ("you should...") or third person ("the user can..."), with no AI byline and no "here's your new component, feel free to modify it" handover. |
| [write-as-bro](write-as-bro/) | Whether it reads human. Hard ban on em dashes and en dashes, plus the vocabulary (delve, leverage, seamless), the filler phrases, and the even paragraph rhythm that make prose sound machine generated. Ships a grep checker. |
| [ui](ui/) | How the interface looks, moves and feels. One exact value per rule for motion, type, color, layout, surfaces, icons, accessibility and copy, plus a dense dark-first house style with OKLCH tokens and component recipes for projects that have no design system yet. |
| [bro-ui](bro-ui/) | Whether the interface is finished. 34 short rules built on perception math (Fitts, Hick, Weber, WCAG contrast, spring damping, Core Web Vitals), ending in a verify pass that has to come back clean before a screen counts as done. Runs only on `/bro-ui`. |

They stack: `me` makes the work mine, `write-as-bro` makes it sound like I wrote it, `ui` makes the interface feel right, `bro-ui` proves it works.

## Install one skill

Clone the collection anywhere, then run that skill's installer. It symlinks the
skill into `~/.claude/skills/` and wires its always-on import:

```bash
git clone https://github.com/broisnischal/skills.git ~/src/claude-skills
bash ~/src/claude-skills/me/install.sh
```

Or link it by hand:

```bash
ln -s ~/src/claude-skills/me ~/.claude/skills/me
```

Per-project instead of personal: pass `--project` to the installer, or link into
`.claude/skills/` inside the repo.

Each skill's own README has the details. MIT.
