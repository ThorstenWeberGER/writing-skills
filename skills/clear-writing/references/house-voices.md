# House voices: sounding like the publication, not just shaped like it

`house-styles.md` gives shape: sentence length, subheads, bullets, headline length. That is the skeleton. This file is the rest of the animal.

**Read this only when the user asks to sound like a publication.** Otherwise the user's own voice governs, and their median sentence is 6 words, below every outlet here.

## Contents

- What voice is made of
- Evidence grading, and why it is on every rule
- Economist
- Financial Times
- Reuters
- HBR
- The same fact in four voices
- What is enforced, and what is not
- The limit that does not go away

*Listed so a partial read still shows the whole scope of this file.*

## What voice is made of

Shape is measurable in one pass. Voice turns out to be six things, and each is recorded per publication below:

1. **The opening move.** What sentence one does before it does anything else.
2. **The signature move.** The device you would notice if it were missing.
3. **Register.** Which words the outlet reaches for, including the ones our own anti-slop list bans.
4. **Punctuation signature.** Dashes, semicolons, fragments, and their rates.
5. **Attribution.** How a claim is sourced, and what happens when it cannot be.
6. **Refusals.** What the outlet never does, which is as diagnostic as what it does.

## Evidence grading, and why it is on every rule

Every rule below carries a grade, because voice rules are far more tempting to invent than shape rules:

| Grade | Meaning | How to use it |
|---|---|---|
| **measured** | counted across the whole sample | Follow it. Enforceable |
| **recorded** | a verbatim fragment captured from the sample, n=1 | Imitate the *move*, never the wording. One instance does not prove a habit, and counting the HBR sample demoted one such rule from house signature to 1 of 5 |
| **inferred** | reasoned from a measured fact, not observed directly | Weakest. Say so if a draft leans on it |

Nothing here is graded higher than the evidence supports. Where a publication's voice feature was never captured, the row says **not captured** rather than guessing.

---

## Economist

*Six full articles, 5,286 words, 269 sentences: two political reports, a business analysis, a business news piece, a data-journalism explainer and a news-brief roundup. Plus the nine excerpts behind `house-styles.md`.*

**Full articles, not excerpts, and that changes the strongest claim in this project.** The nine-excerpt sample produced "zero subheadings and zero bullets in all nine", labelled the dataset's most consistent result. It was measured on excerpts. Full articles carry crossheads.

| Measure | From excerpts | From six full articles |
|---|---|---|
| Sentence median | 13-26 by register | **16-23**, pooled 19 |
| Over 25 words | 20% | **23%**, range 8-36% |
| Em dashes | 1 per 348, absent from 6 of 9 | **zero in all six** |
| Semicolons | about 1 per excerpt | 0-2 per article |
| Headline words | 4, 8, 9, 10 | **7, 8, 9, 10, 10**, median 9. Confirmed |
| Subheads | none, in any excerpt | **crossheads in 2 of 5 articles** |

### The devices, counted

**The standfirst turns against the headline. (measured, 4 of 5)** The headline states; the standfirst adds the qualification that makes the piece worth reading. Two open on *But*. One appends *, too*. One runs a *just as* symmetry between two parties. The exception is the data-journalism piece, whose standfirst is a bare number. So this is where the argument's tension lives, not in the headline.

**A short flat sentence lands early. (measured, 4 of 6)** Three to six words, inside the opening paragraph, doing the work a long sentence set up: *The market shrugged.* *And so he swiftly sidestepped it.* *Which is in Munich.* One article opens on one outright: *Mark Carney is governing through paradox.* The effect is deadpan rather than punchy, and it is the clearest single marker of this voice.

**Crossheads, where they appear, are 3-4 words and allusive. (measured, 2 of 2 articles that use them)** *How to spend it* borrows an FT magazine title. *Can't touch this* is an MC Hammer joke. *Stoppable force, movable object* inverts the immovable-object cliché. Three of three are a joke or a reference, none is a navigation label. The data-journalism piece is the exception that proves the split: its one crosshead is *Methodology*, purely functional.

So the honest rule is **register-dependent, not absent**: news briefs carry none, reports and analysis carry two or three allusive ones, data journalism carries functional labels.

**Enumeration stays in prose.** (measured, from the excerpt sample) *There are three reasons… One is… The second reason… The third reason…* across three paragraphs, with no list. Confirmed by the absence of a single bullet in any of the six full articles.

