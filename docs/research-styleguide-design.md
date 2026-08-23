# What makes a style guide work: research, and what we changed

Research done 2026-08-23. Two questions: how do working prose style guides get built, and what does the platform that runs this skill say about authoring one.

**Reachability matters here.** The egress proxy blocked `vale.sh`, `docs.vale.sh`, `arxiv.org`, `github.blog` and `contentdesign.london`. Anything below marked *secondary* comes from a search-result summary whose page I could not open, so it is graded the way `house-voices.md` grades its own rules and is not acted on as if measured.

## Contents

- Primary: Vale, the prose linter
- Primary: Microsoft's Vale package, and the coverage manifest
- Primary: Anthropic skill-authoring guidance
- Secondary: agent instruction files
- Audit against the official checklist
- What we changed
- What we did not change, and why

---

## Primary: Vale, the prose linter

Vale is the standard tool for enforcing a prose style guide in CI. Its architecture answers questions we had solved ad hoc.

**Markup awareness is a design goal, not a refinement.** Vale advertises "a rich understanding of many markup formats, allowing it to avoid syntax-related false positives and intelligently exclude code snippets from prose-related rules." That is `under_judgment()`, and it is reassuring that the industry tool treats it as foundational: our twelve false positives were not an unusual mistake.

**Three alert levels: error, warning, suggestion.** We have two, FAIL and REVIEW, collapsing warning and suggestion.

**Google's own passive-voice rule ships at `level: suggestion`**, the weakest of the three. Our passive check is REVIEW. Independent agreement that passive voice is not a hard failure.

**Rules enumerate rather than guess.** Google's `Passive.yml` pairs a `raw` regex for the auxiliary verb with an explicit list of about 180 past participles instead of a `-ed` heuristic. This is exactly the fix the FT and Reuters spelling check needed: a generic `-ised` suffix caught *raised, praised, advised, revised, promised, surprised*, and the repair was to enumerate the 24 stems that actually alternate.

**Every rule carries a `link:` to the guidance that justifies it**, plus a `message` that interpolates the offending token. We had the message. We had no link, so a FAIL named a rule without saying where the rule was written.

## Primary: Microsoft's Vale package, and the coverage manifest

The Microsoft package is one rule per file, named for what it checks, with about 40 files. The important part is what its README publishes:

> Each file mirrors one top-level section of the guide, and each key is a subtopic set to `true` or `false`, optionally followed by a comment naming the rules that implement it.

Coverage is stated as numbers: **37 of 64 general guidelines (57.8%)** and **106 of 849 word-list items (12.5%)**. A style guide with 12.5% of its word list enforced says so, in the repository, as data.

This is the strongest single idea in the research. Our drift test proves the wordlists and the reference files agree, which is a consistency check. It never said what fraction of the documented guidance has a check behind it, so unenforced guidance stayed invisible, which is the exact failure this project exists to fix.

## Primary: Anthropic skill-authoring guidance

From `platform.claude.com/docs/en/agents-and-tools/agent-skills/best-practices` and `code.claude.com/docs/en/skills`. Prescriptions relevant to us:

