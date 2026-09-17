---
title: 'hot_standby_feedback for a Reporting Replica: Query Cancellations or Primary
  Bloat?'
date: '2026-09-17'
source: https://dev.to/libme/hotstandbyfeedback-for-a-reporting-replica-query-cancellations-or-primary-bloat-mek
domain: SQL
relevance: 🟡
tags:
- '#ai'
- '#sql'
- '#tool'
related:
- '[[2026-09-08-postgres-autovacuum-isnt-keeping-up-diagnosing-bloat-long-transactions-and-wraparound-warnings]]'
- '[[2026-07-06-your-postgres-already-knows-why-its-slow-you-just-have-to-ask-it]]'
- '[[2026-09-03-speeding-up-a-slow-plsql-routine-with-bulk-collect-and-forall]]'
- '[[2026-08-21-null-in-sql-why-null-finds-nothing-and-what-to-write-instead]]'
- '[[2026-08-11-sql-joins-how-to-join-two-tables-without-losing-or-doubling-rows]]'
- '[[2026-06-29-the-customerid-that-isnt-a-customer]]'
status: unread
---

> **TL;DR:** For a reporting workload on a Postgres streaming replica, the realistic answer is: keep hot_standby_feedback = on , but only if you also cap the replica's query duration with statement_timeout . Feedback without a timeou…

## What’s new and why it matters
For a reporting workload on a Postgres streaming replica, the realistic answer is: keep hot_standby_feedback = on , but only if you also cap the replica's query duration with statement_timeout . Feedback without a timeout hands any analyst an unbounded lever on primary bloat; a timeout without feedback means long queries die with "canceling statement due to conflict with recovery." If reporting queries genuinely need hours, stop sharing the HA replica and give reporting its own replica with max_standby_streaming_delay = -1 , accepting that it lags. This came out of a comment on an earlier post…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Write the query in a scratchpad and run EXPLAIN/QUERY PLAN to verify performance.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/libme/hotstandbyfeedback-for-a-reporting-replica-query-cancellations-or-primary-bloat-mek

## Related notes
- [[2026-09-08-postgres-autovacuum-isnt-keeping-up-diagnosing-bloat-long-transactions-and-wraparound-warnings]]
- [[2026-07-06-your-postgres-already-knows-why-its-slow-you-just-have-to-ask-it]]
- [[2026-09-03-speeding-up-a-slow-plsql-routine-with-bulk-collect-and-forall]]
- [[2026-08-21-null-in-sql-why-null-finds-nothing-and-what-to-write-instead]]
- [[2026-08-11-sql-joins-how-to-join-two-tables-without-losing-or-doubling-rows]]
- [[2026-06-29-the-customerid-that-isnt-a-customer]]
