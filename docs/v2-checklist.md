# clear-writing skill — v2 checklist

Status as of 2026-08-22. v1 shipped and is live at `~/.claude/skills/clear-writing/` (mirrored in this repo under `skills/clear-writing/`).

## 1. Verify the style guides against real sources — LARGELY DONE, by a different route

**Original blocker:** economist.com, wsj.com, bloomberg.com and hbr.org all refuse automated fetching or serve only teasers. The style guides were written from secondary write-ups *describing* those publications' conventions.

**What changed:** rather than keep waiting on paywalled publications, the rules were re-derived from *primary* plain-language authorities that publish their own guidance as open-source repositories:

- [x] **GSA/plainlanguage.gov** — the U.S. federal plain-language guidelines, from the publisher's own repo. Real primary text retrieved.
- [x] **18F/content-guide** — GSA's content guide. Source of the only numeric sentence-length guidance found.
- [x] Re-derived `foundations.md`'s plain-wording and heading/list rules from that text, with per-rule attribution and URLs.
- [x] Corrected three rules that the primary text contradicted or refined (see the file's "Known sourcing gaps"): "short words over long" is really about *familiarity*; active voice has two legitimate exceptions; the "3-6 bullets" range has no primary support and is now labeled house convention.
- [x] Added sourced rules that were missing entirely: hidden verbs, noun strings, abbreviations, list lead-in sentences, list parallelism with the lead-in, nesting caps, paragraph limits with the anti-uniformity rule, "address the reader as you."

**Still open, and probably permanently:**
- [ ] The Economist, WSJ, HBR, Bloomberg, Reuters, Guardian and BBC remain on secondary sourcing. All were unreachable. The affected claims are narrow and flagged in-file.
- [ ] BLUF's military provenance (Army Regulation 25-50) is unverified — the regulation itself was unreachable. The *behavior* is fully primary-sourced; only the origin story is secondhand.
- [ ] Two widely-circulated figures could not be confirmed against their claimed documents (Reuters' "300-800 words per story," AR 25-50's "15-word average sentence"). Deliberately not used.
- [ ] Original plan of bringing print Economist articles back from the library would still improve this. Lower priority now that the load-bearing rules have primary sourcing.

## 2. Audience-specific profiles — DONE

- [x] `references/audiences.md` written, on a deliberately separate axis from format (a summary can go to a CTO *or* a client, so profiles don't multiply per format).
- [x] Three profiles with a real basis: technical peer (Google eng-practices, Nygard ADRs), external client (incident-communication practice), non-native English readers (Google's global-audience guidance, Kohl's *Global English Style Guide*). Decision-maker routes to `formats.md`, which already covers it.
- [x] Documented and resolved the genuine conflict between the technical-peer and non-native profiles: keep domain nouns precise, simplify everything around them.
- [x] Added a cross-cutting "when jargon is the right choice" section with four tests, resolving the tension with `foundations.md`'s plain-word rule. This turned out to be the highest-value single addition — plainlanguage.gov's own carve-out says the plain-word rule was never aimed at domain nouns.
- [x] `SKILL.md` routes to it as pass 3.

Deliberately **not** built: speculative profiles with no real case behind them.

## 3. Use-case templates — DONE (three of four, one deliberately declined)

- [x] `templates/project-readme.md` — from the standard-readme spec, which is a real spec with real numbers.
- [x] `templates/installation.md` — from The Good Docs Project, trimmed hard (its original is calibrated for enterprise/hardware products), plus the classification of install docs as a how-to guide rather than a tutorial.
- [x] `templates/meeting-notes.md` — Robert's Rules' "what was done, not what was said," GitLab's live-document practice and 24-48h async window, and the ADR shape for decision entries.
- [x] `templates/README.md` carries the Diátaxis compass as a routing question.
- [x] **`summary.md` deliberately not built** — `references/formats.md` already covers management and executive summaries with length targets, structure, and the paired email variant. A template would have duplicated it.
- [x] Heeded Diátaxis's explicit warning against exactly this kind of work: "It certainly does not mean that you should create empty structures … Don't do that. It's horrible." No empty scaffolding was created.

## 4. Trim humanizer.md — DONE

- [x] Trimmed from ~4,700 words to ~1,750 (63% reduction). It had been 48% of the skill's total size.
- [x] Dropped patterns specific to encyclopedia articles: name-dropping publications for notability, curly-quote normalization, hyphenated-pair pedantry.
- [x] Cross-referenced rather than duplicated the four patterns already covered by `foundations.md`/`DONTS.md`.
- [x] Removed vestigial standalone-skill scaffolding (the three-mode "how to return the result" system), which never applied to a pass running inside this skill.
- [x] Renamed numbered sections (§1-35) to named ones; updated both inbound references.
- [x] Validated against a slop-heavy paragraph: 13 of 14 tells caught, and the one gap was fixed.

Basis was fitness for this skill's real output types, not a usage log — the file predates any logging. Revisit if a dropped pattern turns out to fire.

## 5. Structural consolidation — DONE (not in the original checklist)

- [x] Deleted `style-general-writing.md`: three of its five rules duplicated `foundations.md`'s plain-wording list, and its only example was already in `examples.md` verbatim. Its two unique rules moved into `foundations.md`.
- [x] Merged `style-management-summary.md` + `article-structure.md` into `formats.md`, organized by deliverable shape. This also fixed article-structure having been a easily-missed sub-bullet in the pass order.
- [x] Kept `DONTS.md` and `examples.md` separate on purpose, and documented why in both: `examples.md` holds only real material, `DONTS.md` holds rules with illustrative examples. Merging would have eroded that invariant.
- [x] `SKILL.md` rewritten: 5 passes over 5 reference files, plus templates.

Net: 8 reference files → 6, with the largest redundancy eliminated. Total skill size is roughly flat (~11.5k words) despite adding an audiences file and four template files, because the humanizer trim and the deduplication paid for them.

## 6. Grow DON'Ts and examples through real use — ONGOING

- [x] `DONTS.md`'s "Other DON'Ts" section seeded with ten general rules, each with a bad/better pair.
- [ ] Keep appending as patterns get flagged in conversation.
- [ ] **`examples.md` still has only the 5 pairs seeded at launch.** This is the one genuinely thin area, and it can't be fixed by research — the file admits only real user-supplied or conversation-captured pairs, never invented ones. It grows only through use.

## Next steps, in priority order

1. **Use the skill and grow `examples.md`.** It's the only remaining structural gap, and only real writing can fill it.
2. **Re-verify the 18F quotations** with one literal re-fetch. They were captured via a summarizing fetch rather than character-for-character, so they're high-confidence but not pinned.
3. **Harvest the remaining reachable primary pages** in `GSA/plainlanguage.gov` — `guidelines/design/`, `guidelines/test/`, `words/avoid-noun-strings` (already used), and the SEC Plain English Handbook it cites.
4. **Revisit the paywalled publications** only if print copies become available. Low value now.
