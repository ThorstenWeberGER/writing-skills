# clear-writing Skill Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Build the `clear-writing` Claude Code Skill at `~/.claude/skills/clear-writing/` per `docs/superpowers/specs/2026-08-22-clear-writing-skill-design.md` — a single skill Claude invokes whenever it drafts or edits prose (its own output or the user's), applying structure rules, plain wording, one of two style guides, a growing DON'Ts list, and a final anti-AI-slop pass.

**Architecture:** One skill directory with a thin `SKILL.md` entry point and six reference files loaded in a fixed pass order, plus a seeded `examples/` tree of real good/bad writing pairs. No code, no tests in the traditional sense — "tests" here are content-presence checks and dry-run verification against real drafts.

**Tech Stack:** Markdown only. No build step. Files live under `~/.claude/skills/clear-writing/`.

## Global Constraints

- Every example in `examples/` must be real (user-supplied or captured from actual conversation) — never fabricated by Claude. Source: spec Non-goals.
- `humanizer.md` is a one-time port of `github.com/blader/humanizer`'s SKILL.md content (MIT-licensed), not a live dependency. Source: spec Non-goals.
- Style guide content must be original synthesis from observed patterns, not bulk-reproduced source text. Quotes under 15 words, attributed, only. Source: spec style-guide section.
- Out of scope for v1: audience profiles beyond management-summary/general-writing, and all four use-case templates (README/installation/summary/meeting-notes). Source: spec Non-goals.

---

### Task 1: Scaffold the skill directory and SKILL.md

**Files:**
- Create: `C:\Users\Thorsten\.claude\skills\clear-writing\SKILL.md`
- Create (empty dirs via placeholder use in later tasks): `C:\Users\Thorsten\.claude\skills\clear-writing\references\`, `C:\Users\Thorsten\.claude\skills\clear-writing\examples\good\`, `C:\Users\Thorsten\.claude\skills\clear-writing\examples\bad\`

**Interfaces:**
- Produces: the skill's frontmatter `name: clear-writing` and `description:` string, which the Skill tool / skill listing uses to decide when to trigger this skill. Later tasks assume this file exists and append no content to it beyond what's written here.

- [ ] **Step 1: Write SKILL.md**

Content:

```markdown
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
```

- [ ] **Step 2: Verify the file was written correctly**

Run: `cat ~/.claude/skills/clear-writing/SKILL.md` (or open the file) and confirm:
- Frontmatter has `name: clear-writing` and a `description:` field.
- The five-step pass order is present, in order, each pointing at a filename that will exist after later tasks.

- [ ] **Step 3: Commit**

```bash
cd "C:\Users\Thorsten\OneDrive\Dokumente\Github\writing-skills"
git add -A
git commit -m "docs: note clear-writing skill scaffolding in progress"
```

(The skill itself lives outside this repo, under `~/.claude/skills/`, so this commit is a no-op placeholder unless you're also tracking a copy in-repo — see Task 8.)

---

### Task 2: Port the humanizer pattern list

**Files:**
- Create: `C:\Users\Thorsten\.claude\skills\clear-writing\references\humanizer.md`
- Source (already cloned locally): `C:/Users/Thorsten/AppData/Local/Temp/claude/humanizer-src/SKILL.md`

**Interfaces:**
- Produces: `references/humanizer.md`, referenced by `SKILL.md` step 5 (Task 1) as the final pass.

- [ ] **Step 1: Copy the source content**

Copy the full body of `C:/Users/Thorsten/AppData/Local/Temp/claude/humanizer-src/SKILL.md` (all 35 patterns across Content, Language and grammar, Style, Chatbot, and Filler-and-hedging sections, plus "Check for false positives" and "How to return the result") into the new file. Keep the MIT attribution and the "Source" section pointing to Wikipedia's "Signs of AI writing" and the original repo.

Replace the frontmatter with a short note instead of the original skill frontmatter (this is now a *reference*, not a standalone skill):

```markdown
# Humanizer reference