**The institutional "we" is gated to data journalism. (measured, 14 hits in one article, 0-4 in the other five)** *The Economist has parsed all of these new rules, line by line.* *We find that…* *Our calculations are based on…* Plus a full Methodology section naming the paper the method comes from. In reports and analysis the publication is invisible; in data journalism it becomes the actor and shows its working.

**Register.** Acronyms glossed once then used bare and **lowercase**: `irgc`, `afd`, `llms`, `oecd`. (measured) Numeric density is genre-calibrated: 3.0 figures per 100 words in news against 0.4 in a Leader. (measured)

**Attribution.** Named sources arrive with an institution and a one-clause gloss: an economist at a named university, the boss of a named polling firm. Claims are hedged with *may*, *might*, *reportedly*, *is expected to*. (recorded across the six; not counted per article, so treat the pattern and not a rate.)

**Refusals.** No bullets, in any of six full articles or nine excerpts. No headline that tells the whole story: the headline poses the puzzle in 4-10 words and the standfirst delivers the point. No navigation-label crossheads outside data journalism.

### The generators

**G1. Write the standfirst against the headline.** State the fact in the headline. Then write the standfirst as the objection, the cost or the twist: start it with *But*, end it with *, too*, or run a *just as* symmetry. If the standfirst restates the headline, you have written the headline twice.

**G2. Plant one short flat sentence in the first paragraph.** Three to six words, no adjectives, immediately after your longest sentence. It should state a consequence or a correction, not an opinion. *The market shrugged.* Not *This was remarkable.*

**G3. Make every crosshead a joke.** If a piece needs crossheads, use two or three of three to four words, each a pun, a title, or an inverted cliché related to the section. If you cannot make it allusive, the section probably does not need a crosshead. Functional labels belong only in a methods section.

**G4. Signpost in prose, never in bullets.** When you have three reasons, write *There are three reasons. One is… The second… The third…* across paragraphs.

**G5. Gloss an acronym once, then lowercase it.** *Islamic Revolutionary Guard Corps (irgc)*, then `irgc`. Or appositive: *a Brandmauer, or firewall*.

**G6. Show the method only when the method is the story.** In a data piece, use *we* and add a Methodology section naming the paper the technique comes from. Everywhere else, keep the publication out of the prose.

### What is enforced

`--house economist` now checks the standfirst turn, the short flat sentence in the opening paragraph, crosshead length where crossheads exist, plus sentence median, dash and semicolon rates, bullet ban, UK spelling, lowercase acronyms and headline type. Subheads are reported rather than failed, because presence is a genuine choice.

Validated against the source: the three new checks reproduce the hand counts exactly, including flagging the data-journalism piece as the one standfirst that does not turn.

## Financial Times

*Five articles on clean text: four news pieces (2,355 words, 94 sentences) and one long read (1,717 words, 72 sentences).*

**This was the thinnest profile of the four, and only because of extraction.** The earlier figures came from print-to-PDF files with no text layer, so captions interleaved with body prose and every number was an upper bound. Pasted text settles them.

| Measure | Old, upper bound | Measured |
|---|---|---|
| Sentence median | 22-27 | **25 news, 20 long read** |
| Over 25 words | ~50% | **47% news, 43% long read.** The old figure held |
| Em dashes | 1 per 214 | **about 1 per 430**, and zero in one piece |
| Headline words | 7-14, median 10.5 | 9-11, informational in news |

The over-25 figure surviving matters: after the first article came in at 39% I suspected the whole row was caption contamination. Two of four news pieces then exceeded 50%. **The FT genuinely writes long, and holding the correction until n=4 is what stopped me overwriting a sound row.**

### The devices, counted

**Attribution is the signature, at 1 per 38-62 words. (measured, 5 of 5)** Every second sentence names who said it: *said, according to, told, claimed, argued, the review said*. This is the tightest habit in any of the four profiles, roughly four times HBR's hedging rate, and it is what makes FT copy feel reported rather than argued. A claim without a source attached is the thing this voice does not do.

**Direct speech carries the story.** Fourteen quoted passages in one 731-word news piece. The reporter supplies connective tissue between quotations rather than narrating over them.

**The epithet replaces the name. (measured, 2-9 per piece, 5 of 5)** *The ChatGPT maker*, *the iPhone maker*, *the start-up*, *the prime minister*, *the consumer goods group*. A company or figure is named once, then referred to by what it is.

