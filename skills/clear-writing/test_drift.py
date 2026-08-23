#!/usr/bin/env python3
"""Fail if check.py's wordlists drift from the reference files.

check.py transcribes term lists out of the reference markdown. That coupling
is invisible: someone can add a jargon row to DONTS.md and the checker will
silently keep passing drafts that contain it. This test makes the coupling
break loudly instead.

It checks both directions:

  MISSING  — documented in a reference file but absent from check.py.
             The dangerous direction: a rule exists and nothing enforces it.
  ORPHAN   — enforced by check.py but not documented anywhere.
             The checker would flag something no reference file justifies.

Terms that are patterns rather than literal strings ("X is the Y of Z") cannot
be grepped, so they are listed in NON_LITERAL below with a reason. That list is
the honest record of what this test does not cover.

    python3 test_drift.py        # exit 0 = in sync
"""

import re
import sys
from pathlib import Path

import check

HERE = Path(__file__).parent
REFS = HERE / "references"

# Bold labels in humanizer.md whose italic term runs feed check.AI_WORDS.
HUMANIZER_LABELS_TO_AI_WORDS = {
    "Inflated importance",
    "Sales language",
    "Overused AI words",
    "Fake depth",
    "Assistant scaffolding left in the text",
    "Knowledge-limit hedges and speculative gap-fill",
    "Announcing instead of stating",
    "Fake-candid openings",
    "Empty upbeat endings",
    "Self-praising process narration",
    "Answering objections nobody raised",
    "Rejecting fake alternatives",
    "Over-agreeable openings",
    "Vague sources",
}

# Documented but not literally greppable. Each needs a reason.
NON_LITERAL = {
    "x is the y of z": "placeholder pattern",
    "x becomes a trap": "placeholder pattern",
    "the language of": "fragment; matches innocent prose",
    "the currency of": "fragment; matches innocent prose",
    "the architecture of": "fragment; matches innocent prose",
    "it's not just x, it's y": "placeholder pattern",
    "not only": "fragment; too common to flag literally",
    "no guessing": "example of a clipped negative, not a fixed phrase",
    "no setup needed": "example of a clipped negative, not a fixed phrase",
    "from the big bang to the cosmic web": "illustrative example, not a term",
    "from birth to dark matter": "illustrative example, not a term",
    "despite its": "fragment; needs the full construction to judge",
    "despite these challenges": "section-shape tell, caught by review not grep",
    "challenges and legacy": "heading shape, varies too much to grep",
    "future outlook": "heading shape, varies too much to grep",
    "industry reports": "needs context; 'reports' alone is innocent",
    "experts argue": "covered by review, low literal frequency",
    "observers have noted": "covered by review, low literal frequency",
    "some critics say": "covered by review, low literal frequency",
    "several sources": "needs context; often legitimate",
    "highlighting": "-ing tail; flagged by the -ing review, not a wordlist",
    "underscoring": "-ing tail; flagged by the -ing review, not a wordlist",
    "ensuring": "-ing tail; also legitimate in most technical prose",
    "reflecting": "-ing tail; also legitimate",
    "contributing to": "-ing tail; also legitimate",
    "serves as": "in AI_WORDS already as the bare form",
    "stands as": "in AI_WORDS already as the bare form",
    "represents": "too common in legitimate technical prose to flag",
    "features": "too common in legitimate technical prose to flag",
    "offers": "too common in legitimate technical prose to flag",
    "rich": "only a tell in the figurative sense; unresolvable by grep",
    "key": "only a tell as an adjective; unresolvable by grep",
    "profound": "rare enough that the review pass covers it",
    "enhancing": "covered by 'enhance' stem",
    "highlight": "verb sense only; 'highlight' is legitimate as a noun",
    "look": "fake-candid opener only in isolation; unresolvable by grep",
    "honestly": "ordinary mid-sentence; only the staged opener is a tell",
    "to be clear": "legitimate in most uses; the tell needs context",
    "i'm not arguing that": "varies too much in form",
    "this isn't really about": "varies too much in form",
    "some might say": "legitimate when the source is named",
    "one might be tempted": "in AI_WORDS already",
    "it would be easy to just": "in AI_WORDS already",
    "a tempting option": "variant of 'a tempting approach', already present",
    "certainly!": "punctuation-sensitive; covered by the bare stem",
    "of course!": "punctuation-sensitive; covered by the bare stem",
    "as of my last update": "covered by the 'as of my last' prefix",
    "while specific details are limited": "varies too much in form",
    "likely grew up": "biography-specific, out of scope for this skill",
    "in accordance with": "in UNFAMILIAR already",
    "enduring": ("adjective sense only. A real Economist feature uses it as a "
                 "verb (\"enduring punishing opening hours\") and our checker "
                 "flagged it; grep cannot tell the two apart"),
    "rather than simply": ("fragment; matches innocent comparative prose. The tell\n                           is the self-praising frame around it, not these two words"),
    "here is a": "too generic to grep; 'here is a list' is legitimate",
    "some might say but": "varies too much in form to grep",
    "implement": ("on the federal dirty-dozen list, but unavoidable and "
                  "correct in engineering prose; flagging it would be noise"),
}

