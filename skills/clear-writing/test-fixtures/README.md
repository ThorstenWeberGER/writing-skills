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
  echo "== $f"; python3 check.py test-fixtures/$f.md $fl | grep -E "^  [0-9]+ FAIL"
done
```
