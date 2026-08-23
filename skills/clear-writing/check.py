#!/usr/bin/env python3
"""Mechanical enforcement for the clear-writing skill.

Runs every check in the skill that a machine can decide. Judgment calls
(is this the strongest point? is the pain point right?) stay in CHECKLIST.md.

    python3 check.py DRAFT.md [--summary] [--email] [--article-half]
                              [--article-full] [--client] [--nonnative]

Exit code 0 = no FAILs. Nonzero = at least one FAIL. REVIEW items never
fail the run; they are things a human has to look at.

Wordlists are transcribed from the reference files. When a rule changes
there, change it here too.
"""

import argparse
import re
from statistics import median as statistics_median
import sys
import unicodedata

# --- wordlists, transcribed from the reference files ----------------------

# foundations.md, plain wording rule 1 ("dirty dozen" + friends)
UNFAMILIAR = [
    "utilize", "utilization", "commence", "promulgate", "assist", "assistance",
    "addressees", "in accordance with", "in order that", "in order to",
    "in the amount of", "in the event of", "facilitate", "endeavor",
    "at this point in time", "due to the fact that", "prior to",
    "subsequent to", "with regard to", "it is important to note that",
]

# humanizer.md, "Overused AI words" + "Sales language" + "Inflated importance"
AI_WORDS = [
    "actually", "additionally", "align with", "crucial", "delve", "emphasize",
    "enhance", "foster", "fostering", "garner", "interplay",
    "intricate", "landscape", "leverage", "pivotal", "robust", "seamless",
    "showcase", "showcasing", "tapestry", "testament", "underscore",
    "underscores", "valuable", "vibrant", "boasts", "exemplifies",
    "commitment to", "nestled", "in the heart of", "groundbreaking",
    "cutting-edge", "state-of-the-art", "best-in-class", "world-class",
    "renowned", "breathtaking", "stands as", "serves as", "is a testament",
    "plays a vital", "plays a crucial", "plays a pivotal", "marks a shift",
    "key turning point", "evolving landscape", "indelible mark",
    "deeply rooted", "reflects broader", "highlights the importance of",
    "underscores the importance of", "honestly?",
    "the real question is", "at its core", "in reality",
    "what really matters", "fundamentally", "the deeper issue",
    "the heart of the matter", "let's dive in", "let's explore",
    "let's break this down", "here's what you need to know",
    "without further ado", "the future looks bright",
    "exciting times lie ahead", "step in the right direction",
    "i hope this helps", "let me know if", "would you like me to",
    "want me to", "great question", "you're absolutely right",
    "as of my last", "based on available information", "it is believed that",
    "maintains a low profile", "here's the thing", "let's be honest",
    "real talk", "don't get me wrong", "to be clear,",
    "a tempting approach", "one might be tempted", "it would be easy to just",
    # self-praising process narration: unfalsifiable claims about one's own
    # diligence, as opposed to a reportable action and its result
    "i made sure", "i was careful", "i deliberately", "note that i checked",
    "what i did here was", "i took care to", "i was deliberate",
]

# audiences.md, "referential vs evaluative" — buzzwords that grade, not name
BUZZWORDS = [
    "synergy", "synergies", "synergize", "holistic", "strategic alignment",
    "move the needle", "circle back", "touch base", "bandwidth",
    "actionable", "value-add", "mission-critical", "paradigm shift",
    "core competencies", "operationalize", "best practice in class",
]

# audiences.md, non-native readers rules 1-2
PHRASAL_IDIOM = [
    "reach out", "figure out", "blow up", "blew up", "roll back", "rolled back",
    "roll out", "come up with", "put off", "carry out", "look into",
    "circle back", "low-hanging fruit", "move the goalposts", "ballpark",
    "touch base", "deep dive", "on the same page", "hit the ground running",
    "boil the ocean", "don't hesitate", "feel free to",
]

