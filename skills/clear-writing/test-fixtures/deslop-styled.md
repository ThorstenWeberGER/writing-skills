# Naming conventions for our warehouse models

We need one consistent approach. Different teams use different patterns today,
which defeats the purpose of a shared warehouse.

The guidance is straightforward. Words like "synergy" and "leverage" should not
appear in model descriptions, and `utilize` should always become `use`.

| Avoid | Use instead |
|---|---|
| utilize | use |
| leverage | use |

We checked every existing model. Roughly 40 percent do not comply. That is worth
fixing now, before the next set of models lands on the same patterns.

Going forward, teams should talk to the data team before naming new models. We
will reply within two working days.
