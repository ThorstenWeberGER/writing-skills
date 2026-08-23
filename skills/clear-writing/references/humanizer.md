# Anti-AI-slop pass

The final pass over any draft: strip the tells that make writing read as machine-generated. Applies to Claude's own output and to a user's draft.

Two hard rules while rewriting:

- **Keep every claim.** You may shorten, merge, split, or reorder. You may not lose a fact, number, name, date, quote, or citation.
- **Invent nothing.** If a sentence needs a missing detail, ask for it or write a simpler sentence. You may add a reaction or opinion when the writer's voice calls for one; you may never add a factual claim. (Fiction is exempt.)

## Match the writer's voice

**Read `voice-sample.md` before rewriting.** It holds verbatim samples of the user's own writing plus the patterns extracted from them. If a fresher sample exists in this conversation, that takes precedence — note its sentence length, word choice, paragraph openings, punctuation, and recurring phrases. Match those habits, and don't formalize casual wording or strip deliberate quirks.

Match the rhythm and word choice; never reproduce typos, missing punctuation, or slips. `voice-sample.md` spells out that distinction.

**A sample overrides the style rules below.** If the sample uses em dashes freely, keep them at roughly the sample's rate — the dash rule does not apply as a ban. **For this user the sample settles it the other way: zero em dashes across every quote, so the ban applies and `--dashes-ok` should not be passed.**

Use personality in essays, blog posts, and opinion pieces where it fits the writer. Keep reference, technical, legal, and factual text neutral.

## Content tells

**Inflated importance.** *stands/serves as, is a testament to, plays a vital/crucial/pivotal role, underscores/highlights the importance of, reflects broader, marks a shift, key turning point, evolving landscape, indelible mark, deeply rooted.* Ordinary facts framed as major turning points or proof of legacy.
> The institute was established in 1989, marking a pivotal moment in the evolution of regional statistics.
> → The institute was established in 1989, part of a wider decentralization of administrative functions.

**Shallow -ing tails.** *highlighting…, underscoring…, ensuring…, reflecting…, contributing to…, fostering…, showcasing…* An -ing clause bolted onto a plain fact to make it sound deeper.
> The palette resonates with the region's beauty, symbolizing local landscapes, reflecting a deep connection to the land.
> → The building is painted blue and gold, colors meant to evoke local bluebonnets.

**Sales language.** *boasts, vibrant, rich (figurative), profound, enhancing, showcasing, exemplifies, commitment to, nestled, in the heart of, groundbreaking, cutting-edge, state-of-the-art, best-in-class, world-class, renowned, breathtaking, seamless, robust.* Prose that reads like an ad — most common on products, teams, and organizations.

**Vague sources.** *industry reports, experts argue, observers have noted, some critics say, several sources.* A claim assigned to unnamed authorities. Name the real source if the material provides one; otherwise cut the claim. Never invent a source.

**Stock "challenges and outlook" sections.** *Despite its… faces several challenges, Despite these challenges, Challenges and Legacy, Future Outlook.* A tacked-on closing section that restates vague claims instead of adding facts. Cut it, or replace with the specific known risks.

## Language tells

**Overused AI words.** *actually, additionally, align with, crucial, delve, emphasize, enduring, enhance, foster, garner, highlight (verb), interplay, intricate, key (adj.), landscape (abstract), leverage, pivotal, robust, seamless, showcase, tapestry, testament, underscore, valuable, vibrant.* Individually fine; in clusters, a strong tell.

**Avoiding *is* and *are*.** *serves as, stands as, represents, boasts, features, offers* in place of plain *is/are/has*.
> Gallery 825 serves as the exhibition space and boasts over 3,000 square feet.
> → Gallery 825 is the exhibition space and has 3,000 square feet.

**"Not X but Y" and clipped negatives.** *It's not just X, it's Y. Not only… but… / "no guessing," "no setup needed"* as sentence-ending fragments.
> It's not merely a song, it's a statement. → The heavy beat adds to the aggressive tone.

**Forced groups of three.** Ideas padded into triples to sound complete ("innovation, inspiration, and industry insights"). Two items, or four, are often the honest count. (Note: a deliberate tricolon for rhythm is a real device — the tell is *filler* thirds that add no information.)

**Synonym cycling and repeated openings.** Renaming the same subject every sentence (*the protagonist / the main character / the central figure / the hero*), or several sentences opening on the same subject. Use one name consistently; merge or restructure repeated openings. Don't ban the repeated word — fix the repeated *pattern*.

**False "from X to Y" ranges.** *from the Big Bang to the cosmic web, from birth to dark matter* — where X and Y aren't endpoints of any real range.

## Formatting tells

**Em and en dashes.** Unless the writer's sample uses them, the final draft should contain no `—` or `–` (also check spaced ` - ` and ` -- `). Replace with a period, comma, colon, or parentheses. Search for both marks before returning the draft.

**Over-bolding.** Bolded terms with no reason to be emphasized. Also see `foundations.md` (headings and lists) — one bold lead-in per list item at most, never bolding every other phrase.

**Bold mini-heading lists.** Every bullet opening with a bold label and a colon, where the labels carry no information the sentence doesn't:
> - **User Experience:** The user experience has been significantly improved…
> - **Performance:** Performance has been enhanced through…
>
> → The update improves the interface, speeds up load times, and adds end-to-end encryption.

**Title Case In Headings.** Use sentence case: "Strategic negotiations and global partnerships."

**Decorative emojis** on headings or list items (🚀 **Launch Phase:**). Cut them.

## Chatbot tells

**Assistant scaffolding left in the text.** *I hope this helps, Certainly!, Of course!, You're absolutely right, Would you like…, Want me to…, let me know, here is a…* Delete — the text should stand on its own.