# audiences.md, external client rules 2 and 6
CLIENT_ETA = [
    "we expect this to be resolved", "should be resolved within",
    "we hope to have", "we hope to resolve", "will be fixed within",
    "expect resolution", "resolved shortly", "back up shortly",
]
CLIENT_EMPTY_APOLOGY = [
    "any inconvenience", "the inconvenience", "inconvenience this may have",
    "sorry for any trouble",
]
CLIENT_BLAME = [
    "our third-party provider", "our third party provider",
    "an upstream provider", "the vendor's fault", "caused by our provider",
]

IRREGULAR_PARTICIPLES = {
    "been", "done", "gone", "seen", "taken", "given", "known", "shown",
    "written", "driven", "broken", "chosen", "spoken", "found", "made",
    "sent", "built", "kept", "left", "lost", "paid", "said", "told",
    "brought", "caught", "held", "run", "set", "put", "cut", "hit", "read",
}

STOPWORDS = {
    "a", "an", "the", "and", "or", "but", "if", "then", "than", "that",
    "this", "these", "those", "of", "to", "in", "on", "at", "by", "for",
    "with", "from", "as", "is", "are", "was", "were", "be", "been", "being",
    "it", "its", "we", "our", "you", "your", "they", "their", "he", "she",
    "his", "her", "i", "my", "not", "no", "can", "will", "would", "should",
    "may", "might", "must", "do", "does", "did", "has", "have", "had",
    "there", "here", "when", "where", "which", "who", "what", "how", "why",
    "all", "any", "some", "each", "more", "most", "other", "into", "over",
    "after", "before", "during", "up", "down", "out", "off", "so", "because",
    # common verbs, so the noun-string heuristic stops flagging verb phrases
    "dropped", "rose", "fell", "cuts", "cut", "left", "gave", "took", "makes",
    "made", "shows", "showed", "means", "meant", "needs", "needed", "wants",
    "runs", "ran", "goes", "went", "comes", "came", "gets", "got", "keeps",
    "kept", "adds", "added", "uses", "used", "says", "said", "tells", "told",
    "stopped", "started", "began", "moved", "changed", "affects", "affected",
    "processed", "duplicated", "triggered", "confirm", "confirmed", "hold",
    "invoice", "invoiced", "please", "recommend", "approve", "reallocating",
}

# Below this many words per AI-tell hit, the words are clustering rather than
# appearing as ordinary register. HBR sits at 1 per 644-787; slop is far denser.
AI_TELL_WORDS_PER_HIT = 200

# references/house-styles.md — measured conventions per publication.
# (sentence-median low, high, dash words-per-hit or None, subheads, bullets)
HOUSE = {
    "economist": dict(med=(13, 26), dash=348, subheads=False, bullets=False,
                      head=(4, 10), stand=(8, 13)),
    "ft":        dict(med=(22, 27), dash=214, subheads=False, bullets=False,
                      head=(7, 14), stand=None),
    "reuters":   dict(med=(24, 32), dash=None, subheads=True, bullets=True,
                      head=None, stand=None),
    "hbr":       dict(med=(12, 22), dash=157, subheads=True, bullets=False,
                      head=(4, 10), stand=(12, 24)),
}

CATEGORY_TAGS = ("DECISION:", "REQUEST:", "ACTION:", "INFO:", "UPDATE:")


# --- helpers -------------------------------------------------------------

def strip_markup(text):
    """Prose only: drop code fences, headings markers, list markers, emphasis."""
    text = re.sub(r"```.*?```", " ", text, flags=re.S)
    text = re.sub(r"`[^`]*`", " ", text)
    out = []
    for line in text.splitlines():
        # A heading is its own unit. Without terminal punctuation it would
        # merge into the following sentence and inflate that sentence's length.
        m = re.match(r"^\s{0,3}#{1,6}\s+(.*)$", line)
        if m:
            h = m.group(1).rstrip()
            line = h if h.endswith((".", "!", "?", ":")) else h + "."
        # A list item is its own unit. Without this it merges into the next
        # line and inflates that sentence's length.
        b = re.match(r"^\s*([-*+]|\d+\.)\s+(.*)$", line)
        if b:
            it = b.group(2).rstrip()
            line = it if it.endswith((".", "!", "?", ":", ";")) else it + "."
        line = re.sub(r"^\s*>\s?", "", line)
        # A subject line is its own unit too, or it merges into the first
        # body sentence and drags that sentence out of the count.
        if re.match(r"^\s*subject\s*:", line, re.I) and not line.rstrip().endswith(
                (".", "!", "?")):
            line = line.rstrip() + "."
        out.append(line)
    text = "\n".join(out)
    return re.sub(r"\*\*|__|\*|_", "", text)


