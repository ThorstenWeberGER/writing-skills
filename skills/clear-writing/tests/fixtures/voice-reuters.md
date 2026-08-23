# Support platform routing fault doubles response times, fix set for this quarter

- Median first response slipped to 9.6 hours from 4.1 over 90 days
- Routing rules misdirect in-app widget tickets to the wrong queue
- Agents re-routed 2,840 tickets by hand, roughly 18% of inbound
- One-week patch set for this quarter, full rewrite deferred to Q1

A fault in the support platform's routing rules has more than doubled median
first-response time, to 9.6 hours from 4.1 over the past 90 days, according to a
review of ticket data and interviews with eight staff.

The rules send tickets raised through the in-app widget to the wrong queue,
forcing agents to re-route 2,840 of them by hand, roughly 18% of inbound volume.

Customer satisfaction fell to 3.9 from 4.4 in the billing queue and to 4.1 from
4.5 in the technical queue, the two receiving the misdirected traffic. A pricing
change landed in the same window, however, and the review could not separate the
two effects.

The team will patch the widget rules in one engineering week this quarter and
defer the eight-week rewrite to the first quarter. Six weeks of available
capacity, less two weeks committed to a weekend on-call gap, could not
accommodate the rewrite now, the review said.
