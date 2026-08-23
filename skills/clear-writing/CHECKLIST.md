# Exit checklist

Run this before returning any draft. It exists because reading a reference file is not the same as applying it. In testing, passes were reported as run while their rules were violated in the same draft.

**Two halves:**

- **`check.py` handles everything mechanical.** Run it first. It decides 22+ checks a machine can decide.
- **This file handles the judgment calls.** No script can tell you whether you found the strongest point.

Work top to bottom. If you cannot confirm an item, say so in your response rather than asserting the draft is clean.

---

## Contents

- Step 0: run the mechanical checks
- Step 1: the point (from `foundations.md`)
- Step 2: why this reader cares (from `foundations.md`)
- Step 3: format (from `formats.md`)
- Step 4: audience deltas (from `audiences.md`)
- Step 5: known violations (from `DONTS.md` and `inputs/examples.md`)
- Step 6: final pass (from `humanizer.md`)
- Reporting

*Listed so a partial read still shows the whole scope of this file.*

## Step 0: run the mechanical checks

```bash
python3 check.py DRAFT.md [flags]
```

Flags, set by what you're writing:

| Flag | When |
|---|---|
| `--summary` | management summary (enforces 150-250 words) |
| `--email` | email variant (≤125 words, ≤5 sentences, CATEGORY subject tag) |
| `--article-half` / `--article-full` | short article (headline length, subhead count, thin sections) |
| `--client` | client-facing note. Adds the fix-ETA, next-update, empty-apology and vendor-blaming checks, plus its own budget of ~200 words / 12 sentences. **Do not combine with `--email`.** Those caps belong to the management-summary variant and a client note cannot meet them while satisfying `audiences.md`'s eight rules. |
| `--nonnative` | non-native readership (phrasal verbs, idioms, tense stacks) |
| `--house NAME` | the user asked for a specific outlet's conventions. Sets subhead/bullet policy, sentence-median and dash-rate targets from `house-styles.md`. Its dash target does **not** override the ban below. |
| `--dashes-ok` | **do not use.** `inputs/voice-sample.md` shows zero em dashes across every sample, so the ban applies to this user. Only revisit if a future sample contradicts that. |

Each flagged line is followed by a `rules behind the flags` footer naming the reference file and section behind it. If one reads `NO SOURCE RECORDED`, the check has no rule written down and that is itself a defect. `python3 check.py --rules` prints the full map.

**Every FAIL must be fixed.** REVIEW items need a decision, not necessarily a change: a flagged passive may be one of the two legitimate exceptions, and a long list may genuinely have eight items. Record the decision; don't just move on.

If you have no file to check (the draft is going straight into chat), write it to a scratch file and run it there anyway. Skipping the script is how the em-dash defect shipped.

---

## Step 1: the point (from `foundations.md`)

- [ ] **Is the first sentence the point?** Not background, not method, not "we analyzed." If a reader stops there, do they have it?
- [ ] **Is it the complication, not the situation?** Name what changed, broke, or is at risk. If the opening describes something that has been true for months, it's the situation.
- [ ] **Did the "so what?" test run?** State the point, ask "so what?", answer, ask again. Stop when the answer is something the reader would act on. A point that survives zero rounds isn't strong enough to lead with.
- [ ] **If the source had several findings: were they clustered before ranking?** Three findings tracing to one root cause are one point, not three. Ranking them flat wastes the reader's attention on restatement.
- [ ] **Were candidates ranked by reader impact, not by how much work they took?**
- [ ] **Is everything after the first sentence in descending importance?** A reader must be able to stop after any paragraph and have the most important material so far.
- [ ] **Did you cut paragraphs that only restate or build up to something already said?**

## Step 2: why this reader cares (from `foundations.md`)

- [ ] **Is the audience named specifically?** Not "stakeholders" or "the team". Name finance leadership, the on-call engineer, this client.
- [ ] **Did the three-why chain run for that audience?** "Why does this matter to them?" three times, until you reach the goal they have and the obstacle blocking it.
- [ ] **Is the point framed as something they have a stake in**, rather than stated as a bare fact?
- [ ] **If this goes to more than one audience: did you run the chain separately for each?** The same fact produces different pain points.

## Step 3: format (from `formats.md`)

- [ ] **Right format chosen?** Management summary, short article, or plain prose under `foundations.md` alone.

**If management summary:**
- [ ] First sentence is the conclusion, recommendation, or ask.
- [ ] **One ask.** If several, numbered. Never a second ask buried in a supporting paragraph.
- [ ] Numbers, not adjectives.
- [ ] **If the source said resources can't cover everything: is the triage stated?** Which asks are this cycle, which are deferred, and why. A flat list makes the reader redo triage you already did.
- [ ] **Is genuinely unresolved uncertainty still present?** Compressing away a "this correlation may not be causal" makes the recommendation look better-supported than it is. Cut restatement; never cut an open question that would change the reader's confidence.
- [ ] **Both the full version and the email variant are present, back to back** (unless the user asked for one).

