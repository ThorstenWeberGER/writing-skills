# Foundations: structure, wording, and formatting

These rules apply to every piece of writing, before picking a style guide (see `style-management-summary.md` or `style-general-writing.md`) or checking for violations (`DONTS.md`, `examples.md`).

## Structure: lead with the point

A reader — or a manager skimming for five seconds — should get the main point from the first sentence, not the last.

**The pyramid principle:** state the conclusion or recommendation first. Support it after, in order of decreasing importance. Never build up to the point — state it, then justify it.

**Wrong order (climactic — point comes last):**
> We looked at three vendors, ran cost comparisons across two quarters, and interviewed the two teams that would use the tool daily. Based on all of this, we recommend Vendor B.

**Right order (pyramid — point comes first):**
> We recommend Vendor B. It costs 18% less than the incumbent over two quarters and both using teams preferred it in interviews.

**How to check it:**
1. Find the single most important sentence — the conclusion, recommendation, or key fact. If it isn't the first sentence, move it there.
2. Order everything else by descending importance. A reader should be able to stop after any paragraph and still have the most important information seen so far.
3. Cut a paragraph entirely if, once reordered, it only restates or builds up to something already said.

**Signal this rule catches:** a summary that opens with background before the finding; a message where the actual request is in the last paragraph; "Based on the above, we therefore..." as a paragraph opener.

### Finding the point before you lead with it

Leading with the point only works if you've correctly identified which point is strongest. Three checks, in order:

1. **Find the complication, not the situation.** Background (what's normally true) isn't the point — the change, gap, or problem that forces a decision now is. If a draft opens with context that hasn't changed, that's the situation talking, not the complication. Ask: *what's different, wrong, or at risk here that wasn't before?* That's the candidate point.
2. **Run the "so what?" test.** State the candidate point, then ask "so what?" and answer it. Ask "so what?" again of that answer. Stop when the answer is something the reader would act on or change their mind about — that final answer is the real point. A point that survives zero rounds of "so what?" (the reader shrugs) isn't strong enough to lead with.
3. **When several points compete, rank by reader impact, not writer effort.** The point that took the most work to produce isn't automatically the strongest one to lead with. Rank candidates by what's most consequential, most urgent, or most likely to change what the reader does next — not by how much analysis went into it.

Once you've found the point this way, feed it into the pyramid: that point goes first, and the situation/complication reasoning that got you there becomes the supporting structure underneath it, not the opening.

**Signal this rule catches:** a strong-sounding opening that's actually still describing the situation ("Our team has been monitoring X for months..."); a "key finding" that produces no reaction when you ask "so what?"; a report leading with the most-researched section instead of the most decision-relevant one.

## Plain wording

1. **Short words over long ones.** "Use" not "utilize." "Help" not "facilitate." "Start" not "commence."
2. **Short sentences.** One idea per sentence. More than one "and" joining independent clauses — consider splitting.
3. **Active voice, named actor.** "The team shipped the fix," not "the fix was shipped."
4. **Concrete over abstract.** A number, name, or date beats a qualitative claim. "Costs rose 18%," not "costs rose significantly."
5. **Cut words that don't change the meaning.** "In order to" → "to." "Due to the fact that" → "because." "At this point in time" → "now."
6. **Common words over jargon.** Use the everyday word unless the audience specifically needs the technical term.

**Quick self-check:** read the sentence aloud. If you wouldn't say it that way to a colleague across a table, rewrite it.

## Headings and lists

1. **Headings tell the reader what's coming.** A heading should let someone decide whether to read the section at all, before they read it.
2. **Bullets are for scannable, parallel items — not narrative.** Use them for steps, features, or short parallel facts. Keep every bullet in a list grammatically parallel (all start with a verb, or all are noun phrases — don't mix).
3. **Keep lists short.** Three to six bullets. More than that stops being scannable and should probably be prose or split into subsections.
4. **Use prose, not bullets, for anything nuanced, sensitive, or narrative.** Bullets read as efficient, not warm — a list is the wrong tool for building rapport or walking through a sensitive topic.
5. **Don't over-format.** A bold lead-in on every bullet, or bolding every other phrase, reads as AI-generated filler rather than genuine emphasis — see `humanizer.md` §15-16.

## Sources

Plain wording and structure: generalized from [plainlanguage.gov](https://www.plainlanguage.gov/)'s federal plain-language guidelines and The Economist's "never use a long word where a short one will do" principle (see `style-general-writing.md` for the full citation). Headings and lists: generalized from standard business-writing guidance on heading/bullet usage (headings should signal section content; keep bullet lists to 3-6 parallel items; prefer prose for sensitive or nuanced content) — original synthesis, not reproduced text. "Finding the point before you lead with it": generalized from Barbara Minto's Pyramid Principle (the "so what?"/"why?" test) and its SCQA framework (Situation-Complication-Question-Answer, where identifying the strongest complication is the key step before drafting), plus journalism's inverted-pyramid and "nut graf" convention for ranking competing points by newsworthiness/reader impact — original synthesis, not reproduced text.
