# clear-writing skill — status and open items

Last updated 2026-08-23. The skill lives in this repo at `skills/clear-writing/`.

Run `./skills/clear-writing/test.sh` to verify the whole thing. Currently all green: drift test in sync, 14/14 rule anchors present, 7/7 fixtures behaving as expected.

---

## Done

### 1. Primary sourcing for the plain-language rules

The original blocker stands: economist.com, wsj.com, bloomberg.com and hbr.org all refuse automated fetching or serve teasers only. Rather than wait, the rules were re-derived from primary authorities that publish their own guidance as open-source repositories.

- [x] **GSA/plainlanguage.gov** — the federal plain-language guidelines, from the publisher's own repo. Real primary text.
- [x] **18F/content-guide** — GSA's content guide, source of the only numeric sentence-length guidance found.
- [x] `foundations.md`'s plain-wording and heading/list rules re-derived with per-rule attribution and URLs.
- [x] **Three rules corrected** where the primary text contradicted them: "short words over long" is really about *familiarity*; active voice has two legitimate exceptions; the "3-6 bullets" range has no primary support and is now labeled house convention.
- [x] Sourced rules added that were missing entirely: hidden verbs, noun strings, abbreviations, list lead-in sentences, parallelism with the lead-in, nesting caps, paragraph limits with the anti-uniformity rule, "address the reader as you."

### 2. Audience profiles

