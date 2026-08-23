#!/usr/bin/env bash
# All checks for the clear-writing skill. Exit 0 = everything green.
set -u
cd "$(dirname "$0")/.."   # skill root: check.py and the reference files live here
rc=0

echo "=== wordlist drift ==="
python3 tests/test_drift.py || rc=1

echo "=== check.py fixtures ==="
for f in bad good em art fullmode-article mgmt-email client-note client-no-time \
         client-no-update naming-vs-using; do
  case $f in
    bad|good)        fl="--client --nonnative";;
    em)              fl="--email";;
    art)             fl="--article-full";;
    fullmode-article) fl="--article-full";;
    mgmt-email)      fl="--email";;
    client-note)     fl="--client";;
    client-no-time)  fl="--client";;
    client-no-update) fl="--client";;
    naming-vs-using) fl="";;
  esac
  out=$(python3 check.py "tests/fixtures/$f.md" $fl 2>&1)
  got=$(printf '%s' "$out" | grep -oE '^  [0-9]+ FAIL' | grep -oE '[0-9]+')
  case $f in
    bad) want=5;; good) want=0;; em) want=2;; art) want=1;;
    fullmode-article) want=0;;
    mgmt-email) want=0;;
    client-note) want=0;;
    client-no-time) want=1;;
    client-no-update) want=1;;
    naming-vs-using) want=5;;
  esac
  if [ "$got" = "$want" ]; then
    echo "  pass    $f.md: $got FAIL as expected"
  else
    echo "  FAIL    $f.md: expected $want FAIL, got $got"
    rc=1
  fi
done

echo "=== naming-vs-using: exclusions must change the outcome ==="
d=$(python3 check.py tests/fixtures/naming-vs-using.md 2>&1 | grep -oE 'buzzword +[0-9]+' | grep -oE '[0-9]+')
t=$(python3 check.py tests/fixtures/naming-vs-using.md --strict 2>&1 | grep -oE 'buzzword +[0-9]+' | grep -oE '[0-9]+')
if [ -n "$d" ] && [ -n "$t" ] && [ "$t" -gt "$d" ]; then
  echo "  pass    exclusions active: $d buzzword hits default vs $t with --strict"
else
  echo "  FAIL    exclusions not working: default=$d strict=$t"; rc=1
fi

echo "=== style-only compression guard ==="
for pair in "styled:0" "overcompressed:1" "style-edited:0" "deslop-styled:0"; do
  f=${pair%%:*}; want=${pair##*:}
  case $f in style-edited) base=style-orig;; deslop-styled) base=deslop-orig;; *) base=orig;; esac
  got=$(python3 check.py "tests/fixtures/$f.md" --compare "tests/fixtures/$base.md" 2>&1 \
        | grep -oE '^  [0-9]+ FAIL' | grep -oE '[0-9]+')
  if [ "$got" = "$want" ]; then
    echo "  pass    $f.md: $got FAIL as expected"
  else
    echo "  FAIL    $f.md: expected $want FAIL, got $got"; rc=1
  fi
done

echo "=== house profiles: conventions honoured, general rules still bite ==="
# An HBR-shaped draft must pass as HBR (title-case subheads are its convention)
# and still fail with no profile named. A Reuters-shaped draft must hit Reuters'
# sentence median with its own summary bullets excluded from the measurement.
hbr_h=$(python3 check.py tests/fixtures/house-hbr.md --house hbr 2>&1 | grep -oE '^  [0-9]+ FAIL' | grep -oE '[0-9]+')
hbr_n=$(python3 check.py tests/fixtures/house-hbr.md 2>&1 | grep -oE '^  [0-9]+ FAIL' | grep -oE '[0-9]+')
if [ "$hbr_h" = "0" ] && [ "$hbr_n" = "1" ]; then
  echo "  pass    house-hbr.md: 0 FAIL as hbr, $hbr_n FAIL with no profile"
else
  echo "  FAIL    house-hbr.md: expected 0 as hbr and 1 bare, got $hbr_h and $hbr_n"; rc=1
fi
rmed=$(python3 check.py tests/fixtures/house-reuters.md --house reuters 2>&1 \
       | grep -oE 'reuters: sentence median [0-9-]+ +[0-9.]+' | grep -oE '[0-9.]+$')
if python3 check.py tests/fixtures/house-reuters.md --house reuters 2>&1 \
   | grep -q '^  pass    reuters: sentence median'; then
  echo "  pass    house-reuters.md: median $rmed inside 24-32 with bullets excluded"
else
  echo "  FAIL    house-reuters.md: median $rmed outside reuters range"; rc=1
fi

