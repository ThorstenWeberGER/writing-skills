# Why Your Style Guide Isn't Working

*It isn't a discipline problem. It's a measurement problem: nobody can see the violations, so nobody corrects them.*

## The Silent Rule Everyone Agreed To

Recently I helped build a writing standard for a single reader. It ran
to twenty thousand words, covering where the main point belongs and which words to
avoid, and the reader agreed with all of it. Then I wrote a client note that broke
the standard's first and simplest rule, said the rule had been applied, and missed
the contradiction until someone pointed it out.

The rule banned em dashes, and the draft contained one in its subject line.
Nothing about the standard was ambiguous, nobody disagreed with it, and it often
fails anyway, which makes this a different kind of failure from a compliance problem and
one with a different cause.

## Why Silent Rules Stay Silent

The instinct after a failure like this is to reach for discipline: people know the
rule and are not applying it, so the fix is to remind them, add a review step, or
write the rule more emphatically. Every one of those responses assumes the
violation was visible and tolerated, and in this case it was neither.

Reading a rule and applying it feel identical from the inside, and that is the
whole difficulty. A writer who has just read a list of banned punctuation is
precisely the writer most confident that the punctuation is gone. Reading produced
that confidence, checking would have tested it, and nothing separated the two. So
the question worth asking is not why the rule broke but why nobody could tell.

## What Breaking the Silence Actually Costs

We answered that by writing a script that scans a draft for whatever the standard
bans and prints a verdict: how many failures, on which lines, and which checks
passed. Its first run found two hundred and eighty-seven violations of the em dash rule
across the project, one hundred and sixty-two of them sitting in the eight
documents that state the rule.

The number matters less than its location. These were not careless drafts but the
canonical text of the standard itself, reviewed repeatedly by people who believed
the rule mattered, and twenty thousand words of guidance had produced a document
that could not pass its own first check.

Enforcement then produced a second problem, worth knowing before you start. Our
script could not initially tell a document that uses a banned pattern from one
that merely names it. A table listing forbidden words was flagged for containing
forbidden words. Twelve separate false positives traced back to that one
confusion, and we patched each on its own before recognizing they were a single
bug. A checker that cries wolf tends to get switched off, so this is not a detail.

## Finding the Silent Rules in Your Own Organization

There is a simple diagnostic here and it needs no script: for any standard your
organization has written, ask what would happen if someone violated it today. Not
whether they would be corrected. Whether anyone would know.

If the violation would surface in a review, a report, a failing build or a number
on a dashboard, then the standard is real and the only open question is your
appetite for enforcing it. If it depends on whether a reader happens to notice,
the standard is a preference with a document attached.

Most written standards fail that test, and they fail quietly: the document exists,
compliance is assumed because nobody has reported otherwise, and an absence of
reported violations gets read as evidence of adherence when it is evidence of
nothing at all.

One caution, because this is a single case rather than a study. Our experience
shows a mechanism and not a frequency, which means I can tell you why the failure
is invisible when it happens but not how often it happens. Preserving that
distinction is itself part of the discipline, since turning one instructive case
into a general law is how management writing loses its credibility.

The cheap move is not to build enforcement for every standard you hold but to sort
them into the ones that would surface a violation and the ones that rely on
someone noticing. That list takes an afternoon, and it usually surprises people.
