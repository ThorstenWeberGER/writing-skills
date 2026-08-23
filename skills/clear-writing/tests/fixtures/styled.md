We got the new pipeline live last week. It was messier than I expected. The old cron jobs had hidden assumptions baked in that nobody documented, so every time we moved one over, something else broke downstream. It took about three weeks longer than planned.

The upside is that the new setup is much easier to reason about. Everything runs through one scheduler now instead of four, and when something fails you can see why without connecting to a box directly.

There is still some cleanup left. Two legacy jobs run in both systems until we are confident the new ones match. I want to remove the old ones by the end of the month.
