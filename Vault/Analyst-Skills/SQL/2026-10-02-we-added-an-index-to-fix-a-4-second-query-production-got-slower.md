---
title: We Added an Index to Fix a 4-Second Query. Production Got Slower.
date: '2026-10-02'
source: https://medium.com/engineering-playbook/we-added-an-index-to-fix-a-4-second-query-production-got-slower-28325efafce0?source=rss------sql-5
domain: SQL
relevance: 🟡
tags:
- '#sql'
related:
- '[[2026-03-28-this-join-took-47-seconds-the-cartesian-product-we-didnt-see]]'
- '[[2026-09-30-10-postgresql-interview-questions-senior-backend-engineers-should-be-able-to-answer]]'
- '[[2026-05-18-how-we-cut-bigquery-slot-usage-by-90-on-one-of-our-most-resource-hungry-service-after-an-outage]]'
- '[[2026-03-10-how-we-got-llms-to-query-our-database-without-leaking-a-single-unauthorized-row]]'
- '[[2026-03-17-i-spent-6-months-optimizing-our-database-then-i-added-one-index]]'
- '[[2026-09-26-postgresql-query-slow-in-production-but-fast-locally-10-reasons-i-check-first]]'
status: unread
---

> **TL;DR:** The query dropped from several seconds to well under a hundred milliseconds in our tests, the execution plan looked dramatically better… Continue reading on Engineering Under Pressure »

## What’s new and why it matters
The query dropped from several seconds to well under a hundred milliseconds in our tests, the execution plan looked dramatically better… Continue reading on Engineering Under Pressure »

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Write the query in a scratchpad and run EXPLAIN/QUERY PLAN to verify performance.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://medium.com/engineering-playbook/we-added-an-index-to-fix-a-4-second-query-production-got-slower-28325efafce0?source=rss------sql-5

## Related notes
- [[2026-03-28-this-join-took-47-seconds-the-cartesian-product-we-didnt-see]]
- [[2026-09-30-10-postgresql-interview-questions-senior-backend-engineers-should-be-able-to-answer]]
- [[2026-05-18-how-we-cut-bigquery-slot-usage-by-90-on-one-of-our-most-resource-hungry-service-after-an-outage]]
- [[2026-03-10-how-we-got-llms-to-query-our-database-without-leaking-a-single-unauthorized-row]]
- [[2026-03-17-i-spent-6-months-optimizing-our-database-then-i-added-one-index]]
- [[2026-09-26-postgresql-query-slow-in-production-but-fast-locally-10-reasons-i-check-first]]
