# Review

A review reports what is wrong, with evidence, ranked by what it costs users. It is read-only unless the user asks for fixes.

## Procedure

1. **Scope.** Name the screen, flow, component or diff being reviewed. If the scope is too large to inspect credibly, narrow it to one complete flow and say what you excluded. For a diff, review what changed plus the surfaces it affects. Pre-existing issues go in a separate short section.
2. **Recon.** Stack, tokens, written guidelines (SKILL.md "Recon first"). Write fixes in the project's idiom.
3. **Inspect in order**, so foundational failures aren't hidden by polish:
   1. Accessibility
   2. Layout and hierarchy
   3. Writing
   4. Typography
   5. Color
   6. Surfaces, icons and motion
   7. The polish pass (SKILL.md, the 20 items)
4. **States.** Default, hover, focus-visible, active, disabled, loading, empty, error, long content, 320px, 200% zoom, dark, reduced motion.
5. **Verify.** Render it when a browser is available. Replay motion at 10%. Measure contrast. Anything you couldn't check is **Not verified**, never a finding and never an implied pass.

## Severity

- **HIGH:** blocks a task, misleads, hides content or controls, risks data loss, or is a systemic failure.
- **MEDIUM:** meaningfully harms comprehension, efficiency, consistency or adaptability.
- **LOW:** isolated polish.

**Always HIGH:** an interactive control with no accessible name · no visible focus · pointer-only paths · motion that ignores reduced-motion · content clipped at 320px or 200% · failing text contrast · meaning carried by color alone · a destructive action with no confirm or undo · truncation with no way to see the full value · an error with no recovery path · the danger color on a non-destructive action · a state shown by motion alone.

Within a severity, rank by reach: a token or shared-component fix outranks the same symptom in one leaf.

## Cheapest fix first

1. **Delete:** the redundant border, the animation on a frequent action, the ARIA a native element makes unnecessary, the filler badge.
2. **Use the platform:** the native element or the browser's focus ring.
3. **Reuse:** an existing token, spacing step or curve.
4. **Correct the value:** the exact value from this skill.
5. **Add:** a new token, wrapper or media query.

Proposing step 5 when step 1 works is itself a finding.

## Output

```md
**Scope:** <what was reviewed> · **Excluded:** <what wasn't>
**Inspected:** a11y ✓ · layout ✓ · writing ✓ · type ✓ · color ✓ · surfaces/motion ✓ · states: <list>

| # | Sev | Location | Before | After | Why |
| - | --- | --- | --- | --- | --- |
| 1 | HIGH | `src/Button.tsx:14` | `<div onClick>` | `<button type="button">` | No keyboard path or role |

**Verified:** <commands, interactions, measurements and results>
**Not verified:** <what couldn't be checked and why>
**Verdict:** Block (any HIGH) | Approve
```

- One row per root cause, listing every location.
- Show the current code in Before and the exact replacement in After. Never paraphrase.
- Cap at 15 rows. If more HIGHs exist than fit, list them first and say how many were cut.
- Use evidence, not taste. A density, radius or voice you merely dislike is not a finding. A documented project convention changes *where* you report (against the token or guideline), not *whether*.
- No findings is a valid result: "No actionable UI findings", plus what you verified.
