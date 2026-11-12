# Writing

Interface copy is design. Clear beats clever, consistent beats varied, and the best error message is the redesign that makes the error impossible.

## Voice

- Read the nearby copy first and match its terms and voice. One product, one voice; tone flexes with the stakes:

| Context | Tone |
| --- | --- |
| Success, onboarding, empty | Warm, can be light |
| Routine actions, settings | Neutral, minimal |
| Errors, destructive confirmation | Calm, plain, no playfulness |
| Data loss, security, billing | Serious, explicit |

- Address the reader as "you". In errors, avoid "we" ("Unable to load", not "We're having trouble...").
- Use plain words a tired reader gets on the first pass. Cut every word that does no work. No idioms or jokes that won't translate.
- **Sentence case** everywhere: buttons, titles, menus, tabs. Store it in natural case.
- One term per concept: if it's "Archive" in the menu, it's "Archive" in the toast.

## Labels

- **Buttons start with a verb and name the outcome:** "Create project", "Save draft", "Delete 3 files". Never "OK", "Submit", "Yes", "Let's go!".
- Confirmation dialogs: the title asks ("Delete this project?"), the body states the consequence ("This removes 24 files for everyone. You can't undo this."), and the buttons are `Delete project` / `Cancel`.
- Flow vocabulary: "Continue" (or "Next", but pick one), "Back", "Done". Never alternate synonyms.
- Toggles describe the ON state: "Send read receipts", not "Disable read receipts".
- Links describe their destination ("View billing docs"). Never "click here"; suffix "Learn more about exports".
- **Drop redundant labels:** don't label what the UI already says (a "Search" heading over a search box, "Name:" before a field already labelled, "Click to" in a tooltip).
- Match the device: "select" works for both; "tap" for touch only, "click" for pointer only.

## Headlines

- **Specific over grand:** "Review pull requests 2× faster with inline AI comments", not "Reimagine your workflow". Name the user, the action and the outcome.
- One idea per headline, `≤ 10` words. A subhead adds the proof or mechanism.
- No "Unlock", "Supercharge", "Seamless", "Revolutionize", "Next-gen", "Elevate" or "Empower". <!-- ai-tells: ignore -->
- No gratuitous italics or gradient words.

## Errors

| Bad | Good |
| --- | --- |
| Invalid input | Use only letters and spaces |
| Password too short | Use at least 8 characters |
| Oops! Something went wrong. | Unable to save. Check your connection and try again. |
| Error 500 | The server couldn't finish this. Try again in a minute. |

- What happened, plus how to fix it, placed next to where it broke. No blame, no "oops", no exclamation marks.
- Phrase hints positively and show them *before* the mistake.
- Offer the recovery action as a button: "Try again", "Reconnect".

## Empty states

- Say what this place is, why it's useful, and offer one next action. "No projects yet. Projects keep tasks and files together. [Create project]".
- Search and filter empty states name the query and offer an exit: "No results for 'quarterly'. [Clear filters]".

## Numbers, time, placeholders

- Use `Intl` formatting. Relative time ("2 min ago") with the absolute time in a tooltip. Plurals via `Intl.PluralRules`/ICU, never `"item(s)"`.
- Never build sentences from fragments around variables; word order changes across languages.
- Placeholders show an example (`name@company.com`), never the label or an instruction.

## Loading and progress copy

Name the work: "Saving…", "Uploading 3 of 12…", "Indexing repository…". Use `…` (one character). No "Please wait". <!-- ai-tells: ignore -->

## Badges and microcopy

**Delete filler badges.** "New", "Beta", "AI" or "Pro" only when they're true and actionable, and never more than one per item. Remove marketing badges from app UI.
