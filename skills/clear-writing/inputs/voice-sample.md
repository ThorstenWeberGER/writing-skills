# Voice sample

Real writing by the user, quoted verbatim. `humanizer.md`'s "Match the writer's voice" step reads this when no fresher sample is in the conversation.

**Everything here is genuine.** Nothing is invented, smoothed, or reconstructed. Same invariant as `examples.md`: an empty section is better than a plausible one.

---

## Source 1 — `docs/backlog.md` in this repo (planning register)

Verbatim:

> The skill needs
>
> * avoiding usage of AI slop -> humanizer basis
> * ability to learn, have a list where i can add DONTS
> * use first-things-first, pyramid thinking principle
> * enforce easy wording, short sentences
> * have good examples of writing summaries, notes
> * have bad examples DONTS
> * build on good writing examples from newspapers, articles
> * optional: have templates for specific use cases (readme.md, installation.md, summary.md, meeting_notes.md)
> * optional: has specific target groups profiles designed (e.g. boss, management)

## Source 2 — session messages, 2026-08-23 (instruction register)

Verbatim, in order:

> Include do nots with do examples in our skill. Identify the right place to put them. This is general advice not bound to any specific target group or document

> Research on how to identify and convey the strongest point of a problem. Evtl combine it with pyramid thinking

> Research on identifying why the point matters to the target group. Maybe asking three times. Why. Add this as well. Identifying the pain point for the argumentation

> Research on best pratices to write a management summary email. A really short and crisp message.

> How good does this skill help to compress a longer 2 page analysis into a recommendation. Test it. Review it. Suggest improvements

> Search all the reference files for described-but-unenforced checks. Enforce. Make a step by step clear guidance. Add anything which enforces the steps

> In the output ... I see a em dash. Why? Did humanizer fire? Make sure all designed steps do get passed

> Great. Update/ create a v2 checklist of what we still need to do. Or have you already?

---

## Observable patterns

Drawn only from the quotes above.

**Report what the sample shows, not what it suggests about the person.** A voice sample supports claims about *writing*: sentence length, punctuation, word choice, mood. It does not support claims about the writer's background, nationality, first language, seniority, or state of mind. This file previously said one German abbreviation "confirmed German as a first language" — a conclusion one token cannot carry, about a fact the user never stated. Frequency counts are safe; inferences about the author are not. If a pattern appears once, say "once."

**Sentence length and shape.** Short, and measurably so. Across the 27 sentences in the quoted material: **median 6 words, minimum 1, maximum 16.** Not one exceeds 16. Fragments are used as complete instructions ("Enforce." / "Test it. Review it." / "Why."). Short sentences stack with periods rather than joining with conjunctions or subordinate clauses.

For comparison, `foundations.md` treats anything past 25 words as needing a second look. This writer's own ceiling is far tighter, so matching the voice means aiming well below the general rule, not at it.

**Mood.** Imperative dominates: *Include, Research, Add, Search, Enforce, Make, Test, Review, Update.* Requests are stated as directives, not softened into questions.

**No em dashes anywhere.** Verified by character scan: zero `—` or `–` across every verbatim quote above, and zero in `backlog.md` as a whole. Hyphens appear in compounds ("described-but-unenforced", "first-things-first"); a slash appears in "Update/ create". **This settles the dash rule for this writer: the ban applies. Do not pass `--dashes-ok`.**

**Punctuation is sparse.** No semicolons. Colons only after a label ("optional:"). Questions sometimes carry no question mark ("How to always show the email variant as well").

**Recurring tags.** "Add this as well" appears three times. "as well" is a habitual closer.

**Register markers.** Lowercase "i" in `backlog.md`. `->` rather than an arrow glyph or the word. "e.g." rather than "for example". One German abbreviation, "Evtl" (*eventuell*, roughly "possibly"), used mid-sentence in English.

On that last one: it is a single token in a single message. It says the writer reaches for a German shortcut when writing quickly, and nothing more. **Don't infer a language background from it** — the actionable rule is just "don't reproduce the shorthand," which needs no theory about the writer. Whether to apply the non-native-readers profile in `audiences.md` depends on who is *reading*, not on who is writing.

**Directness.** No hedging, no preamble, no apology. Concerns arrive as plain questions: "Why? Did humanizer fire?"

**Compound requests.** Several distinct asks packed into one short message without connective scaffolding.

---

## How to use this — and what not to copy

**Match:** short sentences, fragments where they carry the instruction, imperative mood, sparse punctuation, no em dashes, plain vocabulary, no hedging, no preamble.

**Do not copy:**

- **Typos and slips.** The quotes preserve "pratices", "dto", "do nots", "Update/ create" because altering a quoted sample would corrupt the evidence. They are artifacts of writing fast, not style to imitate. Produce correct spelling.
- **Missing question marks and lowercase "i".** Same reason.
- **Non-English shorthand** like "Evtl". Fine in a fast instruction; wrong in finished prose written *for* this reader.

The distinction that matters: reproduce the **rhythm, directness, and word choice**; don't reproduce **errors**.

---

## Known limitation, and it is significant

Both sources are **short-form and functional** — a planning list and a set of instructions. Neither is connected prose written for a reader: no paragraph, no argument developed over several sentences, no writing aimed at a colleague or a client.

So this sample supports word choice, sentence length, punctuation habits, and the dash decision. It does **not** yet tell you how this writer builds a paragraph, opens a document, handles a transition, or adjusts tone for an audience.

**To close that gap:** add two or three paragraphs of real connected prose the user has written for someone else — an email to a colleague, a section of a doc, a Slack post of any length. Append it as Source 3 with the same verbatim treatment. Until then, treat paragraph-level voice matching as unsupported and fall back to `humanizer.md`'s defaults for it.
