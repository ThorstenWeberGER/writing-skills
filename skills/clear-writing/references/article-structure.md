# Structuring a half-page to full-page article

For a standalone short write-up meant to be read as its own piece — a project update, an internal blog post, a docs page, a one-pager. Not a management summary (see `style-management-summary.md`, which has its own length target and BLUF structure) and not a multi-page report.

This governs layout — how many headings, how long each section, when to use bullets — on top of `foundations.md`'s heading/bullet rules, which still apply at the sentence and list level.

## Match structure to length

| Length | Headline | Subheadings | Bullets |
|---|---|---|---|
| Half page (~150-300 words) | One, functions as the point in miniature | None — a subhead below this length adds clutter without aiding navigation | At most one list, only if there's a genuine 3+ item parallel set |
| Full page (~400-700 words) | One | 2-4 (see note below) | Any section with 3-6 parallel items; majority of the piece stays prose |

**Subhead count and section length trade off against each other.** Divide the total length by the number of subheads you actually need — don't force every section to hit some fixed word count independently. At 450 words, four sections run ~110 words each; at 700 words with two sections, they run ~350. Both are fine. If a section comes out thin, cut the subheading and fold it into its neighbour — never pad a thin section to reach a target length.

Don't add a subheading just because the piece is long — add it when a real topic shift happens. A full-page piece on one continuous idea can still run with zero subheadings; a half-page piece that genuinely covers three distinct topics can still earn two.

## Headline

1. **5-10 words.** Long enough to be specific, short enough to scan in one glance.
2. **Front-load the claim or topic**, not a generic label. "Vendor migration slips three weeks after data bug" beats "Migration status update."
3. **It should work like a miniature nut graf** — a reader who reads only the headline should know what the piece is about and roughly why it matters, the same way the lead sentence does in `foundations.md`'s pyramid principle.

## Subheadings (full-page pieces only)

1. **One per genuine topic shift, not per word count.** Total length divided by subhead count sets your section length — see the note under the table. A section under ~40 words usually means the subheading isn't earning its place; fold it into the neighbouring section rather than padding it.
2. **Each previews its section** — same rule as `foundations.md`'s heading rule, just applied at sub-page scale: a reader should be able to decide whether to read the section from the subhead alone.
3. **Cap it at one heading level.** A second level (sub-subheadings) is almost never justified under a page — it signals the piece should be split or the sections are too finely sliced.

## Bullets vs. prose

1. **Same 3-6-item cap as `foundations.md`.** At half-page length, one bullet list is often the only list the piece needs — resist adding a second just for variety.
2. **Open and close on prose, even in a bullet-heavy piece.** The opening paragraph (carrying the point) and the closing line (the takeaway or ask) shouldn't be bulleted — bullets are for the scannable middle, not the frame.

## Worked skeletons

**Half page:**
> Headline → one paragraph opening with the point → one or two supporting paragraphs (optionally one short bullet list) → done. No closing subhead needed.

**Full page:**
> Headline → opening paragraph with the point → 2-3 subheaded sections, each 100-200 words, prose with bullets where a section has a genuine parallel list → short closing paragraph (prose, not a subhead) restating the takeaway or ask.

## Sources

Subheading cadence and headline-length conventions generalized from blog/short-form web-writing guidance (subheads roughly every 100-300 words; headlines around 5-10 words, front-loaded) and scaled down proportionally to half-page/full-page length, since that source guidance addresses full blog posts (1,500-2,500 words) and nothing directly addresses sub-page-length pieces. The headline-as-miniature-nut-graf framing ties back to the journalism convention already cited in `foundations.md` and `style-general-writing.md`. Rules here are original synthesis, not reproduced text.

**Status: the length-to-structure ratios (half page = no subheads, full page = one per 100-200 words) are a proportional extrapolation from blog-length sources, not independently verified against short-form print/docs examples.** Re-derive once real half-page/full-page examples are available — see the v2 checklist.
