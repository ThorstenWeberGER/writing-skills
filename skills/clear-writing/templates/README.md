# Templates

Skeletons for document types with real normative backing. Each is a starting order, not a form to fill in, so delete any section your case doesn't need.

| Template | Use for |
|---|---|
| `project-readme.md` | A software project's README |
| `installation.md` | Install/setup instructions, standalone or as a README section |
| `meeting-notes.md` | Notes that produce decisions and action items |

**Summaries have no template here on purpose.** Management summaries, executive summaries, and status write-ups are fully covered by `references/formats.md`, which has the length targets, the BLUF structure, and the always-paired email variant. A separate template would duplicate it.

## Before picking a template: which kind of document is this?

Most documentation problems come from mixing modes in one document. The [Diátaxis](https://diataxis.fr/) compass routes it in two questions:

| If the content… | …and serves the reader's… | …then it's… |
|---|---|---|
| informs action | acquisition of skill (study) | a **tutorial**: a lesson |
| informs action | application of skill (work) | a **how-to guide**: a recipe |
| informs cognition | application of skill (work) | **reference**: dry description |
| informs cognition | acquisition of skill (study) | **explanation**: the "why" |

The most common and most damaging conflation is tutorial vs. how-to. They differ by whether the reader is *studying* or *working*, **not** by basic vs. advanced. A how-to guide can and often should cover a basic procedure.

Practical consequences:

- **An installation page is a how-to guide**, not a tutorial. It forks by platform ("if this, then that") and doesn't need to be end-to-end. A "getting started" page that *teaches* the product is a separate tutorial, and it should link to the install guide rather than inline it.
- **A README is a deliberate hybrid**: part description, part how-to, part signpost. Diátaxis doesn't model it, and trying to purify it into one mode ruins it.
- **Name how-to guides by the goal**, starting with "How to": "How to integrate performance monitoring" beats "Integrating performance monitoring", which beats the useless "Performance monitoring."
- **Don't create empty mode folders.** Diátaxis is explicit about this: four empty directories waiting to be filled is a worse starting point than unstructured docs that exist.

Sources: [Diátaxis](https://diataxis.fr/) (Daniele Procida), read from its [source repo](https://github.com/evildmp/diataxis-documentation-framework). Adopted by Canonical/Ubuntu, Django, and Cloudflare among others.
