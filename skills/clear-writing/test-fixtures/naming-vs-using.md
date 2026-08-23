# Naming versus using: the false-positive regression fixture

Every block below NAMES a pattern. None should be flagged. The final section
USES the same patterns for real, and every one of those must be flagged.

## Named in a code span

Replace `—` with a comma. The `–` character is also banned. Do not write `utilize`.

## Named in a table

| Avoid | Use instead |
|---|---|
| utilize | use |
| circle back | follow up |
| leverage | use |
| synergy | shared benefit |

## Named in a weak/better line

The fix is simple: "we must leverage synergy" → "the two teams share tooling"

## Named in a short quote

The federal guidance calls out "utilize" and "in order to". HBR uses "circle back"
and "actionable", which is worth knowing.

## Named in a fenced block

```
utilize the synergy to leverage our bandwidth
```

## USED FOR REAL, all of these must fail

We should utilize the synergy here and circle back on bandwidth in order to
move the needle. I made sure to check this rather than guessing. It stands as a
testament to our commitment to excellence — a real prose em dash — and to synergy 🚀
