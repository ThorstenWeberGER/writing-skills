# Foundations: structure, wording, and formatting

These rules apply to every piece of writing, before choosing a format (`formats.md`), adjusting for audience (`audiences.md`), or checking for violations (`DONTS.md`, `inputs/examples.md`).

## Contents

- Structure: lead with the point
- Plain wording
- Headings and lists
- Sources

*Listed so a partial read still shows the whole scope of this file.*

## Structure: lead with the point

A reader, or a manager skimming for five seconds, should get the main point from the first sentence, not the last.

**The pyramid principle:** state the conclusion or recommendation first. Support it after, in order of decreasing importance. Never build up to the point. State it, then justify it.

**Wrong order (climactic, point comes last):**
> We looked at three vendors, ran cost comparisons across two quarters, and interviewed the two teams that would use the tool daily. Based on all of this, we recommend Vendor B.

**Right order (pyramid, point comes first):**
> We recommend Vendor B. It costs 18% less than the incumbent over two quarters and both using teams preferred it in interviews.

**How to check it:**
1. Find the single most important sentence: the conclusion, recommendation, or key fact. If it isn't the first sentence, move it there.
2. Order everything else by descending importance. A reader should be able to stop after any paragraph and still have the most important information seen so far.
3. Cut a paragraph entirely if, once reordered, it only restates or builds up to something already said.

**Signal this rule catches:** a summary that opens with background before the finding; a message where the actual request is in the last paragraph; "Based on the above, we therefore..." as a paragraph opener.

### Where this rule does not apply

The pyramid is for writing someone reads to **decide or act**: summaries, recommendations, status updates, bug reports, most documentation. It is not a universal law of prose.

Measured across four Economist samples in three registers, the opening move is not one convention but three:

| Register | Opening move | Evidence |
|---|---|---|
| **News** | **Pure BLUF.** Point in sentence one, every time. | 7 of 7 news briefs open on the actor and the action: "Mark Carney… said his country would retaliate…", "Gunmen killed more than 40 people…" |
| **Leader / argument** | **Flat thesis, then the turn.** A short plain claim, then the complication that makes it interesting. | Opens "Most people believe humans are different." (5 words), builds the consensus over two paragraphs, then breaks it: "Pontifical clarity is blurring with alarming speed." |
| **Feature / report** | **Scene first, general point within a paragraph or two.** | One piece spends four sentences on a single named bar before the general claim lands in sentence 5. Another opens on a paradox ("conservatives cavort with Marxists") and reaches its point (an election that could put the far right in office) in paragraph 2. |

So the rule is register-dependent, and the thing that stays constant is **how long the delay may last**:

- **Decision, reference, or news writing** → point in sentence one. No exceptions.
- **Argument** → thesis in sentence one, but it may be the *conventional* view you then overturn.
- **Narrative** → concrete opening allowed; the general point by the end of the first paragraph or two.

A nut graf lands early and on purpose. Burying the point on page two is not a narrative lede, it is a buried lede. All three are versions of the same underlying instruction from "Anchor the abstract in something specific" below: get the reader somewhere real, fast. They differ only in whether the abstraction comes first, second, or after a turn.

### Finding the point before you lead with it

Leading with the point only works if you've correctly identified which point is strongest. Three checks, in order:

