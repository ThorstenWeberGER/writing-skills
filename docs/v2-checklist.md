# clear-writing skill — v2 checklist

Everything below is explicitly deferred from v1, not forgotten. v1 shipped and is live at `~/.claude/skills/clear-writing/` (mirrored in this repo under `skills/clear-writing/`).

## 1. Verify the two style guides against real articles (not yet done)

**Status:** blocked in this session. `economist.com` and `wsj.com` refuse automated fetching outright, `bloomberg.com` returns 403, and `hbr.org` only serves a sponsored-content teaser with no real editorial text — no paywall-bypass tricks were attempted. `references/style-management-summary.md` and `references/style-general-writing.md` were written from secondary write-ups *describing* each publication's conventions (HBR's BLUF concept, WSJ's "nut graph" formula, the Economist's public style guide), not from analyzing real published sentences.

**To do:**
- [ ] User to bring back physical/print Economist articles from the library (mentioned as a next-week plan).
- [ ] Once real article text is available (photographed, scanned, typed excerpts — whatever's practical), read it and extract observable patterns: actual sentence length, paragraph length, how technical terms get introduced, how ledes open.
- [ ] Re-derive `style-general-writing.md`'s rules from that analysis; update its "Sources" section to remove the "derived from secondary sources" caveat once done.
- [ ] Same for `style-management-summary.md` if real HBR/Bloomberg text becomes available (WSJ library access, a shared HBR article, etc.).
- [ ] If genuinely not obtainable, that's fine — the current secondary-source version stays as the permanent basis. Note that explicitly rather than leaving the caveat dangling indefinitely.

## 2. Audience-specific profiles (deferred from v1 by design)

Beyond the two existing style guides (management-summary / general-writing), no profiles exist yet for other audiences (e.g. boss, peer engineer, external client).

**To do:**
- [ ] Decide which additional audiences are actually needed (don't build speculative ones — wait until a real case comes up).
- [ ] For each, write a `references/style-<audience>.md` following the same shape as the existing two (rules, weak/better example, sources).
- [ ] Update `SKILL.md`'s "pick one style guide" step to route to the new file(s).

## 3. Use-case templates (deferred from v1 by design)

Original backlog wishlist included templates for README.md, installation.md, summary.md, meeting_notes.md — none exist yet.

**To do:**
- [ ] Confirm which templates are still wanted (may have changed since the original backlog).
- [ ] Add a `templates/` directory to the skill with one file per use case.
- [ ] Update `SKILL.md` to reference templates when the user's request matches a known use case.

## 4. Trim humanizer.md to patterns that actually recur — DONE

`references/humanizer.md` was ported in full (all 35 patterns) from blader/humanizer, on the assumption it'd be trimmed once real usage shows which patterns fire often versus never.

- [x] Trimmed from ~4,700 words to ~1,750 (63% reduction), which had been 48% of the skill's total size.
- [x] Dropped patterns specific to encyclopedia articles: name-dropping publications to prove notability, curly-quote normalization, hyphenated-pair pedantry.
- [x] Cross-referenced rather than duplicated the four patterns already covered by `foundations.md`/`DONTS.md` (passive voice, filler phrases, stacked hedging).
- [x] Removed vestigial standalone-skill scaffolding (the "how to return the result" three-mode system), which didn't apply to a pass running inside this skill.
- [x] Switched numbered sections (§1-35) to named ones and updated the two inbound references.
- [x] Validated by testing against a slop-heavy paragraph: 13 of 14 tells caught; the one gap ("cutting-edge" missing from the sales-language list) was fixed.

Basis for trimming was fitness for this skill's actual output types (summaries, emails, docs, notes, PR descriptions, short articles) rather than logged usage frequency — the file predates any usage log. Revisit if a dropped pattern turns out to fire in practice.

## 5. Grow DON'Ts and examples through real use

`references/DONTS.md`'s "Other DON'Ts" section is currently empty beyond the seeded jargon table, and `examples/` has 5 pairs seeded at launch.

**To do (ongoing, not a one-time task):**
- [ ] Keep appending to `DONTS.md` when a new pattern gets flagged in conversation.
- [ ] Keep adding real before/after pairs to `examples/good/` and `examples/bad/` as they come up — never fabricated ones.