def scan_text(raw):
    """Prose eligible for wordlist scanning.

    humanizer.md's false-positive rules exclude "watched phrases inside
    quotations, titles, or examples where the phrase is being discussed
    rather than used". Markdown tables and before/after demonstration lines
    are exactly that: a jargon table documenting "utilize -> use" is not a
    draft that uses "utilize". Without this, the checker flags the skill's
    own reference files, and any draft that quotes a term to reject it.
    """
    kept = []
    for line in strip_markup(raw).splitlines():
        s = line.strip()
        if s.startswith("|"):                 # markdown table row
            continue
        if "→" in s or "->" in s:             # weak -> better demonstration
            continue
        # A short double-quoted span is a term being named, not used:
        # 'HBR uses "circle back"' is discussion. humanizer.md excludes
        # "watched phrases inside quotations ... being discussed rather
        # than used". Only spans of 1-6 words, so real quoted prose stays.
        s = re.sub(r'"[^"]{1,60}"',
                   lambda m: "" if len(m.group().split()) <= 6 else m.group(), s)
        kept.append(s)
    return "\n".join(kept)


def paragraphs(text):
    return [p.strip() for p in re.split(r"\n\s*\n", text) if p.strip()]


def sentences(text):
    text = re.sub(r"\b([A-Z])\.", r"\1", text)  # initials
    text = re.sub(r"\b(e\.g|i\.e|etc|vs|Mr|Ms|Dr|No)\.", r"\1", text)
    parts = re.split(r"(?<=[.!?])[\s\n]+", text)
    return [s.strip() for s in parts if s.strip()]


def words(s):
    return re.findall(r"[A-Za-z0-9'%$€£-]+", s)


def headings(text):
    found = []
    for line in text.splitlines():
        m = re.match(r"^\s{0,3}(#{1,6})\s+(.*)", line)
        if m:
            found.append((len(m.group(1)), m.group(2).strip()))
    return found


def find_terms(haystack_lower, terms):
    hits = []
    for t in terms:
        for m in re.finditer(r"(?<![a-z])" + re.escape(t) + r"(?![a-z])",
                             haystack_lower):
            hits.append((t, m.start()))
    return hits


def line_of(text, offset):
    return text.count("\n", 0, offset) + 1


class Report:
    def __init__(self):
        self.rows = []

    def add(self, status, check, detail=""):
        self.rows.append((status, check, detail))

    def fail(self, check, detail=""):
        self.add("FAIL", check, detail)

    def review(self, check, detail=""):
        self.add("REVIEW", check, detail)

    def ok(self, check, detail=""):
        self.add("PASS", check, detail)

    def render(self):
        width = max(len(c) for _, c, _ in self.rows) + 2
        icons = {"FAIL": "FAIL  ", "REVIEW": "REVIEW", "PASS": "pass  "}
        lines = []
        for status, check, detail in self.rows:
            line = f"  {icons[status]}  {check.ljust(width)}{detail}"
            lines.append(line.rstrip())
        fails = sum(1 for s, _, _ in self.rows if s == "FAIL")
        revs = sum(1 for s, _, _ in self.rows if s == "REVIEW")
        lines.append("")
        lines.append(f"  {fails} FAIL, {revs} REVIEW, "
                     f"{len(self.rows) - fails - revs} pass")
        return "\n".join(lines)


# --- checks --------------------------------------------------------------

