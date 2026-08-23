# How to derive a style guide that works

Written from building one: roughly 29,000 words, 62 mechanical checks, 23 rule anchors, six evals, and every defect below found the hard way. Research sourcing is in `research-styleguide-design.md`.

## Contents

- The one test that decides everything
- The order to build in
- Where rules come from, and how to label them
- Deriving rules from sample texts
- How to structure the files
- Designing the enforcement
- The failure modes, as a checklist

---

## The one test that decides everything

**For every rule you write, ask what would happen if someone violated it today. Not whether they would be corrected. Whether anyone would know.**

If the answer is "it depends on whether a reader notices", the rule is a preference with a document attached. Rules that fail this test do not degrade slowly. They fail silently and completely, and the absence of reported violations reads as compliance when it is evidence of nothing.

This project banned em dashes across 20,000 words and then shipped 287 of them, 162 inside the documents stating the ban. Nobody disagreed with the rule. Nothing was ambiguous. It failed anyway, because reading a rule and applying it feel identical from the inside.

So the useful split is not good rules against bad rules. It is rules a machine can decide against rules a person must judge, and both need to be written differently.

## The order to build in

We built it backwards and paid for it. The right order:

1. **Run the task without a guide.** Note what actually goes wrong. Not what might.
2. **Write the evals first**, three or more, one per observed failure. Format: the request, the input files, and a list of assertions gradeable from the output alone.
3. **Measure the baseline.** Same prompts, no guide. In a **fresh session**, because context from writing the guide hides the gaps in it.
4. **Write the minimum that passes.** Not the complete theory of good writing.
5. **Add enforcement for whatever a machine can decide.**
6. **Re-measure against the baseline.** A case that passes both with and without the guide is telling you the guide is not what fixed it.

Step 3 is the one everyone skips, including us. Every test we ran lived inside the session that wrote the skill, so what we proved was internal consistency, never effect.

## Where rules come from, and how to label them

Three tiers, and conflating them is how a style guide turns into superstition.

| Tier | Source | How to write it |
|---|---|---|
| **Primary text** | The publisher's own guidance, read from source | State it plainly. Cite the file or section |
| **Measured** | Counted across samples you hold | Give the number and the sample size |
| **House preference** | You just prefer it | **Say so in the rule itself** |

Our em-dash ban is tier three, and the file says so: professional prose runs from zero at Reuters to one per 157 words at HBR. A reader who knows it is a preference can override it for outward-facing work. A reader who thinks it is a quality standard cannot.

Getting this wrong in the other direction is worse. We had a descriptive claim, an AI-slop word list, that was really a preference, and it failed a benchmark publication on a single hit. Two fixes came from that: make density-aware checks fail on clustering rather than presence, and label prescriptive lists as prescriptive.

## Deriving rules from sample texts

The part with the sharpest lessons, because sample-derived rules feel measured whether or not they are.

**Never generalise from two samples.** Three times in this project a finding held across two sources and broke on the third: zero-subheadings broke on Reuters, a headline length range was overturned by one outlier and then vindicated by four more, and a slop word list broke on ordinary management register. Two samples is an anecdote with a number attached.

**Sample by register, not by publication.** Format outranks masthead, measurably. One publication's tips list runs a 12-word median sentence against 19-22 in its own features, same editors. Five features tell you something. Five random pieces tell you the average of several different things.

**Separate the metrics from the devices, because only one of them is generative.**

- *Metrics* (sentence median, dash rate, subhead policy) constrain. They stabilise fast, and after about five same-register samples more data barely moves them.
- *Devices* (how sentence one opens, the signature rhetorical move, how a claim gets attributed, what the outlet refuses to do) generate. They are what a writer can actually deploy on new material.

Metrics are easy to measure and nearly useless on their own: matching a 30-word median gets you a memo with long sentences, not a wire report. Devices are what make imitation recognisable, and they are the ones a small sample leaves at n=1.

**So grade every rule by its evidence, in the rule:**

| Grade | Means | Use |
|---|---|---|
| **measured** | counted across the sample | Follow it. Enforceable |
| **recorded** | one verbatim instance | Imitate the move, never the wording |
| **inferred** | reasoned from a measured fact | Weakest. Say so if a draft leans on it |
| **not captured** | nothing in the sample | Say this rather than guessing |