**This conflicts with our own anti-slop rule, and the publication wins on the facts.** `humanizer.md` flags synonym cycling (*the protagonist / the main character / the central figure*) as an AI tell. The FT does it deliberately and constantly. The distinction is what the substitute carries: an epithet adds information the reader needs (*the iPhone maker* tells you which Apple matters here), while synonym cycling adds nothing and exists to avoid repetition. So the rule stands, narrowed: **cycle only when each substitute earns its place by naming a different relevant fact.**

**Two hard style markers.** *Per cent* is always spelled out, never `%`: 12 instances, zero symbols across five articles. And an omission inside a quotation is a spaced ellipsis, *. . .*, four instances.

### The register split, which corrects a claim made about both publications

Four news pieces and one long read divide on every structural choice:

| | FT news (4) | FT long read (1) |
|---|---|---|
| Headline | informational, tells the whole story | **allusive**: *Why more young workers are leaving the UK behind* |
| Standfirst | states the next fact. **0 of 4 turn** | **turns**: *…has grown every year since 2022, but claims of a brain drain overstate the problem* |
| Sentence median | 25 | 20 |
| Questions in the body | **0 of 4** | **6** |
| Opening | the news, in sentence one | a named person and a specific number, nut graf by paragraph 5 |

**An earlier version of this file contrasted "the FT standfirst adds a fact" against "the Economist standfirst turns" as a difference between the two publications. That was wrong.** It is a difference between registers. FT news does not turn and the FT long read does, with an allusive headline exactly like the Economist's. The rule that survives is broader and more useful: **headline type and standfirst behaviour are set by register, not masthead.** News gets an informational headline and a stating standfirst; a feature gets an allusive headline and a turning standfirst.

**Questions in the body: a feature device, but not a feature rule. (recorded, 6 in one feature and 1 in the other, 0 in all four news pieces)** *So why are people leaving? Who are they?* ... *So how big a problem is this?* The register permits it and news never does it, but one feature leans on it heavily and the other barely at all. Imitate the move where the piece needs signposting; do not treat the rate as a target.

### The generators

**G1. Attach a source to every second sentence.** Draft the facts, then go back and name where each came from: a review, a filing, a named person with their role, a named institution. Target one attribution per 30 to 70 words. If a sentence carries a claim and no source, it is not in this voice.

**G2. Let people talk.** Quote directly and often, and write the linking sentences around the quotations rather than paraphrasing them away.

**G3. Name once, then use the epithet.** After the first mention, refer to the subject by what it is, and make the epithet carry information the reader needs at that point.

**G4. Pick the headline and standfirst as a pair, by register.** News: an informational headline that survives being forwarded alone, plus a standfirst that states the next fact. Feature: an allusive headline, often opening on *Why*, plus a standfirst that turns against it.

**G5. In a feature, ask the reader's questions out loud.** Three or four short questions, at the seams, in the reader's words. In news, none.

**G6. Spell out *per cent* and use a spaced ellipsis in quotations.**

### What is enforced

`--house ft` checks the attribution rate, the standfirst stating rather than turning, *per cent* spelled out, the dash rate, the sentence median, headline length and type, UK spelling and the bullet ban. The profile carries the news register, because that is four of the five articles; `CHECKLIST.md` step 4 carries the feature flip.

Validated against the source: the checks reproduce the hand counts on all five, and correctly flag the long read as the one standfirst that turns. Applying G1 to our own FT draft took it from **zero attributions to 1 per 57 words**, inside the house band.

## Reuters

*4 wire articles plus the Trust Principles pages.*

**The opening move: the packed lead.** (measured) Sentence one carries actor, action, time and cause together, which is why the median sentence is 30 words, the longest of the four. A short wire lead is the wrong instinct. Pack it.

**The signature move: the summary block that does not restate the body.** (measured) 3-4 bullets, 6-17 words, median 11, above every article. It carries the news, the mechanism, the consequence, and each bullet stands alone as a fact the reader can act on. A bullet that paraphrases the lead is the failure.

**Register.** American spelling: "neighbors", "mobilizing". (measured, and the only one of the four that is American.) Plain vocabulary throughout.

**Punctuation signature. Zero em dashes and zero semicolons across the whole sample.** (measured) This is the cleanest punctuation signature of the four, and the only one that matches this user's own habits.