# audiences.md states the external-client rules as prose with quoted bad
# examples, not as an italic term list, so check.py's CLIENT_* lists are
# variant expansions rather than transcriptions. The extractor cannot read
# them. Instead, RULE_ANCHORS below asserts the underlying rules still exist —
# delete a rule from audiences.md and this test fails.
RULE_ANCHORS = {
    "audiences.md": [
        ("Never give a fix ETA", "external client rule 2 -> CLIENT_ETA"),
        ("next-update time", "external client rule 2 -> CLIENT_ETA"),
        ('not "the inconvenience', "rule 6 -> CLIENT_EMPTY_APOLOGY"),
        ("No vendor-blaming", "rule 5 -> CLIENT_BLAME"),
        ("phrasal verbs with single-word verbs",
         "non-native rule 1 -> PHRASAL_IDIOM"),
        ("Referential, not evaluative", "jargon test 4 -> BUZZWORDS"),
    ],
    "formats.md": [
        ("150-250 words", "summary length -> --summary"),
        ("~125 words", "email length -> --email"),
        ("DECISION, REQUEST, ACTION, INFO, UPDATE",
         "subject tags -> CATEGORY_TAGS"),
    ],
    "foundations.md": [
        ("past 25", "sentence limit -> sentence >25 words check"),
        ("150 words and 3-8 sentences", "paragraph limit -> paragraph check"),
        ("Three nouns stacked", "noun strings -> noun string check"),
    ],
    "humanizer.md": [
        ("no `—` or `–`", "dash rule -> em/en dash check"),
        ("voice-sample.md", "voice matching reads the sample file"),
    ],
}

# check.py entries that legitimately have no reference-file counterpart:
# morphological variants and punctuation forms of documented terms.
ORPHAN_OK = {
    "showcasing", "fostering", "underscores", "utilization", "assistance",
    "synergies", "synergize", "endeavor", "prior to", "subsequent to",
    "with regard to", "in order to", "blew up", "rolled back", "roll out",
    "come up with", "put off", "carry out", "deep dive", "ballpark",
    "on the same page", "hit the ground running", "boil the ocean",
    "feel free to", "value-add", "mission-critical", "paradigm shift",
    "best practice in class", "plays a crucial", "plays a pivotal",
    "plays a vital", "is a testament", "a step in the right direction",
    "let me know if", "would you like me to", "want me to", "great question",
    "you're absolutely right", "based on available information",
    "it is believed that", "maintains a low profile", "here's the thing",
    "let's be honest", "real talk", "don't get me wrong", "to be clear,",
    "a tempting approach", "let's dive in", "let's explore",
    "let's break this down", "here's what you need to know",
    "without further ado", "the future looks bright",
    "exciting times lie ahead", "i hope this helps", "as of my last",
    "the real question is", "at its core", "in reality",
    "what really matters", "the deeper issue", "the heart of the matter",
    "marks a shift", "key turning point", "evolving landscape",
    "indelible mark", "deeply rooted", "figure out", "look into",
    "circle back", "touch base", "reach out", "roll back", "blow up",
    "don't hesitate", "low-hanging fruit", "move the goalposts",
    "commitment to", "in the heart of", "operationalize",
    "strategic alignment", "core competencies", "holistic", "synergy",
    "at this point in time", "due to the fact that",
    # CLIENT_* lists: variant expansions of audiences.md prose rules,
    # coupled via RULE_ANCHORS rather than term extraction
    "we expect this to be resolved", "should be resolved within",
    "we hope to have", "we hope to resolve", "will be fixed within",
    "expect resolution", "resolved shortly", "back up shortly",
    "any inconvenience", "the inconvenience", "inconvenience this may have",
    "sorry for any trouble", "our third-party provider",
    "our third party provider", "an upstream provider", "the vendor's fault",
    "caused by our provider",
    "it is important to note that", "in the event of", "in the amount of",
    "in order that", "addressees", "move the needle", "bandwidth",
    "actionable", "leverage", "utilize", "facilitate",
}


def norm(t):
    t = t.strip().lower()
    t = re.sub(r"\(.*?\)", "", t)          # drop parentheticals
    t = t.replace("…", "").replace("...", "")
    t = t.strip(" .,;:*—-–\"'")
    return re.sub(r"\s+", " ", t)


