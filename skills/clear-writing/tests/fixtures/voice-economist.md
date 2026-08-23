# Why nobody owns the rules

*A contractor left, the code stayed, and the queue got longer*

When the Ostrogoths cut Rome's aqueducts in 537 they did not need to storm the
walls. Infrastructure nobody defends is the cheapest thing to break. Something
similar has happened to a support platform whose routing rules were written by a
contractor, documented by nobody, and left running for four years. Median first
response has gone from 4.1 hours to 9.6 over 90 days. The rules send tickets from
the in-app widget to the wrong queue, and agents have been quietly fixing them by
hand.

There are three reasons the damage spread further than the fault. One is volume:
2,840 manual re-routes in 90 days, roughly a fifth of everything arriving, at four
minutes of triage each. The second reason is concentration. The misrouted traffic
lands in two queues, billing and technical, whose satisfaction scores fell from
4.4 to 3.9 and from 4.5 to 4.1. The third reason is that nobody could say why,
because the routing logic had no owner to ask.

Has the routing caused the drop in satisfaction? Probably, and not provably. A
pricing change landed in the same window, and the two effects cannot be pulled
apart with the data to hand. Prudence suggests treating the correlation as
suggestive and the cause as open.

The remedy is unglamorous. One engineering week patches the widget rules and
recovers most of the delay. Eight weeks rewrites the engine properly, which is the
right answer and the wrong quarter: six weeks of capacity, less two for a weekend
on-call gap, does not stretch to eight. So the patch goes in now and the rewrite
waits. Which is roughly how Rome managed it, eventually.
