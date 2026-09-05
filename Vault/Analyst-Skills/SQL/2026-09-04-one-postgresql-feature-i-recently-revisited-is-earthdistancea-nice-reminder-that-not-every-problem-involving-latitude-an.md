---
title: 'One PostgreSQL feature I recently revisited is earthdistance—a nice reminder
  that not every problem involving latitude and longitude requires a full GIS stack.


  The earthdistance extension provides a straightforward way to calculate great-circle
  distances'
date: '2026-09-04'
source: https://dev.to/dshumw/one-postgresql-feature-i-recently-revisited-is-earthdistance-a-nice-reminder-that-not-every-problem-4m0j
domain: SQL
relevance: 🟡
tags:
- '#feature'
- '#sql'
related:
- '[[2026-09-04-postgres-earthdistance]]'
- '[[2026-07-24-how-i-cut-our-database-costs-by-40-with-one-config-change-connection-pooling-explained]]'
- '[[2026-08-11-code-interpreter-is-infrastructure-not-a-prompt]]'
- '[[2026-04-18-postgresql-jsonb-indexing-gin-expression-partial-index-strategies]]'
- '[[2026-06-23-how-a-map-works-mercator-tiles-and-your-gps-pin]]'
- '[[2026-09-01-synthetic-data-generation-faker-sdv-gretel-mimesis-for-safe-test-pipelines]]'
status: unread
---

> **TL;DR:** One PostgreSQL feature I recently revisited is earthdistance—a nice reminder that not every problem involving latitude and longitude requires a full GIS stack. The earthdistance extension provides a straightforward way t…

## What’s new and why it matters
One PostgreSQL feature I recently revisited is earthdistance—a nice reminder that not every problem involving latitude and longitude requires a full GIS stack.

The earthdistance extension provides a straightforward way to calculate great-circle distances.

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Write the query in a scratchpad and run EXPLAIN/QUERY PLAN to verify performance.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/dshumw/one-postgresql-feature-i-recently-revisited-is-earthdistance-a-nice-reminder-that-not-every-problem-4m0j

## Related notes
- [[2026-09-04-postgres-earthdistance]]
- [[2026-07-24-how-i-cut-our-database-costs-by-40-with-one-config-change-connection-pooling-explained]]
- [[2026-08-11-code-interpreter-is-infrastructure-not-a-prompt]]
- [[2026-04-18-postgresql-jsonb-indexing-gin-expression-partial-index-strategies]]
- [[2026-06-23-how-a-map-works-mercator-tiles-and-your-gps-pin]]
- [[2026-09-01-synthetic-data-generation-faker-sdv-gretel-mimesis-for-safe-test-pipelines]]
