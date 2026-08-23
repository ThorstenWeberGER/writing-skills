---
name: clear-writing
description: |
  Apply structure, plain-wording, style, and anti-AI-slop rules whenever
  drafting or editing prose — Claude's own output (docs, summaries, PR
  descriptions, messages) or the user's own draft text. Use whenever asked
  to write, draft, summarize, or edit written content in English.
---

# clear-writing

Apply this skill any time you draft or edit prose for the user, or the user asks you to fix their own draft. Work through the passes below **in order**.

## Pass order

1. **`references/foundations.md`** — always. Find the strongest point (clustering related findings before ranking them), work out why it matters to this specific reader, then lead with it. Plus plain wording, sentence and paragraph limits, headings and lists.
2. **`references/formats.md`** — what shape the deliverable takes. Management summary (always paired with a crisp email variant), or a half-page/full-page article. For notes, messages, and general documentation prose, `foundations.md` alone is the whole ruleset.
3. **`references/audiences.md`** — what changes for this reader: technical peer, external client, non-native English readers. Also the rule for when a technical term is the *right* choice rather than jargon to be replaced. Skip if the audience is a decision-maker — `formats.md` already covers that.
4. **`references/DONTS.md`** and **`examples.md`** — check against known violations. If you catch a new one this conversation and the user confirms it's worth keeping, append it to `DONTS.md`. Only add to `examples.md` if the pair is real, never invented.
5. **`references/humanizer.md`** — final pass for AI-writing tells. If the user's own writing is in this conversation, match its voice per that file's opening section.

## Pass 6 — enforcement, and it is not optional

**`CHECKLIST.md`** — run it before returning any draft. It is the only thing that makes passes 1-5 real: reading a reference file is not the same as applying it, and this skill has already shipped drafts where a pass was reported as run while its rules were violated in the same text.

Two halves:

- **`check.py` decides everything mechanical** — 22+ checks including the literal em-dash scan, sentence and paragraph limits, passive constructions, noun strings, hidden verbs, the AI-tell and buzzword lists, plus conditional checks for summary word counts, email variant limits, article layout, client-facing promises, and non-native readability. Run it with the flags for what you're writing. Every FAIL gets fixed; every REVIEW gets a recorded decision.
- **`CHECKLIST.md`'s steps 1-6 cover the judgment calls** no script can make: is this the strongest point, did the three-why chain run, is the triage stated, was uncertainty preserved, do the four jargon tests pass for this reader, and — the item most likely to catch something real — was any fact, number, or date added or dropped.

**When you report back, say what you ran and what it returned.** Not "applied the clear-writing skill" — that phrasing is exactly what let unenforced passes go unnoticed.

## Templates

`templates/` holds skeletons for document types with real normative backing: `project-readme.md`, `installation.md`, `meeting-notes.md`. Its `README.md` carries the Diátaxis routing question for deciding which *kind* of document you're writing (tutorial, how-to, reference, explanation) — worth reading before writing docs, since mixing those modes is the most common documentation failure. Summaries have no template because `formats.md` covers them.

## Scope

English prose. The four audience profiles in `audiences.md` are the ones with a real basis; don't invent speculative ones. Sourcing status and remaining gaps are tracked in `docs/v2-checklist.md`.
