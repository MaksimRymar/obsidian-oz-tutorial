---
title: 'BigQuery MERGE Is Not a Uniqueness Constraint: A Replay-Safe Tutorial'
date: '2026-11-12'
source: https://dev.to/saravanan_techx/bigquery-merge-is-not-a-uniqueness-constraint-a-replay-safe-tutorial-32a4
domain: SQL
relevance: 🟡
tags:
- '#ai'
- '#sql'
- '#tool'
- '#tutorial'
related:
- '[[2026-06-10-sql-for-data-analysis-the-10-query-patterns-that-matter]]'
- '[[2026-11-11-your-unique-constraint-in-postgresql-lets-duplicates-through-here-is-how-to-find-every-one]]'
- '[[2026-06-13-top-12-sql-interview-problems-for-data-engineers-with-answers]]'
- '[[2026-08-21-how-to-find-duplicate-rows-in-sql-and-decide-what-counts-as-one]]'
- '[[2026-09-01-seeding-fixtures-realistic-test-data-for-warehouse-integration-tests]]'
- '[[2026-10-30-count-accepted-jobs-not-successful-api-calls-when-comparing-ai-workflows]]'
status: unread
---

> **TL;DR:** A MERGE can be atomic and still leave duplicate business keys. The missing ingredient is a clear key and version contract. This tutorial builds a current-state orders table, not an event-history table. One row represents…

## What’s new and why it matters
A MERGE can be atomic and still leave duplicate business keys. The missing ingredient is a clear key and version contract. This tutorial builds a current-state orders table, not an event-history table. One row represents one order_id . It assumes a single writer and a source-provided, monotonically increasing integer version per order. Timestamps alone are not that contract. Why the obvious MERGE fails If two source rows match one existing target row and an update is required, BigQuery can reject the merge. If the key is absent from the target, multiple source rows can instead be inserted: row…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Write the query in a scratchpad and run EXPLAIN/QUERY PLAN to verify performance.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/saravanan_techx/bigquery-merge-is-not-a-uniqueness-constraint-a-replay-safe-tutorial-32a4

## Related notes
- [[2026-06-10-sql-for-data-analysis-the-10-query-patterns-that-matter]]
- [[2026-11-11-your-unique-constraint-in-postgresql-lets-duplicates-through-here-is-how-to-find-every-one]]
- [[2026-06-13-top-12-sql-interview-problems-for-data-engineers-with-answers]]
- [[2026-08-21-how-to-find-duplicate-rows-in-sql-and-decide-what-counts-as-one]]
- [[2026-09-01-seeding-fixtures-realistic-test-data-for-warehouse-integration-tests]]
- [[2026-10-30-count-accepted-jobs-not-successful-api-calls-when-comparing-ai-workflows]]
