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