def run(raw, opts):
    r = Report()
    prose = strip_markup(raw)
    low = scan_text(raw).lower()      # wordlist scans: examples excluded
    raw_low = scan_text(raw).lower()
    sents = sentences(prose)
    paras = paragraphs(prose)
    all_words = words(prose)
    hs = headings(raw)

    # 1. dashes (humanizer.md — the rule that was violated while reported clean)
    dash_hits = [(m.group(), line_of(raw, m.start()))
                 for m in re.finditer(r"[—–]", raw)]
    # require a non-space char before the space, so a line-initial markdown
    # bullet ("\n- item") is not mistaken for a spaced dash
    # Run on markup-stripped text: a blockquoted list item ("> - thing")
    # otherwise reads as a spaced dash, because ">" supplies the preceding
    # non-space character. Same defect class as the bare "- item" case.
    _stripped = strip_markup(raw)
    spaced = [(m.group(1), line_of(_stripped, m.start()))
              for m in re.finditer(r"(?<=\S)[ \t](--?)[ \t]", _stripped)]
    if opts.dashes_ok:
        r.ok("em/en dash", "skipped: --dashes-ok (user sample uses them)")
    elif dash_hits or spaced:
        detail = ", ".join(f"line {ln}" for _, ln in (dash_hits + spaced)[:8])
        r.fail("em/en dash", f"{len(dash_hits) + len(spaced)} found: {detail}")
    else:
        r.ok("em/en dash", "none")

    # 2. emoji (humanizer.md — formatting tells)
    # Unicode category "So" also contains legitimate symbols (degree sign,
    # currency marks, arrows), so match the actual emoji blocks instead. An
    # HBR article was flagged for 7 "emoji" that were all degree signs.
    emoji = [c for c in raw if (
        0x1F300 <= ord(c) <= 0x1FAFF          # pictographs, emoticons, symbols
        or 0x2600 <= ord(c) <= 0x27BF         # misc symbols and dingbats
        or 0x1F000 <= ord(c) <= 0x1F2FF       # mahjong, cards, enclosed
        or ord(c) in (0xFE0F, 0x2B50, 0x2B55) # variation selector, star, circle
    )]
    (r.fail if emoji else r.ok)("decorative emoji",
                                f"{len(emoji)} found" if emoji else "none")

    # 3. sentence length (foundations.md rule 8)
    long_s = [(len(words(s)), s[:55]) for s in sents if len(words(s)) > 25]
    if long_s:
        r.review("sentence >25 words",
                 "; ".join(f'{n}w "{t}..."' for n, t in long_s[:3]))
    else:
        r.ok("sentence >25 words", "none")

    # 4. paragraph length (foundations.md rule 10)
    over250 = [len(words(p)) for p in paras if len(words(p)) > 250]
    over150 = [len(words(p)) for p in paras if 150 < len(words(p)) <= 250]
    if over250:
        r.fail("paragraph >250 words", f"{len(over250)} paragraph(s)")
    elif over150:
        r.review("paragraph >150 words", f"{len(over150)} paragraph(s)")
    else:
        r.ok("paragraph length", "all under 150 words")

    # 5. uniform rhythm (foundations.md rule 10 anti-uniformity)
    lens = [len(words(s)) for s in sents]
    if len(lens) >= 4:
        spread = max(lens) - min(lens)
        if spread <= 4:
            r.review("sentence-length variety",
                     f"all sentences {min(lens)}-{max(lens)} words; vary them")
        else:
            r.ok("sentence-length variety", f"spread {spread} words")

    # 6. passive voice (foundations.md rule 9)
    passives = []
    for s in sents:
        w = words(s)
        for i, tok in enumerate(w[:-1]):
            if tok.lower() in {"is", "are", "was", "were", "be", "been", "being"}:
                nxt = w[i + 1].lower()
                if nxt in {"not", "also", "already", "still", "now"} and i + 2 < len(w):
                    nxt = w[i + 2].lower()
                if (nxt.endswith("ed") and len(nxt) > 4) or nxt in IRREGULAR_PARTICIPLES:
                    passives.append(f"{tok} {nxt}")
    if passives:
        r.review("possible passive voice",
                 f"{len(passives)}: " + ", ".join(sorted(set(passives))[:5]))
    else:
        r.ok("possible passive voice", "none detected")

    # 7. hidden verbs (foundations.md rule 5)
    hidden = re.findall(
        r"\b(?:make|makes|made|take|takes|took|achieve|achieves|effect|give|"
        r"gives|have|has|reach|reaches|conduct|conducts|perform|performs|"
        r"provide|provides)\s+(?:a|an|the)?\s*\w+(?:ment|tion|sion|ance|ancy)\b",
        low)
    if hidden:
        r.review("hidden verb (nominalization)", ", ".join(sorted(set(hidden))[:4]))
    else:
        r.ok("hidden verb (nominalization)", "none detected")

    # 8. noun strings (foundations.md rule 3)
    strings = []
    heading_text = {h for _, h in hs}
    # headings compress deliberately; scanning them produces mostly noise
    for s in (x for x in sents if x not in heading_text):
        # punctuation breaks a noun run, so tokenize on clause boundaries first
        for clause in re.split(r"[^A-Za-z0-9'\- ]+", s):
            run_ = []
            for tok in words(clause):
                if tok.lower() in STOPWORDS or not tok.isalpha():
                    if len(run_) >= 4:
                        strings.append(" ".join(run_))
                    run_ = []
                else:
                    run_.append(tok)
            if len(run_) >= 4:
                strings.append(" ".join(run_))
    if strings:
        r.review("noun string >3", "; ".join(strings[:3]))
    else:
        r.ok("noun string >3", "none detected")

    # 9-12. wordlist scans
    for label, terms, sev in (
        ("unfamiliar/filler word", UNFAMILIAR, "fail"),
        ("evaluative buzzword", BUZZWORDS, "fail"),
    ):
        hits = find_terms(low, terms)
        if hits:
            uniq = sorted({t for t, _ in hits})
            getattr(r, sev)(label, f"{len(hits)}: " + ", ".join(uniq[:6]))
        else:
            r.ok(label, "none")

    # AI-tell words are density-sensitive, which is what humanizer.md already
    # says: "Individually fine; in clusters, a strong tell." Measured against
    # real business prose, HBR features carry these words at 1 per 644-787
    # words as ordinary register. Failing on a single hit would flag a
    # benchmark publication, so only clustering fails.
    hits = find_terms(low, AI_WORDS)
    if not hits:
        r.ok("AI-tell phrase", "none")
    else:
        n = len(all_words) or 1
        per = n / len(hits)
        uniq = ", ".join(sorted({t for t, _ in hits})[:6])
        detail = f"{len(hits)} in {n}w (1 per {round(per)}w): {uniq}"
        (r.fail if per < AI_TELL_WORDS_PER_HIT else r.review)("AI-tell phrase", detail)

    # 12b. virtue by invented contrast (humanizer.md, self-praising narration).
    # A first-person intent verb plus "rather than" in one sentence. Narrow on
    # purpose: bare "rather than" is a legitimate comparative and fires ~50x
    # across this repo, while this shape found only the two real cases.
    vic = re.findall(
        r"\b(?:let me|i(?:'ll| will| made sure| was careful| deliberately|"
        r" took care))\b[^.!?]{0,90}\brather than\b", low)
    if vic:
        r.review("virtue by invented contrast",
                 f"{len(vic)}: delete from 'rather than' on; if only the "
                 f"implication of care is lost, cut it")
    else:
        r.ok("virtue by invented contrast", "none")

    # 13. hedging stack (DONTS.md)
    hedges = find_terms(low, ["perhaps", "possibly", "arguably", "somewhat",
                              "it could be argued", "might possibly",
                              "could potentially", "it seems that"])
    if len(hedges) >= 2:
        r.review("stacked hedging", ", ".join(sorted({t for t, _ in hedges})[:5]))
    else:
        r.ok("stacked hedging", f"{len(hedges)} hedge(s)")

    # 14. title case headings (humanizer.md)
    bad_case = []
    for _, h in hs:
        ws = [w for w in words(h) if w.isalpha()]
        if len(ws) >= 3:
            capped = sum(1 for w in ws[1:] if w[0].isupper() and not w.isupper())
            if capped >= len(ws[1:]) * 0.75:
                bad_case.append(h[:40])
    if bad_case:
        r.fail("Title Case heading", "; ".join(bad_case[:3]))
    else:
        r.ok("Title Case heading", "none")

    # 15. bold-label bullet lists (humanizer.md)
    bold_bullets = re.findall(r"^\s*[-*+]\s+\*\*[^*]+\*\*\s*:", raw, re.M)
    if len(bold_bullets) >= 3:
        r.review("bold mini-heading list", f"{len(bold_bullets)} items")
    else:
        r.ok("bold mini-heading list", f"{len(bold_bullets)} item(s)")

    # 16. FAQ section (foundations.md list rule 10)
    (r.review if re.search(r"^\s*#+.*\bFAQ|frequently asked", raw, re.M | re.I)
     else r.ok)("FAQ section", "present" if re.search(
         r"^\s*#+.*\bFAQ|frequently asked", raw, re.M | re.I) else "none")

    # 17. long bullet lists (foundations.md list rule 7, house convention)
    runs, cur = [], 0
    for line in raw.splitlines():
        if re.match(r"^\s*([-*+]|\d+\.)\s+", line):
            cur += 1
        else:
            if cur:
                runs.append(cur)
            cur = 0
    if cur:
        runs.append(cur)
    big = [n for n in runs if n > 6]
    if big:
        r.review("list >6 items", f"{big} (house convention, overridable)")
    else:
        r.ok("list >6 items", "none")

    # --- conditional: target a measured house style ------------------------
    if opts.house:
        h = HOUSE[opts.house]
        name = opts.house
        med = statistics_median([len(words(x)) for x in sents]) if sents else 0
        lo, hi = h["med"]
        (r.ok if lo <= med <= hi else r.review)(
            f"{name}: sentence median {lo}-{hi}", f"{med:g}")

        n = len(all_words) or 1
        ndash = len(re.findall(r"[—–]", raw))
        if h["dash"] is None:
            (r.ok if ndash == 0 else r.review)(
                f"{name}: no em dashes", "none" if ndash == 0 else f"{ndash} found")
        elif ndash:
            rate = n / ndash
            within = h["dash"] / 2 <= rate <= h["dash"] * 2
            (r.ok if within else r.review)(
                f"{name}: dash rate ~1 per {h['dash']}w", f"1 per {round(rate)}w")
        else:
            r.review(f"{name}: dash rate ~1 per {h['dash']}w",
                     "none used; house style uses them")

        nsub = len([1 for lvl, _ in hs if lvl >= 2])
        if h["subheads"]:
            (r.ok if nsub else r.review)(f"{name}: uses subheads",
                                         f"{nsub} found")
        else:
            (r.ok if not nsub else r.fail)(
                f"{name}: no subheads", "none" if not nsub else f"{nsub} found")

        nb = len(re.findall(r"^\s*[-*+]\s", raw, re.M))
        if h["bullets"]:
            (r.ok if nb else r.review)(f"{name}: uses bullets", f"{nb} found")
        else:
            (r.ok if not nb else r.fail)(
                f"{name}: no bullets", "none" if not nb else f"{nb} found")

        top = [t for lvl, t in hs if lvl == 1]
        if h["head"] and top:
            hw = len(words(top[0])); a, b = h["head"]
            (r.ok if a <= hw <= b else r.review)(
                f"{name}: headline {a}-{b} words", f"{hw} words")

    # --- conditional: style-only, must not have compressed ----------------
    if opts.compare:
        try:
            orig = strip_markup(open(opts.compare, encoding="utf-8").read())
        except OSError as e:
            r.fail("length preserved", f"cannot read original: {e}")
        else:
            o, n = len(words(orig)), len(all_words)
            pct = (n - o) / o * 100 if o else 0.0
            detail = f"{o} -> {n} words ({pct:+.0f}%)"
            if o and pct < -15:
                r.fail("length preserved",
                       detail + " — content was cut, not just reworded")
            elif abs(pct) > 40:
                r.review("length preserved", detail + " — large change")
            else:
                r.ok("length preserved", detail)
            # paragraph count is the other structural tell
            po, pn = len(paragraphs(orig)), len(paras)
            (r.ok if po == pn else r.review)(
                "structure preserved",
                f"{po} -> {pn} paragraphs" +
                ("" if po == pn else " — style-only edits should not merge or split"))

    # --- conditional: management summary (formats.md rule 6) --------------
    if opts.summary:
        n = len(all_words)
        if 150 <= n <= 250:
            r.ok("summary 150-250 words", f"{n} words")
        else:
            r.fail("summary 150-250 words", f"{n} words")

    # --- conditional: email variant (formats.md email rules 1-2) ----------
    if opts.email:
        n = len(all_words)
        (r.ok if n <= 125 else r.fail)("email <=125 words", f"{n} words")
        # formats.md's 5-sentence cap governs prose. Its own summary-block
        # guidance encourages bullets, so counting bullet items as sentences
        # would make the two rules contradict each other.
        bullet_items = {
            re.sub(r"^\s*([-*+]|\d+\.)\s+", "", l).rstrip(" .!?:;").lower()
            for l in raw.splitlines() if re.match(r"^\s*([-*+]|\d+\.)\s+", l)
        }
        def is_subject(x):
            return (x.lower().startswith("subject")
                    or any(x.upper().startswith(t) for t in CATEGORY_TAGS))
        body = [s for s in sents
                if not is_subject(s)
                and s.rstrip(" .!?:;").lower() not in bullet_items]
        (r.ok if len(body) <= 5 else r.fail)("email <=5 sentences",
                                             f"{len(body)} sentences")
        subj = next((l for l in raw.splitlines()
                     if re.search(r"subject\s*:", l, re.I)
                     or (re.match(r"^\s{0,3}#\s+", l)
                         and any(t in l.upper() for t in CATEGORY_TAGS))), None)
        if subj is None:
            r.fail("email subject line", "missing")
        elif any(t in subj.upper() for t in CATEGORY_TAGS):
            r.ok("email subject CATEGORY tag", "present")
        else:
            r.fail("email subject CATEGORY tag",
                   "expected one of " + "/".join(t.rstrip(':') for t in CATEGORY_TAGS))

    # --- conditional: article layout (formats.md short article) -----------
    if opts.article_half or opts.article_full:
        n = len(all_words)
        subs = [h for lvl, h in hs if lvl >= 2]
        top = [h for lvl, h in hs if lvl == 1]
        if top:
            hw = len(words(top[0]))
            (r.ok if 5 <= hw <= 10 else r.review)(
                "headline 5-10 words", f'{hw} words: "{top[0][:45]}"')
        else:
            r.review("headline", "no level-1 heading found")
        if len({lvl for lvl, _ in hs if lvl >= 2}) > 1:
            r.fail("one subheading level", "multiple sub-levels used")
        else:
            r.ok("one subheading level", "ok")
        if opts.article_half:
            (r.ok if 150 <= n <= 300 else r.review)("half page 150-300 words",
                                                    f"{n} words")
            (r.ok if not subs else r.fail)(
                "half page: no subheadings",
                "none" if not subs else f"{len(subs)} found")
        else:
            (r.ok if 400 <= n <= 700 else r.review)("full page 400-700 words",
                                                    f"{n} words")
            (r.ok if 2 <= len(subs) <= 4 else r.review)(
                "full page 2-4 subheadings", f"{len(subs)} found")
            thin = []
            blocks = re.split(r"^\s*#{2,6}\s+.*$", raw, flags=re.M)
            for b in blocks[1:]:
                c = len(words(strip_markup(b)))
                if 0 < c < 40:
                    thin.append(c)
            if thin:
                r.review("section >=40 words", f"thin section(s): {thin}")
            else:
                r.ok("section >=40 words", "ok")

    # --- conditional: client-facing (audiences.md external client) --------
    if opts.client:
        # A client note has its own length budget. audiences.md requires eight
        # things of one (impact, hold instruction, cause, ownership, unknown
        # scope, evidence so far, next update, concrete apology), so it cannot
        # fit the management-summary email caps of 125 words / 5 sentences.
        # Combining --client with --email applies the wrong document's limits.
        n = len(all_words)
        body = [x for x in sents
                if not any(x.upper().startswith(t) for t in CATEGORY_TAGS)]
        (r.ok if n <= 200 else r.review)("client note <=200 words", f"{n} words")
        (r.ok if len(body) <= 12 else r.review)(
            "client note <=12 sentences", f"{len(body)} sentences")
        if opts.email:
            r.review("--client with --email",
                     "email caps are for the management-summary variant, "
                     "not a client note; drop --email")

        eta = find_terms(raw_low, CLIENT_ETA)
        (r.fail if eta else r.ok)(
            "no fix ETA promised",
            ", ".join(sorted({t for t, _ in eta})[:3]) if eta else "none")
        nxt = re.search(r"next update", raw_low)
        (r.ok if nxt else r.fail)("next-update time given",
                                  "present" if nxt else "missing")
        ap = find_terms(raw_low, CLIENT_EMPTY_APOLOGY)
        (r.fail if ap else r.ok)(
            "no empty apology",
            ", ".join(sorted({t for t, _ in ap})[:3]) if ap else "none")
        bl = find_terms(raw_low, CLIENT_BLAME)
        (r.review if bl else r.ok)(
            "no vendor-blaming",
            ", ".join(sorted({t for t, _ in bl})[:3]) if bl else "none")

    # --- conditional: non-native readership (audiences.md) ----------------
    if opts.nonnative:
        ph = find_terms(low, PHRASAL_IDIOM)
        (r.fail if ph else r.ok)(
            "phrasal verb / idiom",
            ", ".join(sorted({t for t, _ in ph})[:6]) if ph else "none")
        tense = re.findall(r"\b(?:had been|would have been|will have been|"
                           r"has been being|had had)\b", low)
        (r.review if tense else r.ok)(
            "complex tense stack",
            ", ".join(sorted(set(tense))[:4]) if tense else "none")

    return r