**Knowledge-limit hedges and speculative gap-fill.** *as of my last update, while specific details are limited, based on available information, likely grew up, it is believed that, maintains a low profile.* State what the source doesn't show, or cut the sentence. Never present a guess as fact.

**Over-agreeable openings.** *Great question! You're absolutely right that…* Cut, and answer directly.

**Announcing instead of stating.** *Let's dive in, let's explore, let's break this down, here's what you need to know, without further ado.* Also its casual form ("one thing that bit me hard — pay attention here").
> Let's dive into how caching works. Here's what you need to know.
> → Next.js caches at three layers: request memoization, the data cache, and the router cache.

**A heading restated as its own first sentence.**
> ## Performance
> Speed matters.
> When users hit a slow page, they leave.
>
> → Cut "Speed matters."

## Rhetorical-fakery tells

These are the subtlest and the most worth catching, because each one *looks* like good writing.

**Fake depth.** *the real question is, at its core, in reality, what really matters, fundamentally, the deeper issue, the heart of the matter.* An ordinary point dressed as a hidden truth.

**Formulaic sayings.** *X is the Y of Z, X becomes a trap, the language of, the currency of, the architecture of.* "Symmetry is the language of trust" → "Symmetric layouts feel more predictable to users."

**Forced punchlines.** A row of dramatic fragments, each straining to land. One short sentence for emphasis is fine; four in a row is a tell.
> Then AlphaEvolve arrived. No preference for symmetry. No aesthetic prior. The old rules were gone.
> → AlphaEvolve changed the search because it didn't favor symmetry or human-looking designs.

**Fake-candid openings.** *Honestly?, Look, Here's the thing, Let's be honest, Real talk* — as standalone theatrical pauses before a routine point. (Mid-sentence "honestly" is ordinary speech; the tell is the staged opener.)

**Answering objections nobody raised.** *This isn't really about…, I'm not arguing that…, To be clear…, Don't get me wrong…, Some might say… but.* Cut the unsupported defense; if it contains a real claim, state that claim directly. Keep an objection that the text actually attributes to someone.

**Rejecting fake alternatives.** *A tempting approach would be…, One might be tempted to…, It would be easy to just…* An option no reader would consider, dismissed in a clause and never mentioned again — usually a fossil of an earlier draft. State the real constraint instead. One rejected option can be legitimate in a design doc; several short unrelated rejections are the tell.

**Stale version-talk in docs.** Documentation should describe current behavior. Keep "this replaced the old approach" to changelogs, release notes, and migration guides.

**Empty upbeat endings.** *The future looks bright, exciting times lie ahead, a major step in the right direction.* End on the last concrete fact instead.

## Don't over-correct

Covered elsewhere, not here: **passive voice and hidden actors**, **filler phrases** ("in order to," "due to the fact that"), and **stacked hedging qualifiers** are all handled in `foundations.md` (plain wording) and `DONTS.md`. Don't re-litigate them in this pass.

**Never treat these as evidence on their own:**

- Polished grammar and consistent style — many writers are professionals or edited.
- Dry or bland prose. AI prose has *specific* tells; dryness alone is just dryness.
- Formal vocabulary generally (only the listed overused words count).
- One *however*, *moreover*, or *additionally*. The tell is pile-up.
- Curly quotes — macOS, Word, and Google Docs auto-curl by default.
- Em dashes alone — many journalists use them constantly. Evidence only alongside sales-y rhythm.
- One short sentence for emphasis; deliberate anaphora ("She came. She saw. She conquered.").
- Real scope statements, legal notices, safety warnings, corrections, named objections, and FAQ answers.
- Genuine alternatives weighed in a design doc.
- Missing citations. Most writing is uncited.
- Watched phrases inside quotations, titles, or examples where the phrase is being *discussed* rather than used.

When unsure, look for several tells together. One em dash proves nothing.

**Human details to preserve:** oddly specific facts; mixed feelings and unresolved tension ("this bothers me and I can't say why"); era-bound slang and in-jokes; deliberate first-person choices; uneven sentence rhythm; genuine self-interrupting asides and parentheticals. These carry the writer's voice — keep them unless they damage meaning.

## Before returning the draft

1. **Run a literal character search for `—` and `–`.** Not a mental check — an actual scan of the text. Every hit goes unless a user writing sample in this conversation uses them; verify that sample exists rather than assuming it. This rule is the one most often reported as applied while being violated in the same draft, because dashes read as good punctuation on reread.
2. Ask: **what still sounds AI-generated?** Fix by restating the point naturally, not by patching one flagged phrase.
3. Ask: **did the rewrite add or drop any fact, number, name, date, quote, or citation?** Either is an error.

If a sentence stays awkward after two attempts, rewrite the whole paragraph around its main point.

These three feed the exit checklist in `SKILL.md`, which is what actually gates the response. Reading this file is not the same as having applied it.

## Source

Condensed from [Wikipedia: Signs of AI writing](https://en.wikipedia.org/wiki/Wikipedia:Signs_of_AI_writing) (WikiProject AI Cleanup) via [github.com/blader/humanizer](https://github.com/blader/humanizer) (MIT). Trimmed from the original 35-pattern port: patterns specific to encyclopedia articles (name-dropping publications to prove notability, curly-quote normalization, hyphenated-pair pedantry) were dropped, and patterns duplicating `foundations.md`/`DONTS.md` were cross-referenced rather than restated. Wikipedia's underlying point: "LLMs use statistical algorithms to guess what should come next. The result tends toward the most statistically likely result that applies to the widest variety of cases."

---

**This file is not self-enforcing.** The checks described above are gated by `CHECKLIST.md` — run it, and `check.py`, before returning any draft.
