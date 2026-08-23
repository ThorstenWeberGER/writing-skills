The new pipeline is live. Migration took three weeks longer than planned because undocumented assumptions in the old cron jobs broke downstream consumers.

One scheduler replaces four, and failures are now diagnosable without shell access. Two legacy jobs still run in parallel; recommend decommissioning by month end.
