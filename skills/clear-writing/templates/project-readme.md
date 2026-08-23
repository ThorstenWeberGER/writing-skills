# Template: project README

Only five items appear in every source surveyed: **name, one-line description, install, usage, license.** Everything else is project-dependent, so delete what doesn't apply. The ordering below is stable across sources: identity → what and why → who for → prerequisites → install → use → help → contribute → legal.

## Skeleton

```markdown
# {Project name}                      ← must match the repo and package-manager name

{One-sentence description}            ← max 120 chars, no heading, matches the package-manager description

[badges]                              ← optional, no heading

## Table of contents                  ← required only if the README exceeds ~100 lines

## Description
What it does, why it's useful, and how it differs from the alternatives.
Pattern: "With {project} you can {verb} {noun}. Unlike {alternative}, {project} {verb} {noun}."

## Who this is for
"Intended for {target user} who wants to {objective}." Cheap to write, and it
stops readers who are in the wrong place.

## Requirements
Versions, OS constraints, dependencies. Only if constrained.

## Installation
Numbered, explicit steps. Assume the reader is a novice in this ecosystem.
If this outgrows a section, split it out: see `installation.md`.

## Usage
Examples liberally, and show expected output. An example with no output
leaves the reader unsure whether it worked.

## Support
Where to ask questions, and where to report bugs.

## Contributing
Whether PRs are accepted at all. How to run tests and linters.

## Project status
Say so if the project is unmaintained or a successor exists. Silence here
wastes a reader's afternoon.

## License
Always last. Full name or SPDX identifier, plus the copyright owner.
```

## Rules with real numbers

- **Description: 120 characters max**, and it must match what the package manager shows.
- **Table of contents: required above ~100 lines**, optional below. If present, it links every section after itself.
- **License is the last section.** Not negotiable in the spec.
- **GitHub truncates rendered content past 500 KiB.** A README approaching that is the wrong container.
- **README resolution order on GitHub:** `.github/` → repo root → `docs/`.

## The main failure mode

**A README is not a substitute for documentation.** GitHub's guidance is that a README carries only what's needed to get started and contribute, with longer material in a wiki or docs site. Google's internal convention goes further: a package README can legitimately be little more than a signpost: purpose, contact, status, usage, links.

That said, the makeareadme.com guidance takes the opposite side on length and is worth knowing: *too long is better than too short*. If a README feels too long, move material into other documentation rather than deleting it.

Other warned-against failures: title or description drifting out of sync with the package registry; an install section that assumes ecosystem fluency; no statement of whether contributions are accepted; usage examples with no expected output.

## Sources

[standard-readme spec](https://github.com/RichardLitt/standard-readme/blob/main/spec.md), the only actual spec, and the source of every hard number above. [Make a README](https://www.makeareadme.com/) ([repo](https://github.com/dguo/make-a-readme)), the most-cited informal convention, and the source of the length counter-argument. [The Good Docs Project README template](https://gitlab.com/tgdp/templates), source of the "who this is for" section and the fill-in-the-blank description patterns. [Google's engineering doc guide](https://google.github.io/styleguide/docguide/READMEs.html), the internal-monorepo signpost convention. GitHub's own README guidance was reachable only via search snippets; its five questions (what, why, how to start, where to get help, who maintains) and the 500 KiB limit are reported from those.