The grades are not decoration. They are what stops the next writer from treating one clever sentence as a house habit.

**Keep the samples out of the repository.** Measurements, plus quotations under 15 words, attributed. And extraction quality caps everything downstream: our thinnest profile is thin only because it came from print-to-PDF files with no text layer, so captions interleaved with body prose and every sentence figure became an upper bound.

**Never infer things about the writer.** A sample supports claims about writing: sentence length, punctuation, word choice, mood. It does not support claims about nationality, first language, seniority or state of mind. One German abbreviation once got recorded as confirming a first language, which is a conclusion one token cannot carry.

## How to structure the files

For a guide an agent reads, the platform constraints are specific and worth obeying:

- **Entry point under 500 lines.** It stays in context across turns once loaded, so length is a recurring cost.
- **One level of references.** A file referenced from a referenced file gets partially read.
- **A table of contents in anything over 100 lines**, so a partial read still shows the whole scope.
- **Group by domain**, so a request about one thing does not load four.
- **The description is the trigger.** Third person, what it does and when to use it, in the words a user would actually say.

Split the content three ways, by how often it is read: always-on rules that fail silently, the entry point and its exit gate, and reference detail loaded on demand. Our always-on layer is capped at six rules because everything there costs context on every turn, writing or not.

## Designing the enforcement

**Two halves, and be honest about the line.** A script decides the mechanical rules. A checklist carries the ones no script can: is this the strongest point, was any fact added or dropped, does this term pass the jargon tests for this reader. Ours is 62 mechanical checks and seven judgment steps, and the judgment step that catches the most real problems is the facts audit.

**The proxy trap is the defect you will hit repeatedly.** Every serious bug in our checker was one check measuring a proxy for what it cared about:

| It measured | It cared about |
|---|---|
| a literal phrase, "next update" | whether a next-update time was promised |
| word loss | content loss |
| any single hit | clustering |
| table rows as sentences | prose sentences |
| text naming a pattern | text committing it |

The last one alone caused twelve false positives, each patched separately before anyone noticed they were one bug. When you write a check, name the thing it actually measures and the thing you meant, side by side. If they differ, that is your next bug.

**Enumerate, do not guess at morphology.** A generic `-ised` suffix caught *raised, praised, advised, revised, promised, surprised*. The fix was listing the 24 stems that actually alternate. The industry tool does the same thing: its passive-voice rule ships about 180 explicit participles rather than an `-ed` heuristic.

**A checker that cries wolf gets switched off**, so report exclusions rather than applying them silently, and give a flag that disables them.

**Every finding must name the rule behind it.** A failure that says only `Title Case heading` sends the reader hunting. One that says `foundations.md: Headings and lists` does not. Mapping checks to rules also produces a coverage number, which is the only honest answer to "how much of this guide is actually enforced".

**Test that the guide discriminates.** If it defines four voices, write one sample per voice, score each against all four, and require every sample to fit its own best. A guide whose categories a checker cannot tell apart is decoration. Then break one sample on purpose and confirm the test fails.

**Report what you ran, not that you applied something.** "0 FAIL, 1 REVIEW, passive kept under the actor-irrelevant exception" is auditable. "Applied the style guide" is the phrasing that let unenforced passes go unnoticed in the first place.

## The failure modes, as a checklist

Every one of these actually happened here.

- [ ] A rule is described somewhere and enforced nowhere
- [ ] The guide violates its own rules, in the file stating them
- [ ] A finding generalises from two samples
- [ ] A house preference is written as a quality standard, or the reverse
- [ ] A check measures a proxy for the thing it cares about
- [ ] A check fires on text that names a pattern rather than using it
- [ ] A morphological heuristic stands in for an enumerated list
- [ ] A tolerance constant has no justification
- [ ] A finding cannot be traced to a written rule
- [ ] An n=1 instance is written as a habit
- [ ] A trait is inferred about a person from their writing
- [ ] A specific appears that was not in the source
- [ ] A hedge in the source is hardened in the output
- [ ] The guide has never been measured against not having it
