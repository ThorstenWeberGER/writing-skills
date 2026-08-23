# clear-writing skill — status and open items

Last updated 2026-08-23. The skill lives in this repo at `skills/clear-writing/`. Start with its `README.md`, which is the user-facing manual; this file tracks status and open work.

Run `./skills/clear-writing/test.sh` to verify the whole thing. Currently all green: drift test in sync, 14/14 rule anchors present, 9 fixtures behaving as expected. About 23,300 words across the skill; 66 checks in `check.py`.

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

The pattern is stable and worth stating on its own: **purpose-built fixtures kept passing while real documents exposed every one of these.**

**In the skill's own output:**

- [x] Two em dashes and an agentless passive shipped while passes 1 and 5 were reported as run. Cause of the whole enforcement layer.
- [x] A vague source reference ("approximately last Tuesday") silently rewritten as a specific date. Caught by the facts audit after surviving two earlier review passes.
- [x] 26 em dashes in the README, a document that documents the no-em-dash preference.
- [x] Duplicated and misnumbered rules in `foundations.md`, self-inflicted during the primary-source rewrite.

**In `check.py`, ten false positives or missing rules:**

- [x] Heading merged into the following sentence (no terminal punctuation), inflating that sentence's length.
- [x] List items merged the same way, producing a phantom 39-word sentence.
- [x] `Subject:` line merged into the first body sentence, dragging it out of the email count.
- [x] Markdown H1 subject line not recognised, because only a literal `Subject:` was matched.
- [x] Bullet items counted against the 5-sentence prose cap, making two rules in `formats.md` contradict each other. That contradiction was self-inflicted when the Reuters summary block was added.
- [x] Bare list markers counted as spaced dashes; three of four "dashes" in a real draft were bullets.
- [x] Blockquoted list items (`> - thing`) counted as spaced dashes, because `>` supplies the preceding non-space character.
- [x] Degree signs counted as decorative emoji, because the check tested the whole Unicode `So` category.
- [x] AI-tell words failing on a single hit, while `humanizer.md` already said "individually fine; in clusters, a strong tell". Now density-aware at 200 words per hit.
- [x] Terms flagged when being *discussed* rather than used, in two forms: markdown tables and before/after lines, then short quoted spans.

**Three over-generalisations, all the same shape:** a finding held across two publications and broke on the third. Zero subheadings (broke on Reuters), the 5-10 word headline range (broke on one 4-word outlier, then four samples vindicated the original rule), and the AI-tell wordlist (broke on HBR's ordinary register). Recorded in `README.md` as a standing caution, since it is the most transferable lesson here.

### 9. House-style profiles

- [x] `references/house-styles.md` turns the publication measurements into **selectable targets**, which the data in `foundations.md` was not: that holds the same numbers as *evidence for or against our rules*.
- [x] Four profiles (Economist, FT, Reuters, HBR) with sentence-length range, dash and semicolon rates, subhead and bullet policy, headline and standfirst conventions, plus a table for choosing between them.
- [x] `check.py --house economist|ft|reuters|hbr` enforces the measurable parts. Subhead and bullet policy fail; sentence median, dash rate and headline length review. Verified by contrast: our own subheaded article fails as Economist and passes as HBR.
- [x] Two limits stated in the file rather than buried: these give **conventions, not voice**, and every convention exists for a purpose that may not transfer.
- [x] Records the conflict that surfaces immediately: three of four profiles use em dashes and the user's writing contains none, so **the voice preference wins**.

### 10. Management-email guidance

- [x] Answered which house style suits a management email: **none of them whole.** The 125-word / 5-sentence cap implies a 25-word ceiling; Reuters' median is 30. Only HBR's tips format (median 12) matches, and our own fixtures run 10-12.
- [x] `house-styles.md` records a **transfer table** instead of a winner: take the informational 7-14 word subject line from FT/Reuters, the summary bullets and zero-dash punctuation from Reuters, the sentence length from HBR's tips format. Reject every publication's sentence length.
- [x] `formats.md` cross-references it from the email subject-line rule.

### 11. The manual

- [x] `skills/clear-writing/README.md`. Nine sections: mode choice, architecture, the four inputs and how to extend each, a task-to-recipe table with a worked email example, the two halves of enforcement, extension points, design decisions, known limits, provenance.
- [x] Written through the skill and checked with `check.py`, which is what surfaced the last two false positives.

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

`NON_LITERAL` has 54 entries and `ORPHAN_OK` has 114. Each entry is individually justified, but the escape hatch is now big enough that adding to it is easier than fixing the coupling. Nothing distinguishes "genuinely can't be grepped" from "someone didn't want to deal with it."

**Fix:** periodically re-audit the allowlists, or make additions require a reason string that the test prints (NON_LITERAL already does; ORPHAN_OK does not).

### E. `check.py`'s heuristics are approximations

Passive voice and noun-string detection are pattern matches, not parsing. That's why they emit REVIEW rather than FAIL. Acceptable, but it means those two rules are advisory in practice.

**Possible fix:** a real POS tagger would make both precise, at the cost of adding a dependency to a currently stdlib-only script. Probably not worth it.

### F2. Ground rules and multi-device install — DONE

- [x] `CLAUDE.md` at the repo root holds **six always-on rules**, chosen by one test: did this fail in practice, and did it fail silently? No em dashes; jargon tests apply to chat replies; never generalise from one or two samples; report what you ran; invent no specifics; do not infer traits about people from their writing. Each has a named incident behind it.
- [x] Three-layer split documented in `CLAUDE.md` and `README.md`: always-on rules, project conventions, on-demand skill. The always-on layer is deliberately capped at six because it costs context every turn.
- [x] `install.sh` symlinks the skill and `CLAUDE.md` into `~/.claude/`, so `git pull` updates every machine. `--status`, `--force`, `--uninstall`.
- [x] **Refuses to clobber an existing `~/.claude/CLAUDE.md`**, since overwriting it would silently drop rules someone relies on. `--force` backs up first. All four paths tested, including the destructive one.
- [x] The jargon rule now explicitly covers chat replies, in `audiences.md` and as a `CHECKLIST.md` step, with the "dogfooding" failure recorded as the worked example.

### F. Installation location still unverified on your own machines

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

1. **Use the skill on real drafts and grow `examples.md`** (A). Still the only gap that research cannot close.
2. **Add a connected-prose voice sample** (B). Two or three paragraphs you wrote for someone else. Highest value per effort of anything left, because it is the one input that would let paragraph-level voice matching switch from *unsupported* to working.
3. **Run `./install.sh` on each machine you use** (F). It is verified working in this container; whether it is live on your own machines is still unconfirmed from here.
4. **Re-audit the drift allowlists** (D) once they stop growing.
5. **Use a template for a real document** (H), which would test the three that have never produced one.
6. **Pin the 18F quotations** with one literal re-fetch (I).

**Deliberately stopping:** more published prose. Four publications and ~25,000 words settled which rules are house convention and which are real practice. The last three batches found checker bugs rather than changed guidance, which is the signal that this input is exhausted.
