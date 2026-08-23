#!/usr/bin/env bash
# All checks for the clear-writing skill. Exit 0 = everything green.
set -u
cd "$(dirname "$0")"
rc=0

echo "=== wordlist drift ==="
python3 test_drift.py || rc=1

echo "=== check.py fixtures ==="
for f in bad good em art; do
  case $f in
    bad|good) fl="--client --nonnative";;
    em)       fl="--email";;
    art)      fl="--article-full";;
  esac
  out=$(python3 check.py "test-fixtures/$f.md" $fl 2>&1)
  got=$(printf '%s' "$out" | grep -oE '^  [0-9]+ FAIL' | grep -oE '[0-9]+')
  case $f in
    bad) want=5;; good) want=0;; em) want=2;; art) want=1;;
  esac
  if [ "$got" = "$want" ]; then
    echo "  pass    $f.md — $got FAIL as expected"
  else
    echo "  FAIL    $f.md — expected $want FAIL, got $got"
    rc=1
  fi
done

echo
[ $rc -eq 0 ] && echo "ALL GREEN" || echo "FAILURES ABOVE"
exit $rc
