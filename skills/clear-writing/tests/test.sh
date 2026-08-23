#!/usr/bin/env bash
# All checks for the clear-writing skill. Exit 0 = everything green.
set -u
cd "$(dirname "$0")/.."   # skill root: check.py and the reference files live here
rc=0

echo "=== wordlist drift ==="
python3 tests/test_drift.py || rc=1

echo "=== check.py fixtures ==="
for f in bad good em art fullmode-article mgmt-email client-note naming-vs-using; do
  case $f in
    bad|good)        fl="--client --nonnative";;
    em)              fl="--email";;
    art)             fl="--article-full";;
    fullmode-article) fl="--article-full";;
    mgmt-email)      fl="--email";;
    client-note)     fl="--client";;
    naming-vs-using) fl="";;
  esac
  out=$(python3 check.py "tests/fixtures/$f.md" $fl 2>&1)
  got=$(printf '%s' "$out" | grep -oE '^  [0-9]+ FAIL' | grep -oE '[0-9]+')
  case $f in
    bad) want=5;; good) want=0;; em) want=2;; art) want=1;;
    fullmode-article) want=0;;
    mgmt-email) want=0;;
    client-note) want=0;;
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