Ported from [github.com/blader/humanizer](https://github.com/blader/humanizer) (MIT license), based on Wikipedia's ["Signs of AI writing"](https://en.wikipedia.org/wiki/Wikipedia:Signs_of_AI_writing). Kept in full for now — trim to the patterns that actually recur once we've used this for a while.

---

[... full pattern content follows, unchanged from source ...]
```

- [ ] **Step 2: Verify content completeness**

Run: count section headings to confirm all 35 patterns made it across:

```bash
grep -c "^### " "C:\Users\Thorsten\.claude\skills\clear-writing\references\humanizer.md"
```

Expected: `35`

- [ ] **Step 3: Commit**

No repo commit needed here (file lives under `~/.claude/skills/`, outside this repo) — proceed to Task 3. If you're keeping an in-repo mirror per Task 8, commit there instead.

---

### Task 3: Write structure.md (pyramid principle)

**Files:**
- Create: `C:\Users\Thorsten\.claude\skills\clear-writing\references\structure.md`

**Interfaces:**
- Produces: `references/structure.md`, referenced by `SKILL.md` step 1.

- [ ] **Step 1: Write the file**

```markdown
# Structure: lead with the point

Before checking wording or style, check structure. A reader (or a manager skimming for five seconds) should get the main point from the first sentence, not the last.

## The pyramid principle

State the conclusion or recommendation first. Support it after, in order of decreasing importance. Never build up to the point — state it, then justify it.

**Wrong order (climactic — point comes last):**
> We looked at three vendors, ran cost comparisons across two quarters, and interviewed the two teams that would use the tool daily. Based on all of this, we recommend Vendor B.

**Right order (pyramid — point comes first):**
> We recommend Vendor B. It costs 18% less than the incumbent over two quarters and both using teams preferred it in interviews.

## How to check it

1. Find the single most important sentence in the draft — the conclusion, recommendation, or key fact.
2. If it is not the first sentence, move it there.
3. Everything else follows in descending order of importance. The reader should be able to stop after any paragraph and still have the most important information they've seen so far.
4. Cut a paragraph entirely if, once reordered, it turns out to only restate or build up to something already said.

## Signal this rule catches

- A summary that opens with background, context, or process before the finding or ask.
- A message where the actual request is in the last sentence or last paragraph.
- "Based on the above, we therefore..." as a paragraph opener — the giveaway that the point was saved for last.
```

- [ ] **Step 2: Verify**

Confirm the file has both a "wrong order" and "right order" example, and a numbered checklist — these are what `SKILL.md` step 1 depends on when checking a draft.

- [ ] **Step 3: Commit**

Same note as Task 2 — commit only if mirroring in-repo (Task 8).

---

### Task 4: Write plain-wording.md

**Files:**
- Create: `C:\Users\Thorsten\.claude\skills\clear-writing\references\plain-wording.md`

**Interfaces:**
- Produces: `references/plain-wording.md`, referenced by `SKILL.md` step 2.

- [ ] **Step 1: Write the file**

Base this on plainlanguage.gov's documented guidance (generalized rules, not verbatim reproduction) plus The Economist's short-words principle (sourced during Task 5's research — cross-reference is fine since both converge on the same rule):

```markdown
# Plain wording

Rules for word choice and sentence construction, independent of structure (see `structure.md`) or which style guide applies (see the two `style-*.md` files).

## Rules

1. **Short words over long ones.** If a one- or two-syllable word means the same thing, use it. "Use" not "utilize." "Help" not "facilitate." "Start" not "commence."
2. **Short sentences.** One idea per sentence. If a sentence has more than one "and" joining independent clauses, consider splitting it.
3. **Active voice, named actor.** "The team shipped the fix" not "the fix was shipped." Say who did what.
4. **Concrete over abstract.** A number, name, or date beats a qualitative claim. "Costs rose 18%" not "costs rose significantly."
5. **Cut words that don't change the meaning.** If deleting a word leaves the sentence meaning the same, delete it. Common offenders: "in order to" → "to"; "due to the fact that" → "because"; "at this point in time" → "now."
6. **Common words over jargon.** If there's an everyday English word for it, use that instead of a technical, corporate, or foreign term — unless the audience specifically needs the technical term.

## Quick self-check

Read the sentence aloud. If you wouldn't say it that way to a colleague across a table, rewrite it.

## Source

Generalized from [plainlanguage.gov](https://www.plainlanguage.gov/)'s documented federal plain-language guidelines, and The Economist's "never use a long word where a short one will do" principle (itself drawn from Orwell's rules for writing — see `style-general-writing.md` for the full Economist citation).
```

- [ ] **Step 2: Verify**

Confirm all 6 rules are present and each has a concrete before/after or example, not just an abstract instruction (avoids the "add appropriate X" placeholder failure mode).

- [ ] **Step 3: Commit**

Same note as Task 2.

---

### Task 5: Research and write the two style guides

This is the research step — read real, accessible content from the five publications and extract observable patterns before writing. Do not skip straight to writing from memory.

**Files:**
- Create: `C:\Users\Thorsten\.claude\skills\clear-writing\references\style-management-summary.md`
- Create: `C:\Users\Thorsten\.claude\skills\clear-writing\references\style-general-writing.md`

**Interfaces:**
- Produces: both style files, referenced by `SKILL.md` step 3 (Task 1) as the two mutually-exclusive style choices.

- [ ] **Step 1: Research HBR/Bloomberg (management-summary inputs)**

Search for and read 2-3 accessible sources on: HBR's BLUF guidance for executive writing, and Bloomberg/military BLUF format. (Already partially done during brainstorming — reuse those findings: BLUF = lead with conclusion/key message; executives should get the point within the first 30 seconds; Situation-Complication-Solution as a structure.) Note down, in your own words, 4-6 concrete rules — not copied sentences.

- [ ] **Step 2: Research Economist/WSJ/FT (general-writing inputs)**

Search for and read 2-3 accessible sources on: The Economist's public style guide (short words, no jargon, "do not be stuffy"), WSJ's narrative-lede formula (specific human/scene detail → nut graph → broader context), and FT's approach to making technical/global topics accessible. Note down 4-6 concrete rules in your own words.

- [ ] **Step 3: Write style-management-summary.md**

```markdown
# Style: management summaries

For status updates, recommendations, proposals, and anything read by a decision-maker who needs the point before the detail. Weighted toward Harvard Business Review's and Bloomberg's conventions.

## Rules

1. **BLUF — Bottom Line Up Front.** The first sentence is the conclusion, recommendation, or ask. A reader who stops after sentence one should still know what you want from them.
2. **Situation → Complication → Solution.** After the BLUF sentence, give just enough of: what's the situation, what's the problem/complication, what's the proposed solution — in that order, each in one or two sentences.
3. **Visual signposting.** Use bold lead-ins or short bullets so a skimming reader can scan the shape of the argument without reading every word. Don't overuse — one bold lead-in per list item, not per sentence (see `humanizer.md` §15-16 for the failure mode of overdoing this).
4. **One ask per summary.** If there are multiple asks, number them. Don't bury a second ask in a supporting paragraph.
5. **Numbers, not adjectives.** "Reallocate $100k from print to digital" not "significantly increase digital investment."

## Example

**Weak (buries the ask):**
> We have conducted an exhaustive analysis of market trends and evaluated multiple operational strategies going forward, considering budget constraints and team capacity across both channels.

**Better (BLUF + concrete):**
> We recommend reallocating $100k from print to digital ads next quarter. Digital converts at 3x the rate of print in this segment, and the shift can happen within existing budget.

## Sources

Patterns drawn from Harvard Business Review's coverage of BLUF-style executive communication (the "military email" framing: lead with the point so a reader knows what's needed within the first 30 seconds) and Bloomberg/wire-style inverted-pyramid convention (most important fact first, supporting detail after, in descending order of importance). Rules here are original synthesis, not reproduced text.
```

- [ ] **Step 4: Write style-general-writing.md**

```markdown
# Style: general writing

For explanations, documentation, notes, and messages that aren't a management ask. Weighted toward The Economist's, The Wall Street Journal's, and the Financial Times' conventions.

## Rules

1. **Plain English, no jargon.** If there's an everyday word, use it instead of a technical, foreign, or corporate one. (Shared with `plain-wording.md` — this style guide leans on it harder.)
2. **Short words over long ones.** Never use a long word where a short one will do.
3. **Ground the abstract in something specific.** Instead of describing an issue in the abstract, show its effect on a real person, team, or number, then generalize. A concrete opening detail earns the reader's attention before the broader point.
4. **Authoritative but accessible on technical topics.** Explain the technical term once, plainly, then use it — don't avoid technical precision, but don't assume the reader already has it either.
5. **Don't be stuffy.** Write the way you'd speak to a colleague, not the way a policy document or press release would.

## Example

**Weak (abstract, no human anchor):**
> Our customer support operation experienced high call volumes due to ongoing systemic outages.

**Better (concrete, human-anchored):**
> Over 400 customers waited an average of 45 minutes on hold yesterday after our main server failed.

## Sources

Patterns drawn from The Economist's public style guide (favor short, plain words; avoid jargon; "do not be stuffy — use the language of everyday speech"), the Wall Street Journal's narrative-lede convention (open on a specific person, scene, or detail before widening to the general point — the "nut graph" technique), and the Financial Times' approach of keeping technical/global topics accessible without dumbing them down. Rules here are original synthesis, not reproduced text; no source article text is copied.
```

- [ ] **Step 5: Verify both files**

Confirm each file has: a clear "who this is for" line, a numbered rule list with concrete rather than vague rules, one worked weak/better example, and a Sources section naming the publications without quoting more than a short attributed phrase from any of them.

- [ ] **Step 6: Commit**

Same note as Task 2 (mirror to in-repo copy in Task 8 if applicable).

---

### Task 6: Seed DONTS.md

**Files:**
- Create: `C:\Users\Thorsten\.claude\skills\clear-writing\references\DONTS.md`

**Interfaces:**
- Produces: `references/DONTS.md`, referenced by `SKILL.md` step 4.

- [ ] **Step 1: Write the file**

```markdown
# DON'Ts

A flat, growing list. Add an entry any time a specific pattern should be avoided — one line, plain jargon-to-plain-alternative or a short rule, with an optional note on why.

Edit this file directly at any time. Claude may also append an entry when you flag something mid-conversation (e.g., "don't do X") — ask for confirmation before adding unless the user has clearly already said to remember it.

## Jargon to avoid

| Jargon | Use instead | Why |
|---|---|---|
| Leverage | Use / take advantage of | State specifically how the tool or asset is used |
| Synergy / synergize | Combine / work together | Name the exact benefit instead of the buzzword |
| Actionable | Practical / useful | Present the specific recommendation directly |
| Circle back / touch base | Follow up / speak with | Include a specific time and channel |
| Bandwidth | Capacity / time | State clearly whether you have the time or team resources |
| Move the needle | Make progress | Replace the vague claim with a measurable target |
| Utilize / facilitate | Use / help | Multi-syllable verbs add stiffness for no benefit |
| In order to | To | Cutting "in order" tightens the sentence |
| At this point in time | Now / currently | One word instead of four |

## Other DON'Ts

(Empty — add general rules here as they come up, in addition to the jargon table above.)
```

- [ ] **Step 2: Verify**

Confirm the table has all 9 jargon rows from the design spec, and there's a clear place ("Other DON'Ts") for freeform additions that aren't jargon substitutions.

- [ ] **Step 3: Commit**

Same note as Task 2.

---

### Task 7: Seed examples/good and examples/bad

**Files:**
- Create: `C:\Users\Thorsten\.claude\skills\clear-writing\examples\bad\active-voice.md`, `.../good/active-voice.md`
- Create: `C:\Users\Thorsten\.claude\skills\clear-writing\examples\bad\conciseness.md`, `.../good/conciseness.md`
- Create: `C:\Users\Thorsten\.claude\skills\clear-writing\examples\bad\concrete-data.md`, `.../good/concrete-data.md`
- Create: `C:\Users\Thorsten\.claude\skills\clear-writing\examples\bad\human-impact.md`, `.../good/human-impact.md`
- Create: `C:\Users\Thorsten\.claude\skills\clear-writing\examples\bad\bluf.md`, `.../good/bluf.md`

**Interfaces:**
- Produces: 10 example files, referenced by `SKILL.md` step 4 (`examples/bad/` for violation-checking) and step 5 (`examples/good/` for voice-matching).

- [ ] **Step 1: Write the active-voice pair**

`examples/bad/active-voice.md`:
```markdown
# Bad: passive voice hides the actor

> A determination was made by management that layoffs would need to be implemented due to budget deficits.

Problem: passive construction ("a determination was made," "would need to be implemented") hides who did what and pads the sentence.
```

`examples/good/active-voice.md`:
```markdown
# Good: active voice, named actor

> Management cut 50 jobs to offset a $2 million budget deficit.

Why it works: names the actor (management), the action (cut), and the concrete reason (the deficit, with a number) in one direct sentence.
```

- [ ] **Step 2: Write the conciseness pair**

`examples/bad/conciseness.md`:
```markdown
# Bad: filler words bury the point

> In spite of the fact that sales were slow in Q1, we are currently of the opinion that Q2 will see growth.

Problem: "in spite of the fact that" and "we are currently of the opinion that" are filler — the sentence says the same thing without them.
```

`examples/good/conciseness.md`:
```markdown
# Good: same point, a third of the words

> Although Q1 sales lagged, we expect Q2 growth.
```

- [ ] **Step 3: Write the concrete-data pair**

`examples/bad/concrete-data.md`:
```markdown
# Bad: vague hyperbole instead of a number

> The recent launch of our new software feature resulted in a massive surge in overall user engagement.

Problem: "massive surge" and "overall user engagement" give no way to judge how big the change actually was.
```

`examples/good/concrete-data.md`:
```markdown
# Good: exact metric and timeframe

> Daily active users rose 22% in the two weeks following the software release.
```

- [ ] **Step 4: Write the human-impact pair**

`examples/bad/human-impact.md`:
```markdown
# Bad: abstract operational language

> Our customer support operation experienced high call volumes due to ongoing systemic outages.

Problem: describes the issue in operational abstraction, with no sense of what actually happened to anyone.
```

`examples/good/human-impact.md`:
```markdown
# Good: grounded in real, specific impact

> Over 400 clients waited an average of 45 minutes on hold yesterday after our main server failed.
```

- [ ] **Step 5: Write the BLUF pair**

`examples/bad/bluf.md`:
```markdown
# Bad: point saved for the end

> We have conducted an exhaustive analysis of market trends and evaluated multiple operational strategies going forward...

Problem: this is a preamble. The reader has no idea what's being asked or recommended after reading the whole sentence.
```

`examples/good/bluf.md`:
```markdown
# Good: recommendation stated first

> We recommend reallocating $100k from print to digital ads next quarter to capture higher conversion rates.

Why it works: the ask is the first sentence. Rationale can follow, but the reader already has what they need.
```

- [ ] **Step 6: Verify all 10 files exist**

Run:
```bash
ls "C:\Users\Thorsten\.claude\skills\clear-writing\examples\good" "C:\Users\Thorsten\.claude\skills\clear-writing\examples\bad"
```
Expected: 5 files listed in each directory, matching filenames (`active-voice.md`, `conciseness.md`, `concrete-data.md`, `human-impact.md`, `bluf.md`).

- [ ] **Step 7: Commit**

Same note as Task 2.

---

### Task 8: Decide on in-repo mirroring, then validate end-to-end

**Files:**
- Read: all files created in Tasks 1-7
- Optionally create: a mirrored copy under this repo (e.g. `skills/clear-writing/`) if the user wants the skill itself version-controlled in `github.com/ThorstenWeberGER/writing-skills` rather than only living under the user-global `~/.claude/skills/`.

**Interfaces:**
- Consumes: the complete skill directory from Tasks 1-7.
- Produces: a validated, working skill; optionally, an in-repo mirror committed to git.

- [ ] **Step 1: Ask the user whether to mirror the skill into this repo**

The design spec's repo (`writing-skills`) was originally meant to house this skill's development. Confirm with the user: should `~/.claude/skills/clear-writing/` be the only copy (global, works everywhere), or should this repo also carry a synced copy (e.g. `skills/clear-writing/`) for version history and portability to other machines? If yes, copy the full directory tree into the repo and commit it.

- [ ] **Step 2: Dry-run validation against a real draft**

Pick one real piece of text the user has previously written or a draft Claude would naturally produce (e.g., a status update). Manually walk it through the five-step pass order in `SKILL.md`:
1. Check structure.md — does it lead with the point?
2. Check plain-wording.md — any long words, filler, passive voice to cut?
3. Apply the correct style guide.
4. Check DONTS.md and examples/bad — any jargon-table hits?
5. Apply humanizer.md's pattern check.

Confirm the resulting rewrite is demonstrably better against each of the five checks — not just "looks fine."

- [ ] **Step 3: Dry-run validation on a second draft**

Repeat Step 2 with a second, different draft (ideally one meant for `style-management-summary.md` if the first used `style-general-writing.md`, or vice versa) to confirm both style-guide branches actually get exercised and produce sensible output.

- [ ] **Step 4: Final commit**

```bash
cd "C:\Users\Thorsten\OneDrive\Dokumente\Github\writing-skills"
git add -A
git commit -m "docs: complete clear-writing skill implementation plan and validation notes"
git push
```