echo "=== house voices: each draft fits its own profile best ==="
# The discriminating property. A voice guide that cannot tell its four voices
# apart is decoration, so every fixture is scored against all four profiles and
# must rank its own strictly first on (FAIL, REVIEW), lexicographically.
score() {  # $1 fixture voice, $2 profile -> "FAIL REVIEW"
  local out; out=$(python3 check.py "tests/fixtures/voice-$1.md" --house "$2" 2>&1)
  local f r
  f=$(printf '%s' "$out" | grep -oE '^  [0-9]+ FAIL' | grep -oE '[0-9]+')
  r=$(printf '%s' "$out" | grep -cE "^  REVIEW  $2:")
  echo "${f:-99} ${r:-99}"
}
for d in economist ft reuters hbr; do
  own=$(score "$d" "$d"); of=${own%% *}; orv=${own##* }
  worst=""
  for h in economist ft reuters hbr; do
    [ "$h" = "$d" ] && continue
    o=$(score "$d" "$h"); xf=${o%% *}; xr=${o##* }
    if [ "$of" -gt "$xf" ] || { [ "$of" -eq "$xf" ] && [ "$orv" -ge "$xr" ]; }; then
      worst="$worst $h(${xf}F/${xr}R)"
    fi
  done
  if [ "$of" -eq 0 ] && [ -z "$worst" ]; then
    echo "  pass    voice-$d.md: best as $d (${of}F/${orv}R)"
  else
    echo "  FAIL    voice-$d.md: own=${of}F/${orv}R, not strictly best;$worst"; rc=1
  fi
done

echo "=== every flagged check traces back to a written rule ==="
# Vale attaches a link to every rule so a finding leads to its guidance. The
# equivalent here is SOURCES. A check with no entry prints NO SOURCE RECORDED,
# which means a reader cannot find the rule behind a failure.
orphan=0
for pair in "tests/fixtures/bad.md:--client --nonnative" "tests/fixtures/em.md:--email" \
            "tests/fixtures/art.md:--article-full" "tests/fixtures/naming-vs-using.md:" \
            "tests/fixtures/client-no-time.md:--client" \
            "tests/fixtures/voice-hbr.md:--house hbr" \
            "tests/fixtures/voice-reuters.md:--house reuters" \
            "tests/fixtures/voice-economist.md:--house economist" \
            "tests/fixtures/voice-ft.md:--house ft"; do
  f=${pair%%:*}; fl=${pair#*:}
  n=$(python3 check.py "$f" $fl 2>&1 | grep -c 'NO SOURCE RECORDED')
  if [ "$n" != "0" ]; then
    echo "  FAIL    $f: $n flagged check(s) with no rule recorded"
    python3 check.py "$f" $fl 2>&1 | grep 'NO SOURCE RECORDED' | sed 's/^/          /'
    orphan=1
  fi
done
if [ $orphan -eq 0 ]; then
  echo "  pass    all flagged checks name their rule"
else
  rc=1
fi

echo "=== eval suite is well-formed ==="
# The eval format is the one the skill-authoring docs specify. These cannot be
# run from inside the authoring session (that is the point of them), so what is
# testable here is that the file stays valid and its input files still exist.
python3 - <<'EOF' || rc=1
import json, os, sys
base = "evals"
try:
    d = json.load(open(os.path.join(base, "evals.json")))
except Exception as e:
    print(f"  FAIL    evals.json does not parse: {e}"); sys.exit(1)
bad, ids = [], set()
for e in d:
    for k in ("id", "skills", "query", "files", "expected_behavior", "gap"):
        if k not in e:
            bad.append(f"{e.get('id', '?')}: missing field {k}")
    if e.get("id") in ids:
        bad.append(f"duplicate id {e['id']}")
    ids.add(e.get("id"))
    for f in e.get("files", []):
        if not os.path.exists(os.path.join(base, f)):
            bad.append(f"{e.get('id')}: input file not found: {f}")
    if not e.get("expected_behavior"):
        bad.append(f"{e.get('id')}: no assertions")
if len(d) < 3:
    bad.append(f"only {len(d)} evals; the authoring checklist asks for at least three")
if bad:
    print("  FAIL    evals.json:")
    for b in bad:
        print(f"            {b}")
    sys.exit(1)
n = sum(len(e["expected_behavior"]) for e in d)
print(f"  pass    evals.json: {len(d)} cases, {n} assertions, all input files present")
EOF

echo "=== the skill's own files obey the dash rule ==="
# The rule was described for 20,000 words while 200+ dashes sat in the files
# describing it. Enforced here so it cannot drift back.
for f in SKILL.md CHECKLIST.md references/*.md templates/*.md inputs/*.md \
         ../../README.md ../../CLAUDE.md ../../docs/v2-checklist.md; do
  if python3 check.py "$f" 2>&1 | grep -q '^  FAIL    em/en dash'; then
    echo "  FAIL    $f carries an em or en dash outside a code span"; rc=1
  fi
done
[ $rc -eq 0 ] && echo "  pass    all prose files clean"

echo "=== the scripts carry only their known dash literals ==="
# Counted in lines. check.py needs the two regexes it scans with; test_drift.py
# needs the humanizer.md rule anchor and its strip() char class; test.sh needs
# only the grep below. Any other hit is a slip.
for pair in "check.py:2" "tests/test_drift.py:2" "tests/test.sh:1"; do
  f=${pair%%:*}; want=${pair##*:}
  got=$(grep -c '—\|–' "$f" | tr -d ' ')
  if [ "$got" = "$want" ]; then
    echo "  pass    $f: $want known dash literal(s)"
  else
    echo "  FAIL    $f: expected $want dash literal(s), found $got"; rc=1
  fi
done

echo
[ $rc -eq 0 ] && echo "ALL GREEN" || echo "FAILURES ABOVE"
exit $rc
