# Data quality issue, internal note

We found duplicate customer records in the warehouse. The duplication started
some time toward the end of last month, most likely when the new ingestion job
went live. Roughly four thousand accounts are affected, though we are still
counting. Invoicing should be held until we have deduplicated, because a
duplicated account bills twice.

We do not yet know whether the older records or the newer ones are authoritative.
