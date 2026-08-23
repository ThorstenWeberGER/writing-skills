# When Routing Breaks, Agents Become the Router

The platform did not fail. The rules nobody owns did, and the cost landed on the
people paid to work around them.

## What The Numbers Actually Say

Median first response has moved from 4.1 hours to 9.6 hours over 90 days, and the
damage is not spread evenly. It concentrates in the two queues fed by the in-app
widget, because the routing rules send widget tickets to the wrong place. Agents
absorbed the difference: 2,840 manual re-routes in the period, roughly 18% of
inbound, at about four minutes of triage each that nobody planned for.

## The Cause Has No Owner

The rules engine was written by a contractor who has since left, and it is
undocumented. That single fact explains three of the four findings in the review.
Treating them as three problems invites three fixes; treating them as one invites
the right one.

## What The Satisfaction Data Can And Cannot Tell You

Customer satisfaction fell from 4.4 to 3.9 in billing and from 4.5 to 4.1 in
technical, the two queues taking the misrouted traffic. The correspondence is
suggestive. It is not proof: a pricing change landed in the same window, and the
review could not separate the two effects. Reporting this as a routing outcome
would overstate what the data supports.

## Sequence Beats Ambition

Q4 capacity is six weeks, and the weekend on-call gap claims two of them. The
eight-week rewrite is the right answer to the underlying fragility and the wrong
answer to this quarter. Patch the widget rules in one week now, and take the
rewrite in Q1 with the whole budget it needs.