def main():
    p = argparse.ArgumentParser(add_help=True)
    p.add_argument("file")
    p.add_argument("--summary", action="store_true",
                   help="management summary: enforce 150-250 words")
    p.add_argument("--email", action="store_true",
                   help="email variant: enforce <=125 words, <=5 sentences, subject tag")
    p.add_argument("--article-half", action="store_true")
    p.add_argument("--article-full", action="store_true")
    p.add_argument("--client", action="store_true",
                   help="client-facing: ETA, next-update, apology, blame checks")
    p.add_argument("--nonnative", action="store_true",
                   help="non-native readership: phrasal verbs, idioms, tenses")
    p.add_argument("--dashes-ok", action="store_true",
                   help="user's own writing sample uses em dashes")
    p.add_argument("--house", choices=sorted(HOUSE),
                   help="target a measured publication's conventions "
                        "(see references/house-styles.md)")
    p.add_argument("--compare", metavar="ORIGINAL",
                   help="style-only mode: fail if the draft lost more than "
                        "15%% of the original's words (i.e. it compressed "
                        "when it was only meant to be reworded)")
    opts = p.parse_args()

    try:
        raw = open(opts.file, encoding="utf-8").read()
    except OSError as e:
        print(f"cannot read {opts.file}: {e}", file=sys.stderr)
        return 2

    rep = run(raw, opts)
    print(f"\nclear-writing checks — {opts.file}\n")
    print(rep.render())
    fails = sum(1 for s, _, _ in rep.rows if s == "FAIL")
    print("\n  FAIL = fix before returning. REVIEW = look at it and decide.")
    print("  Judgment checks are not here — run CHECKLIST.md too.\n")
    return 1 if fails else 0


if __name__ == "__main__":
    sys.exit(main())