- [x] `references/audiences.md`, on a separate axis from format so profiles don't multiply per format.
- [x] Technical peer (Google eng-practices, Nygard ADRs), external client (incident-communication practice), non-native English readers (Google global-audience, Kohl's *Global English Style Guide*). Decision-maker routes to `formats.md`.
- [x] The conflict between the technical-peer and non-native profiles documented and resolved: keep domain nouns precise, simplify everything around them.
- [x] "When jargon is the right choice" — four tests. The highest-value single addition, since plainlanguage.gov's own carve-out shows the plain-word rule was never aimed at domain nouns.

### 3. Templates

- [x] `project-readme.md` (standard-readme spec), `installation.md` (Good Docs Project, trimmed), `meeting-notes.md` (Robert's Rules + GitLab + ADR shape).
- [x] `templates/README.md` carries the Diátaxis routing compass.
- [x] `summary.md` deliberately **not** built — `formats.md` already covers summaries. Heeded Diátaxis's own warning against creating empty template scaffolding.

### 4. humanizer.md trim

- [x] 4,700 → ~1,750 words. It had been 48% of the skill.
- [x] Dropped encyclopedia-specific patterns; cross-referenced rather than duplicated what `foundations.md`/`DONTS.md` already cover; removed vestigial standalone-skill scaffolding; renamed §1-35 to named sections.

### 5. Structural consolidation

- [x] `style-general-writing.md` deleted — 3 of 5 rules duplicated `foundations.md`, and its only example was already in `examples.md` verbatim.
- [x] `style-management-summary.md` + `article-structure.md` merged into `formats.md`.
- [x] `DONTS.md` and `examples.md` kept separate on purpose, with the reason recorded in both.

### 6. Enforcement layer

This was the largest piece of work and wasn't in the original checklist. It exists because the skill kept shipping drafts where a pass was *reported* as applied while its rules were violated in the same text.

- [x] **`check.py`** — 22+ mechanical checks, stdlib only, exit 1 on any FAIL. Conditional flags for `--summary`, `--email`, `--article-half/full`, `--client`, `--nonnative`, `--dashes-ok`, `--compare`.
- [x] **`CHECKLIST.md`** — the judgment half, step by step. Requires reporting what was run, not "applied the skill".
- [x] **`test_drift.py`** — fails when `check.py`'s wordlists drift from the reference files, in three directions (MISSING, ORPHAN, BROKEN RULE ANCHOR). Verified it can actually fail by injecting each direction.
- [x] **`test.sh`** — drift test plus 7 fixtures.
- [x] Every reference file ends by stating it is not self-enforcing.

### 7. Style-only mode

- [x] `SKILL.md` picks a mode before anything else. Style-only (the default) runs plain wording + DONTS + humanizer and explicitly does not restructure, compress, reorder, or impose a format.
- [x] `--compare ORIGINAL` enforces the mode's characteristic failure: fails past 15% word loss, flags changed paragraph count. Verified — a real style edit passes at +4%, a compressed rewrite of the same text fails at −59%.

### 8. Defects found and fixed by testing

Worth recording because of the pattern: **purpose-built fixtures kept passing while real documents exposed the bugs.**

- [x] Two em dashes and an agentless passive shipped while passes 1 and 5 were reported as run. Cause of the whole enforcement layer.
- [x] A vague source reference ("approximately last Tuesday") silently rewritten as a specific date. Caught by the facts-audit step, after surviving two earlier review passes.
- [x] Duplicated and misnumbered rules in `foundations.md`, self-inflicted during the primary-source rewrite.
- [x] Markdown bullet markers counted as spaced dashes — three of four "dashes" in a real draft were bullets.
- [x] Wordlist scans flagging terms that were being *discussed*, not used, in violation of `humanizer.md`'s own false-positive rule. Seven of nine FAILs on the design doc were this.
- [x] Four wordlist gaps found by the drift test; noun-string heuristic flagging verb phrases.

---

## Open

### A. `examples.md` has only its 5 launch pairs — the one real content gap

Can't be fixed by research. The file admits only real user-supplied or conversation-captured pairs, never invented ones, and that invariant is deliberate. It grows only through use.

**Blocked on:** actual use of the skill on real drafts.

### B. Voice sample exists but covers only short-form writing — PARTLY DONE

- [x] `voice-sample.md` created from real material: `backlog.md` plus the user's session instructions, quoted verbatim.
- [x] Patterns extracted and **measured** rather than estimated: 27 sentences, median 6 words, max 16, none longer. Imperative mood dominant, sparse punctuation, "as well" as a habitual closer.
- [x] **The em-dash question is settled empirically:** character scan finds zero `—`/`–` across every quote and across `backlog.md`. The ban applies; `--dashes-ok` should not be passed. `CHECKLIST.md`'s flag table now says so.
- [x] Records the distinction that matters: match rhythm and word choice, never reproduce typos or missing punctuation from a sample.
- [x] Wired into `humanizer.md`, `SKILL.md`, and `CHECKLIST.md`, with a drift-test rule anchor so the wiring can't silently rot.

**Still open:** both sources are short-form and functional — a planning list and a set of instructions. Neither is connected prose written for a reader. So the sample supports word choice, sentence length, punctuation, and the dash decision, but says nothing about how this writer opens a document, builds a paragraph, or handles a transition.

**Needs:** two or three paragraphs of real connected prose the user wrote for someone else — an email to a colleague, a section of a doc, a Slack post. Appended as Source 3, same verbatim treatment. Until then paragraph-level voice matching is explicitly marked unsupported.

### C. CI — DONE

- [x] `.github/workflows/clear-writing-tests.yml` runs `test.sh` on any push or PR touching the skill, plus manual dispatch. Verified the suite passes when invoked from the repo root the way CI does.

Closed because "only runs when someone remembers" was the same failure mode the enforcement layer exists to fix, one level up.

### D. The drift test's allowlists are large enough to hide drift

`NON_LITERAL` has 53 entries and `ORPHAN_OK` has 114. Each entry is individually justified, but the escape hatch is now big enough that adding to it is easier than fixing the coupling. Nothing distinguishes "genuinely can't be grepped" from "someone didn't want to deal with it."

**Fix:** periodically re-audit the allowlists, or make additions require a reason string that the test prints (NON_LITERAL already does; ORPHAN_OK does not).

### E. `check.py`'s heuristics are approximations

Passive voice and noun-string detection are pattern matches, not parsing. That's why they emit REVIEW rather than FAIL. Acceptable, but it means those two rules are advisory in practice.

**Possible fix:** a real POS tagger would make both precise, at the cost of adding a dependency to a currently stdlib-only script. Probably not worth it.

### F. Installation and distribution unverified

The previous version of this file claimed the skill was "live at `~/.claude/skills/clear-writing/`". In this container it is **not** — the synced skills mirror doesn't contain it, so the skill exists only in this repo. Whether it's installed on the user's own machine can't be verified from here.

**Needs:** confirm where it should actually live, and how it gets there.

### G. Mode selection isn't enforced, only documented

`SKILL.md` says to pick style-only or full mode first, but nothing checks that the right one was used. `--compare` catches unwanted compression only if someone remembers to pass it.

**Inherent limit,** same class as `CHECKLIST.md`'s judgment steps: the enforcement layer can verify outputs, not intentions.

### H. Templates are untested against real use

`project-readme.md`, `installation.md` and `meeting-notes.md` were derived from good sources but have never been used to produce an actual document. The Diátaxis routing in `templates/README.md` isn't referenced by `CHECKLIST.md` or `check.py`.

### I. Sourcing status

- [x] **Four publications are now primary**, all supplied by the user rather than fetched: The Economist (9 excerpts, 3,131w), the Financial Times (4 articles, ~3,400w), Reuters (4 articles plus the Trust Principles pages), and HBR (5 articles, 14,557w). Roughly 25,000 words of measured professional prose.
- [ ] WSJ, Bloomberg, Guardian and BBC remain secondary. All block automated fetching. The affected claims are narrow and flagged in-file, and after four publications the marginal value of a fifth is low.
- [ ] BLUF's military provenance (Army Regulation 25-50) unverified. The *behavior* is fully primary-sourced; only the origin story is secondhand.
- [ ] Two widely-circulated figures could not be confirmed against their claimed documents (Reuters' "300-800 words per story", AR 25-50's "15-word average sentence"). Deliberately unused.
- [ ] 18F quotations were captured via a summarizing fetch, not character-for-character. High confidence, not pinned.
- [ ] Reachable-but-unharvested primary pages in `GSA/plainlanguage.gov`: `guidelines/design/`, `guidelines/test/`, plus the SEC Plain English Handbook it cites.

---

## Next steps, in priority order

1. **Use the skill on real drafts and grow `examples.md`** (A). The only gap research can't close.
2. **Add a connected-prose voice sample** (B). The short-form sample is in place; a real paragraph or two is what is missing.
3. ~~Add CI~~ — done.
4. **Re-audit the drift allowlists** (D) once they stop growing.
5. **Confirm where the skill is installed** (F).
6. **Pin the 18F quotes** with one literal re-fetch (I).
7. **Everything else** is low value or inherently bounded. The paywalled publications in particular: leave them unless print copies turn up.
