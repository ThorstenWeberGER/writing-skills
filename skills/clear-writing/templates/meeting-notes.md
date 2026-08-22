# Template: meeting notes

The governing rule is 150 years old and still the sharpest thing anyone has said about it:

> Minutes should contain mainly a record of what was done at the meeting, not what was said by the members.

Notes are a record of decisions and actions, not a transcript. Everything below follows from that.

## Skeleton

```markdown
# {Meeting name} — {date}

**Attendees:** …
**Absent:** …            ← matters, because of the async rule below
**Purpose:** one sentence on what this meeting was for.

## Decisions
1. **{Decision}**
   - Context: what made this necessary.
   - Consequences: what gets easier, and what gets harder.

## Action items
1. {Owner} will {specific deliverable} by {date}. — why it matters
2. …

## Discussion (optional)
Only what a reader needs to understand a decision above. Not a play-by-play.

## Open questions
Things deliberately unresolved, with who owns resolving them.
```

## Rules

1. **Number the items, don't bullet them.** Numbered items can be referenced later ("re: decision 3") — bullets can't.
2. **Every action item names an owner, a specific deliverable, and a date.** Formula: *{Owner} will {verb + specific deliverable} by {deadline}*, plus a short note on why it matters. Any of the three missing and the item won't happen.
3. **Each decision carries its context and its consequences** — including the negative ones. A decision recorded as an outcome alone is unusable in six months, because nobody can tell whether the reasoning still applies. Borrow the architecture-decision-record shape: one decision per entry, and consequences means "what becomes easier *or harder* because of this."
4. **Write during the meeting, not afterwards from memory.** The agenda document becomes the notes document, edited live by whoever is present.
5. **Hold decisions open 24-48 hours when stakeholders were absent.** In a distributed or cross-timezone team, a decision made by whoever happened to be awake isn't a decision yet. Post the notes, name the window, then let it settle.
6. **Keep the note-taker's opinion out.** Record what the group decided, not what you thought of it.
7. **Share with everyone affected, not just attendees.** The people who most need the notes are the ones who weren't there.

## Failure modes

- A transcript instead of a record — the dominant failure, and what rule 1 above exists to prevent.
- Discussion captured with no decision attached, or a decision with no reasoning attached.
- Action items with no owner, no date, or a vague verb ("look into," "follow up on," "align on").
- Notes written up hours later, so half of it is reconstruction.
- Decisions treated as settled when the people they affect never saw them.

## Sources

The "what was done, not what was said" rule and the header-block structure come from **Robert's Rules of Order** ([rulesonline.com](http://www.rulesonline.com/rror-10.htm)), the long-established convention for minutes. The live-document practice, numbered-not-bulleted convention, and the 24-48 hour async window come from the [GitLab Handbook](https://handbook.gitlab.com/handbook/company/culture/all-remote/live-doc-meetings) — one company's documented practice, but battle-tested at scale and distinctive. The decision-entry shape (one per record, context + consequences, consequences including what gets harder) is [Michael Nygard's ADR template](https://github.com/joelparkerhenderson/architecture-decision-record). The owner/verb/deadline formula is common across vendor guidance.

**Deliberately omitted:** the meeting-notes literature is dominated by transcription-vendor content marketing, which circulates confident statistics ("73% increase in action-item completion," "if it takes more than 30 seconds to find your tasks…") that trace to no study. The underlying sentiment is well-supported; the numbers are not, so none are quoted here.
