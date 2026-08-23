# Audiences: what changes when the reader changes

Deltas only — what differs from `foundations.md`, which still applies underneath. Audience is a separate axis from format: a management summary can go to a CTO or to a client, so read this alongside `formats.md` rather than instead of it.

- **[Decision-maker](#decision-maker)** (manager, exec, budget holder)
- **[Technical peer](#technical-peer)** (PR descriptions, RFCs, design docs, ADRs)
- **[External client](#external-client)** (status updates, incidents, release notes)
- **[Non-native English readers](#non-native-english-readers)** (mixed international teams)
- **[When jargon is the right choice](#when-jargon-is-the-right-choice)** — cross-cutting

---

## Decision-maker

Fully covered by `formats.md` → Management summary. Nothing to add here: BLUF, one ask, triage under constraint, and the paired email variant are the deltas.

---

## Technical peer

The reader has the code. What they don't have is your reasoning — and they'll read this in 18 months with no memory of the discussion.

1. **First line is an imperative-mood sentence that stands alone.** Then a blank line, then the body. It has to make sense to someone skimming version-control history. "Deflake CheckoutTest by injecting a fixed clock," not "Fixing the flaky checkout test." Google's list of real-world failures: *Fix bug. Fix build. Moving code from A to B. Phase 1. Add convenience functions.*
2. **The body explains *why*, not *what*.** The diff already shows what changed. What it can't show is why the change exists — which is what a future reader needs to know whether they may move the fence. "Adds a Redis cache to the pricing lookup" → "Pricing lookup is 80% of p99 latency on checkout. Cached in Redis rather than in-process because three services need the same values."
3. **Write down what you rejected, and the non-goals.** In general writing this reads as padding; here it's load-bearing, because it pre-empts the reviewer's first three objections. "We will use Kafka. Rejected SQS (no replay, and we need to rebuild projections); rejected Postgres LISTEN/NOTIFY (drops messages on reconnect). Non-goal: replacing the batch export path."
4. **State the negative consequences, not just the benefits.** The ADR question is "what becomes easier *or more difficult* because of this?" — "Easier: one artifact to deploy. Harder: we can't roll the schema back independently any more; rollbacks need a forward-fix migration."
5. **Be self-contained. Don't outsource the reasoning to a ticket link.** Link the ticket *and* carry enough context that the description still works when the link rots. "See JIRA-4471" → "JIRA-4471: EU tenants see stale invoice totals for up to 15 min because the read replica lags during nightly reindex."
6. **Use the exact domain term and the exact identifier.** Don't paraphrase into plain English — the precise term is shorter, less ambiguous, and what people will grep for. "Fixed a problem where the same message got handled twice" → "Made `OrderPlaced` handling idempotent (dedupe on `eventId`); at-least-once delivery from SQS was double-charging."
7. **Name the review you want.** "Please check the migration ordering in `002_*`; the rest is a mechanical rename." General writing has no equivalent — it's a request for attention, not information.

---

## External client

Every sentence is a commitment someone may quote back to you. And the reader's question usually isn't "what happened" — it's "what does this mean for me, and when will I hear from you again."

1. **Lead with impact in the customer's terms. Describe symptoms, never internals.** "The order-ingest consumer group is rebalancing repeatedly" → "Some customers cannot submit new orders. Orders already submitted are unaffected."
2. **Never give a fix ETA. Always give a next-update time.** This is the strongest rule in the space, and a real inversion of normal advice: instead of answering the reader's actual question, you substitute a different promise you can keep. "We expect resolution within the hour" → "We don't yet have a restoration estimate. Next update at 12:45 UTC, or sooner if that changes."
3. **Say "we don't know" as a bounded factual statement:** unknown cause + known impact + current action + next checkpoint. "We're looking into it and hope to have news soon" → "We have not identified the cause. Confirmed impact: order submission fails for EU customers since 11:20 UTC. We are rolling back this morning's deploy to test one hypothesis. Next update 12:45 UTC."
4. **Publish before you understand — and don't speculate in the same breath.** Silence creates a vacuum, so the first message goes out within minutes, deliberately incomplete. The incompleteness isn't a flaw to apologize for. What you must not do is fill it with a guess: "This appears to be caused by our hosting provider" is speculation, even when it turns out right.
5. **Own it in the first person. No vendor-blaming, no agentless passive.** A third party may have caused it; to your customer it's still your service. Note this is the *opposite* grammar from an internal blameless postmortem, for the same event. "An error was introduced by an upstream provider" → "We took the reporting API offline for 40 minutes. Our provider's outage triggered it; running without a fallback was our decision, and we're adding one."
6. **Apologize for the concrete impact, not "the inconvenience."** "We apologize for any inconvenience" is technically an apology and entirely empty. "We're sorry. For about 90 minutes you couldn't invoice your own customers, on the last business day of the month."
7. **Don't grade severity on the customer's behalf** ("a minor issue") and **don't state absolutes before you have evidence.** "No customer data was affected" becomes "we have found no evidence that customer data was affected, and that check is ongoing."
8. **For routine updates: decisions-needed at the top, and bad news arrives with a mitigation and a recommendation attached.** Include when you first detected the problem. "Decision needed from you by Thursday: approve reduced scope for phase 1. Status: amber — blocked on API credentials since 4 Aug, costing a week. Mitigation: built against a mock. Recommendation: ship phase 1 without the sync."

**Release notes** (same audience): one plain sentence of *outcome* per entry, ordered by user impact rather than ticket number, internal feature names and issue IDs stripped, and an explicit "no action needed" where true. "[PLAT-8821] Refactored the entitlement resolver to use the v2 claims cache" → "Permission changes now take effect immediately instead of after up to 10 minutes. No action needed."

---

## Non-native English readers

Comprehension cost here is driven by *lexical unpredictability* and *structural ambiguity* — not by sentence length. So these deltas are mostly grammatical. Note that the usual advice to "write in a friendly conversational voice" actively backfires, because figurative language is how conversational tone normally gets made.

1. **Replace phrasal verbs with single-word verbs; never split the ones you keep.** You can't deduce "blow up" or "roll back" from its parts, they're hard to look up, and they vary between English-speaking countries. "Figure out why the job blew up, then roll the change back" → "Determine why the job failed, then revert the change." Where you keep one: "Set up the system," not "Set the system up."
2. **Zero idioms, metaphors, sports/seasonal/cultural references** — including ones that don't feel like idioms. Use words in their primary sense. "Let's circle back on the low-hanging fruit before we move the goalposts" → "Let's discuss the simplest improvements again before we change the target."
3. **Keep the syntactic cues native speakers drop.** Explicit "that" (especially after *assume, ensure, require, specify*), relative pronouns, no stacked nouns. This directly inverts normal tightening advice, which says to delete exactly these words. "Ensure the values the parser returns match the config schema validation rule set" → "Ensure that the values that the parser returns match the rules in the configuration schema."
4. **Present tense, active voice, subject-verb-object, subject and verb near the front, one clause per sentence.** The specific addition here is a ban on complex tense stacks that ordinary English style finds unremarkable. "Had the migration been run before the reindex was triggered, we would not have been seeing these duplicates" → "We ran the migration too late. The reindex started first. That creates the duplicates."
5. **One term per concept, repeated verbatim.** Elegant variation is good style in English and reads as "these are different things" to a second-language reader. Also avoid using one word as both noun and verb nearby: "Update the record. The update job runs hourly. After the next update job, the record shows the new value."
6. **Unstack negation — state the positive condition.** "Don't assume the flag isn't disabled unless nothing else is failing" → "Check the flag. If the flag is off, turn it on. Do this only if all other checks pass."
7. **Disambiguate `-ing` headings, and make modality explicit.** "Filtering options" could mean how to filter, or options for filtering — write "Options for filtering." And "may" collides permission with possibility: prefer *can* (ability), *might* (possibility), *is allowed to* (permission).

### The conflict you will hit constantly

Technical-peer rule 6 (use the exact domain term) and the rules above (simplify the lexicon, add syntactic cues) pull in opposite directions — and anyone writing an RFC for a mixed international engineering team is in both audiences at once.

**They operate on different parts of the sentence.** Keep the domain nouns at full precision (`idempotent`, `at-least-once delivery`, `p99`); simplify everything around them — no phrasal verbs, no metaphors, present tense, explicit "that," one clause per sentence. The failure mode is doing it backwards: plain nouns wrapped in native-speaker idiom, which is the worst of both.

---

## When jargon is the right choice

`foundations.md` says to prefer the familiar word. That rule was never aimed at domain nouns, and the plain-language movement itself is explicit about the carve-out: jargon means *unnecessarily complicated language used to impress rather than inform*. A necessary technical term isn't jargon at all, and special terms can be the clearest way to communicate within an audience that shares them.

The carve-out has a hard limit from the same source: going beyond necessary technical terms into jargon causes misunderstanding or alienation **even when every reader is a specialist**. An expert audience is not a blanket license.

**A term is the right choice when all four hold:**

1. **Shared** — the audience already uses it. Not "could look it up."
2. **Non-substitutable** — the plain paraphrase loses precision or runs longer. `idempotent` beats "safe to run more than once with the same result." If the paraphrase is both shorter and equally exact, the term was decoration.
3. **Canonical** — it's the name in the code, the API, the error message, the log. The reader will search for it, and paraphrasing costs them.
4. **Referential, not evaluative** — it names a thing rather than grading something.

**Test 4 is the one that catches buzzwords, and it's the cheapest to run: does the term name a thing, or grade something?** *Eventual consistency, back-pressure, p99, TLS termination* name things. *Leverage synergies, best-in-class, holistic, robust, seamless, strategic alignment* grade things. Corporate buzzwords aren't failed domain terms — they're adjectives and abstractions posing as nouns, and they fail even with a fully expert audience. A softer fifth test: would you say it out loud to this person? Domain terms survive that; buzzwords rarely do.

**Why defining the term doesn't fully fix it.** Jargon degrades processing *fluency* independently of comprehension: in one study, readers who still understood the text showed more resistance to persuasion, higher risk perception, and lower support. The text merely *feels* hard, and the feeling does the damage. So for a lay or mixed audience, substitution beats glossing. That finding concerns *unshared* vocabulary, though — it says nothing against a term the audience uses daily.

**And note what plain language still governs for experts:** usability research with science, technology, and medical domain experts found that even highly educated readers want succinct, scannable text without unnecessary complexity. Read precisely, that's about sentence architecture, nesting, abstraction, and connective tissue — not about replacing domain nouns. So: **plain language always governs the verbs, transitions, abstractions, and sentence structure. It does not govern the noun that names the referent.**

**Mixed-audience override.** When a document has several audiences — a PR a PM will read, an RFC that reaches the client, a status page — evaluate the four tests against the *least-expert reader who has to act on it*, not the average one. In practice: precise term plus a five-word gloss on first use for a mixed technical audience, full substitution for a customer-facing one.

---

## Sources

**Technical peer.** [Google's engineering practices on CL descriptions](https://google.github.io/eng-practices/review/developer/cl-descriptions.html) (read from repo source) — the imperative first line, the why-not-what rule, self-containment, and the list of real failure examples. [Michael Nygard's ADR template](https://github.com/joelparkerhenderson/architecture-decision-record) — the consequences-include-what-gets-harder rule. [Design Docs at Google](https://www.industrialempathy.com/posts/design-docs-at-google/) — rejected alternatives and non-goals. Rule 6 (exact domain term) and rule 7 (name the review you want) are inferred rather than directly sourced.

**External client.** [Atlassian incident communication](https://www.atlassian.com/incident-management/incident-communication), [Statuspage communication tips](https://support.atlassian.com/statuspage/docs/incident-communication-tips/), [incident.io](https://incident.io/blog/incident-communication-best-practices), [PagerDuty response guide](https://response.pagerduty.com/during/during_an_incident/) — all reached via search summaries, not direct fetch. Rule 7 is inferred from the no-speculation rule rather than stated in a source.

**Non-native readers.** [Google's guidance on writing for a global audience](https://developers.google.com/style/translation) — metaphors, primary-sense usage, present tense, standard word order, terminology consistency. [Kohl, *The Global English Style Guide*](https://www.oreilly.com/library/view/the-global-english/9781599946573/) — syntactic cues, unsplit phrasal verbs, `-ing` heading ambiguity. Rule 6 (unstacked negation) and the modality half of rule 7 are inferred.

**Jargon.** [plainlanguage.gov's avoid-jargon guidance](https://github.com/GSA/plainlanguage.gov/blob/main/_pages/guidelines/words/avoid-jargon.md) (primary text) — the definition and the technical-term carve-out. [Bullock et al. 2019, *Jargon as a barrier to effective science communication*](https://journals.sagepub.com/doi/abs/10.1177/0963662519865687) and [Shulman et al. 2020](https://journals.sagepub.com/doi/10.1177/0261927X20902177) — the processing-fluency finding; note the authors' own caveats (online experiment, non-representative sample, context-stripped messages). [NN/g, *Plain language is for everyone, even experts*](https://www.nngroup.com/articles/plain-language-experts/). The four-test framework is original synthesis over these sources.

Examples throughout are illustrative constructions, not sourced quotations. Real before/after pairs belong in `examples.md`.

---

**This file is not self-enforcing.** The checks described above are gated by `CHECKLIST.md` — run it, and `check.py`, before returning any draft.
