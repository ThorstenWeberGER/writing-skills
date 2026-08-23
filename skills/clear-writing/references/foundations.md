# Foundations: structure, wording, and formatting

These rules apply to every piece of writing, before choosing a format (`formats.md`), adjusting for audience (`audiences.md`), or checking for violations (`DONTS.md`, `examples.md`).

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
3. **Cluster before you rank.** When compressing a longer source with many findings, check whether some are really one point wearing different clothes — symptoms of the same root cause, or restatements of the same fact from different angles. Group those together first. Ranking five flat findings when three of them share a root cause wastes the reader's attention on restatement and can crowd out a genuinely separate point.
4. **When several points compete, rank by reader impact, not writer effort.** The point that took the most work to produce isn't automatically the strongest one to lead with. Rank candidates by what's most consequential, most urgent, or most likely to change what the reader does next — not by how much analysis went into it.

Once you've found the point this way, feed it into the pyramid: that point goes first, and the situation/complication reasoning that got you there becomes the supporting structure underneath it, not the opening.

**Signal this rule catches:** a strong-sounding opening that's actually still describing the situation ("Our team has been monitoring X for months..."); a "key finding" that produces no reaction when you ask "so what?"; a report leading with the most-researched section instead of the most decision-relevant one; three "separate" findings in a summary that all trace back to one root cause and could be one bullet.

### Identifying why the point matters to the target group (the pain point)

A correctly identified point can still fall flat if it's stated as a fact rather than as something the reader has a stake in. Before leading with the point, translate it into the target group's pain point:

1. State the point in one sentence, naming the specific target group (not "people" or "the team" — the actual audience: finance leadership, the on-call engineer, a specific customer segment).
2. Ask "why does this matter to [that group]?" and answer in one sentence.
3. Ask "why does *that* matter to them?" of your own answer.
4. Ask a third time. Three rounds is usually enough to move past a restated fact and land on the actual pain point — the goal they have and the obstacle stopping them, which together explain why they'd act.

**Worked example:**
- Point: "Vendor B costs 18% less than the incumbent."
- Why does that matter to finance leadership? → "It frees up budget this quarter."
- Why does that matter to them? → "They're already over budget on tooling and need to make cuts somewhere."
- Why does that matter to them? → "Without a cut, they have to choose between cutting tooling or cutting headcount." → *That's* the pain point: switching vendors isn't about the discount, it's the alternative to a headcount cut.

Different target groups can produce different pain points from the same fact — run the three-why chain separately for each audience the same point is going to, rather than assuming one chain covers everyone.

**Signal this rule catches:** a point stated as a bare fact with no stake attached ("Latency increased by 200ms"); the same pitch sent to two different audiences with no change in what's emphasized; an argument that's technically true but that the specific reader has no reason to act on.

## Plain wording

### Words

1. **Familiar words over unfamiliar ones.** The real rule is familiarity, not length — "utilize" is bad because it's unusual, not because it's long, and a long familiar word beats a short obscure one. Federal guidance puts it as picking the commonly used word over the unusual or obscure. Worst repeat offenders: *utilize, commence, implement, assist, promulgate, in accordance with, in order that, in the event of, in the amount of*.
2. **Concrete over abstract.** A number, name, or date beats a qualitative claim. "Costs rose 18%," not "costs rose significantly."
3. **Break up noun strings.** Three nouns stacked in a row is the limit; past that it becomes unreadable, because the reader keeps mistaking an adjective for the noun. "Customer data platform migration project plan" → "the plan for migrating the customer data platform." Cut inessential describing words first; if you can't, open the construction up with prepositions and articles.
4. **Minimize abbreviations — prefer a nickname.** A wall of acronyms forces the reader back up the page to decode. Rather than defining "Resource Advisory Council (RAC)" and using RAC throughout, just call it "the Council." Don't define abbreviations everyone already knows (API, SQL, CIA, PhD) — defining them wastes the reader's time.
5. **Kill hidden verbs (nominalizations).** Use the strongest, most direct verb form available. Watch endings *-ment, -tion, -sion, -ance* paired with a light verb (*make, take, achieve, effect, give, have, reach, conduct*): "we manage the program," not "we are responsible for management of the program"; "we analyze the data," not "we conduct an analysis of the data."
6. **Jargon means complexity used to impress, not technical terms.** Federal guidance is explicit that this rule is not a ban on technical vocabulary: a necessary domain term is not jargon. Explain the term on first reference, then use it. Writing for your audience does not mean dumbing content down. See `audiences.md` for when a technical term is the *correct* choice.
7. **Cut words that don't change the meaning.** "In order to" → "to." "Due to the fact that" → "because." "At this point in time" → "now."

### Sentences and paragraphs

8. **One idea per sentence.** This is the actual primary rule, not a word count — a long, complicated sentence usually means you aren't sure yet what you want to say. As a comprehension guide: readers get about 90% of a sentence under 14 words, and comprehension drops sharply past 25, so treat anything over ~25 words as needing a second look. Don't make every sentence short, though — see rule 10.
9. **Active voice, actor named as the subject.** "The team shipped the fix," not "the fix was shipped." Federal guidance calls this the single highest-impact change available: not "it must be done" but "you must do it." **Two legitimate exceptions:** when one action follows another as a matter of law and the law itself is the actor, and when it genuinely doesn't matter who acted. Also don't confuse passive voice with past tense — "the team shipped it" is past tense and active.
10. **Short paragraphs, but varied.** One topic per paragraph, opening with a topic sentence that captures its essence. Keep paragraphs under ~150 words and 3-8 sentences; never past 250. **Deliberately vary paragraph and sentence length** — if everything is the same size the writing turns choppy. An occasional one-sentence paragraph is fine.
11. **Address the reader as "you."** Direct address beats third-person abstraction about "users" or "the team" where the reader is the one who has to act.