**Attribution is the strongest voice feature here.** (recorded, n=1 for the anonymity formula) Sourcing is explicit, and when a source cannot be named the reason is given in the same sentence: "two people familiar with the deal… could not be named because the information was not public." Never an unsourced characterisation. If you cannot name the basis, say that you cannot and why.

**Refusals.** No dashes. No semicolons. No editorial adjective where a figure will do. And do not carry the all-caps crossheads ("LARGER VEHICLES, OTHER STICKING POINTS", 5-6 words) outside wire copy: that is typesetting, and it reads as shouting anywhere else.

---

## HBR

*The same five articles as `house-styles.md`, re-extracted. 20,588 body words, 917 sentences: three magazine features, one digital article, one curated-tips list.*

**Sample size did not grow, extraction quality did.** The first pass recovered 14,557 words through a lossier route. Decoding each font's ToUnicode table recovers 20,588 and fixes the shifted-encoding runs, so these figures replace the earlier ones. Four moved, one held.

| Measure | First pass | Re-measured | |
|---|---|---|---|
| Sentence median | 12-22 | **11 tips, 17-18 features, 21 digital** | features run shorter than thought |
| Over 25 words | 29% | **24%** (6% tips to 34%) | |
| Em dashes | 1 per 157 | **1 per 174**, range 156-193 | held |
| Semicolons | up to 12 | **up to 19**, 1 per 623 overall | |
| Register words | 1 per 644-787 | **1 per 849-2,616** | sparser than thought |

### The devices, counted across all five

The first pass recorded devices one instance at a time. Counting them is what changes their status, and one recorded rule did not survive it.

**The dek: name the belief, then reverse it. (measured, 2 of 5, in two shapes)**