1. **Find the complication, not the situation.** Background (what's normally true) isn't the point. The change, gap, or problem that forces a decision now is. If a draft opens with context that hasn't changed, that's the situation talking, not the complication. Ask: *what's different, wrong, or at risk here that wasn't before?* That's the candidate point.
2. **Run the "so what?" test.** State the candidate point, then ask "so what?" and answer it. Ask "so what?" again of that answer. Stop when the answer is something the reader would act on or change their mind about. That final answer is the real point. A point that survives zero rounds of "so what?" (the reader shrugs) isn't strong enough to lead with.
3. **Cluster before you rank.** When compressing a longer source with many findings, check whether some are really one point wearing different clothes: symptoms of the same root cause, or restatements of the same fact from different angles. Group those together first. Ranking five flat findings when three of them share a root cause wastes the reader's attention on restatement and can crowd out a genuinely separate point.
4. **When several points compete, rank by reader impact, not writer effort.** The point that took the most work to produce isn't automatically the strongest one to lead with. Rank candidates by what's most consequential, most urgent, or most likely to change what the reader does next, not by how much analysis went into it.

Once you've found the point this way, feed it into the pyramid: that point goes first, and the situation/complication reasoning that got you there becomes the supporting structure underneath it, not the opening.

**Signal this rule catches:** a strong-sounding opening that's actually still describing the situation ("Our team has been monitoring X for months..."); a "key finding" that produces no reaction when you ask "so what?"; a report leading with the most-researched section instead of the most decision-relevant one; three "separate" findings in a summary that all trace back to one root cause and could be one bullet.

### Identifying why the point matters to the target group (the pain point)

A correctly identified point can still fall flat if it's stated as a fact rather than as something the reader has a stake in. Before leading with the point, translate it into the target group's pain point:

1. State the point in one sentence, naming the specific target group (not "people" or "the team", but the actual audience: finance leadership, the on-call engineer, a specific customer segment).
2. Ask "why does this matter to [that group]?" and answer in one sentence.
3. Ask "why does *that* matter to them?" of your own answer.
4. Ask a third time. Three rounds is usually enough to move past a restated fact and land on the actual pain point: the goal they have and the obstacle stopping them, which together explain why they'd act.

**Worked example:**
- Point: "Vendor B costs 18% less than the incumbent."
- Why does that matter to finance leadership? → "It frees up budget this quarter."
- Why does that matter to them? → "They're already over budget on tooling and need to make cuts somewhere."
- Why does that matter to them? → "Without a cut, they have to choose between cutting tooling or cutting headcount." → *That's* the pain point: switching vendors isn't about the discount, it's the alternative to a headcount cut.

Different target groups can produce different pain points from the same fact, so run the three-why chain separately for each audience the same point is going to, rather than assuming one chain covers everyone.

**Signal this rule catches:** a point stated as a bare fact with no stake attached ("Latency increased by 200ms"); the same pitch sent to two different audiences with no change in what's emphasized; an argument that's technically true but that the specific reader has no reason to act on.

## Plain wording

### Words

1. **Familiar words over unfamiliar ones.** The real rule is familiarity, not length: "utilize" is bad because it's unusual, not because it's long, and a long familiar word beats a short obscure one. Federal guidance puts it as picking the commonly used word over the unusual or obscure. Worst repeat offenders: *utilize, commence, implement, assist, promulgate, in accordance with, in order that, in the event of, in the amount of*.
2. **Concrete over abstract.** A number, name, or date beats a qualitative claim. "Costs rose 18%," not "costs rose significantly."
3. **Break up noun strings.** Three nouns stacked in a row is the limit; past that it becomes unreadable, because the reader keeps mistaking an adjective for the noun. "Customer data platform migration project plan" → "the plan for migrating the customer data platform." Cut inessential describing words first; if you can't, open the construction up with prepositions and articles.
4. **Gloss abbreviations on first use; prefer a nickname where one reads better.** A wall of acronyms forces the reader back up the page to decode. Rather than defining "Resource Advisory Council (RAC)" and using RAC throughout, just call it "the Council." Don't define abbreviations everyone already knows (API, SQL, CIA, PhD), because defining them wastes the reader's time. **Measured caveat:** four Economist samples use acronyms freely rather than minimising them, but gloss every non-obvious one on first mention ("Alternative for Germany (afd)", "large language models (llms)") and then use it bare. Gloss-then-use is the working convention; wholesale avoidance is not.
5. **Kill hidden verbs (nominalizations).** Use the strongest, most direct verb form available. Watch endings *-ment, -tion, -sion, -ance* paired with a light verb (*make, take, achieve, effect, give, have, reach, conduct*): "we manage the program," not "we are responsible for management of the program"; "we analyze the data," not "we conduct an analysis of the data."
6. **Jargon means complexity used to impress, not technical terms.** Federal guidance is explicit that this rule is not a ban on technical vocabulary: a necessary domain term is not jargon. Explain the term on first reference, then use it. Writing for your audience does not mean dumbing content down. See `audiences.md` for when a technical term is the *correct* choice.
7. **Cut words that don't change the meaning.** "In order to" → "to." "Due to the fact that" → "because." "At this point in time" → "now."

### Sentences and paragraphs

8. **One idea per sentence.** This is the actual primary rule, not a word count: a long, complicated sentence usually means you aren't sure yet what you want to say. As a comprehension guide: readers get about 90% of a sentence under 14 words, and comprehension drops sharply past 25, so treat anything over ~25 words as needing a second look. Don't make every sentence short, though; see rule 10.
9. **Active voice, actor named as the subject.** "The team shipped the fix," not "the fix was shipped." Federal guidance calls this the single highest-impact change available: not "it must be done" but "you must do it." **Two legitimate exceptions:** when one action follows another as a matter of law and the law itself is the actor, and when it genuinely doesn't matter who acted. Also don't confuse passive voice with past tense: "the team shipped it" is past tense and active.
10. **Short paragraphs, but varied.** One topic per paragraph, opening with a topic sentence that captures its essence. Keep paragraphs under ~150 words and 3-8 sentences; never past 250. **Deliberately vary paragraph and sentence length.** If everything is the same size the writing turns choppy. An occasional one-sentence paragraph is fine.
11. **Address the reader as "you."** Direct address beats third-person abstraction about "users" or "the team" where the reader is the one who has to act.

**Quick self-check:** read the sentence aloud. If you wouldn't say it that way to a colleague across a table, rewrite it. This is also the anti-stuffiness test: write the way you'd speak, not the way a policy document or press release would.

### Two rules that go beyond word choice

1. **Anchor the abstract in something specific, then generalize.** Don't describe an issue only in the abstract. Show its effect on a real person, team, or number first, and widen from there. "Our support operation experienced high call volumes due to systemic outages" says less than "Over 400 clients waited 45 minutes on hold yesterday after our main server failed." A concrete opening detail earns attention before the broader point does. (This is the journalistic narrative-lede/nut-graf move, applied at sentence scale.)
2. **On technical topics, be precise *and* accessible.** Explain the technical term once, plainly, then use it freely. Don't avoid precision to seem approachable, and don't assume the reader already has the term. When jargon *is* the precise word, keeping it is correct; see `audiences.md` on when the plain-word rule should not apply.

## Headings and lists

1. **Headings tell the reader what's coming.** A heading should let someone decide whether to read the section at all, before they read it. Clear beats clever.
2. **Every list needs a lead-in sentence.** Don't drop a list in cold; introduce what it contains.
3. **Every item must be parallel:** grammatically consistent with each other *and* with the lead-in, so each item reads correctly when joined to it. All verbs, or all noun phrases; don't mix.
4. **Numbers for sequence or priority, bullets for everything else.** If order doesn't matter, don't imply it with numbers.
5. **Nest at most two or three levels.** Deeper than that, restructure instead.
6. **Convert comma-separated series into lists** *in scanned writing.* A sentence carrying four or more parallel items is usually a list trying to escape, and the eye gravitates to list items. **But in narrative prose, ordinal signposting beats bullets.** A measured Economist feature enumerates three causes across three paragraphs entirely in prose ("There are three reasons… One is… The second reason… The third reason…") with no list at all. Same information, and it reads rather than scans. Pick by whether the reader is scanning or reading.
7. **Keep lists short: 3-6 items.** *House convention, not sourced practice.* The federal guidance caps nesting depth, not item count. It holds up in practice for scannability, but treat it as a default to override when a list genuinely has eight things in it.
8. **Use prose, not bullets, for anything nuanced, sensitive, or narrative.** Bullets read as efficient, not warm: the wrong tool for building rapport or walking through a sensitive topic.
9. **Don't over-format.** A bold lead-in on every bullet, or bolding every other phrase, reads as AI-generated filler rather than genuine emphasis; see `humanizer.md` ("Formatting tells").
10. **Avoid FAQ sections.** They usually signal that content which belongs in the body got exiled to a list of questions nobody asked.

## Sources

### Primary sources

The plain-wording and heading/list rules are derived from primary text, retrieved from the publishers' own open-source repositories (both archived, so they reflect the guidance as last published):

- **U.S. federal plain-language guidelines**, published by GSA at [`GSA/plainlanguage.gov`](https://github.com/GSA/plainlanguage.gov) sourced the lead-with-the-point rule (`guidelines/organize/`), main-idea-before-exceptions, one-idea-per-sentence (`concise/write-short-sentences`), the paragraph limits and anti-uniformity rule (`concise/write-short-paragraphs`, itself citing Garner's *Legal Writing in Plain English* and Murawski's *Writing Readable Regulations*), active voice with its two exceptions (`conversational/use-active-voice`), hidden verbs (`words/avoid-hidden-verbs`), familiar-over-obscure wording and the "dirty dozen" (`words/use-simple-words-phrases`), the jargon-is-not-technical-terms distinction (`words/avoid-jargon`), and the list mechanics (`organize/use-lists`).
- **18F Content Guide**, published by GSA at [`18F/content-guide`](https://github.com/18F/content-guide) sourced the sentence-comprehension figures (~90% comprehension under 14 words; sharp drop past 25), descending-importance/"little inverted pyramids" paragraph structure, clear-not-clever headings, converting comma series into lists, the anti-FAQ rule, and "you" as the primary form of address.

The two rules under "beyond word choice" absorb a since-removed `style-general-writing.md` (its other three rules duplicated the plain-wording list above): the concrete-anchor rule generalizes the Wall Street Journal's narrative-lede/nut-graf convention, and the technical-accessibility rule generalizes the Financial Times' approach to technical topics.

Method rules: "Finding the point before you lead with it" generalizes Barbara Minto's Pyramid Principle (the "so what?"/"why?" test, plus its MECE grouping requirement, which is the basis for "cluster before you rank") and its SCQA framework, together with journalism's inverted-pyramid and nut-graf convention for ranking competing points. "Identifying why the point matters to the target group" generalizes the Toyota "5 Whys" technique (cut to three rounds and aimed at audience relevance rather than root cause) and the Jobs-to-be-Done framing of a pain point as an unmet goal plus its blocking obstacle.

All rules are original synthesis. Quoted fragments are under 15 words and attributed.

### Known sourcing gaps

- **The 3-6 bullet range is house convention**, labeled as such in the rule itself. No primary source gives an item count.
- **No active-voice percentage target exists** in any primary source; don't invent one.
- **BLUF's military provenance (Army Regulation 25-50) is unverified:** the regulation was unreachable. The *behavior* is fully primary-sourced above; only the acronym's origin story is secondhand.
- **The Economist is now primary.** Nine excerpts from eight articles, supplied by the user and measured directly: a news section (7 briefs), a Leader, a culture feature, a politics report (two sections), a business piece, and three further reports (Iran, US infrastructure, Brazil). 3,131 words, 168 sentences. Text not reproduced here; measurements only.

  | Excerpt | Words | Sents | Median | Mean | Max | Over 25w | Em dashes |
  |---|---|---|---|---|---|---|---|
  | News briefs | 401 | 24 | 16 | 16.7 | 29 | 4 (17%) | 1 |
  | Leader | 473 | 28 | 13 | 16.9 | 43 | 5 (18%) | 4 |
  | Feature (culture) | 619 | 33 | 18 | 18.8 | 39 | 7 (21%) | 4 |
  | Report (politics, open) | 191 | 9 | 22 | 21.2 | 49 | 1 (11%) | 0 |
  | Report (politics, later) | 281 | 19 | 14 | 14.8 | 31 | 1 (5%) | 0 |
  | Business | 310 | 14 | 22 | 22.1 | 41 | 3 (21%) | 0 |
  | Report (Iran) | 195 | 10 | 21.5 | 19.5 | 28 | 2 (20%) | 0 |
  | Report (infrastructure) | 398 | 20 | 21.5 | 19.9 | 43 | 4 (20%) | 0 |
  | Report (Brazil) | 263 | 11 | **26** | 23.9 | 34 | **7 (64%)** | 0 |
  | **Total** | **3,131** | **168** | n/a | n/a | 49 | **34 (20%)** | **9** |

  **Zero subheadings and zero bullets in all nine.** Eight articles, 191-619 words each. This is the dataset's strongest and most consistent result, and why the subhead-count table in `formats.md` is scoped to scanned writing only.

  **What else generalises:**

  - **20% of sentences exceed 25 words** overall, but the spread is wide: 5% in one report section, **64% in the Brazil piece, whose median sentence is 26 words**. Analytical political writing runs long by design. Rule 8's threshold is a prompt to look, never a limit.
  - **Median sentence length ranges 13-26 by register.** There is no target length.
  - **Em dashes are rare and optional**, not characteristic: 9 across 3,131 words (one per 348), and present in only **three of nine** excerpts. Six excerpts contain none at all. This is the clearest evidence that the dash ban in `humanizer.md` is a voice preference, not a quality rule. Good writing here mostly does without them anyway.
  - **Semicolons are near-absent**, at most one per excerpt.
  - **Abbreviations are glossed then used bare**, in two forms: parenthetical ("Islamic Revolutionary Guard Corps (irgc)", "the Centrão (big centre)") and appositive ("a Brandmauer, or firewall", "known as Lula"). Hence rule 4 is gloss-on-first-use, not minimise.
  - **Numeric density is genre-calibrated**: 3.0 figures per 100 words in news, 0.4 in the Leader.
  - **The concrete anchor recurs at every scale**, including historical: one piece opens "When the Ostrogoths wanted to cripple Rome in 537, they destroyed its aqueducts" before turning to present-day cyber-attacks.
  - **A rhetorical question can carry a structural pivot** ("Has the policy worked?" turns description into assessment).
  - **A single sentence fragment for comic timing is legitimate** ("Which is in Munich."), consistent with `humanizer.md`'s caveat that a row of fragments is the tell, not one.

  Four rules were corrected against this material: the subhead table, convert-series-to-lists, the pyramid rule's scope (now three registers), and rule 4 on abbreviations. The headline rule was corrected and then partly reverted; see `formats.md`, where a single 4-word outlier briefly overturned a range that four samples then vindicated.

- **The Financial Times is now partly primary.** Four articles supplied as PDFs (two news, one world report, one long read on AI-generated financial scams) and measured: ~3,400 words of body prose, 130 usable sentences.

  **Extraction caveat, and it matters.** These were print-to-PDF files with no text layer, so the text was recovered by decompressing content streams. That is lossy: photo captions and standfirsts interleave with body prose, ligatures come back as placeholders, and 9 of 139 sentence units were discarded as join artifacts. Caption contamination inflates sentence length, so the FT figures below are **upper bounds**, not the clean measurements the Economist rows are. Treat them as indicative.

  | Measure | Economist (9 excerpts) | FT (4 articles) |
  |---|---|---|
  | Median sentence | 13-26 by register | 22-27 |
  | Over 25 words | **20%** | **~50%** (upper bound) |
  | Em dash rate | 1 per 348 words | 1 per 214 words |
  | Headline length | 4, 8, 9, 10 (median 8.5) | 7, 10, 11, 14 (median 10.5) |
  | Subheadings | 0 in 9 of 9 | none detected, but this method cannot prove absence |

  **What the second publication changes:**

  - **The 25-word threshold is weaker than one publication suggested.** Two quality broadsheets exceed it routinely: a fifth of Economist sentences, around half of FT's. Rule 8's threshold is a prompt to look at a sentence, and nothing more. Do not treat it as a ceiling.
  - **Em dashes are more common in the FT** than the Economist, at roughly one per 214 words. Across both publications the mark is unremarkable in professional prose. This is now two independent sources confirming that `humanizer.md`'s dash ban is a voice preference for this user, not a quality standard.
  - **Headline conventions differ by publication, and the difference is instructive.** FT headlines are longer and fully informational: "Russian 'double-tap' attack on Ukrainian shopping mall kills at least 16" tells you the whole story. Economist headlines are shorter and allusive ("Why everybody hates Palantir") and lean on the standfirst to deliver the point. Both pair a headline with a standfirst; they divide the labour differently. See `formats.md`.

- **HBR is now primary, and it exposed three defects in our own checker.** Five articles measured: three magazine features, one digital article, and one curated-tips list. 14,557 words, 665 sentences.

  | Measure | Value |
  |---|---|
  | Median sentence | **12-22** (12 in the tips list, 19-22 in features) |
  | Over 25 words | 29% (195 of 665) |
  | Em dashes | **1 per 157 words, the highest of four publications** |
  | Semicolons | up to 12 in one article |
  | Subheadings | **yes** (confirmed by inspection: "Common Causes of False Alignment", "The Consequences of False Alignment", "Reaching True Agreement") |
  | Headline / dek | 4-10 words / 12-24 words, often two sentences |

  **The defect.** Running `check.py` over HBR returned FAILs on "AI-tell phrases": *actually, crucial, underscore, commitment to, fundamentally, landscape, valuable.* These are ordinary management-register vocabulary, and HBR carries them at **1 per 644-787 words**. Meanwhile `humanizer.md` already said of that list: "Individually fine; in clusters, a strong tell." The checker never implemented the second half of its own rule, so it failed on a single hit. It is now density-aware: clustering fails, sparse use reviews. Dense slop still fails at 1 per 3 words.

  **A second carve-out came from HBR's dek.** "It isn't a failure of the technology. It's a failure of management." is the "Not X but Y" shape our anti-slop pass flags, used well: the halves name two different diagnoses, so the contrast carries information. `humanizer.md` now distinguishes genuine antithesis from the empty version, with a delete-the-first-half test.

  **Validated at n=5.** Two further articles moved the em dash rate only from 1 per 161 to 1 per 157, and over-25-word sentences from 33% to 29%. AI-tell density on the fresh articles came in at 1 per 905 and 1 per 1,668 words, both far above the 200-word threshold, so the density fix holds on data it was not tuned on.

  **A format finding inside one publication.** The curated-tips article runs a median sentence of 12 words against 19-22 in the features, and structures itself as headed micro-sections with short imperative headings ("Trust your preparation.", "Accept mistakes quickly.", "Manage emotions before they manage you.", 3 to 9 words) rather than a bulleted list. Format drives sentence length and structure *within* a publication, not only between publications.

  **Two more checker defects, both false positives:**

  - **Degree signs counted as decorative emoji.** The check tested Unicode category `So`, which contains legitimate symbols. Seven "emoji" in an HBR feature were all `°`. Now matched against real emoji blocks; verified that actual emoji still fail and `21°C` does not.
  - **Buzzwords flagged in literal use.** "circle back" fired on "in the aftermath of a decision, they circle back with all stakeholders", where it carries its plain meaning. Left as a FAIL deliberately: unlike the AI-tell list, `BUZZWORDS` is **prescriptive, not descriptive:** it records words we choose to avoid, not words professionals avoid. HBR uses "circle back" and "actionable"; that is worth knowing and does not by itself make them good choices. The plain-language argument stands on its own.

  Not recorded: `check.py` also reported 250-word paragraphs, but the PDF extraction merges wrapped lines and loses paragraph boundaries, so that is an artifact of the method rather than a finding about HBR.

- **Reuters is now primary, and it overturned this file's strongest claim.** Four wire articles plus the Thomson Reuters Trust Principles pages, measured directly.

  Earlier versions of this section said "zero subheadings and zero bullets" was the dataset's most consistent result, across nine Economist excerpts and four FT articles. **That was a publication pattern, not a fact about professional prose.** Reuters uses both:

  - **A bulleted summary block above every article.** 3-4 bullets, 6-17 words each, median 11. It is a BLUF summary: the news, the mechanism, the consequence.
  - **All-caps crossheads in longer pieces**, 5-6 words each ("LARGER VEHICLES, OTHER STICKING POINTS").

  This is the third time in this project that a finding held across two sources and then broke on the third. The correct generalisation is narrower: **magazine and broadsheet features, leaders and news avoid subheads and bullets; wire copy uses both**, because it is written to be scanned and re-cut by subscribing editors. That is exactly the split `formats.md` routes on, so the genre rule is confirmed even as the universal claim fails.

  | Measure | Economist (9 excerpts) | FT (4 articles) | Reuters (4 articles) |
  |---|---|---|---|
  | Median sentence | 13-26 by register | 22-27 | **30** |
  | Over 25 words | 20% | ~50% | **57%** |
  | Em dashes | 1 per 348 words | 1 per 214 words | **0** |
  | Semicolons | ~1 per excerpt | 0-2 | **0** |
  | Subheadings | 0 of 9 | none detected | **yes, all-caps** |
  | Bullets | 0 of 9 | none detected | **yes, summary block** |

  **The 25-word threshold is now settled across three publications.** They exceed it in 20%, ~50% and 57% of sentences, and wire copy's *median* sentence is 30 words, because a wire lead packs actor, action, time and cause into sentence one. Rule 8 is a prompt to look at a sentence. It is not a limit, and treating it as one would make our writing less like every professional outlet measured.

  **A useful calibration.** Running `check.py` over Reuters news returns **0 FAIL**. Running it over Reuters' own Trust Principles pages returns **1 FAIL** and roughly ten times the passive-voice rate (7 passives in 292 words against 2 in 618). The checker separates good journalism from institutional boilerplate, which is the behaviour these rules are for.

- **WSJ, HBR, Bloomberg, Reuters, Guardian, and BBC remain secondary.** All are paywalled or block automated fetching. Rules attributed to them come from write-ups describing their conventions. Widely-circulated figures for Reuters (300-800 words per story) and AR 25-50 (15-word average sentence) could not be verified against either document and are deliberately not used here.

---

**This file is not self-enforcing.** The checks described above are gated by `CHECKLIST.md`. Run it, and `check.py`, before returning any draft.
