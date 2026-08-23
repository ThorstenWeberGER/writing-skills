# Test fixtures for check.py

Regression fixtures. Expected results:

| Fixture | Flags | Expected |
|---|---|---|
| `bad.md` | `--client --nonnative` | 5 FAIL, exit 1 |
| `good.md` | `--client --nonnative` | 0 FAIL, exit 0 |
| `em.md` | `--email` | 2 FAIL, exit 1 |
| `art.md` | `--article-full` | 1 FAIL, exit 1 |

`bad.md` is the real draft that shipped with two em dashes while the humanizer
pass was reported as applied. `good.md` is its corrected form. Keep both — the
pair is the regression test for the defect that motivated `check.py`.

Run all four:

```bash
cd skills/clear-writing
for f in bad good em art; do
  case $f in bad|good) fl="--client --nonnative";; em) fl="--email";; art) fl="--article-full";; esac
  echo "== $f"; python3 check.py tests/fixtures/$f.md $fl | grep -E "^  [0-9]+ FAIL"
done
```

## `naming-vs-using.md` — the false-positive regression

The most important fixture. Twelve separate false positives were found during
development, all from one blind spot: **text that names a pattern looks
identical to text that commits it.** A jargon table documenting `utilize -> use`
is not a draft that uses "utilize".

This fixture names every pattern in all five contexts (code span, fenced block,
markdown table, weak/better line, short quote) and then uses the same patterns
for real in a final section. Expected: **5 FAIL**, and every one from the
use section.

`tests/test.sh` also asserts that `--strict` finds *more* hits than the default. If
the exclusions ever stop working, the counts converge and that check fails. A
passing FAIL count alone would not catch it, because the fixture would still
fail for the right total by the wrong route.
