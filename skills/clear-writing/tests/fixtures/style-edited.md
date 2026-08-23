
- **BLUF**: long analytical preamble → recommendation stated in sentence one.

Each pair goes into `examples/bad/<rule>.md` (weak version) and `examples/good/<rule>.md` (rewrite), so the pairing itself doubles as a short rule explanation.

### Plain-wording.md content

Rules generalized from plainlanguage.gov's documented guidance: short sentences, common words, active voice, one idea per sentence. That guidance is the basis for the ruleset, not text to reproduce.

## Error handling / edge cases

- No writing sample available for voice-matching: humanizer.md's default guidance applies, judging formal, casual, or technical tone from context rather than from a sample.
- Reference/legal/technical text: personality additions from humanizer.md are suppressed per its own guidance. Factual and reference text stays neutral.
- Conflicting DON'T vs. style-model guidance: DONTS.md wins, because a user-specific override beats general style guidance.

## Testing / validation

This is a prose-guidance skill rather than executable code, so validation is manual. Run it against a handful of real drafts: the user's own past writing, and a fresh Claude-drafted doc. Confirm the output matches expectations, and check that additions to DONTS.md and examples get picked up on the next invocation.

## Open items for v2 (explicitly deferred, not forgotten)
