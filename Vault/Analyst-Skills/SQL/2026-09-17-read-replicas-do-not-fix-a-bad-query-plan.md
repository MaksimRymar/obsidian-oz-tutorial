---
title: Read Replicas Do Not Fix a Bad Query Plan
date: '2026-09-17'
source: https://dev.to/_66d02d0cc1ece7d1137c5f/read-replicas-do-not-fix-a-bad-query-plan-4fdn
domain: SQL
relevance: 🟡
tags:
- '#best-practice'
- '#sql'
- '#support-analytics'
- '#tool'
related:
- '[[2026-03-30-database-indexing-explained-whats-actually-happening-under-the-hood]]'
- '[[2026-06-17-lie-to-the-postgres-planner-explain-your-query-at-10000-the-rows]]'
- '[[2026-09-05-how-query-optimizers-work-statistics-cardinality-join-order]]'
- '[[2026-09-14-why-the-index-i-added-made-my-query-slower]]'
- '[[2026-05-20-learning-sql-as-if-you-built-it-yourself]]'
- '[[2026-07-06-your-postgres-already-knows-why-its-slow-you-just-have-to-ask-it]]'
status: unread
---

> **TL;DR:** PagerDuty fired because our order history page stopped responding. I opened the primary's pg_stat_activity and saw the same statement four times: SELECT * FROM orders WHERE customer_id = 88213 ORDER BY created_at DESC LI…

## What’s new and why it matters
PagerDuty fired because our order history page stopped responding. I opened the primary's pg_stat_activity and saw the same statement four times: SELECT * FROM orders WHERE customer_id = 88213 ORDER BY created_at DESC LIMIT 50 ; No index on customer_id . Postgres was running a sequential scan over the whole table, filtering down to 50 rows. Disk read throughput on the primary was pinned, and every other query queued behind it. The fix everyone agreed on in Slack was "add read replicas and move reporting traffic over." We had done exactly that. It made things worse. The replicas were running th…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Write the query in a scratchpad and run EXPLAIN/QUERY PLAN to verify performance.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/_66d02d0cc1ece7d1137c5f/read-replicas-do-not-fix-a-bad-query-plan-4fdn

## Related notes
- [[2026-03-30-database-indexing-explained-whats-actually-happening-under-the-hood]]
- [[2026-06-17-lie-to-the-postgres-planner-explain-your-query-at-10000-the-rows]]
- [[2026-09-05-how-query-optimizers-work-statistics-cardinality-join-order]]
- [[2026-09-14-why-the-index-i-added-made-my-query-slower]]
- [[2026-05-20-learning-sql-as-if-you-built-it-yourself]]
- [[2026-07-06-your-postgres-already-knows-why-its-slow-you-just-have-to-ask-it]]
