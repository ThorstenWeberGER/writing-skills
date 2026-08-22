# Template: installation instructions

**An install page is a how-to guide, not a tutorial.** It serves someone doing work, not someone studying: it forks by platform, doesn't need to run end to end, and shouldn't teach the product. A "getting started" page that teaches is a separate tutorial, and it links to this page rather than inlining it.

Related distinction worth keeping straight: an install guide covers installing the product; a how-to guide covers doing something with it *after* installation. How-to guides link back here instead of repeating install steps.

## Standalone or a README section?

- **Integrated** (a section inside the README) — few dependencies, one or two platforms, under roughly ten steps.
- **Standalone** (its own page, self-contained, carrying its own system requirements) — multiple platforms or editions, real prerequisites, or a troubleshooting section that's outgrowing its slot.

## Skeleton

Full version below; delete aggressively. This is a maximalist enterprise shape — a Python library needs maybe five of these sections.

```markdown
# Installing {product}

{One or two sentences: what you'll have when you're done.}

## Installation types                 ← only if there's more than one path
| Type | Description | Steps |
|---|---|---|
| Linux (apt) | … | [↓](#linux) |
| Docker | … | [↓](#docker) |

## System requirements
Per installation type, if they differ.

## Before you begin
Prerequisites, credentials, access. A table works well:
| Type | Prerequisite | Notes |

## Installation steps
### Step 1 — {one-sentence description of the step}
1.1. …
1.2. …
{Optional: the command, and what its output should look like.}

## Verify the installation
The command that proves it worked, and the output to expect.
Never skip this section.

## Post-installation
Configuration · Upgrading · Downgrading · Uninstalling

## Troubleshooting
Per problem: symptom → cause → solution → who to contact.
Flag anything with security implications explicitly.

## Next steps
Where to go now — usually the tutorial or the how-to index.

## Version history                    ← if versions matter to the reader
```

## Ordering decision you have to make once

Either **system requirements → per-platform install sections**, or **per-platform sections → requirements inside each.** Both are valid; the source guidance deliberately declines to pick. Choose one and stay consistent, because mixing them is what makes install pages feel disorganized.

## Failure modes to design against

- **Prerequisites discovered mid-install.** Everything the reader must have goes before step 1, never inline at step 6.
- **No verification step.** Without "run this, expect that," the reader can't tell success from silent failure. This is the most commonly missing section.
- **Platform variants flattened into one procedure**, with parenthetical asides for each OS. Use the installation-types table and separate sections instead.
- **No uninstall or downgrade path.** People need to back out.
- **Version ambiguity** — instructions that don't say which version they apply to.
- **Security-relevant steps not flagged** (disabling verification, broad permissions, exposing a port).
- **Troubleshooting interleaved with the happy path.** It goes after, never woven through. Once it outgrows a section, it becomes its own document.

## Sources

Skeleton adapted (and substantially trimmed) from [The Good Docs Project installation-guide template](https://gitlab.com/tgdp/templates), a volunteer tech-writing community — its section *ordering* is the reusable part, its completeness is calibrated for enterprise and hardware products. The how-to-guide classification, the platform forking ("if this, then that"), and the "practical usability over completeness" principle come from [Diátaxis](https://diataxis.fr/how-to-guides/). Note: Diátaxis never mentions installation directly — that classification is an inference from its compass (installation informs action and serves work, so: how-to guide), not a citation.
