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
    # Commercialese and verbed-noun jargon, adopted from proselint's
    # Garner-sourced lists (BSD). Dead business-letter formulas, and nouns
    # made into verbs. "in regard to" is the variant we had missed.
    "in regard to", "acknowledging yours of", "beg to advise",
    "enclosed herewith", "enclosed please find", "further to your letter",
    "further to yours of", "agendize", "disincentivize",
    "in the affirmative", "in the negative", "per your order",
    "per your request",
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

# audiences.md, "referential vs evaluative": buzzwords that grade, not name
BUZZWORDS = [
    "synergy", "synergies", "synergize", "holistic", "strategic alignment",
    "move the needle", "circle back", "touch base", "bandwidth",
    "actionable", "value-add", "mission-critical", "paradigm shift",
    "core competencies", "operationalize", "best practice in class",
    # From proselint's corporate-speak list (BSD). Its source is a business
    # column rather than a usage authority, so each was judged against jargon
    # test 4, does the term name a thing or grade one. These grade.
    "at the end of the day", "no brainer", "win-win", "think outside the box",
    "bang for your buck", "par for the course", "apples to apples",
    "drill-down",
]

# audiences.md, non-native readers rules 1-2
PHRASAL_IDIOM = [
    "reach out", "figure out", "blow up", "blew up", "roll back", "rolled back",
    "roll out", "come up with", "put off", "carry out", "look into",
    "circle back", "low-hanging fruit", "move the goalposts", "ballpark",
    "touch base", "deep dive", "on the same page", "hit the ground running",
    "boil the ocean", "don't hesitate", "feel free to",
    # Same proselint list, opposite verdict: these name real things and fail
    # only the shared-vocabulary test, so they belong here, not in BUZZWORDS.
    "all hands on deck", "back to the drawing board", "get the ball rolling",
    "take this offline", "thrown under the bus", "on my plate", "ping me",
    "elephant in the room", "on my radar",
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

# audiences.md rule 2: "Never give a fix ETA. Always give a next-update time."
# The commitment and the time are checked separately, because a promise with no
# time on it ("we will update you shortly") is the failure the rule names.
NEXT_UPDATE_COMMIT = re.compile(
    r"\b(next\s+(?:update|checkpoint)"
    r"|(?:i|we)\s*(?:will|'ll|shall)\s+(?:write|update|email|contact|report"
    r"|be\s+in\s+touch|follow\s+up|come\s+back|let\s+you\s+know)"
    r"|updates?\s+(?:you|again)"
    r"|further\s+update)", re.I)
NEXT_UPDATE_TIME = re.compile(
    r"(\{[^}]{1,30}\}|<[^>]{1,30}>"                      # template placeholder
    r"|\b\d{1,2}:\d{2}"                                  # 12:45
    r"|\b\d{1,2}\s*[ap]\.?m\.?"                         # 5pm
    r"|\b(?:mon|tues|wednes|thurs|fri|satur|sun)day"
    r"|\b(?:jan|feb|mar|apr|may|jun|jul|aug|sep|oct|nov|dec)[a-z]*\s+\d{1,2}"
    r"|\b\d{1,2}\s+(?:jan|feb|mar|apr|may|jun|jul|aug|sep|oct|nov|dec)[a-z]*"
    r"|\bwithin\s+\S+\s+(?:minute|hour|day|week)s?"
    r"|\b(?:end\s+of\s+)?(?:today|tomorrow|this\s+afternoon|this\s+evening)"
    r"|\bby\s+(?:the\s+)?(?:end\s+of\s+)?\S+\s+(?:morning|afternoon|week)"
    r")", re.I)

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

# references/house-styles.md holds the measured conventions per publication.
# (sentence-median low, high, dash words-per-hit or None, subheads, bullets)
HOUSE = {
    # Re-measured over six full articles, 5,286 words, 269 sentences. The
    # subhead policy was wrong: it was derived from excerpts, and full articles
    # carry allusive crossheads.
    "economist": dict(med=(16, 23), dash=348, subheads="optional", bullets=False,
                      head=(4, 10), stand=(8, 13),
                      semis=400, spelling="uk", headline="allusive",
                      lc_acronyms=True,
                      crosshead=(2, 5), stand_turn="turn", short_opener=True),
    # Re-measured on clean text: four news pieces (2,355 words) and one long
    # read (1,717). The dash rate was badly inflated by the old PDF extraction;
    # the ~50% over-25-words figure survived. Values here are the news register.
    "ft":        dict(med=(23, 28), dash=430, subheads=False, bullets=False,
                      head=(7, 14), stand=None,
                      semis=1700, spelling="uk", headline="informational",
                      stand_turn="state", attribution=(30, 70),
                      percent_spelled=True),
    # Four held-out articles later confirmed most of this. The crosshead range
    # was too narrow and the median floor too high for an interview.
    "reuters":   dict(med=(21, 33), dash=None, subheads=True, bullets=True,
                      head=None, stand=None,
                      semis=None, spelling="us", attribution=True,
                      crosshead=(2, 9), quote_first=True),
    # Re-measured over the same five articles with per-font ToUnicode decoding,
    # which recovers 20,588 body words against 14,557 on the first pass. Four
    # figures moved; the dash rate held.
    "hbr":       dict(med=(11, 21), dash=174, subheads=True, bullets=False,
                      titlecase=True,
                      head=(4, 10), stand=(12, 24),
                      semis=288, spelling="us", headline="allusive",
                      register=1200, dek="correction",
                      hedge=(130, 200), subhead_term=0.5),
}

# house-voices.md, Economist: acronyms glossed once then used bare and lowercase.
GLOSSED_ACRONYM = re.compile(r"\((?:the\s+)?([A-Za-z]{2,6})\)")
# house-voices.md, Reuters: a claim carries its basis, or says it cannot.
ATTRIBUTION = re.compile(
    r"\b(according to|said|told (?:reuters|the)|people familiar"
    r"|could not be (?:named|reached)|declined to comment"
    r"|(?:the )?(?:review|report|filing|data) (?:said|showed|found))\b", re.I)
# Spelling signature. Reuters is the only American profile of the four.
# A generic -ised suffix is not usable: it catches raised, praised, advised,
# revised, promised, surprised, none of which have a -ized variant. So the
# alternating stems are listed instead of guessed at.
_ISE_STEMS = ("organ", "recogn", "real", "priorit", "mobil", "util", "apolog",
              "critic", "emphas", "minim", "maxim", "summar", "categor",
              "standard", "special", "character", "normal", "central",
              "digit", "modern", "optim", "legal", "author", "custom")
_ISE = "|".join(_ISE_STEMS)
UK_SPELLING = re.compile(
    r"\b(?:" + _ISE + r")(?:ise|ises|ised|ising|isation|isations)\b"
    r"|\b(?:analyse|analysed|analysing|analyses)\b"
    r"|\b(?:neighbour|labour|behaviour|favour|colour|centre|centres"
    r"|defence|licence|programme|travelling|modelling)s?\b", re.I)
US_SPELLING = re.compile(
    r"\b(?:" + _ISE + r")(?:ize|izes|ized|izing|ization|izations)\b"
    r"|\b(?:analyze|analyzed|analyzing|analyzes)\b"
    r"|\b(?:neighbor|labor|behavior|favor|color|center|centers"
    r"|defense|license|program|traveling|modeling)s?\b", re.I)
# house-voices.md, HBR: ordinary management register at ~1 per 700 words.
HBR_REGISTER = ("actually", "crucial", "underscore", "underscores",
                "commitment to", "fundamentally", "landscape", "valuable")

# Where each check's rule is written down. Vale attaches a `link:` to every
# rule so a finding leads back to the guidance that justifies it; this is the
# same idea against local files. Also the coverage manifest: `--rules` prints
# it, and a check with no entry here is a check nobody can trace to a rule.
SOURCES = {
    "em/en dash":                   "humanizer.md: Em and en dashes",
    "decorative emoji":             "humanizer.md: Formatting tells",
    "AI-tell phrase":               "humanizer.md: Inflated importance",
    "virtue by invented contrast":  "humanizer.md: Virtue by invented contrast",
    "stacked hedging":              "humanizer.md: Hedging",
    "bold mini-heading list":       "humanizer.md: Over-bolding",
    "sentence >25 words":           "foundations.md: Plain wording, rule 8",
    "sentence-length variety":      "foundations.md: Plain wording, rule 10",
    "paragraph length":             "foundations.md: Plain wording, rule 10",
    "paragraph >150 words":         "foundations.md: Plain wording, rule 10",
    "paragraph >250 words":         "foundations.md: Plain wording, rule 10",
    "possible passive voice":       "foundations.md: Plain wording, rule 9",
    "hidden verb (nominalization)": "foundations.md: Plain wording, rule 5",
    "unfamiliar/filler word":       "foundations.md: Plain wording, rule 1",
    "noun string >3":               "foundations.md: Plain wording, rule 6",
    "Title Case heading":           "foundations.md: Headings and lists",
    "list >6 items":                "foundations.md: Headings and lists, rule 7",
    "one subheading level":         "foundations.md: Headings and lists",
    "FAQ section":                  "foundations.md: Headings and lists",
    "evaluative buzzword":          "audiences.md: When jargon is the right choice",
    "phrasal verb / idiom":         "audiences.md: Non-native readers, rule 2",
    "complex tense stack":          "audiences.md: Non-native readers",
    "no fix ETA promised":          "audiences.md: External client, rule 2",
    "next-update time given":       "audiences.md: External client, rule 2",
    "no empty apology":             "audiences.md: External client",
    "no vendor-blaming":            "audiences.md: External client, rule 4",
    "client note <=200 words":      "audiences.md: External client",
    "client note <=12 sentences":   "audiences.md: External client",
    "--client with --email":        "CHECKLIST.md: Step 0 flag table",
    "summary 150-250 words":        "formats.md: Management summary, rule 6",
    "email <=125 words":            "formats.md: Email variant",
    "email <=5 sentences":          "formats.md: Email variant",
    "email subject CATEGORY tag":   "formats.md: Email variant",
    "email subject line":           "formats.md: Email variant",
    "headline":                     "formats.md: Short article, headline",
    "headline 5-10 words":          "formats.md: Short article, rule 1",
    "half page 150-300 words":      "formats.md: Short article, length table",
    "full page 400-700 words":      "formats.md: Short article, length table",
    "half page: no subheadings":    "formats.md: Short article, length table",
    "section >=40 words":           "formats.md: Short article",
    "length preserved":             "SKILL.md: Style-only mode",
    "structure preserved":          "SKILL.md: Style-only mode",
    "naming contexts excluded":     "check.py: under_judgment()",
    # House checks are keyed on the part after the profile name.
    "sentence median":              "house-styles.md: the profile tables",
    "dash rate":                    "house-styles.md: the profile tables",
    "no em dashes":                 "house-styles.md: the profile tables",
    "uses subheads":                "house-styles.md: the profile tables",
    "no subheads":                  "house-styles.md: the profile tables",
    "uses bullets":                 "house-styles.md: the profile tables",
    "no bullets":                   "house-styles.md: the profile tables",
    "headline 4-10 words":          "house-styles.md: the profile tables",
    "headline 7-14 words":          "house-styles.md: the profile tables",
    "semicolons":                   "house-voices.md: Punctuation signature",
    "no semicolons":                "house-voices.md: Punctuation signature",
    "spelling":                     "house-voices.md: Register",
    "claims attributed":            "house-voices.md: Reuters, Attribution",
    "lowercase acronyms":           "house-voices.md: Economist, Register",
    "management register":          "house-voices.md: HBR, Register",
    "register":                     "house-voices.md: HBR, Register",
    "correction dek":               "house-voices.md: HBR, The opening move",
    "coined term across subheads":  "house-voices.md: HBR, The signature move",
    "hedge":                        "house-voices.md: HBR, Attribution",
    "allusive headline":            "house-voices.md: Economist, Refusals",
    "informational headline":       "house-voices.md: FT, The opening move",
    "subheads optional":            "house-voices.md: Economist, Refusals",
    "crossheads":                   "house-voices.md: Economist, The signature move",
    "quote before attribution":     "house-voices.md: Reuters, Attribution",
    "standfirst turns":             "house-voices.md: Economist, The opening move",
    "standfirst states":            "house-voices.md: FT, The opening move",
    "standfirst":                   "house-voices.md: FT, The opening move",
    "attribution":                  "house-voices.md: FT, Attribution",
    "per cent spelled out":         "house-voices.md: FT, Register",
    "short flat sentence early":    "house-voices.md: Economist, Register",
}


def source_for(check):
    """The reference file and section behind a check name, or None."""
    if check in SOURCES:
        return SOURCES[check]
    # House checks arrive as "reuters: uses bullets"; key on the tail, and
    # strip the measured numbers the label interpolates.
    tail = check.split(": ", 1)[-1]
    for key in (tail, re.sub(r"\s*[~0-9].*$", "", tail).strip()):
        if key in SOURCES:
            return SOURCES[key]
    return None


CATEGORY_TAGS = ("DECISION:", "REQUEST:", "ACTION:", "INFO:", "UPDATE:")


# --- helpers -------------------------------------------------------------

def prose_sentences(sents, raw):
    """Sentences minus list items, headings and Subject lines.

    Publication sentence medians were measured from body prose. A document that
    follows Reuters' own summary-bullet convention would otherwise be judged
    against Reuters' sentence target on a population half made of 8-word
    bullets, so the profile's own advice would push it out of the profile's own
    range. Same defect class as counting a table row as a sentence.
    """
    items = {
        re.sub(r"^\s*([-*+]|\d+\.)\s+", "", l).rstrip(" .!?:;").lower()
        for l in raw.splitlines() if re.match(r"^\s*([-*+]|\d+\.)\s+", l)
    }
    items |= {l.lstrip("# ").rstrip(" .!?:;").lower()
              for l in raw.splitlines() if l.startswith("#")}
    # A standfirst or dek is display copy, not body prose. Publication medians
    # were measured on the body, so counting it pulled one fixture's median
    # below its own profile's range.
    items |= {m.group(1).rstrip(" .!?:;").lower()
              for m in (re.match(r"^\s*[*_]([^*_].*?)[*_]\s*$", l)
                        for l in raw.splitlines()) if m}

    def skip(x):
        return (x.lower().startswith("subject")
                or any(x.upper().startswith(t) for t in CATEGORY_TAGS)
                or x.rstrip(" .!?:;").lower() in items)
    return [x for x in sents if not skip(x)]


def strip_markup(text):
    """Prose only: drop code fences, headings markers, list markers, emphasis."""
    # Blank rather than delete, preserving newlines, so a reported line number
    # is the same regardless of which path produced the text. Spaces add no
    # words, so length metrics are unaffected.
    _sp = lambda m: re.sub(r"[^\n]", " ", m.group())
    text = re.sub(r"```.*?```", _sp, text, flags=re.S)
    text = re.sub(r"`[^`]*`", _sp, text)
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
        # A standfirst or dek is its own unit. house-voices.md makes it a
        # first-class element for every profile, and a whole-line italic with no
        # terminal stop merged into the first body sentence: one FT fixture
        # reported a 64-word sentence that was a standfirst plus a lead.
        d = re.match(r"^\s*[*_]([^*_].*?)[*_]\s*$", line)
        if d:
            t = d.group(1).rstrip()
            line = t if t.endswith((".", "!", "?", ":", ";")) else t + "."
        # A subject line is its own unit too, or it merges into the first
        # body sentence and drags that sentence out of the count.
        if re.match(r"^\s*subject\s*:", line, re.I) and not line.rstrip().endswith(
                (".", "!", "?")):
            line = line.rstrip() + "."
        out.append(line)
    text = "\n".join(out)
    return re.sub(r"\*\*|__|\*|_", "", text)


# Contexts where a pattern is being NAMED rather than USED. This is the single
# blind spot behind twelve separate false positives found during development:
# text that names a pattern looks identical to text that commits it. Each check
# used to decide eligibility for itself, so every new check reintroduced the bug.
# One function now owns the decision, and it reports what it removed.
NAMING_CONTEXTS = (
    ("fenced code", re.compile(r"```.*?```", re.S)),
    ("code span", re.compile(r"`[^`\n]*`")),
    ("table row", re.compile(r"^[ \t]*\|.*$", re.M)),
    ("weak/better line", re.compile(r"^.*(?:→|->).*$", re.M)),
    ("short quote", re.compile(r'"[^"\n]{1,60}"')),
    # An italic run holding a comma-separated list is a term list being named,
    # not prose using those terms. The reference files enumerate every banned
    # word this way, so humanizer.md reported 104 AI-tell phrases for the file
    # that lists them. Two commas is the discriminator: emphasis almost never
    # contains two, and a two-item list is short enough to read as prose.
    # Wrapped lines are allowed inside the run, a blank line is not, and the
    # lookarounds keep the pattern off ** bold ** markers.
    ("italic term run", re.compile(
        r"(?<!\*)\*(?!\*)"
        r"(?:[^*\n]|\n(?!\n))*?,(?:[^*\n]|\n(?!\n))*?,(?:[^*\n]|\n(?!\n))*?"
        r"\*(?!\*)")),
)


def _blank(text, pattern):
    """Replace a match with spaces, keeping newlines so offsets stay valid."""
    return pattern.sub(lambda m: re.sub(r"[^\n]", " ", m.group()), text)


def under_judgment(raw, strict=False):
    """The text whose patterns the author is actually asserting.

    Use this for every pattern and wordlist check: em dashes, emoji, AI-tell
    words, buzzwords, unfamiliar words, invented-contrast frames, heading case.
    The question those ask is "is the author committing this?", and a jargon
    table documenting "utilize -> use" is not a draft that uses "utilize".

    Do NOT use it for length or structure metrics (word, sentence, paragraph
    counts, subhead and bullet policy). Those measure the document as it will be
    read, so a table or a quotation still counts.

    Blanks rather than deletes, so reported line numbers stay correct. Returns
    (text, removals) where removals is a list of (kind, count), because a silent
    exclusion could hide a real violation and this checker exists precisely
    because invisible behaviour cannot be trusted.
    """
    if strict:
        return strip_markup(raw), []
    text, removals = raw, []
    for kind, pattern in NAMING_CONTEXTS:
        if kind == "short quote":
            # Only spans short enough to be a term being named. Longer quoted
            # passages are real prose and stay under judgment.
            n = 0
            def repl(m):
                nonlocal n
                if len(m.group().split()) <= 6:
                    n += 1
                    return re.sub(r"[^\n]", " ", m.group())
                return m.group()
            text = pattern.sub(repl, text)
        else:
            n = len(pattern.findall(text))
            text = _blank(text, pattern)
        if n:
            removals.append((kind, n))
    return strip_markup(text), removals


def scan_text(raw):
    """Backward-compatible wrapper. Prefer under_judgment."""
    return under_judgment(raw)[0]


def paragraphs(text, raw=None):
    """Blank-line-separated blocks, minus markdown tables.

    A table block has no sentences in it, so counting it as one paragraph
    reported four reference files as carrying a 250-word paragraph. Sentence
    counting already drops table rows; this is the other half of that fix.
    """
    # List markers are gone from `text` once strip_markup has run, so when the
    # raw source is available the block structure is read from that instead.
    src = raw if raw is not None else text
    out = []
    for blk in re.split(r"\n\s*\n", src):
        lines = [l for l in blk.splitlines() if l.strip()]
        if not lines:
            continue
        table = sum(1 for l in lines if l.lstrip().startswith("|"))
        if table and table >= len(lines) - 1:   # allow one lead-in line
            continue
        # A run of list items is a list, not a paragraph. Consecutive items
        # carry no blank line between them, so a nine-rule numbered list read
        # as one 250-word paragraph in three reference files.
        items = sum(1 for l in lines
                    if re.match(r"^\s*([-*+]|\d+\.)\s+", l))
        if items >= 2:
            continue
        kept = [l for l in lines if not l.lstrip().startswith("|")]
        if kept and " ".join(kept).strip():
            out.append("\n".join(kept).strip())
    return out


def sentences(text):
    """Prose sentences. Table rows are content but not sentences, so they are
    dropped here while still counting toward word and paragraph totals: a
    four-column row was otherwise reported as a 35-word sentence."""
    text = "\n".join(l for l in text.splitlines()
                     if not re.match(r"^[ \t]*\|", l))
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

        # Every flag names the file and section its rule is written in, so a
        # finding leads back to the guidance instead of stopping at a label.
        flagged = [c for st, c, _ in self.rows if st in ("FAIL", "REVIEW")]
        if flagged:
            seen, pairs = set(), []
            for c in flagged:
                src = source_for(c)
                key = (c, src)
                if key in seen:
                    continue
                seen.add(key)
                pairs.append((c, src or "NO SOURCE RECORDED"))
            w = max(len(c) for c, _ in pairs) + 2
            lines.append("")
            lines.append("  rules behind the flags:")
            for c, src in pairs:
                lines.append(f"    {c.ljust(w)}{src}")
        return "\n".join(lines)


# --- checks --------------------------------------------------------------

def run(raw, opts):
    r = Report()
    prose = strip_markup(raw)
    judged, removals = under_judgment(raw, strict=opts.strict)
    low = judged.lower()          # every pattern/wordlist check uses this
    raw_low = low
    sents = sentences(prose)
    paras = paragraphs(prose, raw)
    all_words = words(prose)
    hs = headings(raw)

    if removals:
        r.ok("naming contexts excluded",
             ", ".join(f"{n} {k}" for k, n in removals) + "  (--strict to scan all)")

    # 1. dashes (humanizer.md, the rule that was violated while reported clean)
    dash_hits = [(m.group(), line_of(judged, m.start()))
                 for m in re.finditer(r"[—–]", judged)]
    # require a non-space char before the space, so a line-initial markdown
    # bullet ("\n- item") is not mistaken for a spaced dash
    # Run on markup-stripped text: a blockquoted list item ("> - thing")
    # otherwise reads as a spaced dash, because ">" supplies the preceding
    # non-space character. Same defect class as the bare "- item" case.
    spaced = [(m.group(1), line_of(judged, m.start()))
              for m in re.finditer(r"(?<=\S)[ \t](--?)[ \t]", judged)]
    if opts.dashes_ok:
        r.ok("em/en dash", "skipped: --dashes-ok (user sample uses them)")
    elif dash_hits or spaced:
        detail = ", ".join(f"line {ln}" for _, ln in (dash_hits + spaced)[:8])
        r.fail("em/en dash", f"{len(dash_hits) + len(spaced)} found: {detail}")
    else:
        r.ok("em/en dash", "none")

    # 2. emoji (humanizer.md, formatting tells)
    # Unicode category "So" also contains legitimate symbols (degree sign,
    # currency marks, arrows), so match the actual emoji blocks instead. An
    # HBR article was flagged for 7 "emoji" that were all degree signs.
    emoji = [c for c in judged if (
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
        # house-styles.md records HBR's subheads as title case, so writing
        # correct HBR would otherwise guarantee a FAIL the profile asked for.
        # A named profile downgrades the general rule; it never silences it.
        if opts.house and HOUSE[opts.house].get("titlecase"):
            r.review("Title Case heading",
                     f"{len(bad_case)} found; {opts.house} subheads are title "
                     "case, so this is the profile's convention")
        else:
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
        # Measured on prose only, the way the publications were measured.
        pros = prose_sentences(sents, raw)
        med = statistics_median([len(words(x)) for x in pros]) if pros else 0
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
            # A factor of 2 either side. Publication dash rates were measured
            # across whole articles; a 700-word draft carrying one dash against
            # a 348-word target is in character, two is not.
            within = h["dash"] / 2 <= rate <= h["dash"] * 2
            (r.ok if within else r.review)(
                f"{name}: dash rate ~1 per {h['dash']}w", f"1 per {round(rate)}w")
        else:
            r.review(f"{name}: dash rate ~1 per {h['dash']}w",
                     "none used; house style uses them")

        nsub = len([1 for lvl, _ in hs if lvl >= 2])
        if h["subheads"] == "optional":
            # Two of five full articles carry crossheads and three carry none,
            # so presence is a choice. What is consistent is their shape.
            r.ok(f"{name}: subheads optional", f"{nsub} found")
        elif h["subheads"]:
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

        # ---- voice, from house-voices.md -----------------------------------
        # Shape checks above answer "is it built like them". These answer
        # "does it sound like them". Only the measurable half; wit, the quality
        # of a concrete anchor and whether an antithesis names two real
        # diagnoses stay in CHECKLIST.md.

        # Punctuation signature: semicolons, per profile.
        nsemi = judged.count(";")
        if h.get("semis") is None:
            (r.ok if nsemi == 0 else r.review)(
                f"{name}: no semicolons",
                "none" if nsemi == 0 else f"{nsemi} found")
        elif nsemi:
            srate = n / nsemi
            # Semicolons only fail for being too frequent, so the band is
            # one-sided. A factor of 3 is looser than the dash factor because
            # the counts are smaller: HBR ranges 0 to 12 within one masthead.
            (r.ok if srate >= h["semis"] / 3 else r.review)(
                f"{name}: semicolons ~1 per {h['semis']}w", f"1 per {round(srate)}w")
        else:
            r.ok(f"{name}: semicolons ~1 per {h['semis']}w", "none, within range")

        # Spelling signature. Reuters is the only American profile of the four.
        want = h.get("spelling")
        if want:
            uk = {m.group().lower() for m in UK_SPELLING.finditer(judged)}
            us = {m.group().lower() for m in US_SPELLING.finditer(judged)}
            wrong = us if want == "uk" else uk
            (r.ok if not wrong else r.review)(
                f"{name}: {want.upper()} spelling",
                "consistent" if not wrong
                else f"{len(wrong)} other-side form(s): " + ", ".join(sorted(wrong)[:4]))

        # Reuters: a claim carries its basis, or says it cannot.
        # Reuters: presence of a basis. FT uses the same key for a rate, so
        # this is guarded on the boolean rather than on truthiness.
        if h.get("attribution") is True:
            hits = ATTRIBUTION.findall(judged)
            (r.ok if hits else r.fail)(
                f"{name}: claims attributed",
                f"{len(hits)} attribution phrase(s)" if hits
                else "none; wire copy names its basis or says it cannot")

        # Economist: a glossed acronym is used bare and lowercase afterwards.
        if h.get("lc_acronyms"):
            shouty = []
            for m in GLOSSED_ACRONYM.finditer(judged):
                tok = m.group(1)
                if tok.isupper() and len(tok) >= 2:
                    later = judged[m.end():]
                    if re.search(r"\b" + re.escape(tok) + r"\b", later):
                        shouty.append(tok)
            (r.ok if not shouty else r.review)(
                f"{name}: lowercase acronyms",
                "none in caps" if not shouty
                else "glossed then used in caps: " + ", ".join(sorted(set(shouty))[:4]))

        # HBR: the management register is present, and stays near 1 per 700.
        if h.get("register"):
            rh = [t for t in HBR_REGISTER if re.search(r"\b" + t + r"\b", low)]
            cnt = sum(len(re.findall(r"\b" + t + r"\b", low)) for t in HBR_REGISTER)
            target = h["register"]
            if not cnt:
                r.review(f"{name}: management register",
                         f"none of {len(HBR_REGISTER)} register words used; "
                         f"house runs ~1 per {target}w")
            else:
                rate = n / cnt
                # The 700-word target is the midpoint of a measured 644-787
                # range. 3.5 puts the floor at 200 words per hit, which is
                # exactly AI_TELL_WORDS_PER_HIT: below that the same words
                # read as slop rather than register, so the two agree.
                (r.ok if rate >= target / 3.5 else r.review)(
                    f"{name}: register ~1 per {target}w",
                    f"1 per {round(rate)}w ({', '.join(rh[:4])})")

        # The dek. Counting all five articles rather than admiring one, the
        # "It isn't X. It's Y." shape is 1 of 5, not the house move. What 2 of 5
        # share is a correction: name the belief the reader holds, then reverse
        # it. The other shape puts the reversal inside sentence one and the
        # consequence in sentence two. So this reviews rather than requires.
        if h.get("dek") == "correction":
            dek = ""
            if top:
                after = raw.split(top[0], 1)[-1].strip().splitlines()
                dek = next((l.strip() for l in after
                            if l.strip() and not l.startswith("#")), "")
            ds = sentences(dek)
            neg = re.search(r"\b(is ?n[o']t|was ?n[o']t|did ?n[o']t|does ?n[o']t"
                            r"|no longer|not a|not the|when they (?:actually )?"
                            r"do ?n[o']t|rather than)\b", dek, re.I)
            dw = len(words(dek))
            lo, hi = h.get("stand", (12, 24))
            if dek and neg and lo <= dw <= hi:
                r.ok(f"{name}: correction dek", f"{len(ds)} sentence(s), {dw} words")
            elif dek:
                r.review(f"{name}: correction dek",
                         f"{dw} words, negation {'present' if neg else 'absent'}; "
                         f"2 of 5 name the belief then reverse it, in {lo}-{hi} words")
            else:
                r.review(f"{name}: correction dek", "no dek found under the headline")

        # The coined term, carried through the subheads. This was the strongest
        # new finding: 3 of the 3 articles that coin a term put it in most of
        # their subheads, inflected, and negated where the argument turns
        # (False Alignment -> True Agreement -> True Disagreement).
        frac = h.get("subhead_term")
        if frac and nsub >= 2:
            subs = [t for lvl, t in hs if lvl >= 2]
            stop = set(STOPWORDS) | {"your", "our", "their", "what", "how", "why",
                                     "ways", "find", "five", "the", "and", "isnt"}
            counts = {}
            for w in re.findall(r"[a-z]{5,}", " ".join(subs).lower()):
                if w not in stop:
                    counts[w] = counts.get(w, 0) + 1
            best, hits = None, 0
            for w, c in counts.items():
                # not `n`: that name holds the document word count in this scope
                k = sum(1 for x in subs if w[:5] in x.lower())
                if k > hits:
                    best, hits = w, k
            share = hits / len(subs) if subs else 0
            (r.ok if share >= frac else r.review)(
                f"{name}: coined term across subheads",
                f"{hits}/{len(subs)} carry {best!r} ({round(share*100)}%)"
                if best else f"0/{len(subs)}; house repeats one coined term")

        # Hedging, distributed rather than stacked. HBR hedges once every ~160
        # words and never twice in a sentence, and that reads as authority. Our
        # stacked-hedging check found 0 in 4 of 5 articles, so the two rules are
        # measuring different things and both are right.
        hb = h.get("hedge")
        if hb:
            nh = len(re.findall(
                r"\b(may|might|can|often|tends? to|suggests?|appears? to|likely)\b",
                judged, re.I))
            rate = n / nh if nh else 0
            lo, hi = hb
            if nh and lo <= rate <= hi:
                r.ok(f"{name}: hedge 1 per {lo}-{hi}w", f"1 per {round(rate)}w")
            elif nh:
                r.review(f"{name}: hedge 1 per {lo}-{hi}w",
                         f"1 per {round(rate)}w; house qualifies about once "
                         "every eight sentences")
            else:
                r.review(f"{name}: hedge 1 per {lo}-{hi}w",
                         "none; house hedges steadily and never twice in a sentence")

        # Crosshead shape. Where the Economist uses them they are 3-4 words and
        # allusive: "How to spend it", "Can't touch this", "Stoppable force,
        # movable object". Two of two articles that use editorial crossheads
        # make them a joke, so the count is what is checked and the wit is not.
        cw = h.get("crosshead")
        if cw and nsub:
            subs = [t for lvl, t in hs if lvl >= 2]
            lo, hi = cw
            fit = [t for t in subs if lo <= len(words(t)) <= hi]
            (r.ok if len(fit) == len(subs) else r.review)(
                f"{name}: crossheads {lo}-{hi} words",
                f"{len(fit)}/{len(subs)} in range"
                + ("" if len(fit) == len(subs)
                   else "; house crossheads are short and allusive"))

        # Reuters puts the quote before the attribution: "...", said Name, title
        # at Firm. Held back for a turn on one article's 5-of-5, then confirmed
        # at 7 against 1 across three of four held-out articles.
        if h.get("quote_first"):
            qs = len(re.findall(r'["\u201d],?\s+(?:said|added|told)\s+[A-Z]', raw))
            sq = len(re.findall(r'\b[A-Z][a-z]+ (?:said|added)[:,]?\s+["\u201c]', raw))
            if not qs and not sq:
                r.review(f"{name}: quote before attribution", "no attributed quotes")
            else:
                (r.ok if qs > sq else r.review)(
                    f"{name}: quote before attribution",
                    f"{qs} quote-first, {sq} name-first"
                    + ("" if qs > sq else "; house leads with the quote"))

        # The standfirst turns against the headline rather than restating it.
        # 4 of 5: two open on "But", one adds ", too", one runs a "just as"
        # symmetry. The one that does not is the data-journalism piece, whose
        # standfirst is a bare number.
        want_sf = h.get("stand_turn")
        if want_sf:
            sf = ""
            if top:
                after = raw.split(top[0], 1)[-1].strip().splitlines()
                sf = next((l.strip() for l in after
                           if l.strip() and not l.startswith("#")), "")
            sf_plain = sf.strip("*_ ")
            # A turn can sit mid-standfirst as easily as at the front: the FT
            # long read runs "...has grown every year since 2022 - but claims
            # of a brain drain overstate the problem". Anchoring to the start
            # missed it and reported the piece as stating a fact.
            turn = bool(re.search(
                r"^(?:But|Yet|Though|Still|And yet)\b"
                r"|\bbut\b|\byet\b|\balthough\b|\bthough\b"
                r"|, too\b|\bjust as\b|\brather than\b", sf_plain, re.I))
            if not sf:
                r.review(f"{name}: standfirst", "no standfirst found")
            elif want_sf == "turn":
                (r.ok if turn else r.review)(
                    f"{name}: standfirst turns",
                    "adds a turn" if turn
                    else "restates the headline; house adds the qualification here")
            else:
                # FT news: the standfirst states the next fact and does not
                # argue. 0 of 4 news standfirsts turn. The long read does turn,
                # so this is a register rule and CHECKLIST.md carries that.
                (r.ok if not turn else r.review)(
                    f"{name}: standfirst states", "adds a fact" if not turn
                    else "turns; house news states the next fact instead")

        # A short flat sentence early. 4 of 6 put one of six words or fewer in
        # the opening paragraph: "The market shrugged.", "Which is in Munich."
        if h.get("short_opener"):
            paras = paragraphs(prose, raw)
            first = next((p for p in paras
                          if len(words(p)) > 25 and p.strip() not in
                          (t for _, t in hs)), "")
            shorts = [x for x in sentences(first) if 1 <= len(words(x)) <= 6]
            (r.ok if shorts else r.review)(
                f"{name}: short flat sentence early",
                f'"{shorts[0][:40]}"' if shorts
                else "none in the opening paragraph")

        # FT: every claim names who said it. 1 per 38-58 words across five
        # articles, which is the tightest single habit in any of the four
        # profiles and roughly four times HBR's hedging rate.
        ar = h.get("attribution")
        if isinstance(ar, tuple):
            na = len(re.findall(
                r"\b(said|says|according to|claimed|added|told|reported|revealed"
                r"|argued|alleged|asserted|accused|acknowledged|cautioned"
                r"|complained|emphasised|insisted|estimates|describes)\b",
                judged, re.I))
            lo, hi = ar
            rate = n / na if na else 0
            if na and lo <= rate <= hi:
                r.ok(f"{name}: attribution 1 per {lo}-{hi}w", f"1 per {round(rate)}w")
            elif na:
                r.review(f"{name}: attribution 1 per {lo}-{hi}w",
                         f"1 per {round(rate)}w; house names a source about "
                         "every second sentence")
            else:
                r.review(f"{name}: attribution 1 per {lo}-{hi}w",
                         "none; house attributes constantly")

        # "per cent" spelled out, never the symbol. 12 instances, 0 symbols.
        if h.get("percent_spelled"):
            sym = judged.count("%")
            spelled = len(re.findall(r"\bper cent\b", judged, re.I))
            if not sym and not spelled:
                r.ok(f"{name}: per cent spelled out", "no percentages")
            else:
                (r.ok if not sym else r.review)(
                    f"{name}: per cent spelled out",
                    f"{spelled} spelled, {sym} as %"
                    + ("" if not sym else "; house spells it out"))

        # Headline type: allusive poses a puzzle, informational tells the story.
        if h.get("headline") and top:
            allusive = re.match(r"^(why|how|what|when|where|the case for"
                                r"|it'?s time)\b", top[0].strip(), re.I)
            if h["headline"] == "allusive":
                (r.ok if allusive else r.review)(
                    f"{name}: allusive headline",
                    "poses a puzzle" if allusive
                    else "reads informational; house leans on the standfirst")
            else:
                (r.ok if not allusive else r.review)(
                    f"{name}: informational headline",
                    "tells the story" if not allusive
                    else "opens allusively; house headlines travel alone")

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

            # Removing slop legitimately shortens text, so raw word loss is a
            # poor proxy for content loss when the original was padded. Count
            # the slop that disappeared and treat roughly two words per removed
            # phrase as explained loss. Without this, a clean de-slopping edit
            # fails a check the checklist says must always be fixed.
            def slop_hits(text):
                lo = under_judgment(text)[0].lower()
                return sum(len(find_terms(lo, L))
                           for L in (AI_WORDS, UNFAMILIAR, BUZZWORDS))
            removed = max(0, slop_hits(open(opts.compare, encoding="utf-8").read())
                          - slop_hits(raw))
            explained = removed * 2
            unexplained = max(0, (o - n) - explained)
            upct = unexplained / o * 100 if o else 0.0

            if o and upct > 15:
                r.fail("length preserved",
                       detail + f". {unexplained} words unexplained by the "
                       f"{removed} slop phrase(s) removed; content was cut")
            elif o and pct < -15:
                r.review("length preserved",
                         detail + f", but {removed} slop phrase(s) removed "
                         f"accounts for most of it; confirm no claim was lost")
            elif abs(pct) > 40:
                r.review("length preserved", detail + ", large change")
            else:
                r.ok("length preserved", detail)
            # paragraph count is the other structural tell
            po, pn = len(paragraphs(orig)), len(paras)
            (r.ok if po == pn else r.review)(
                "structure preserved",
                f"{po} -> {pn} paragraphs" +
                ("" if po == pn else ". Style-only edits should not merge or split"))

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
        body = prose_sentences(sents, raw)
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
        # A commitment and a time, in the same sentence. Requiring the literal
        # words "next update" failed a note that said "I will write again by
        # Friday 5 September", which is exactly what the rule asks for: the
        # check was measuring a phrase as a proxy for a promise.
        committed = [x for x in sents if NEXT_UPDATE_COMMIT.search(x)]
        timed = [x for x in committed if NEXT_UPDATE_TIME.search(x)]
        if timed:
            r.ok("next-update time given", "present")
        elif committed:
            r.fail("next-update time given",
                   "a next update is promised with no time on it: "
                   f"\"{committed[0][:60].strip()}\"")
        else:
            r.fail("next-update time given", "missing")
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
    p.add_argument("file", nargs="?")
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
    p.add_argument("--strict", action="store_true",
                   help="scan naming contexts too (code spans, tables, quoted "
                        "terms, weak/better lines). Off by default because a "
                        "jargon table documenting a word is not a use of it")
    p.add_argument("--dashes-ok", action="store_true",
                   help="user's own writing sample uses em dashes")
    p.add_argument("--house", choices=sorted(HOUSE),
                   help="target a measured publication's conventions "
                        "(see references/house-styles.md)")
    p.add_argument("--compare", metavar="ORIGINAL",
                   help="style-only mode: fail if the draft lost more than "
                        "15%% of the original's words (i.e. it compressed "
                        "when it was only meant to be reworded)")
    p.add_argument("--rules", action="store_true",
                   help="print the check-to-rule coverage manifest and exit")
    opts = p.parse_args()

    if opts.rules:
        # Microsoft's Vale package publishes what fraction of its style guide
        # the rules implement. Same idea: say what is enforced and where the
        # rule lives, so unenforced guidance is visible rather than assumed.
        by_file = {}
        for check, src in sorted(SOURCES.items()):
            by_file.setdefault(src.split(":")[0], []).append((check, src))
        total = sum(len(v) for v in by_file.values())
        print(f"\ncheck-to-rule coverage: {total} checks mapped to a rule\n")
        for f in sorted(by_file):
            print(f"  {f}  ({len(by_file[f])})")
            w = max(len(c) for c, _ in by_file[f]) + 2
            for check, src in by_file[f]:
                print(f"    {check.ljust(w)}{src.split(': ', 1)[-1]}")
            print()
        print("  Judgment-only rules, enforced by CHECKLIST.md and not by any")
        print("  check: is this the strongest point, did the three-why chain")
        print("  run, is the triage stated, was uncertainty preserved, do the")
        print("  four jargon tests pass, was any fact added or dropped, and")
        print("  the house-voice items in step 4.\n")
        return 0

    try:
        if not opts.file:
            print("error: a file is required unless you pass --rules")
            return 2
        raw = open(opts.file, encoding="utf-8").read()
    except OSError as e:
        print(f"cannot read {opts.file}: {e}", file=sys.stderr)
        return 2

    rep = run(raw, opts)
    print(f"\nclear-writing checks: {opts.file}\n")
    print(rep.render())
    fails = sum(1 for s, _, _ in rep.rows if s == "FAIL")
    print("\n  FAIL = fix before returning. REVIEW = look at it and decide.")
    print("  Judgment checks are not here. Run CHECKLIST.md too.\n")
    return 1 if fails else 0


if __name__ == "__main__":
    sys.exit(main())
