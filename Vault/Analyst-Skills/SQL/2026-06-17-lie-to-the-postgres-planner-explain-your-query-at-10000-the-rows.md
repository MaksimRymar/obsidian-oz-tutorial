---
title: 'Lie to the Postgres planner: EXPLAIN your query at 10,000 the rows'
date: '2026-06-17'
source: https://dev.to/hitoshi1964/lie-to-the-postgres-planner-explain-your-query-at-10000-the-rows-2gkp
domain: SQL
relevance: 🟡
tags:
- '#python'
- '#sql'
- '#tool'
related:
- '[[2026-03-30-database-indexing-explained-whats-actually-happening-under-the-hood]]'
- '[[2026-03-09-sql-window-functions-dont-have-to-be-scary]]'
- '[[2026-06-10-sql-for-data-analysis-the-10-query-patterns-that-matter]]'
- '[[2026-04-14-why-postgresql-ignores-your-index]]'
- '[[2026-04-21-sql-window-functions-and-ctes]]'
- '[[2026-03-03-sql-joins-window-functions-the-skills-that-separate-analysts-from-beginners]]'
status: unread
---

> **TL;DR:** Your query is snappy in dev. Then it hits production data and the plan quietly flips from an Index Scan to a Seq Scan, or a Nested Loop to a Hash Join, and everything falls over. The painful part: you can't see that comi…

## What’s new and why it matters
Your query is snappy in dev. Then it hits production data and the plan quietly flips from an Index Scan to a Seq Scan, or a Nested Loop to a Hash Join, and everything falls over. The painful part: you can't see that coming on a dev database with 5,000 rows , because the planner picks plans based on how big it thinks the tables are. So let's change what it thinks. The planner runs on pg_class statistics When Postgres plans a query, it doesn't count your rows — it reads cached estimates from the catalog, mainly pg_class.reltuples (estimated row count) and relpages (size in pages). ANALYZE refres…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Write the query in a scratchpad and run EXPLAIN/QUERY PLAN to verify performance.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/hitoshi1964/lie-to-the-postgres-planner-explain-your-query-at-10000-the-rows-2gkp

## Related notes
- [[2026-03-30-database-indexing-explained-whats-actually-happening-under-the-hood]]
- [[2026-03-09-sql-window-functions-dont-have-to-be-scary]]
- [[2026-06-10-sql-for-data-analysis-the-10-query-patterns-that-matter]]
- [[2026-04-14-why-postgresql-ignores-your-index]]
- [[2026-04-21-sql-window-functions-and-ctes]]
- [[2026-03-03-sql-joins-window-functions-the-skills-that-separate-analysts-from-beginners]]
