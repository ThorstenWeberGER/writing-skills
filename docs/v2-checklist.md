# clear-writing skill: status and open items

Last updated 2026-08-23. The skill lives in this repo at `skills/clear-writing/`. Start with the repo-root `README.md`, which is the user-facing manual; this file tracks status and open work.

Run `./skills/clear-writing/tests/test.sh` to verify the whole thing. Currently all green: drift test in sync, 23/23 rule anchors present, 16 fixtures behaving as expected. About 20,000 words of rules (28,900 counting fixtures and scripts); 66 checks in `check.py`.

---

## Done

### 1. Primary sourcing for the plain-language rules

The original blocker stands: economist.com, wsj.com, bloomberg.com and hbr.org all refuse automated fetching or serve teasers only. Rather than wait, the rules were re-derived from primary authorities that publish their own guidance as open-source repositories.

- [x] **GSA/plainlanguage.gov**: the federal plain-language guidelines, from the publisher's own repo. Real primary text.
- [x] **18F/content-guide**: GSA's content guide, source of the only numeric sentence-length guidance found.
- [x] `foundations.md`'s plain-wording and heading/list rules re-derived with per-rule attribution and URLs.
- [x] **Three rules corrected** where the primary text contradicted them: "short words over long" is really about *familiarity*; active voice has two legitimate exceptions; the "3-6 bullets" range has no primary support and is now labeled house convention.
- [x] Sourced rules added that were missing entirely: hidden verbs, noun strings, abbreviations, list lead-in sentences, parallelism with the lead-in, nesting caps, paragraph limits with the anti-uniformity rule, "address the reader as you."

### 2. Audience profiles

