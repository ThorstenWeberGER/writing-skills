# clear-writing skill — design

Date: 2026-08-22

## Problem

Writing produced or edited in this workflow — by the user or by Claude — should read like a human wrote it, lead with the point, use plain wording, and avoid the user's known pet peeves. Today there is no shared, reusable ruleset: preferences live in the user's head and get re-explained every time. `backlog.md` in this repo captured the original wishlist.

## Goal

One Claude Code Skill, `clear-writing`, that Claude invokes any time it drafts or edits prose for the user — its own output and the user's drafts alike — applying a consistent ruleset that the user can extend over time.

## Non-goals (v1)

- Audience-specific profiles (boss/management/etc.) — deferred to v2.
- Use-case templates (README.md, installation.md, summary.md, meeting_notes.md) — deferred.
- Fabricated example prose — every example in `examples/` must be real, supplied by the user or captured from an actual conversation.
- Live dependency on the external `humanizer` repo — its ruleset is ported in once and version-controlled here, not pulled at runtime.

## Design

### Structure

```
clear-writing/
  SKILL.md                 # entry point: when to invoke, and the pass order
  references/
    structure.md           # pyramid principle / first-things-first
    plain-wording.md       # plainlanguage.gov rules, short sentences
    style-models.md         # wire/news (AP/Reuters) + business-explainer (Economist/Bloomberg) notes
    humanizer.md             # full pattern list ported from github.com/blader/humanizer SKILL.md
    DONTS.md                  # flat, growing list of user-specific don'ts
  examples/
    good/                      # user's real writing samples (also used as humanizer voice-match input)
    bad/                        # real DON'T violations, captured as they occur
```

### SKILL.md — pass order

When drafting or editing prose, Claude works through the references in this order:

1. **structure.md** — does the text lead with the point? Reorder if it buries the lede.
2. **plain-wording.md** — plain wording, short sentences (plainlanguage.gov basis).
3. **style-models.md** — sanity-check against wire/news and business-explainer conventions.
4. **DONTS.md** and `examples/bad/` — check for known violations.
5. **humanizer.md** — final surface-level pass for AI-writing tells (inflated claims, stock phrasing, passive voice, chatbot artifacts, etc.), matching voice against a file in `examples/good/` when one is relevant to the context.

This is a single skill (not a chain of separate skills) so the whole ruleset loads and applies together, and all references live in one place under version control.

### DONTS.md workflow

- Editable directly by the user at any time.
- Claude appends an entry when the user flags something mid-conversation (e.g., "don't do X") — one line, plus a short example if one is available.

### Examples workflow

- Seeded from real writing the user supplies during/after this design (not fabricated).
- Grown the same way as DONTS.md: when a bad pattern is caught in conversation, it can be captured into `examples/bad/` with the user's confirmation.

### humanizer.md content

Ported in full from `github.com/blader/humanizer`'s `SKILL.md` (MIT-licensed), covering all 35 documented AI-writing patterns across four categories: content patterns, language patterns, chatbot patterns, and filler/hedging patterns. Kept in full for now; trimmed later once the user sees which patterns actually fire often versus never.

### Style-models.md content

Sourced from the user's own research into business/journalistic writing standards. Five reference publications, each contributing a specific principle rather than being treated as one undifferentiated "news style":

- **The Economist** — plain English, brevity, active voice, short/simple words over corporate jargon.
- **The Wall Street Journal** — narrative structure, concrete data over adjectives, human-centric framing (ground abstract issues in real impact on real people).
- **Harvard Business Review** — BLUF (Bottom Line Up Front), Situation-Complication-Solution structure, visual signposting (bold lead-ins, bullets) for scannability.
- **Financial Times** — authoritative tone while keeping technical material globally accessible.
- **Bloomberg News** — BLUF for rapid scanning.

This supersedes the earlier generic "wire/news + business-explainer" framing from the initial design pass — it's more specific and directly actionable (named sources, a concrete rule checklist, worked examples), so it becomes the primary content of `style-models.md`.

### DONTS.md seed content

Seeded (not empty at v1 after all) with the user's buzzword blacklist — corporate jargon mapped to plain alternatives, with a best-practice note for each:

| Jargon | Plain alternative | Best practice |
|---|---|---|
| Leverage | Use / take advantage of | State specifically *how* the tool or asset is used |
| Synergy / synergize | Combine / work together | Detail the exact benefit of working together |
| Actionable | Practical / useful | Present the specific recommendation directly |
| Circle back / touch base | Follow up / speak with | Include a specific time and channel |
| Bandwidth | Capacity / time | State clearly whether you have the time or team resources |
| Move the needle | Make progress | Replace vague claims with measurable targets |
| Utilize / facilitate | Use / help | Multi-syllable verbs add stiffness |
| In order to | To | Cutting "in order" tightens sentences |
| At this point in time | Now / currently | Use one word instead of four |

### Examples/ seed content

Seeded with the user's own weak-vs-good pairs (real, user-authored — not fabricated by Claude), one per rule this skill enforces:

- **Active voice**: passive/buried-actor sentence → direct subject-verb-object rewrite.
- **Conciseness**: filler-laden hedge → same point in a third of the words.
- **Concrete data**: vague hyperbole ("massive surge") → exact metric and timeframe.
- **Human impact**: abstract operational language → tangible effect on real people.
- **BLUF**: long analytical preamble → recommendation stated in sentence one.

Each pair goes into `examples/bad/<rule>.md` (weak version) and `examples/good/<rule>.md` (rewrite), so the pairing itself doubles as a mini rule explanation.

### Plain-wording.md content

Rules generalized from plainlanguage.gov's documented guidance (short sentences, common words, active voice, one idea per sentence, etc.), used as the ruleset basis rather than reproduced verbatim.

## Error handling / edge cases

- No writing sample available for voice-matching: humanizer.md's default guidance applies (formal/casual/technical judged from context) instead of a specific voice sample.
- Reference/legal/technical text: personality additions from humanizer.md are suppressed per its own existing guidance — factual/reference text stays neutral.
- Conflicting DON'T vs. style-model guidance: DONTS.md wins (user-specific override beats general style guidance).

## Testing / validation

Given this is a prose-guidance skill rather than executable code, validation is: run it against a handful of real drafts (the user's own past writing, and a fresh Claude-drafted doc), confirm the output matches expectations, and check that DONTS.md / examples additions actually get picked up on the next invocation.

## Open items for v2 (explicitly deferred, not forgotten)

- Audience profiles (boss/management/peer/client).
- Use-case templates (README, installation, summary, meeting notes).
- Trimming humanizer.md down to patterns that actually recur in this user's writing.
