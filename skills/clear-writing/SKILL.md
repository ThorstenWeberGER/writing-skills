---
name: clear-writing
description: |
  Apply structure, plain-wording, style, and anti-AI-slop rules whenever
  drafting or editing prose — Claude's own output (docs, summaries, PR
  descriptions, messages) or the user's own draft text. Use whenever asked
  to write, draft, summarize, or edit written content in English.
---

# clear-writing

Apply this skill any time you draft or edit prose for the user, or the user asks you to fix their own draft. Work through the references below **in order**. Do not skip a step; do not reorder them.

## Pass order

1. **`references/structure.md`** — pyramid principle. Does the text lead with the point? Reorder if it buries the lede.
2. **`references/plain-wording.md`** — plain wording and short sentences.
3. Pick **one** style guide based on what you're writing:
   - `references/style-management-summary.md` — for status updates, recommendations, decisions, anything meant for a manager or other decision-maker.
   - `references/style-general-writing.md` — for everything else: explanations, notes, documentation, messages.
4. **`references/DONTS.md`** and **`examples/bad/`** — check the draft against known violations. If you catch a new one during this conversation and the user confirms it's worth tracking, append it to `DONTS.md` (one line) and optionally save a `before`/`after` pair to `examples/bad/` and `examples/good/`.
5. **`references/humanizer.md`** — final surface-level pass for AI-writing tells (inflated claims, stock phrasing, passive voice, chatbot artifacts, etc.). If a file in `examples/good/` is relevant to the current context, match its voice per that reference's "Match the writer's voice" section.

## Scope

This skill governs English prose. It does not cover audience-specific profiles beyond the two style guides above, and it does not provide document templates — both are deferred.