- [x] `references/audiences.md`, on a separate axis from format so profiles don't multiply per format.
- [x] Technical peer (Google eng-practices, Nygard ADRs), external client (incident-communication practice), non-native English readers (Google global-audience, Kohl's *Global English Style Guide*). Decision-maker routes to `formats.md`.
- [x] The conflict between the technical-peer and non-native profiles documented and resolved: keep domain nouns precise, simplify everything around them.
- [x] "When jargon is the right choice", four tests. The highest-value single addition, since plainlanguage.gov's own carve-out shows the plain-word rule was never aimed at domain nouns.

### 3. Templates

- [x] `project-readme.md` (standard-readme spec), `installation.md` (Good Docs Project, trimmed), `meeting-notes.md` (Robert's Rules + GitLab + ADR shape).
- [x] `templates/README.md` carries the Diátaxis routing compass.
- [x] `summary.md` deliberately **not** built, because `formats.md` already covers summaries. Heeded Diátaxis's own warning against creating empty template scaffolding.

### 4. humanizer.md trim

- [x] 4,700 → ~1,750 words. It had been 48% of the skill.
- [x] Dropped encyclopedia-specific patterns; cross-referenced rather than duplicated what `foundations.md`/`DONTS.md` already cover; removed vestigial standalone-skill scaffolding; renamed §1-35 to named sections.

### 5. Structural consolidation

- [x] `style-general-writing.md` deleted: 3 of 5 rules duplicated `foundations.md`, and its only example was already in `inputs/examples.md` verbatim.
- [x] `style-management-summary.md` + `article-structure.md` merged into `formats.md`.
- [x] `DONTS.md` and `inputs/examples.md` kept separate on purpose, with the reason recorded in both.

### 6. Enforcement layer

This was the largest piece of work and wasn't in the original checklist. It exists because the skill kept shipping drafts where a pass was *reported* as applied while its rules were violated in the same text.

- [x] **`check.py`**: 22+ mechanical checks, stdlib only, exit 1 on any FAIL. Conditional flags for `--summary`, `--email`, `--article-half/full`, `--client`, `--nonnative`, `--dashes-ok`, `--compare`.
- [x] **`CHECKLIST.md`**: the judgment half, step by step. Requires reporting what was run, not "applied the skill".
- [x] **`tests/test_drift.py`**: fails when `check.py`'s wordlists drift from the reference files, in three directions (MISSING, ORPHAN, BROKEN RULE ANCHOR). Verified it can actually fail by injecting each direction.
- [x] **`tests/test.sh`**: drift test plus 7 fixtures.
- [x] Every reference file ends by stating it is not self-enforcing.

### 7. Style-only mode

- [x] `SKILL.md` picks a mode before anything else. Style-only (the default) runs plain wording + DONTS + humanizer and explicitly does not restructure, compress, reorder, or impose a format.
- [x] `--compare ORIGINAL` enforces the mode's characteristic failure: fails past 15% word loss, flags changed paragraph count. Verified: a real style edit passes at +4%, a compressed rewrite of the same text fails at −59%.

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

- [x] the repo-root `README.md`. Nine sections: mode choice, architecture, the four inputs and how to extend each, a task-to-recipe table with a worked email example, the two halves of enforcement, extension points, design decisions, known limits, provenance.
- [x] Written through the skill and checked with `check.py`, which is what surfaced the last two false positives.

---

### 12. File layout

- [x] The manual moved from inside the skill to the repo root as `README.md`, so it is the first thing the repo shows rather than a file three levels down.
- [x] Grouped into subfolders by how often each file is read: `references/` (on demand), `inputs/` (supplied by you), `templates/`, `tests/`. Only `SKILL.md`, `CHECKLIST.md` and `check.py` stay at the skill's top level.
- [x] `test-fixtures/` became `tests/fixtures/`; `test.sh` and `test_drift.py` moved under `tests/` with the import and fixture paths rewired.
- [x] `backlog.md` moved to `docs/`, leaving the repo root at four files.
- [x] Verified after the move: `tests/test.sh` all green, `install.sh --status` links intact, and `inputs/` plus `tests/` reachable through the installed symlink.

### 13. The dash rule now applies to the skill's own files (DONE)

- [x] Cleared every em and en dash out of the nine prose files, the four templates, the two input files, the fixture README, `docs/v2-checklist.md` and `CLAUDE.md`. 257 of the repo's 287 dash characters removed, each replacement chosen per instance: a period, comma, colon, semicolon or parentheses depending on what the sentence was doing.
- [x] Also cleared them from `check.py`, `tests/test_drift.py` and `tests/test.sh`, whose comments and printed output carried them.
- [x] The remaining 30 characters, across 17 lines, are all deliberate: the two regexes `check.py` scans with, `test_drift.py`'s rule anchor and `strip()` char class, the code-span mentions in `humanizer.md`, `inputs/voice-sample.md`, `CLAUDE.md`, `README.md` and this file, and the four fixtures that exist to be caught (`bad.md`, `naming-vs-using.md`, `deslop-orig.md`, `style-orig.md`). Those name the mark or test for it rather than using it.
- [x] `CLAUDE.md` rule 6 held a real violation, in the always-on file that states the rule. Fixed.
- [x] **Enforced, not just done.** `tests/test.sh` now runs the dash check over every prose file in the skill plus `README.md`, `CLAUDE.md` and this file, and locks the script literal counts at 2/2/1 so a new one fails. Verified by injecting a violation in each direction: both guards fail, exit code 1.

### 14. End-to-end test, 2026-08-23

Ran the skill on fresh material rather than on its own fixtures: a 561-word Q3 analysis into a management summary plus email variant (full mode), a 180-word team message reworded (style-only), and a client note.

- [x] Full mode: summary 220 words, 0 FAIL 2 REVIEW; email 113 words, 4 sentences, 0 FAIL 0 REVIEW. The clustering rule worked as intended: three of the source's four findings shared one root cause and were led with as one point, not ranked flat.
- [x] **The facts audit caught five real defects** the mechanical half could not see: three hedges silently dropped from estimates (*roughly* 18%, *roughly* $60k, *perhaps* four weeks), one claim added that the source never made ("we do not recommend it"), and a timing softened to "recent" where the source said "toward the end of last month". Fixed in the draft. The vague date was **not** converted into a specific one, which is the failure rule 5 exists for.
- [x] **The style-only compression guard caught a real 22% cut** on the first attempt at a wording-only pass. Second attempt: 180 to 159 words, 12%, 3 to 3 paragraphs, pass.
- [x] `--house` on all four profiles behaves as documented: our summary reviews against Reuters for missing subheads and bullets and passes its no-dash target.

**One defect found and fixed:** the `--client` next-update check required the literal words "next update", so a note ending "I will write again by Friday 5 September" failed it. Same shape as the defects in section 8: the check measured a phrase as a proxy for a promise. It now looks for a commitment verb and a time expression in the same sentence, and distinguishes *no follow-up promised* from *a follow-up promised with no time on it*. Two fixtures lock both branches, and a 15th rule anchor ties it to `audiences.md`.

### 15. House-style demo, and two conflicts resolved

Rendered one set of facts as a Reuters wire piece and as an HBR argument, then checked each against its own profile and against a profile it was not written for. The HBR-shaped draft passes as HBR and fails as Economist on subheads, so the profiles do discriminate rather than just print numbers.

**Two conflicts between a house profile and a general rule, both now resolved in `check.py`:**

- **Reuters' bullets against Reuters' sentence median.** The profile prescribes a 3-4 bullet summary block, and its 30-word median was measured on body prose. Measuring the median across a document that follows the bullet convention mixed 8-word bullets with 40-word leads: the same draft measured 14 whole-document and 41 body-only. `prose_sentences()` now excludes list items, headings and subject lines, and the email 5-sentence check reuses it instead of its own duplicate. Both figures now agree.
- **HBR's title-case subheads against the Title Case rule.** Writing correct HBR guaranteed a FAIL the profile itself asked for. A named title-case profile downgrades that check to REVIEW and says which profile did it; with no profile, or a sentence-case one, it still fails.

Locked with `tests/fixtures/house-hbr.md` (0 FAIL as hbr, 1 FAIL bare) and `house-reuters.md` (median inside 24-32 with bullets excluded), plus two rule anchors in `house-styles.md`, bringing the anchor count to 17.

Also fixed two genuine uses of "actionable" in our own files, in `house-styles.md` and `inputs/voice-sample.md`.

### 16. House voices, not just house shapes

`house-styles.md` gave conventions and said so, disclaiming voice. That disclaimer was stronger than the evidence warranted: the recorded observations already held opening moves per register, signature rhetorical devices, register bands, punctuation signatures, attribution formulas and refusals.

- [x] `references/house-voices.md`, 1,940 words. Six components per publication: opening move, signature move, register, punctuation signature, attribution, refusals. Plus a same-fact-four-voices table and an explicit list of what is not enforceable by counting.
- [x] **Every rule carries an evidence grade**, because voice rules invite invention in a way shape rules do not: **measured** (counted across the sample), **recorded** (a verbatim fragment, n=1, imitate the move never the wording), **inferred** (reasoned from a measured fact). Where nothing was captured the row says **not captured** instead of guessing. FT is labelled the thinnest profile of the four.
- [x] Six new voice checks in `check.py`, all driven off the profile dict: semicolon rate, spelling signature, Reuters attribution, Economist lowercase acronyms, HBR register band, HBR antithetical dek, plus allusive-versus-informational headline.
- [x] Wired into `SKILL.md` pass 3, and `CHECKLIST.md` step 4 carries the judgment half: right opening move, signature device earning its place, nothing quoted from the guide reused, no `inferred` row written as if measured.
- [x] 23 rule anchors, up from 17.

**The test that makes it real.** Four fixtures, one per voice, each scored against all four profiles. Every fixture must rank its own profile strictly first on (FAIL, REVIEW). All four do, at 0 FAIL and one REVIEW against their own profile. Verified capable of failing: adding two bullets to the Economist fixture breaks it. A voice guide whose four voices a checker cannot tell apart is decoration, and this is the assertion that would catch that.

**Three defects found by writing the fixtures:**

- **A generic `-ised` suffix is not a UK spelling test.** It caught *raised, praised, advised, revised, promised, surprised*, none of which have a `-ized` form. Replaced with the 24 stems that actually alternate. Verified zero hits on a bait sentence of six false positives and ten hits each on real UK and US lists.
- **A standfirst merged into the first body sentence**, giving the FT fixture a phantom 64-word sentence. Whole-line italics are now terminated as their own unit, like headings and list items.
- **And then excluded from the median**, because display copy is not body prose. Counting it pulled the Economist fixture to 12.5, below its own 13-26 band. All four fixtures now sit inside their own band: 13, 25, 25.5, 17.

### 17. Audited against published guidance on building style guides

Researched how working prose style guides get built, and what the platform running this skill says about authoring one. Full record with sourcing and reachability caveats in `docs/research-styleguide-design.md`.

- [x] **Tables of contents** added to all seven reference files over 100 lines. The authoring docs are explicit: a file over 100 lines needs one, so a partial read still shows the file's scope.
- [x] **The three tolerance divisors documented**, per Ousterhout's law as the docs cite it. The HBR register floor turned out to sit at exactly `AI_TELL_WORDS_PER_HIT`, so the register check and the slop check now agree by construction rather than by accident.
- [x] **`SOURCES`, Vale's `link:` field against local files.** 62 checks mapped to the file and section stating their rule, printed as a `rules behind the flags` footer under every FAIL and REVIEW. A check with no entry prints `NO SOURCE RECORDED`, and `tests/test.sh` fails on it across nine fixtures and every flag combination. Verified by deleting an entry.
- [x] **`check.py --rules`, a coverage manifest**, after Microsoft's Vale package, which publishes its own coverage as 37/64 guidelines and 106/849 word-list items. Ours prints the 62 mapped checks by file, then names the judgment-only rules no check covers.
- [x] **Description rewritten in third person** with the deliverable types and the trigger verbs a user would say.
- [x] Confirmed already compliant: SKILL.md at 56 lines against a 500-line ceiling, references one level deep, the validator-fix-repeat loop, concrete examples, consistent terminology.

**Two independent confirmations worth recording.** Vale advertises excluding code from prose rules as a design goal, so our twelve naming-versus-using false positives were the normal shape of this mistake rather than an unusual one. And Google's own Vale rule ships passive voice at `level: suggestion`, the weakest of three, matching our REVIEW.

### 18. Evals exist, and have not been run

`evals/evals.json`, six cases and 34 assertions, in the format the authoring docs specify. Each carries a `gap` field naming the development failure it targets, because the docs say to build evals against real gaps and this skill was built before its evals existed. Two are the founding failures: the em dash shipped while its pass was reported as run, and "toward the end of last month" returned as a specific date. A test keeps the file valid and its inputs present.

**Why they are not run, and why that matters.** The docs say a baseline comparison needs a fresh session per case, with the skill disabled for one arm, because leftover context from authoring masks gaps in the written instructions. **Every test this project has ever run has run inside the authoring session**, which is precisely that condition. So `tests/test.sh` and `evals/` measure different things and neither substitutes for the other. One case, `should-not-trigger-on-a-code-question`, measures trigger accuracy, which had never been tested at all.

### 19. proselint audit, and the self-check widened to every rule (DONE)

Cloned proselint (BSD) and compared term by term: **148 of ours against 837 of theirs in the overlapping categories, 6 shared.** Not a failure of either list. proselint encodes print-era usage authorities, 30 of its 76 files sourced to Garner, with 2014 dates and no concept of an LLM tell. Ours targets AI prose, buzzwords and structure.

- [x] **The one category that genuinely overlaps is corporate and bureaucratic language, and we held 3 of 55.** 30 terms adopted, each judged rather than bulk-imported: 13 into `UNFAMILIAR` (Garner-sourced commercialese and verbed nouns), 8 into `BUZZWORDS`, 9 into `PHRASAL_IDIOM`.
- [x] **The split is the finding.** proselint puts all 25 corporate-speak terms in one bucket with one verdict. Our four jargon tests split them: `win-win` grades, so it is banned; `elephant in the room` names a real thing, so it gets substituted for this audience. Different lists, different fix. The architecture held on data it was not built from.
- [x] The adoption forced the drift test to learn three new documentation locations. Documented literal terms went 104 to 134, all matched.

**Item K closed, and the self-check widened.** Three proxy defects fixed:

- **Italic term runs are now a naming context.** Two commas is the discriminator, wrapped lines allowed, blank lines not, and lookarounds keep it off `**bold**`. `humanizer.md` went from 104 AI-tell hits to zero, because it lists the tells rather than committing them.
- **Tables are not paragraphs.** A table block has no sentences in it; counting it as one reported 250-word paragraphs in four files.
- **Nor are list blocks.** Consecutive items carry no blank line, so a nine-rule numbered list read as one paragraph. `paragraphs()` now reads block structure from the raw source, because `strip_markup` has already removed the markers it needs.

Three genuine one-line fixes fell out: a quotation trimmed to fit the short-quote context, an example emoji moved into a code span, and one ordinary "actually" removed.

`tests/test.sh` now asserts **0 FAIL on every guidance file and repo doc**, not just no dashes. That was blocked until the three defects above were fixed, and it is the check that would have caught the two hand-found "actionable" uses automatically. Verified by injecting a violation.

## Open

### A. `inputs/examples.md` has only its 5 launch pairs: the one real content gap

Can't be fixed by research. The file admits only real user-supplied or conversation-captured pairs, never invented ones, and that invariant is deliberate. It grows only through use.

**Blocked on:** actual use of the skill on real drafts.

### B. Voice sample exists but covers only short-form writing (PARTLY DONE)

- [x] `inputs/voice-sample.md` created from real material: `backlog.md` plus the user's session instructions, quoted verbatim.
- [x] Patterns extracted and **measured** rather than estimated: 27 sentences, median 6 words, max 16, none longer. Imperative mood dominant, sparse punctuation, "as well" as a habitual closer.
- [x] **The em-dash question is settled empirically:** character scan finds zero `—`/`–` across every quote and across `backlog.md`. The ban applies; `--dashes-ok` should not be passed. `CHECKLIST.md`'s flag table now says so.
- [x] Records the distinction that matters: match rhythm and word choice, never reproduce typos or missing punctuation from a sample.
- [x] Wired into `humanizer.md`, `SKILL.md`, and `CHECKLIST.md`, with a drift-test rule anchor so the wiring can't silently rot.

**Still open:** both sources are short-form and functional: a planning list and a set of instructions. Neither is connected prose written for a reader. So the sample supports word choice, sentence length, punctuation, and the dash decision, but says nothing about how this writer opens a document, builds a paragraph, or handles a transition.

**Needs:** two or three paragraphs of real connected prose the user wrote for someone else: an email to a colleague, a section of a doc, a Slack post. Appended as Source 3, same verbatim treatment. Until then paragraph-level voice matching is explicitly marked unsupported.

### C. CI (DONE)

- [x] `.github/workflows/clear-writing-tests.yml` runs `tests/test.sh` on any push or PR touching the skill, plus manual dispatch. Verified the suite passes when invoked from the repo root the way CI does.

Closed because "only runs when someone remembers" was the same failure mode the enforcement layer exists to fix, one level up.

### D. The drift test's allowlists are large enough to hide drift

`NON_LITERAL` has 54 entries and `ORPHAN_OK` has 114. Each entry is individually justified, but the escape hatch is now big enough that adding to it is easier than fixing the coupling. Nothing distinguishes "genuinely can't be grepped" from "someone didn't want to deal with it."

**Fix:** periodically re-audit the allowlists, or make additions require a reason string that the test prints (NON_LITERAL already does; ORPHAN_OK does not).

### E. `check.py`'s heuristics are approximations

Passive voice and noun-string detection are pattern matches, not parsing. That's why they emit REVIEW rather than FAIL. Acceptable, but it means those two rules are advisory in practice.

**Possible fix:** a real POS tagger would make both precise, at the cost of adding a dependency to a currently stdlib-only script. Probably not worth it.

### F2. Ground rules and multi-device install (DONE)

- [x] `CLAUDE.md` at the repo root holds **six always-on rules**, chosen by one test: did this fail in practice, and did it fail silently? No em dashes; jargon tests apply to chat replies; never generalise from one or two samples; report what you ran; invent no specifics; do not infer traits about people from their writing. Each has a named incident behind it.
- [x] Three-layer split documented in `CLAUDE.md` and `README.md`: always-on rules, project conventions, on-demand skill. The always-on layer is deliberately capped at six because it costs context every turn.
- [x] `install.sh` symlinks the skill and `CLAUDE.md` into `~/.claude/`, so `git pull` updates every machine. `--status`, `--force`, `--uninstall`.
- [x] **Refuses to clobber an existing `~/.claude/CLAUDE.md`**, since overwriting it would silently drop rules someone relies on. `--force` backs up first. All four paths tested, including the destructive one.
- [x] The jargon rule now explicitly covers chat replies, in `audiences.md` and as a `CHECKLIST.md` step, with the "dogfooding" failure recorded as the worked example.

### F. Installation location still unverified on your own machines

`./install.sh` has been run in this container: `--status` reports both the skill and `CLAUDE.md` linked, and the links survive the folder restructure. Whether it is installed on the user's own machines can't be verified from here.

**Needs:** run `./install.sh` once per machine, then `--status` to confirm.

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

### L. Nothing has been measured against a baseline, or on more than one model

Two items from the authoring checklist are open, and both need conditions this session cannot create:

- **Run `evals/` in fresh sessions**, with-skill against without-skill. A case both arms pass is telling you the skill is not what fixed it, and we currently cannot distinguish those cases from real wins. `evals/README.md` gives two ways to run it.
- **Test on Haiku, Sonnet and Opus.** The checklist asks for all three. Everything here has run on one model, and the docs note a skill that suits one may under-instruct a smaller one.

---

## Next steps, in priority order

1. **Use the skill on real drafts and grow `inputs/examples.md`** (A). Still the only gap that research cannot close.
2. **Add a connected-prose voice sample** (B). Two or three paragraphs you wrote for someone else. Highest value per effort of anything left, because it is the one input that would let paragraph-level voice matching switch from *unsupported* to working.
3. **Run `./install.sh` on each machine you use** (F). It is verified working in this container; whether it is live on your own machines is still unconfirmed from here.
4. **Run the evals against a baseline in a fresh session** (L). Until that happens, no claim about this skill's effect is measured, only its internal consistency.
5. **Supply five same-register texts per publication** to turn the five `recorded, n=1` devices and three `not captured` attribution rows into measured habits.
5. **Fix the two proxy defects in K** and widen the self-check to 0 FAIL. This is the one that keeps finding real problems.
6. **Re-audit the drift allowlists** (D) once they stop growing.
5. **Use a template for a real document** (H), which would test the three that have never produced one.
6. **Pin the 18F quotations** with one literal re-fetch (I).

**Deliberately stopping:** more published prose. Four publications and ~25,000 words settled which rules are house convention and which are real practice. The last three batches found checker bugs rather than changed guidance, which is the signal that this input is exhausted.
