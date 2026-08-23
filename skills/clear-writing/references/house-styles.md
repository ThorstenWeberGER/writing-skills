# House styles: measured conventions you can target

Four publications, measured from material the user supplied. Roughly 25,000 words. Pick one when you want a draft to follow a specific outlet's conventions: `check.py --house economist|ft|reuters|hbr` enforces the measurable parts.

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
| Subheads / bullets | **none, in any excerpt** |
| Headline | **4-10 words, median 8.5. Allusive** — poses a puzzle or names an oddity |
| Standfirst | 8-13 words, median 11. **Carries the "so what"** the headline withholds |

**Structure.** No subheads even at 619 words. Ordinal signposting in the prose does the navigating: "There are three reasons… One is… The second reason… The third reason…" Enumeration stays in prose rather than becoming a list.

**Opening depends on the register:** news is pure BLUF; a Leader states a flat conventional thesis then turns against it; a feature opens on a scene and lands the general point by sentence 5 or paragraph 2.

**Pick this for** a piece someone reads start to finish, where you want a short intriguing title and a subtitle doing the explaining.

---

## Financial Times

*4 articles, ~3,400 words. Two news, one report, one long read.*

| | |
|---|---|
| Sentence median | **22-27** |
| Over 25 words | ~50% (upper bound; see caveat) |
| Em dashes | 1 per 214 words |
| Subheads / bullets | none detected |
| Headline | **7-14 words, median 10.5. Informational** — tells the whole story, works with no standfirst |

**Caveat:** these came from print-to-PDF files with no text layer, recovered by decompressing content streams. Captions interleave with body prose, so the sentence figures are upper bounds, not clean measurements.

**Pick this for** a headline that may travel alone: a subject line, a Slack post, a link stripped of its subtitle. FT-style headlines survive separation; Economist-style ones do not.

---

## Reuters

*4 wire articles plus the Trust Principles pages.*

| | |
|---|---|
| Sentence median | **30** — the longest measured; mean 29.4 |
| Over 25 words | 57% |
| Em dashes | **0** |
| Semicolons | **0** |
| Subheads | **yes**, all-caps, 5-6 words |
| Bullets | **yes** — a summary block above every article, 3-4 bullets, 6-17 words, median 11 |

**The summary block** carries the news, the mechanism, the consequence. Each bullet stands alone as an actionable fact; none restates the body.

**Long leads are deliberate.** A wire lead packs actor, action, time and cause into sentence one, which is why the median is 30 words.

**Spelling is American** ("neighbors", "mobilizing"), unlike the FT and Economist. Sourcing is explicit about anonymity and its reason: "two people familiar with the deal… could not be named because the information was not public."

**Pick this for** anything that will be skimmed, forwarded, or re-cut by someone else. Do not copy the all-caps crossheads; that is wire styling and reads as shouting elsewhere.

---

## HBR

*5 articles, 14,557 words. Three features, a digital article, a curated-tips list.*

| | |
|---|---|
| Sentence median | **12-22** — 12 in the tips list, 19-22 in features |
| Over 25 words | 29% |
| Em dashes | **1 per 157 words — the heaviest of the four** |
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

### When a house style conflicts with the user's voice

It will, immediately, on em dashes. Three of the four profiles use them; the user's own writing contains none, so `humanizer.md` bans them. Targeting HBR will produce `REVIEW  hbr: dash rate ~1 per 157w — none used; house style uses them`.

**The voice preference wins.** A house style governs shape, not punctuation habits the writer has already settled. The same applies to sentence length: if a profile's median pulls far from the writer's own, follow the profile only for outward-facing work where the house convention is the point, and say so.

**None of these is the default.** Absent an instruction, `foundations.md` plus `formats.md` govern, and those are tuned for the user's own work rather than to any masthead. Note especially that the user's own writing runs a **6-word median sentence**, far below every publication here, so adopting a house style moves *away* from their voice by design. That is a legitimate choice for an outward-facing piece and the wrong one for a personal note.

---

## Sources

All measured from articles and PDFs the user supplied during development. No text is reproduced here beyond quotations under 15 words. Per-rule provenance, including which of this skill's own rules each publication corrected, is in `foundations.md` under Sources.
