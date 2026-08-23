# House styles: measured conventions you can target

Four publications, measured from material the user supplied. Roughly 25,000 words. Pick one when you want a draft to follow a specific outlet's conventions: `check.py --house economist|ft|reuters|hbr` enforces the measurable parts.

## Contents

- What this can and cannot give you
- Economist
- Financial Times
- Reuters
- HBR
- Choosing between them
- For a management email, no single house style fits
- Sources

*Listed so a partial read still shows the whole scope of this file.*

## What this can and cannot give you

**It gives you conventions.** Sentence length, dash and semicolon rates, whether to use subheads and bullets, how headlines pair with standfirsts, where the point goes. All measured, all enforceable.

**It does not give you voice.** The Economist reads as it does because of wit, cultural allusion, "your correspondent", and a century of house editing. Reuters reads as it does because subscribing editors re-cut its copy. Matching a median sentence length of 30 words will not make a memo read like a wire report; it will make it a memo with long sentences.

So use these to answer "how should this be shaped?" and not "make me sound like them." Anyone promising the second from measurements alone is selling you the skeleton as the animal.

**And note the purpose behind each convention**, because copying a convention without its purpose is how writing goes wrong. Reuters bullets its summaries because editors buy the copy and re-cut it. The Economist runs 600 words with no subheads because people read it end to end on a Sunday. Neither reason may apply to you.

---

## Economist

*9 excerpts, 3,131 words. News briefs, a Leader, features, reports.*

| | |
|---|---|
| Sentence median | **13-26**, varying by register; mean 16.7-23.9 |
| Over 25 words | 20% |
| Em dashes | 1 per 348 words; absent from 6 of 9 excerpts |
| Semicolons | about 1 per excerpt |
| Subheads | **crossheads in 2 of 5 full articles**, 3-4 words, allusive. None in any excerpt |
| Bullets | **none**, in six full articles or nine excerpts |
| Headline | **4-10 words, median 8.5. Allusive.** Poses a puzzle or names an oddity |
| Standfirst | 8-13 words, median 11. **Carries the "so what"** the headline withholds |

**Structure.** No subheads in any excerpt, and none at 619 words, but full articles do carry two or three allusive crossheads. The excerpt sample could not show this. Ordinal signposting in the prose does the navigating: "There are three reasons… One is… The second reason… The third reason…" Enumeration stays in prose rather than becoming a list.

**Opening depends on the register:** news is pure BLUF; a Leader states a flat conventional thesis then turns against it; a feature opens on a scene and lands the general point by sentence 5 or paragraph 2.

**Pick this for** a piece someone reads start to finish, where you want a short intriguing title and a subtitle doing the explaining.

---

## Financial Times

*4 articles, ~3,400 words. Two news, one report, one long read.*

| | |
|---|---|
| Sentence median | **25 news, 20 features** |
| Over 25 words | **47% news, 38% features** |
| Em dashes | **about 1 per 430 words**, and zero in one of five |
| Subheads / bullets | none detected |
| Headline | **7-14 words, median 10.5. Informational.** Tells the whole story, works with no standfirst |

**Caveat:** these came from print-to-PDF files with no text layer, recovered by decompressing content streams. Captions interleave with body prose, so the sentence figures are upper bounds, not clean measurements.

**Pick this for** a headline that may travel alone: a subject line, a Slack post, a link stripped of its subtitle. FT-style headlines survive separation; Economist-style ones do not.

---

## Reuters

*4 wire articles plus the Trust Principles pages.*

| | |
|---|---|
| Sentence median | **21-32 by register**, pooled 26 over four held-out articles; the interview runs shortest |
| Over 25 words | 57% |
| Em dashes | **0** |
| Semicolons | **0** |
| Subheads | **yes**, all-caps, **2-9 words** (eight articles) |
| Bullets | **yes**: a summary block above every article, 3-4 bullets, 6-17 words, median 11 |

**The summary block** carries the news, the mechanism, the consequence. Each bullet stands alone as a fact the reader can act on; none restates the body.

**Long leads are deliberate.** A wire lead packs actor, action, time and cause into sentence one, which is why the median is 30 words.

**Spelling is American** ("neighbors", "mobilizing"), unlike the FT and Economist. Sourcing is explicit about anonymity and its reason: "two people familiar with the deal… could not be named because the information was not public."

**Pick this for** anything that will be skimmed, forwarded, or re-cut by someone else. Do not copy the all-caps crossheads; that is wire styling and reads as shouting elsewhere.

---

## HBR

*5 articles, 14,557 words. Three features, a digital article, a curated-tips list.*

| | |
|---|---|
| Sentence median | **12-22**: 12 in the tips list, 19-22 in features |
| Over 25 words | 29% |
| Em dashes | **1 per 157 words, the heaviest of the four** |
| Semicolons | up to 12 in one article |
| Subheads | **yes**, title case, full phrases ("Common Causes of False Alignment") |
| Headline | 4-10 words, allusive like the Economist |
| Dek | **12-24 words, often two sentences**, frequently antithetical |

