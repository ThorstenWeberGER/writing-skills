---
name: clear-writing
description: |
  Applies structure, plain-wording, style and anti-AI-slop rules to English
  prose, and verifies mechanically that they were applied. Covers drafts,
  summaries, management emails, client notes, short articles, README and docs
  pages, PR descriptions and chat replies, plus four measured publication
  house styles. Use when asked to write, draft, summarize, edit, tighten,
  clean up, de-slop or restructure written text, or to match a house style or
  the user's own voice.
---

# clear-writing

Apply this skill any time you draft or edit prose for the user, or the user asks you to fix their own draft.

## Pick the mode first

**Style-only mode** is the default for ordinary writing and for editing the user's own text. Runs three things and nothing else:

- `references/foundations.md` → **the plain-wording section only** (words, sentences, paragraphs). Not the point-finding, pain-point, or pyramid sections.
- `references/DONTS.md`
- `references/humanizer.md`, which reads `inputs/voice-sample.md` for the user's own voice

**Do not restructure in this mode.** Don't reorder to lead with the point, don't compress, don't cut content, don't merge or split paragraphs, don't impose a format, don't add a summary or an email variant. Change wording; remove slop; leave the shape alone. If the structure genuinely hurts the text, say so in one sentence and let the user decide. Don't act on it.

Verify with `python3 check.py DRAFT.md --compare ORIGINAL.md`, which fails if the draft lost more than 15% of the original's words. That guard exists because silent compression is this mode's characteristic failure.

**Full mode** applies only when the user asks for a deliverable with a shape: a summary, a recommendation, a status update for a decision-maker, a structured article, a README. Then run the full pass order below.

**When in doubt, style-only.** "Write X," "clean this up," "does this read well," "make it sound like me" are all style-only. Full mode needs an actual signal: "summarize," "recommend," "write the update for my boss," "turn this into a one-pager."

## Full-mode pass order

1. **`references/foundations.md`**. Always. Find the strongest point (clustering related findings before ranking them), work out why it matters to this specific reader, then lead with it. Plus plain wording, sentence and paragraph limits, headings and lists.
2. **`references/formats.md`**. What shape the deliverable takes. Management summary (always paired with a crisp email variant), or a half-page/full-page article. For notes, messages, and general documentation prose, `foundations.md` alone is the whole ruleset.
3. **`references/house-styles.md`** and **`references/house-voices.md`**. Only when the user asks for a specific outlet ("write this like the Economist"). `house-styles.md` gives the shape: sentence length, subheads, bullets, headline length. `house-voices.md` gives the voice: the opening move, the signature device, the register band, the punctuation signature, the attribution habit and the refusals, each graded by how strong its evidence is. Both are enforced by `check.py --house economist|ft|reuters|hbr`. The user's own voice preferences override either. Skip entirely otherwise.
4. **`references/audiences.md`**. What changes for this reader: technical peer, external client, non-native English readers. Also the rule for when a technical term is the *right* choice rather than jargon to be replaced. Skip if the audience is a decision-maker, because `formats.md` already covers that.
5. **`references/DONTS.md`** and **`inputs/examples.md`**. Check against known violations. If you catch a new one this conversation and the user confirms it's worth keeping, append it to `DONTS.md`. Only add to `inputs/examples.md` if the pair is real, never invented.
6. **`references/humanizer.md`**. Final pass for AI-writing tells. If the user's own writing is in this conversation, match its voice per that file's opening section.

## Pass 6: enforcement, and it is not optional

**`CHECKLIST.md`**. Run it before returning any draft. It is the only thing that makes passes 1-5 real: reading a reference file is not the same as applying it, and this skill has already shipped drafts where a pass was reported as run while its rules were violated in the same text.

Two halves:

Every FAIL and REVIEW prints the file and section its rule is written in, so a
finding leads back to the guidance. `python3 check.py --rules` prints the whole
check-to-rule map plus the judgment-only rules no check covers.

- **`check.py` decides everything mechanical:** 22+ checks including the literal em-dash scan, sentence and paragraph limits, passive constructions, noun strings, hidden verbs, the AI-tell and buzzword lists, plus conditional checks for summary word counts, email variant limits, article layout, client-facing promises, and non-native readability. Run it with the flags for what you're writing. Every FAIL gets fixed; every REVIEW gets a recorded decision.
- **`CHECKLIST.md`'s steps 1-6 cover the judgment calls** no script can make: is this the strongest point, did the three-why chain run, is the triage stated, was uncertainty preserved, do the four jargon tests pass for this reader, and, the item most likely to catch something real, was any fact, number, or date added or dropped.

**When you report back, say what you ran and what it returned.** Not "applied the clear-writing skill", which is exactly the phrasing that let unenforced passes go unnoticed.

## Templates

`templates/` holds skeletons for document types with real normative backing: `project-readme.md`, `installation.md`, `meeting-notes.md`. Its `README.md` carries the Diátaxis routing question for deciding which *kind* of document you're writing (tutorial, how-to, reference, explanation). Worth reading before writing docs, since mixing those modes is the most common documentation failure. Summaries have no template because `formats.md` covers them.

## Scope

English prose. The four audience profiles in `audiences.md` are the ones with a real basis; don't invent speculative ones. Sourcing status and remaining gaps are tracked in `docs/v2-checklist.md`.
