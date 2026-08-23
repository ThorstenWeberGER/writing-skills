#!/usr/bin/env bash
# All checks for the clear-writing skill. Exit 0 = everything green.
set -u
cd "$(dirname "$0")"
rc=0

echo "=== wordlist drift ==="
python3 test_drift.py || rc=1

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
  out=$(python3 check.py "test-fixtures/$f.md" $fl 2>&1)
  got=$(printf '%s' "$out" | grep -oE '^  [0-9]+ FAIL' | grep -oE '[0-9]+')
  case $f in
    bad) want=5;; good) want=0;; em) want=2;; art) want=1;;
    fullmode-article) want=0;;
    mgmt-email) want=0;;
    client-note) want=0;;
    naming-vs-using) want=5;;
  esac
  if [ "$got" = "$want" ]; then
    echo "  pass    $f.md — $got FAIL as expected"
  else
    echo "  FAIL    $f.md — expected $want FAIL, got $got"
    rc=1
  fi
done

echo "=== naming-vs-using: exclusions must change the outcome ==="
d=$(python3 check.py test-fixtures/naming-vs-using.md 2>&1 | grep -oE 'buzzword +[0-9]+' | grep -oE '[0-9]+')
t=$(python3 check.py test-fixtures/naming-vs-using.md --strict 2>&1 | grep -oE 'buzzword +[0-9]+' | grep -oE '[0-9]+')
if [ -n "$d" ] && [ -n "$t" ] && [ "$t" -gt "$d" ]; then
  echo "  pass    exclusions active — $d buzzword hits default vs $t with --strict"
else
  echo "  FAIL    exclusions not working — default=$d strict=$t"; rc=1
fi

echo "=== style-only compression guard ==="
for pair in "styled:0" "overcompressed:1" "style-edited:0" "deslop-styled:0"; do
  f=${pair%%:*}; want=${pair##*:}
  case $f in style-edited) base=style-orig;; deslop-styled) base=deslop-orig;; *) base=orig;; esac
  got=$(python3 check.py "test-fixtures/$f.md" --compare "test-fixtures/$base.md" 2>&1 \
        | grep -oE '^  [0-9]+ FAIL' | grep -oE '[0-9]+')
  if [ "$got" = "$want" ]; then
    echo "  pass    $f.md — $got FAIL as expected"
  else
    echo "  FAIL    $f.md — expected $want FAIL, got $got"; rc=1
  fi
done

echo
[ $rc -eq 0 ] && echo "ALL GREEN" || echo "FAILURES ABOVE"
exit $rc
