# Formats: what shape the deliverable takes

Pick the section matching what you're writing. This covers *shape* — length, structure, layout. For who it's going to and what that changes, see `audiences.md`. For finding and framing the point in the first place, `foundations.md` comes first and applies to all of these.

- **[Management summary](#management-summary)** — status updates, recommendations, decisions, anything a decision-maker reads to act on. Always paired with an email variant.
- **[Short article](#short-article-half-page-to-full-page)** — a standalone half-page or full-page piece: project write-up, internal blog post, docs page, one-pager.
- **Anything else** — notes, explanations, messages, documentation prose: `foundations.md` alone is the whole ruleset. No separate format rules needed.

---

## Management summary

For anything read by a decision-maker who needs the point before the detail.

1. **BLUF — Bottom Line Up Front.** The first sentence is the conclusion, recommendation, or ask. A reader who stops after sentence one should still know what you want from them.
2. **Situation → Complication → Solution.** After the BLUF sentence, give just enough of: what's the situation, what's the problem, what's proposed — in that order, each in one or two sentences.
3. **Visual signposting.** Bold lead-ins or short bullets so a skimming reader can scan the argument's shape. One bold lead-in per list item, not per sentence (see `humanizer.md` under "Formatting tells").
4. **One ask per summary.** If there are several, number them. Never bury a second ask in a supporting paragraph.
5. **Numbers, not adjectives.** "Reallocate $100k from print to digital," not "significantly increase digital investment."
6. **Target length holds regardless of source length.** The full version lands around 150-250 words (roughly a half page), whether the source was a paragraph or a 10-page analysis. A longer source means cutting harder, not writing longer — if the compressed version keeps growing with the source, the extra detail belongs in an attachment.
7. **When resources can't cover every valid ask, triage — don't flatten.** If not everything is affordable this cycle, say which asks are for now and which are deferred, and why. A numbered list with no stated priority makes the reader redo the triage you already did.
8. **Don't silently cut genuine uncertainty.** If something is materially unresolved — a correlation that might not be causal, an unassessed risk — compressing it away makes the recommendation look better-supported than it is. Keep it in one clause: "…though this may reflect existing dissatisfaction rather than an independent cause." Cut restatement and detail; never cut an open question that would change the reader's confidence.

**Weak (buries the ask):**
> We have conducted an exhaustive analysis of market trends and evaluated multiple operational strategies going forward, considering budget constraints and team capacity across both channels.

**Better (BLUF + concrete):**
> We recommend reallocating $100k from print to digital ads next quarter. Digital converts at 3x the rate of print in this segment, and the shift can happen within existing budget.

### Always also produce the crisp email variant

Whenever you produce a management summary, also produce the email variant below — regardless of whether it's actually going out as an email. Show both, back to back, unless the user has said they only want one. This gives a ready-to-forward version even when the primary deliverable is a doc, a Slack message, or a report.

The email variant follows every rule above, plus:

1. **The subject line does half the work.** Formula: `CATEGORY: specific ask + deadline`. "DECISION: Approve $100k print→digital shift by Friday" beats "Marketing budget question." Categories worth standardizing on: DECISION, REQUEST, ACTION, INFO, UPDATE.
2. **Cap it at 3-5 sentences, ~125 words.** If the honest version needs more, email is the wrong container: write the BLUF sentence plus one supporting sentence and attach the detail.
3. **Assume the reader is on a phone between meetings.** No large unbroken blocks. More than two items becomes a real bulleted list, not a comma run-on.
4. **Bold the one thing you need from them.** In an email specifically — unlike a report — bold the ask itself, not just a lead-in word, so a phone-scanning reader spots the decision without reading around it.
5. **Know when to break the length rule.** A genuinely complex decision crushed into 3 sentences reads as evasive. If the content can't survive the cut, flag it ("more context below, but the ask is:") rather than silently overrunning.

**Example:**
> **Subject: DECISION: Approve $100k print→digital shift by Friday**
>
> Recommend reallocating $100k from print to digital ads next quarter — digital converts at 3x the rate in this segment, no new budget needed.
>
> Full analysis attached. Need your sign-off by Friday to hit the Q2 media buy deadline.

---

## Short article (half page to full page)

For a standalone piece read on its own terms. Governs layout on top of `foundations.md`'s heading and bullet rules, which still apply at sentence and list level.

| Length | Headline | Subheadings | Bullets |
|---|---|---|---|
| Half page (~150-300 words) | One, the point in miniature | None — a subhead at this length is clutter, not navigation | At most one list, and only for a genuine 3+ item parallel set |
| Full page (~400-700 words) | One | 2-4 (see the trade-off below) | Any section with 3-6 parallel items; the majority stays prose |

**Subhead count and section length trade off against each other.** Divide total length by the number of subheads you actually need — don't force each section to hit a fixed word count independently. At 450 words, four sections run ~110 words each; at 700 words with two sections, ~350 each. Both are fine. If a section comes out thin, cut its subheading and fold it into the neighbour; never pad to reach a target.

Add a subheading when a real topic shift happens, not because the piece got long. A full-page piece on one continuous idea can run with zero subheadings; a half-page piece genuinely covering three topics can earn two.

**Genre overrides the subhead count, and the table above is written for the scanning case.** A measured Economist feature runs **619 words across 8 paragraphs with zero subheadings and zero bullets** — and it works, because paragraph breaks and ordinal signposting in the prose ("There are three reasons… One is… The second reason… The third reason…") carry the structure instead. That is the narrative convention: continuous prose, transitions doing the navigation.

So decide by how the piece will be read:

- **Scanned** — docs page, internal write-up, anything a reader will skim for the part they need: use the subhead counts above.
- **Read start to finish** — a narrative piece, an essay, a story-shaped update: subheads are optional and often wrong. Signpost inside the prose instead.

Getting this backwards produces the two familiar failures: a narrative chopped into administrative sections, or a reference page written as an undifferentiated wall.

**Headline:**
1. **5-10 words** — specific enough to be informative, short enough to scan at a glance.
2. **Front-load the claim**, not a generic label. "Vendor migration slips three weeks after data bug" beats "Migration status update."
3. **It works like a miniature nut graf.** Someone who reads only the headline should know what the piece says and roughly why it matters — the headline does at article scale what the lead sentence does in `foundations.md`'s pyramid principle.

**Or split it in two, which is what professional practice actually does.** A measured Economist business piece pairs a **4-word headline** with a **12-word standfirst**:

> **Why everybody hates Palantir**
> *Beyond America, the company risks becoming a victim of its own hype*

Neither half satisfies rule 1 or 2 alone. The headline is shorter than 5 words and poses a question rather than front-loading a claim; the standfirst is longer than 10 words and carries the actual angle. **Together** they do the job the single-headline rule describes: the headline earns the click, the standfirst delivers the point.

So treat rules 1-3 as governing *the pair, not one line*:

- **One line only** (a PR title, a doc heading, an email subject) → rules 1-3 as written. The line must carry the claim, because nothing else will.
- **Headline plus standfirst or deck** → the headline may be short and provocative; the standfirst must then carry the claim in a full clause. Never let both be vague, and never make the headline a bare label with no standfirst to rescue it.

**This is one observed headline, not a pattern.** The pair structure is a well-established magazine convention, but the specific 4-and-12 word split is a single data point. Don't treat those numbers as targets.

**Subheadings** (full-page only):
1. **One per genuine topic shift.** A section under ~40 words means the subheading isn't earning its place.
2. **Each previews its section** — a reader decides whether to read on from the subhead alone.
3. **One heading level only.** Sub-subheadings under a page mean the piece should be split or the sections are sliced too finely.

**Bullets vs. prose:**
1. **Same 3-6 item cap as `foundations.md`.** At half-page length one list is usually all the piece needs — don't add a second for variety.
2. **Open and close on prose.** The opening paragraph (carrying the point) and the closing line (takeaway or ask) are never bulleted. Bullets are for the scannable middle, not the frame.

**Skeletons:**
> **Half page:** Headline → paragraph opening with the point → one or two supporting paragraphs (optionally one short list) → stop. No closing subhead.
>
> **Full page:** Headline → opening paragraph with the point → 2-4 subheaded sections sized by the trade-off above, prose with bullets where a section has a real parallel list → short prose closing paragraph with the takeaway or ask.

---

## Sources

**Management summary.** Patterns drawn from Harvard Business Review's coverage of BLUF-style executive communication (lead with the point so a reader knows what's needed within the first 30 seconds) and Bloomberg/wire-service inverted-pyramid convention (most important fact first, supporting detail in descending order). Email-specific rules drawn from BLUF-for-email guidance on word-count caps (~125-150 words), category-tagged subject lines, and mobile-first skimming, plus the "three-sentence email" convention. Rules 6-8 (length target independent of source length, triage over flattening, preserving genuine uncertainty) came from dry-running this skill against a multi-page source analysis with competing findings, where no documented rule covered any of the three.

**Short article.** Subheading cadence and headline length generalized from short-form web-writing guidance (subheads roughly every 100-300 words; headlines around 5-10 words, front-loaded), scaled down proportionally — that source guidance addresses full blog posts of 1,500-2,500 words, and nothing found addresses sub-page pieces directly. The headline-as-nut-graf framing ties to the journalism convention cited in `foundations.md`.

All rules here are original synthesis, not reproduced source text.

**Status: partly derived from secondary sources.** HBR, Bloomberg and WSJ are paywalled or block automated fetching, so those publication-convention rules still come from write-ups *describing* them rather than analysis of published sentences. **The Economist is no longer in that group:** a full feature supplied by the user was measured directly, and the short-article subhead rule above was corrected as a result — see `foundations.md` sources for the measurements. The short-article length ratios are a proportional extrapolation, not verified against real sub-page examples. See the v2 checklist for what primary sourcing has since been substituted in.

---

**This file is not self-enforcing.** The checks described above are gated by `CHECKLIST.md` — run it, and `check.py`, before returning any draft.
