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

## Exit checklist — run every item before returning the draft

Reading a pass is not the same as applying it. Each item below is mechanically checkable; do not report the draft as finished until every one is confirmed. Skipping this is the skill's known failure mode: in testing, passes 1 and 5 were described as run while two em dashes and a passive construction went out in the same draft.

1. **Scan the literal characters `—` and `–`.** Every hit must go, replaced by a period, comma, colon, or parentheses. The only exemption is a writing sample from the user in this conversation that uses them — check for one; don't assume it exists. Also check spaced ` - ` and ` -- ` used as dashes.
2. **Read every sentence for a hidden actor.** For each passive construction, either name the actor or confirm one of the two exceptions in `foundations.md` rule 9 applies. Client-facing drafts fail this twice over, because an agentless passive also dodges ownership (`audiences.md`, external client rule 5).
3. **Check the first sentence carries the point**, not background. If a reader stopping there wouldn't know the point, it's misordered.
4. **If pass 2 used the management-summary section:** confirm both the full version and the crisp email variant are present, back to back, unless the user asked for just one.
5. **Scan for the tells you claim to have removed.** Pick the three most likely from `humanizer.md` for this text type and search for them explicitly rather than trusting the earlier read.
6. **Confirm no fact, number, name, date, or citation was added or dropped** relative to the source.

If you cannot confirm an item, say so in the response instead of asserting the draft is clean.

## Templates

`templates/` holds skeletons for document types with real normative backing: `project-readme.md`, `installation.md`, `meeting-notes.md`. Its `README.md` carries the Diátaxis routing question for deciding which *kind* of document you're writing (tutorial, how-to, reference, explanation) — worth reading before writing docs, since mixing those modes is the most common documentation failure. Summaries have no template because `formats.md` covers them.

## Scope

English prose. The four audience profiles in `audiences.md` are the ones with a real basis; don't invent speculative ones. Sourcing status and remaining gaps are tracked in `docs/v2-checklist.md`.
