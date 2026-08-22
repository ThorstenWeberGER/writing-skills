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

1. **`references/foundations.md`** — pyramid principle (lead with the point), how to find the strongest point before leading with it, how to identify why that point matters to the target group (the pain point, via a three-why chain), plain wording, and heading/bullet formatting. Applies to everything, always.
2. Pick **one** style guide based on what you're writing:
   - `references/style-management-summary.md` — for status updates, recommendations, decisions, anything meant for a manager or other decision-maker. Always produce the crisp email variant (subject-line formula, word/sentence caps) alongside the full version, regardless of delivery medium, unless the user has said they only want one.
   - `references/style-general-writing.md` — for everything else: explanations, notes, documentation, messages.
3. **`references/DONTS.md`** and **`examples.md`** — check the draft against known violations. If you catch a new one during this conversation and the user confirms it's worth tracking, append it to `DONTS.md` (one line) and optionally add a weak/better pair to `examples.md`.
4. **`references/humanizer.md`** — final surface-level pass for AI-writing tells (inflated claims, stock phrasing, passive voice, chatbot artifacts, etc.). If a relevant sample exists in this conversation, match its voice per that reference's "Match the writer's voice" section.
5. **Self-check before returning the result:** if step 2 used `style-management-summary.md`, confirm the response actually includes both the full version and the crisp email variant, back to back. If only one is present and the user didn't ask for just one, add the missing one before responding.

## Scope

This skill governs English prose. It does not cover audience-specific profiles beyond the two style guides above, and it does not provide document templates — both are deferred.
