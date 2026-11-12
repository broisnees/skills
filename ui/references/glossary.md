# Glossary

Precise words for precise prompts. If you can name the effect, you can ask for it or fix it.

## Typography

| Term | Meaning | Where it lives |
| --- | --- | --- |
| **Kerning** | Spacing adjustment between specific letter pairs (AV, To) from the font's kerning table | `font-kerning: normal` (keep on) |
| **Tracking** | Uniform letter-spacing across a run of text; negative for large text, positive for small caps | `letter-spacing` |
| **Leading** | Vertical distance between lines | `line-height` |
| **x-height** | Height of lowercase letters; governs perceived size more than the font size does | Font choice, `font-size-adjust` |
| **Tabular numbers** | Equal-width digits so changing values don't shift | `font-variant-numeric: tabular-nums` |
| **Widow** | A single word stranded on the last line of a paragraph | `text-wrap: pretty` |
| **Orphan** | A paragraph's first line stranded at the bottom of a column | `orphans`, layout |
| **Line length / measure** | Characters per line; 60-75 is ideal | `max-width: 65ch` |
| **Balanced text** | Lines of near-equal length in a heading | `text-wrap: balance` |
| **Optical sizing** | Glyph shapes adjusted for the size they're rendered at | `font-optical-sizing: auto` |
| **Hanging punctuation** | Quotes and bullets set outside the text edge so the letters align | `hanging-punctuation` |

## Layout and visual

| Term | Meaning |
| --- | --- |
| **Optical centre** | The perceived center, slightly above the geometric center. Center things by eye. |
| **Optical alignment** | Nudging shapes (icons, triangles, round glyphs) so they *look* aligned |
| **Concentric radius** | Inner radius = outer radius − padding |
| **Layout shift** | Content jumping as things load or change (CLS) |
| **Safe area** | Screen region clear of notches, rounded corners and the home indicator: `env(safe-area-inset-*)` |
| **Touch target / hit area** | The tappable region, which may exceed the visible element (24px minimum, 44px recommended) |
| **Affordance** | A visual cue that tells you how something can be used (a button looks pressable) |
| **Progressive disclosure** | Showing only what's needed now and revealing more on demand |
| **Elevation** | Perceived height of a surface, shown with shadow or lightness |
| **OKLCH** | A perceptual color space: Lightness, Chroma, Hue. Equal numeric steps look equal. |
| **Semantic token** | A color or size named by role (`--text-secondary`), not by value |
| **Scrim** | A dimming layer behind a modal |
| **Vibrancy** | Text and icons tuned to stay legible on blurred or translucent material |

## Interaction

| Term | Meaning |
| --- | --- |
| **Optimistic update** | Show the result before the server confirms; roll back on failure |
| **Combobox** | A text input plus a listbox of suggestions (autocomplete, searchable select) |
| **Command palette** | A keyboard-summoned (⌘K) searchable list of every action |
| **Roving tabindex** | One tab stop per composite widget; arrows move inside it |
| **Focus trap** | Keeping focus inside a modal until it closes |
| **Skeleton** | A placeholder shaped like the coming content |
| **Stale-while-revalidate** | Show cached data while fetching fresh data |
| **Hysteresis** | A movement threshold before a gesture commits |

## Motion

| Term | Meaning |
| --- | --- |
| **Easing** | The acceleration curve of a transition (ease-out, ease-in-out) |
| **Spring** | Physics-based motion defined by stiffness and damping (or duration and bounce), with no fixed timeline |
| **Critically damped** | A spring that settles with no overshoot (`bounce: 0`) |
| **Interruptible animation** | Can be reversed or redirected mid-flight, starting from its current value |
| **Origin-aware animation** | Scales or grows from the element that triggered it (`transform-origin` at the anchor) |
| **Stagger** | Successive delays across a group of items entering |
| **Shared element transition** | One element morphs between two views (`layoutId`, View Transitions) |
| **Crossfade** | Old fades out while new fades in, overlapping |
| **Rubber-banding** | Increasing resistance when dragging past a boundary, then a spring back |
| **Momentum / projection** | Using release velocity to predict where a flicked object lands |
| **Velocity handoff** | The animation continues at the finger's speed when a drag ends |
| **Squash and stretch** | Deforming a moving object along its motion axis (a toggle knob stretching about 12%) |
| **Arc** | Natural objects travel on curved paths, not straight lines |
| **Pop in / scale in** | Entering from `scale(0.95)` + `opacity: 0` |
| **Mask / clip reveal** | Revealing via `clip-path` rather than fading or resizing |
| **Pulse** | A single brief scale-up to confirm an action |
| **Pop layout** | Exiting items are taken out of flow so the rest reflow immediately (`mode="popLayout"`) |
| **FLIP** | First, Last, Invert, Play: the technique behind layout animations |
| **Scroll-driven animation** | Animation progress tied to scroll position (`animation-timeline: scroll()`) |
| **Reduced motion** | The OS preference to minimize movement: `prefers-reduced-motion` |
