# House styles: measured conventions you can target

Four publications, measured from material the user supplied. Roughly 25,000 words. Pick one when you want a draft to follow a specific outlet's conventions: `check.py --house economist|ft|reuters|hbr` enforces the measurable parts.

## Contents

- What this can and cannot give you
- The four profiles
- Choosing between them
- For a management email, no single house style fits
- When a house style conflicts with a general rule
- When a house style conflicts with the user's voice
- Sources

*Listed so a partial read still shows the whole scope of this file.*

## What this can and cannot give you

**It gives you conventions.** Sentence length, dash and semicolon rates, whether to use subheads and bullets, how headlines pair with standfirsts, where the point goes. All measured, all enforceable.

**It does not give you voice.** The Economist reads as it does because of wit, cultural allusion, "your correspondent", and a century of house editing. Reuters reads as it does because subscribing editors re-cut its copy. Matching a median sentence length of 30 words will not make a memo read like a wire report; it will make it a memo with long sentences.

So use these to answer "how should this be shaped?" and not "make me sound like them." Anyone promising the second from measurements alone is selling you the skeleton as the animal.

**And note the purpose behind each convention**, because copying a convention without its purpose is how writing goes wrong. Reuters bullets its summaries because editors buy the copy and re-cut it. The Economist runs 600 words with no subheads because people read it end to end on a Sunday. Neither reason may apply to you.

---

## The four profiles

**The measured numbers live in one place: `house-voices.md`.** They used to be restated here as well, and the duplication did exactly what this project exists to prevent. A review found this file stale on three figures that `check.py` and `house-voices.md` had already moved: the Economist sentence median, the HBR sentence median and the HBR dash rate. The drift test did not catch it, because its anchors point at the file that was being kept current.

So this file no longer carries measurements. It carries the decisions you make with them.

| Publication | Pick it for | Sample behind it |
|---|---|---|
| **Economist** | continuous prose read end to end; a short intriguing title with a subtitle doing the explaining | 9 excerpts plus 6 full articles |
| **Financial Times** | a headline that must survive being forwarded alone; reported copy where every claim carries a source | 6 articles, 4 news and 2 features |
| **Reuters** | anything skimmed, forwarded or re-cut by someone else | 4 wire articles plus 6 held out |
| **HBR** | a sectioned management argument for a practitioner deciding whether to change something | 5 articles, re-extracted |

**What a profile can give you.** Sentence length, dash and semicolon rates, subhead and bullet policy, how a headline pairs with a standfirst, where the point goes. All measured, all enforceable with `check.py --house NAME`.

**What it cannot.** Voice, as `house-voices.md` sets out at length: wit, the quality of a concrete anchor, whether an antithesis names two real diagnoses. Matching a median sentence length of 30 words will not make a memo read like a wire report; it will make it a memo with long sentences.

**And note the purpose behind each convention**, because copying a convention without its purpose is how writing goes wrong. Reuters bullets its summaries because editors buy the copy and re-cut it. The Economist runs 600 words with no subheads because people read it end to end on a Sunday. Neither reason may apply to you.

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