The first pass called *"It isn't a failure of the technology. It's a failure of management."* the house opening move on the strength of one instance. **At five it is 1 of 5.** What 2 of 5 share is the reversal, in two different syntaxes: one splits it across two short sentences, the other puts the reversal inside sentence one (*behave as if they agree ... when they actually don't*) and the consequence in sentence two. The other three deks promise contents or state a benefit. So the correction dek is a strong option, not the house signature, and `check.py` reviews for it rather than requiring it.

**The opening makes the problem the reader's, before any argument. (measured, 4 of 4 substantive)**

This is the real shared move, and it is stronger evidence than the dek. Four vehicles, one per article:

| Vehicle | How sentence one goes |
|---|---|
| Shared predicament | Leaders routinely decide under pressure, and here is who does it harder |
| Second-person hypothetical | *Imagine you are sitting on the capital allocation committee* |
| Name and define the phenomenon | The thing plaguing you, named and defined in one sentence |
| Settled finding, then dated authority | Most change efforts fail, and in 1993 a named figure concluded as much |

None opens on the thesis. None opens on the author. The reader or their situation is in sentence one every time.

**The coined term runs through the subheads, inflected. (measured, 3 of 3 that coin one)**

The strongest new finding. Each article that coins a term repeats it across most of its subheads, changing its grammatical form, and negates it where the argument turns: *False Alignment* becomes *Common Causes of*, then *The Consequences of*, then *Reaching True Agreement*, then *Facing True Disagreement*. Another runs *Centering, Center, Centers, Centered* through four of five. A third puts *Workslop* in all three. Subheads are title case and full noun phrases, as recorded, but that was the surface of this.

**Hedging is distributed, never stacked. (measured, 1 per 138-175 words, 5 of 5)**

HBR qualifies a claim roughly once every eight sentences: *may, might, often, tends to, suggests, appears to.* 128 instances in 20,588 words. It reads as authority rather than weakness because no sentence carries two. Our own stacked-hedging check found **zero stacked hedges in four of five articles** and one in the fifth, so the distributed rate and the stacking ban are measuring different things and both hold.

**Attribution is sparse and specific, not statistical. (measured)** This fills a row that used to read *not captured*.

| Move | Rate |
|---|---|
| Hedge a claim | 1 per 160 words |
| First person research (*our research, we surveyed*) | 1 per 1,715 words, in 3 of 5 |
| Percentage | 1 per 1,583 words, in 3 of 5 |
| Dated citation (*In 1993 …*) | 1 per 2,573 words |

So a percentage is rare enough to be an event. A named figure arrives with a relative clause saying what they did, not a job title. (recorded: one instance of that shape, so imitate the move and do not count on the rate.)

### The generators

A metric constrains. These produce. Each is a procedure, with the count behind it.

**G1. Write the dek by reversal.** Write the sentence the reader already believes. Negate it. Name the real cause. Keep the pair inside 12-24 words. Then apply the deletion test from `humanizer.md`: cut the first half, and if you lose a real alternative the reader might have held, keep it. If you only lose drama, use a contents-promise dek instead, which is what 3 of 5 do.

**G2. Put the reader in sentence one.** Pick one of the four vehicles above and write sentence one so it contains the reader or their situation. If sentence one contains your thesis, you have written the second sentence first.

**G3. Coin one term, then conjugate it.** Name the thing your argument is about in two or three words. Use it in at least half your subheads, changing its form as the argument moves, and negate it at the turn. `check.py --house hbr` counts the share and reviews below half.

**G4. Hedge on a metronome.** Draft without hedges, then add one qualifier roughly every 150 to 200 words, at the claims that need it. Never two in a sentence. Enforced both ways: the rate reviews outside 130-200, and stacking reviews on its own.

**G5. Spend numbers like money.** One percentage per 1,500 words or so, on the claim carrying the argument. Attribute the rest by naming who found it and when.

**G6. Define by exclusion at section level.** *What X Is, and Isn't* as a subhead. (recorded, 1 of 5.)

### What is enforced

`--house hbr` now checks the correction dek, the coined term across subheads, and the hedge rate, alongside sentence median, dash and semicolon rates, subhead and bullet policy, spelling, register band and headline type.

Running it on our own HBR-voice drafts found both at **1 per 237-282 words against the house 138-175**, so our imitation under-hedges by about half. That is the kind of gap a metric cannot show and a generator can.

### Punctuation signature

Em dashes 1 per 174 words, the heaviest of the four publications. Semicolons up to 19 in one article. If the user's dash ban is in force, this voice comes out correspondingly thinner, and that should be said rather than hidden.

### Refusals

No bullets, despite the subheads (measured, 5 of 5). The tips format uses headed micro-sections with 3-9 word imperative headings carrying a terminal period, not a bulleted list.

**Format outranks masthead.** The tips list runs an 11-word median against 17-18 in the features. Pick the format first, then the voice.

## The same fact in four voices

One fact: a routing fault in a support platform doubled response times, and the fix is a one-week patch now with a rewrite next quarter.

| Voice | Opens with | Because |
|---|---|---|
| **Economist** | "When a contractor leaves, the code stays. Usually nobody notices." then the fault | Concrete anchor first, general point by sentence 5 |
| **FT** | "Support platform routing fault doubles response times to 9.6 hours" as the headline, lead does not withhold | Headline tells the whole story |
| **Reuters** | Four summary bullets, then a 30-word lead packing fault, effect, period and cause | Written to be scanned and re-cut |
| **HBR** | "The platform did not fail. The rules nobody owns did." | Names the wrong diagnosis, then corrects it |

Full worked drafts live in `tests/fixtures/voice-*.md`, each passing its own profile and failing at least one other.

## What is enforced, and what is not

`check.py --house NAME` checks the measurable half of the voice:

| Enforced | How |
|---|---|
| Punctuation signature | dash rate, semicolon rate per profile |
| Subhead and bullet policy | presence or absence per profile |
| Sentence median | prose sentences only, excluding bullets and headings |
| Headline length and type | word count, plus whether it opens allusively |
| Economist lowercase acronyms | a glossed acronym used bare in caps afterwards reviews |
| Reuters attribution | an attribution phrase must appear |
| Reuters spelling | British forms review under the Reuters profile |
| HBR register density | the management words must appear, and stay near 1 per 700 |
| HBR antithetical dek | a two-sentence dek where the second corrects the first |

**Not enforced, and not enforceable by counting:** wit, the quality of a concrete anchor, whether a rhetorical question sits at a real hinge, whether an antithesis names two genuinely different diagnoses. Those are judgment, and `CHECKLIST.md` step 4 carries them.

## The limit that does not go away

These profiles were built from 25,000 words of one sample per publication, and the voice features are thinner evidence than the shape features: several are n=1 verbatim fragments, graded as such above. **Imitating a recorded move is legitimate; reproducing a recorded sentence is not.** No fragment quoted in this file should appear in a draft.

A voice profile also cannot supply what these publications actually have: editors, house training, and in the Economist's case a century of accumulated habit. What it can supply is the opening move, the punctuation, the register band and the refusals, which is most of what a reader uses to place a piece.