**Quick self-check:** read the sentence aloud. If you wouldn't say it that way to a colleague across a table, rewrite it. This is also the anti-stuffiness test — write the way you'd speak, not the way a policy document or press release would.

### Two rules that go beyond word choice

1. **Anchor the abstract in something specific, then generalize.** Don't describe an issue only in the abstract — show its effect on a real person, team, or number first, and widen from there. "Our support operation experienced high call volumes due to systemic outages" says less than "Over 400 clients waited 45 minutes on hold yesterday after our main server failed." A concrete opening detail earns attention before the broader point does. (This is the journalistic narrative-lede/nut-graf move, applied at sentence scale.)
2. **On technical topics, be precise *and* accessible.** Explain the technical term once, plainly, then use it freely. Don't avoid precision to seem approachable, and don't assume the reader already has the term. When jargon *is* the precise word, keeping it is correct — see `audiences.md` on when the plain-word rule should not apply.

## Headings and lists

1. **Headings tell the reader what's coming.** A heading should let someone decide whether to read the section at all, before they read it. Clear beats clever.
2. **Every list needs a lead-in sentence.** Don't drop a list in cold — introduce what it contains.
3. **Every item must be parallel** — grammatically consistent with each other *and* with the lead-in, so each item reads correctly when joined to it. All verbs, or all noun phrases; don't mix.
4. **Numbers for sequence or priority, bullets for everything else.** If order doesn't matter, don't imply it with numbers.
5. **Nest at most two or three levels.** Deeper than that, restructure instead.
6. **Convert comma-separated series into lists.** A sentence carrying four or more parallel items is usually a list trying to escape — the eye naturally gravitates to list items.
7. **Keep lists short: 3-6 items.** *House convention, not sourced practice* — the federal guidance caps nesting depth, not item count. It holds up in practice for scannability, but treat it as a default to override when a list genuinely has eight things in it.
8. **Use prose, not bullets, for anything nuanced, sensitive, or narrative.** Bullets read as efficient, not warm — the wrong tool for building rapport or walking through a sensitive topic.
9. **Don't over-format.** A bold lead-in on every bullet, or bolding every other phrase, reads as AI-generated filler rather than genuine emphasis — see `humanizer.md` ("Formatting tells").
10. **Avoid FAQ sections.** They usually signal that content which belongs in the body got exiled to a list of questions nobody asked.

## Sources

### Primary sources

The plain-wording and heading/list rules are derived from primary text, retrieved from the publishers' own open-source repositories (both archived, so they reflect the guidance as last published):

- **U.S. federal plain-language guidelines**, published by GSA at [`GSA/plainlanguage.gov`](https://github.com/GSA/plainlanguage.gov) — sourced the lead-with-the-point rule (`guidelines/organize/`), main-idea-before-exceptions, one-idea-per-sentence (`concise/write-short-sentences`), the paragraph limits and anti-uniformity rule (`concise/write-short-paragraphs`, itself citing Garner's *Legal Writing in Plain English* and Murawski's *Writing Readable Regulations*), active voice with its two exceptions (`conversational/use-active-voice`), hidden verbs (`words/avoid-hidden-verbs`), familiar-over-obscure wording and the "dirty dozen" (`words/use-simple-words-phrases`), the jargon-is-not-technical-terms distinction (`words/avoid-jargon`), and the list mechanics (`organize/use-lists`).
- **18F Content Guide**, published by GSA at [`18F/content-guide`](https://github.com/18F/content-guide) — sourced the sentence-comprehension figures (~90% comprehension under 14 words; sharp drop past 25), descending-importance/"little inverted pyramids" paragraph structure, clear-not-clever headings, converting comma series into lists, the anti-FAQ rule, and "you" as the primary form of address.

The two rules under "beyond word choice" absorb a since-removed `style-general-writing.md` (its other three rules duplicated the plain-wording list above): the concrete-anchor rule generalizes the Wall Street Journal's narrative-lede/nut-graf convention, and the technical-accessibility rule generalizes the Financial Times' approach to technical topics.

Method rules: "Finding the point before you lead with it" generalizes Barbara Minto's Pyramid Principle (the "so what?"/"why?" test, plus its MECE grouping requirement, which is the basis for "cluster before you rank") and its SCQA framework, together with journalism's inverted-pyramid and nut-graf convention for ranking competing points. "Identifying why the point matters to the target group" generalizes the Toyota "5 Whys" technique (cut to three rounds and aimed at audience relevance rather than root cause) and the Jobs-to-be-Done framing of a pain point as an unmet goal plus its blocking obstacle.

All rules are original synthesis. Quoted fragments are under 15 words and attributed.

### Known sourcing gaps

- **The 3-6 bullet range is house convention**, labeled as such in the rule itself. No primary source gives an item count.
- **No active-voice percentage target exists** in any primary source; don't invent one.
- **BLUF's military provenance (Army Regulation 25-50) is unverified** — the regulation was unreachable. The *behavior* is fully primary-sourced above; only the acronym's origin story is secondhand.
- **The Economist, WSJ, HBR, Bloomberg, Reuters, Guardian, and BBC remain secondary.** All are paywalled or block automated fetching. Rules attributed to them come from write-ups describing their conventions. Widely-circulated figures for Reuters (300-800 words per story) and AR 25-50 (15-word average sentence) could not be verified against either document and are deliberately not used here.

---

**This file is not self-enforcing.** The checks described above are gated by `CHECKLIST.md` — run it, and `check.py`, before returning any draft.