| Rule | Us |
|---|---|
| SKILL.md under 500 lines | 56 lines. Fine |
| References one level deep from SKILL.md | Already true, verified |
| Reference files over 100 lines get a table of contents | **Was missing on all seven** |
| Descriptions in third person, with what and when | Was imperative |
| No voodoo constants; justify every value (Ousterhout's law) | **Three undocumented divisors** |
| At least three evaluations | **We had none** |
| Test with Haiku, Sonnet and Opus | **Never done** |
| Feedback loop: run validator, fix, repeat | Already the CHECKLIST pattern |

Two facts about the runtime that change how the files should be ordered:

- A skill's body **stays in context across turns** once loaded, so its length is a recurring cost rather than a one-off.
- After compaction, only **the first 5,000 tokens of each invoked skill** are re-attached, with a 25,000-token budget shared across skills. SKILL.md is about 1,100 tokens, so it survives whole. Anything important must stay early in it.

And the methodological point, which is the sharpest thing in the research:

> The check for both is a baseline comparison. Collect a few realistic prompts, run each one in a fresh session with the skill available and again with it disabled, and compare the results. A fresh session matters because leftover context from authoring the skill will mask gaps in the written instructions.

Every test we have ever run on this skill ran inside the authoring session. That is the condition the docs name as the one that hides gaps. The docs also separate **trigger accuracy** from **output quality** and say to measure them apart. We had measured only output quality, and only under the masking condition.

## Secondary: agent instruction files

From search summaries whose sources I could not open. Recorded, not acted on.

- A GitHub study across 2,500+ repositories reportedly found instruction files past 150 lines give diminishing returns and can raise inference cost 20-23% without improving performance.
- A reported finding that LLM-generated instruction files reduced task success in 5 of 8 settings.
- "One real snippet showing your style beats three paragraphs describing it."
- An `always do / ask first / never do` structure for rules.

The first two are single studies I could not read. The third and fourth agree with the primary Anthropic guidance on concrete examples and clear degrees of freedom, so nothing here needed a change of its own.

The `AGENTS.md` convention itself (primary, via its repository) sets no length or precedence rules and is deliberately loose: "a README for agents."

## Audit against the official checklist

Ten of the checklist's items already held. Six did not:

1. No tables of contents in seven reference files over 100 lines.
2. Three tolerance divisors with no justification.
3. No evaluations, in any format.
4. No rule-to-source link, so a FAIL named a check but not the guidance.
5. No coverage manifest.
6. Description written imperatively rather than in third person.

## What we changed

**Tables of contents** in all seven files over 100 lines, listing every section so a partial read still shows the file's scope.

**The three divisors documented.** The dash band is a factor of 2 either side because publication rates were measured over whole articles. The semicolon band is one-sided and looser at 3 because the counts are small: HBR ranges 0 to 12 inside one masthead. The HBR register floor is 3.5, chosen because it puts the floor at exactly 200 words per hit, which is `AI_TELL_WORDS_PER_HIT`: below that the same words stop being register and become slop, so the two checks now agree by construction rather than by coincidence.

**`SOURCES`, Vale's `link:` against local files.** 62 checks mapped to the file and section stating their rule. Every FAIL and REVIEW now prints a `rules behind the flags` footer, and a check with no entry prints `NO SOURCE RECORDED`. `tests/test.sh` runs nine fixtures across every flag combination and fails if any flagged check has no rule behind it. Verified by deleting one entry.

**`check.py --rules`, the coverage manifest.** Prints the 62 checks grouped by the file their rule lives in, then names the judgment-only rules that no check covers.

**`evals/evals.json`, six cases and 34 assertions.** Format per the docs. Each case carries a non-standard `gap` field naming the development failure it comes from, because the docs are firm that evals should target real gaps and this skill was built before its evals existed. Two are the founding failures: the em dash that shipped while its pass was reported as run, and "toward the end of last month" that came back as a specific date. One case, `should-not-trigger-on-a-code-question`, measures trigger accuracy, which we had never tested at all. A test asserts the file stays valid and its inputs exist.

**The description**, now third person, naming the deliverable types and the trigger verbs a user would actually say.

## What we did not change, and why

**No third severity level.** Vale splits warning from suggestion. Ours would be churn across 62 checks for a distinction the CHECKLIST already forces a decision on.

**One rule per file, Vale-style, was rejected.** It suits a package consumed by a tool. This skill is read by a model whose docs warn against deeply nested references and reward one level of depth, so grouping by domain in `references/` is the better fit for the same underlying goal.

**The evals have not been run.** They need a fresh session per case with the skill disabled for the baseline arm, which cannot be produced from inside this one. Running them from the authoring session would reproduce the exact mistake the research identified. Two ways to run them are in `evals/README.md`, and the number that matters is the with-skill against without-skill difference.

**Multi-model testing has not been done.** The checklist asks for Haiku, Sonnet and Opus. Everything here has run on one model.

## Sources

- [Vale](https://github.com/errata-ai/vale), [Google's Vale package](https://github.com/errata-ai/Google), [Microsoft's Vale package](https://github.com/errata-ai/Microsoft), all read from repository source
- [Skill authoring best practices](https://platform.claude.com/docs/en/agents-and-tools/agent-skills/best-practices) and [Skills in Claude Code](https://code.claude.com/docs/en/skills)
- [AGENTS.md](https://github.com/openai/agents.md), read from repository source
- Secondary, pages unreachable: [Vale docs](https://vale.sh/), [GitHub's agents.md study](https://github.blog/ai-and-ml/github-copilot/how-to-write-a-great-agents-md-lessons-from-over-2500-repositories/), [Content Design London](https://contentdesign.london/blog/create-a-great-style-guide-that-people-use)