**The dek does real argumentative work.** "It isn't a failure of the technology. It's a failure of management." Two sentences, two competing diagnoses, the second correcting the first.

**Format changes the shape more than the masthead does.** The tips list runs a 12-word median against 19-22 in features, and structures itself as headed micro-sections with 3-9 word imperative headings ("Trust your preparation.", "Accept mistakes quickly.") rather than bullets.

**Pick this for** a management argument that needs sections, where the reader is a practitioner deciding whether to change something.

---

## Choosing between them

| If you want… | Use |
|---|---|
| A title that survives being forwarded alone | **FT** |
| A short intriguing title with a subtitle explaining it | **Economist** or **HBR** |
| Something skimmed, re-cut, or acted on fast | **Reuters** |
| A sectioned argument for practitioners | **HBR** |
| Continuous prose read end to end | **Economist** |

## For a management email, no single house style fits

Asked which of the four to use for a management email, the honest answer is none of them whole, and the reason is structural: **all four are written for readers who chose to read. An email interrupts someone.**

The arithmetic settles it. `formats.md` caps the email variant at 125 words and 5 sentences, so the ceiling is 25 words per sentence. Measured against that:

| House | Median | Fits a 5-sentence email? |
|---|---|---|
| Reuters | 30 | **No.** Two sentences would eat the whole budget |
| FT | 22-27 | Barely |
| Economist | 13-26 | At the lower end only |
| HBR features | 19-22 | Barely |
| **HBR tips list** | **12** | **Yes** |

Our own email fixtures run a median of 10-12 words. That is the register, and only HBR's tips-list format comes close.

**So take elements, not a whole style:**

| Take | From | Why |
|---|---|---|
| **Informational subject line, 7-14 words, carrying the whole point** | FT / Reuters | A subject line always travels alone. This is the highest-value transfer of the four. |
| **Summary bullets when there are 3+ facts**: 3-4 items, 6-17 words, each standing alone | Reuters | Already how `formats.md` structures a scanned summary |
| **No em dashes, no semicolons** | Reuters | The only profile matching the user's own punctuation |
| **Short imperative micro-headings (3-9 words)** for a multi-item update | HBR tips list | Turns a wall of asks into scannable items |
| **Explicit sourcing for a contested claim** ("per the Q3 close", "two of three vendors") | Reuters | Wire practice: name the basis, or say you cannot |

**And explicitly reject:**

- **Every publication's sentence length.** All four medians are too long. Write 10-20 word sentences.
- **The Economist's allusive headline.** "Why everybody hates Palantir" works because a standfirst rescues it. A subject line has no standfirst.
- **HBR's subheads and dash rate.** Sections are wrong under 125 words, and it is the heaviest dash user of the four.

**The short version: Reuters for the subject line and the bullets, HBR's tips register for sentence length, and `formats.md`'s email variant for everything else.** The email variant is already tighter than any masthead here, which is the correct relationship: it was tuned for a reader who did not ask for the message.

### When a house style conflicts with a general rule

Two conflicts are real and both are resolved in `check.py` rather than left to judgment.

**Title-case subheads.** HBR's subheads are title case, and the always-on rule fails Title Case headings. Writing correct HBR would therefore guarantee a failure the profile itself asked for. So a named title-case profile downgrades that check to REVIEW and says which profile did it. Naming no profile, or naming one whose subheads are sentence case, and the rule still fails. `tests/fixtures/house-hbr.md` locks both directions.

**Sentence median measured over bullets.** Reuters prescribes a summary block of 3-4 bullets, and its 30-word median was measured on body prose. Measuring the median over a document that follows the bullet convention mixes 8-word bullets with 40-word leads, so following the profile pushed a draft out of the profile's own range: the same draft measured 14 whole-document and 41 body-only. The median now excludes list items, headings and subject lines, so both figures agree.

### When a house style conflicts with the user's voice

It will, immediately, on em dashes. Three of the four profiles use them; the user's own writing contains none, so `humanizer.md` bans them. Targeting HBR will produce `REVIEW  hbr: dash rate ~1 per 157w, none used; house style uses them`.

**The voice preference wins.** A house style governs shape, not punctuation habits the writer has already settled. The same applies to sentence length: if a profile's median pulls far from the writer's own, follow the profile only for outward-facing work where the house convention is the point, and say so.

**None of these is the default.** Absent an instruction, `foundations.md` plus `formats.md` govern, and those are tuned for the user's own work rather than to any masthead. Note especially that the user's own writing runs a **6-word median sentence**, far below every publication here, so adopting a house style moves *away* from their voice by design. That is a legitimate choice for an outward-facing piece and the wrong one for a personal note.

---

## Sources

All measured from articles and PDFs the user supplied during development. No text is reproduced here beyond quotations under 15 words. Per-rule provenance, including which of this skill's own rules each publication corrected, is in `foundations.md` under Sources.
