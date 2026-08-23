# Measuring two newspapers changed four of our writing rules

We tested our writing skill against real published prose and found that four of its rules were house convention dressed up as craft. Thirteen excerpts from The Economist and the Financial Times, about 7,400 words in total, are now the evidence base. Three rules survived unchanged.

## What we got wrong

Our biggest error was prescribing subheadings. The rule said a 400 to 700 word article needs two to four of them. Nine Economist excerpts have none at all, and none were detected in four FT articles either. Structure comes instead from paragraph breaks and ordinal signposting in the prose. We now route on how a piece is read: subheads for scanned writing, prose signposting for narrative.

The sentence length threshold was the second problem. We flagged anything past 25 words for review, which reads as a ceiling. The Economist crosses it in a fifth of its sentences and the FT in roughly half. One report's median sentence is 26 words. The threshold is a prompt to look, not a limit.

We also told writers to minimise abbreviations. Both publications use them freely but gloss every non-obvious one on first mention, then use it bare. Alternative for Germany (afd) and large language models (llms) are typical. Gloss on first use is now the rule.

Finally, our em dash ban claimed too much. The mark appears once per 348 words at The Economist and once per 214 at the FT. It is unremarkable in professional prose. The ban stays, because Thorsten's own writing contains none, but we now call it a voice preference rather than a quality standard.

## What held up

Measurement confirmed three rules rather than correcting them. Opening on something concrete before widening to the general point recurs at every scale, including one piece that starts with the Ostrogoths cutting Rome's aqueducts in 537 before turning to present-day cyber-attacks. Glossing a technical term once and then using it bare is standard. And a single sentence fragment for emphasis is fine, which is what our anti-slop pass already said.

## The method mattered more than any single finding

Every correction came from measuring real text, never from reasoning about it. Purpose-built test fixtures passed while real documents exposed defects, including two bugs in our own checker: markdown bullets counted as dashes, and terms flagged when an article was discussing them rather than using them.

Worth noting one failure of our own. We corrected the headline rule after a single four-word headline broke its range, then had to revert when three more headlines landed inside it. Correcting a sound rule from one sample is the same mistake we make when we generalise from one bad meeting.