def split_terms(run):
    """Split an italic term run into candidate terms."""
    out = []
    for piece in re.split(r",|\s/\s", run):
        piece = norm(piece)
        if not piece or len(piece) < 3:
            continue
        # "stands/serves as" -> "stands as", "serves as"
        m = re.match(r"^(\w+)/(\w+)\s+(.*)$", piece)
        if m:
            out += [f"{m.group(1)} {m.group(3)}", f"{m.group(2)} {m.group(3)}"]
            continue
        if "/" in piece:
            out += [norm(p) for p in piece.split("/") if len(norm(p)) >= 3]
            continue
        out.append(piece)
    return out


def documented():
    """Every literal term the reference files ask to be flagged."""
    found = {}

    # humanizer.md: **Label.** *term, term, term*
    text = (REFS / "humanizer.md").read_text(encoding="utf-8")
    for m in re.finditer(r"^\*\*(.+?)\.?\*\*\s+\*(.+?)\*", text, re.M):
        label, run = m.group(1).strip().strip('.'), m.group(2)
        if label in HUMANIZER_LABELS_TO_AI_WORDS:
            for t in split_terms(run):
                found.setdefault(t, "humanizer.md")

    # foundations.md rule 1: italic offender run after "repeat offenders:"
    f = (REFS / "foundations.md").read_text(encoding="utf-8")
    m = re.search(r"repeat offenders:\s*\*(.+?)\*", f)
    if m:
        for t in split_terms(m.group(1)):
            found.setdefault(t, "foundations.md")

    # DONTS.md jargon table, first column
    d = (REFS / "DONTS.md").read_text(encoding="utf-8")
    sec = re.search(r"## Jargon to avoid(.*?)(?=\n## )", d, re.S)
    if sec:
        for line in sec.group(1).splitlines():
            if line.startswith("|") and "---" not in line:
                cell = line.split("|")[1].strip()
                if cell and cell.lower() != "jargon":
                    for t in split_terms(cell):
                        found.setdefault(t, "DONTS.md")

    # audiences.md: the evaluative-buzzword italic run
    a = (REFS / "audiences.md").read_text(encoding="utf-8")
    for m in re.finditer(r"\*(leverage synergies[^*]+)\*", a, re.I):
        for t in split_terms(m.group(1)):
            found.setdefault(t, "audiences.md")

    return found


def enforced():
    lists = (check.UNFAMILIAR + check.AI_WORDS + check.BUZZWORDS
             + check.PHRASAL_IDIOM + check.CLIENT_ETA
             + check.CLIENT_EMPTY_APOLOGY + check.CLIENT_BLAME)
    return {norm(t) for t in lists}


def main():
    docs, enf = documented(), enforced()
    missing, covered = [], 0

    for term, src in sorted(docs.items()):
        if term in NON_LITERAL:
            continue
        if term in enf or any(term in e or e in term for e in enf):
            covered += 1
        else:
            missing.append((term, src))

    doc_terms = set(docs) | set(NON_LITERAL)
    orphans = sorted(
        t for t in enf
        if t not in doc_terms and t not in ORPHAN_OK
        and not any(t in d or d in t for d in doc_terms)
    )

    anchor_fails = []
    for fname, anchors in RULE_ANCHORS.items():
        text = (REFS / fname).read_text(encoding="utf-8")
        for needle, why in anchors:
            if needle not in text:
                anchor_fails.append((fname, needle, why))

    print(f"\nwordlist drift check\n")
    print(f"  documented literal terms : {len(docs) - sum(1 for t in docs if t in NON_LITERAL)}")
    print(f"  declared non-literal     : {len(NON_LITERAL)}")
    print(f"  enforced in check.py     : {len(enf)}")
    print(f"  matched                  : {covered}")

    if missing:
        print(f"\n  MISSING from check.py ({len(missing)}) "
              f"— documented but not enforced:")
        for t, src in missing:
            print(f"    - {t!r}  ({src})")
    if orphans:
        print(f"\n  ORPHAN in check.py ({len(orphans)}) "
              f"— enforced but not documented:")
        for t in orphans:
            print(f"    - {t!r}")

    n_anchors = sum(len(v) for v in RULE_ANCHORS.values())
    print(f"  rule anchors             : "
          f"{n_anchors - len(anchor_fails)}/{n_anchors} present")

    if anchor_fails:
        print(f"\n  BROKEN RULE ANCHOR ({len(anchor_fails)}) "
              f"— check.py enforces a rule its reference file no longer states:")
        for fname, needle, why in anchor_fails:
            print(f"    - {fname}: {needle!r} missing  ({why})")

    if missing or orphans or anchor_fails:
        print("\n  FAIL: wordlists have drifted.")
        print("  Fix by adding the term to check.py, documenting it in a")
        print("  reference file, or declaring it in NON_LITERAL/ORPHAN_OK")
        print("  with a reason.\n")
        return 1

    print("\n  PASS: check.py and the reference files agree.\n")
    return 0


if __name__ == "__main__":
    sys.exit(main())
