We finally got the new pipeline live last week. It was messier than I expected. The old cron jobs had a bunch of hidden assumptions baked in that nobody documented, so every time we moved one over something else broke downstream. Took about three weeks longer than planned.

The upside is that the new setup is much easier to reason about. Everything runs through one scheduler now instead of four, and when something fails you can actually see why without SSHing into a box.

Still some cleanup left. Two legacy jobs are running in both systems until we're confident the new ones match. I'd like to kill the old ones by end of month.
