# Evaluations

Six cases in `evals.json`, in the format the Anthropic skill-authoring docs specify: `skills`, `query`, `files`, `expected_behavior`. Each also carries a `gap` field, which is not part of the standard format and is here because of a rule the docs are firm about.

## Why each case exists

> Create evaluations BEFORE writing extensive documentation. This ensures your Skill solves real problems rather than documenting imagined ones.

This skill was built the other way round, so these evals were written afterwards. To keep them from being imagined requirements dressed as tests, every case's `gap` field names a failure that actually happened during development and is recorded in `docs/v2-checklist.md`. Nothing here tests a problem we invented.

Two are the founding cases: an em dash shipped in a client note while the pass that bans it was reported as run, and a source reading "toward the end of last month" that came back as a specific date and survived two review passes.

## What they measure

The docs separate two questions, and so do these:

- **Output quality**, five cases. Does the result match what the skill promises when it runs.
- **Trigger accuracy**, one case. `should-not-trigger-on-a-code-question` fails if the skill loads on a request that is not about prose. That is a cost question: a skill's body stays in context across turns once loaded.

## Running them

These need a **fresh session per case**, with the skill available for one run and disabled for the other. From the docs:

> A fresh session matters because leftover context from authoring the skill will mask gaps in the written instructions.

That is why they have not been run yet. Every test in `tests/test.sh` runs inside the authoring session, which is exactly the condition the docs warn masks gaps, so these evals and that suite measure different things and neither substitutes for the other.

Two ways to run them:

1. `/plugin install skill-creator@claude-plugins-official`, then ask Claude to evaluate this skill. It spawns a subagent per case, grades each assertion, and writes `benchmark.json` comparing pass rate, tokens and time with the skill against without it.
2. By hand: open a new session, paste the `query` with the `files` attached, and check the output against each assertion.

**The number that matters is the with-skill against without-skill difference**, not the with-skill pass rate on its own. A case both sides pass is telling you the skill is not what fixed it.

## Assertions are written to be gradeable

Each one is checkable against the output without knowing what the author intended. "Contains zero em dashes and zero en dashes" is gradeable. "Reads well" is not, and is deliberately absent. Where an assertion needs a number it names it, so two graders reach the same verdict.
