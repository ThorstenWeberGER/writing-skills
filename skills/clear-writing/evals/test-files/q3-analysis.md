# Q3 Support Platform Review

## Background

The support platform has been in place since 2021. It handles inbound tickets
across email, chat and the in-app widget, and routes them to one of four queues
based on a rules engine that was written by a contractor who has since left.
Ticket volume has grown steadily in line with customer growth, which is what we
would expect.

## Methodology

We pulled 90 days of ticket data from the warehouse, cross-referenced it against
the CSAT survey responses, and interviewed six agents and two team leads. We also
reviewed the on-call log for the same period. Where the data was ambiguous we
erred on the side of the more conservative interpretation.

## Findings

**Finding 1: first-response time has degraded.** Median first response moved from
4.1 hours to 9.6 hours across the 90 days. The degradation is not uniform; it is
concentrated in the two queues that the rules engine feeds from the in-app widget.

**Finding 2: agents are re-routing tickets manually.** Agents manually re-routed
2,840 tickets in the period, roughly 18% of inbound. Each manual re-route costs
an agent about four minutes of triage they would not otherwise do. Interviews
confirmed this is because the rules engine sends widget tickets to the wrong queue.

**Finding 3: CSAT has dropped in two queues.** CSAT fell from 4.4 to 3.9 in the
billing queue and from 4.5 to 4.1 in the technical queue. These are the same two
queues that receive misrouted widget traffic. It should be said, however, that we
cannot fully separate this from the pricing change that landed in the same window,
so the causal link to routing is plausible but not established.

**Finding 4: the on-call rota is understaffed at weekends.** Weekend on-call has
been a single engineer since the team reorganisation toward the end of last month.
Two of the three sev-2 incidents in the period happened at weekends and both took
over two hours to acknowledge.

## Discussion

Taken together, the picture is one of a platform whose routing layer is no longer
fit for purpose. The rules engine is undocumented, its author has left, and it is
now the proximate cause of the response-time degradation, the manual re-routing
burden, and most likely the CSAT decline as well. The weekend on-call gap is a
separate matter but is worth flagging in the same breath because it also drives
resolution time.

## Options

We considered three options. Option A is to rewrite the rules engine, which we
estimate at eight engineering weeks. Option B is to replace it with a vendor
product, which carries a licence cost of roughly $60k a year and a migration of
perhaps four weeks. Option C is to patch the widget routing rules only, which is
about one engineering week but leaves the underlying fragility in place.

Our available Q4 engineering capacity is six weeks. We also need two weeks for
the weekend on-call fix, which involves hiring rather than engineering but does
need engineering time to hand over the runbook.

## Conclusion

We recommend Option C now and Option A in Q1. Patching the widget routing rules
would recover most of the first-response degradation within one week, at which
point the manual re-routing burden should largely disappear. The full rewrite is
the right long-term answer but does not fit in Q4 alongside the on-call work.