**If short article:**
- [ ] Each subheading marks a genuine topic shift, not a word-count interval.
- [ ] Opening paragraph and closing line are prose, not bullets.
- [ ] Headline front-loads the claim and works as a miniature nut graf.

## Step 4: audience deltas (from `audiences.md`)

- [ ] **Which profile applies?** Technical peer, external client, non-native readers, decision-maker (→ `formats.md`), or none.
- [ ] **Deltas for that profile actually applied**, not just read.
- [ ] **Run the four tests on the chat reply too, not just the draft.** A reply explaining the work is prose written for this reader. "Dogfooding" failed three of four and shipped anyway.
- [ ] **For every technical term, run the four tests:** shared by this audience · non-substitutable without losing precision · canonical (the name in the code, API, logs) · referential not evaluative. A term failing any test gets substituted or glossed.
- [ ] **Mixed audience?** Evaluate those tests against the *least-expert reader who has to act on the text*, not the average one.
- [ ] **Technical + non-native at once?** Keep domain nouns at full precision; simplify everything around them. The failure mode is the inverse: plain nouns wrapped in native-speaker idiom.

**If a house voice was requested (`house-voices.md`):**
- [ ] **Register picked before masthead?** Headline type and standfirst behaviour follow the register, not the publication: news takes an informational headline and a standfirst that states the next fact, a feature takes an allusive headline and a standfirst that turns against it. This holds across both the Economist and the FT, and treating it as a house difference was a recorded error.
- [ ] **Right opening move for that outlet and register?** This is the biggest single tell. Economist news leads BLUF, its Leader states the conventional thesis then turns, its feature opens on a particular. HBR names the wrong diagnosis then corrects it. Reuters packs actor, action, time and cause into sentence one.
- [ ] **Signature device present and earning its place?** A concrete anchor that anchors nothing, a rhetorical question away from the hinge, or an antithesis whose halves say the same thing are all worse than not using the device.
- [ ] **Nothing quoted from the guide appears in the draft.** The verbatim fragments in `house-voices.md` are graded n=1 and are there to show the move, not to be reused. Imitate the move; never the wording.
- [ ] **An `inferred` or `not captured` row was not written as if measured.** If the draft leans on one, say so.

## Step 5: known violations (from `DONTS.md` and `inputs/examples.md`)

- [ ] Scanned against `DONTS.md` (the script covers the term lists; the ten general don'ts need a read).
- [ ] **If a new violation surfaced this conversation and the user confirmed it: appended to `DONTS.md`.**
- [ ] **Nothing invented was added to `inputs/examples.md`.** That file admits only real user-supplied or conversation-captured pairs. An empty slot is the honest state.

## Step 6: final pass (from `humanizer.md`)

- [ ] **Facts audit: was any fact, number, name, date, quote, or citation added or dropped?** Both are errors. **This is the item most likely to catch a real problem.** In testing it caught a vague source reference ("approximately last Tuesday") silently rewritten as a specific date, which had survived two earlier review passes. Check dates and figures against the source explicitly, one at a time.
- [ ] **Dash scan actually run** (script step 0, or a literal character search). The user-sample exemption is *verified*, not assumed.
- [ ] **Voice matched against `inputs/voice-sample.md`** (or a fresher sample in this conversation, which takes precedence) on sentence length, word choice, punctuation habits, em-dash rate. Match rhythm and word choice; never reproduce typos or missing punctuation from a sample.
- [ ] **Paragraph-level voice:** `inputs/voice-sample.md` currently holds only short-form material, so paragraph openings and transitions fall back to `humanizer.md` defaults. Don't claim voice-matched paragraphs until a connected-prose sample exists.
- [ ] **No virtue by invented contrast.** Search for "rather than". For each, delete everything from it onward. If you only lose the implication that you were thoughtful, cut it. Both recorded cases came from chat replies, not documents.
- [ ] **Read the whole thing once more and ask: what still sounds AI-generated?** Fix by restating naturally, not by patching the flagged phrase.
- [ ] **Didn't over-correct.** Polished grammar, one *however*, curly quotes, a single short sentence for emphasis, real scope statements, and genuinely weighed alternatives are all fine. Several tells together are evidence; one is not.

---

## Reporting

State what you ran. "Ran `check.py --summary --client`: 0 FAIL, 1 REVIEW (passive in *are affected*, kept under the actor-irrelevant exception). Judgment steps 1-6 clear." That's a claim someone can audit.

Do not write "applied the clear-writing skill". That phrasing is what let unenforced passes go unnoticed in the first place.
