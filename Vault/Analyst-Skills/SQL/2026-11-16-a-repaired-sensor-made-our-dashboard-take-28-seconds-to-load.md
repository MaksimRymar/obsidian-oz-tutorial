---
title: A repaired sensor made our dashboard take 28 seconds to load
date: '2026-11-16'
source: https://dev.to/solutionmarket/a-repaired-sensor-made-our-dashboard-take-28-seconds-to-load-1548
domain: SQL
relevance: 🔴
tags:
- '#ai'
- '#sql'
- '#support-analytics'
- '#tool'
related:
- '[[2026-05-08-from-2-hours-to-3-minutes-eliminating-missed-tests-in-ai-memory-consistency-testing]]'
- '[[2026-09-27-how-to-catch-a-missing-index-in-a-test-when-your-test-table-has-20-rows]]'
- '[[2026-05-29-part-11-indexes-and-performance]]'
- '[[2026-08-31-realtime-access-revocation-data-contracts-30-second-online-classroom-recovery]]'
- '[[2026-10-16-an-ai-explained-sql-group-by-in-four-lines-one-of-them-is-wrong]]'
- '[[2026-08-08-postgresql-internals-what-is-actually-inside-an-8-kb-page]]'
status: unread
---

> **TL;DR:** InfraGuard Engineering Devlog, part 5 of 6. Restoring a stopped sensor on October 30 made telemetry healthier and the console slower. Recorded cold-cache tests averaged 13.3 seconds for the first view and reached 28.5 se…

## What’s new and why it matters
InfraGuard Engineering Devlog, part 5 of 6. Restoring a stopped sensor on October 30 made telemetry healthier and the console slower. Recorded cold-cache tests averaged 13.3 seconds for the first view and reached 28.5 seconds. A weak-TLS aggregation was responsible. Recent 24-hour TLS data had grown to 3.01 million of 11.67 million rows. The optimizer changed its access plan; one query took 13–36 seconds. One covering index helped An index covering time and TLS version let this query read the index alone. The recorded online build took 82 seconds and added 353 MB. The aggregation then complete…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Write the query in a scratchpad and run EXPLAIN/QUERY PLAN to verify performance.
- Add a short note: what changed in your workflow?

## Relevance
🔴

## Source
https://dev.to/solutionmarket/a-repaired-sensor-made-our-dashboard-take-28-seconds-to-load-1548

## Related notes
- [[2026-05-08-from-2-hours-to-3-minutes-eliminating-missed-tests-in-ai-memory-consistency-testing]]
- [[2026-09-27-how-to-catch-a-missing-index-in-a-test-when-your-test-table-has-20-rows]]
- [[2026-05-29-part-11-indexes-and-performance]]
- [[2026-08-31-realtime-access-revocation-data-contracts-30-second-online-classroom-recovery]]
- [[2026-10-16-an-ai-explained-sql-group-by-in-four-lines-one-of-them-is-wrong]]
- [[2026-08-08-postgresql-internals-what-is-actually-inside-an-8-kb-page]]
