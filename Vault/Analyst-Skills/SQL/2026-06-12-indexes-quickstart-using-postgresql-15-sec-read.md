---
title: 'Indexes: Quickstart Using PostgreSQL (15 sec read)'
date: '2026-06-12'
source: https://dev.to/effessdev/indexes-quickstart-using-postgresql-min-read-55ee
domain: SQL
relevance: 🟡
tags:
- '#sql'
related:
- '[[2026-02-28-clustered-vs-non-clustered-index-in-sqlcomplete-guide-with-examples]]'
- '[[2026-05-10-why-where-phone-null-returns-nothing-in-sql]]'
- '[[2026-04-24-sql-like-and-wildcards-pattern-matching-made-simple]]'
- '[[2026-04-11-master-mysql-views-and-window-functions-advanced-query-optimization-guide]]'
- '[[2026-04-29-postgresql-subquery-and-cte-optimization]]'
- '[[2026-02-27-sql-query-optimization-15-techniques-to-speed-up-your-database-2026]]'
status: unread
---

> **TL;DR:** Let's consider a table user . When we execute a query to find Emily , we are actually going through each record , looking whether the name column equals Emily . Indexes comes in when you want to speed this up. Let's crea…

## What’s new and why it matters
Let's consider a table user . When we execute a query to find Emily , we are actually going through each record , looking whether the name column equals Emily . Indexes comes in when you want to speed this up. Let's create an Index with the name idx_users_name (the name can be anything, and it doesn't matter functionally): CREATE INDEX idx_users_name ON users ( name ); Now when you run SELECT * FROM users WHERE name = 'Emily' ; Postgres will use the index we just created (not by the name, the name is just for us) to execute that query, and the time complexity is reduced from O(n) to O(log n) .

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Write the query in a scratchpad and run EXPLAIN/QUERY PLAN to verify performance.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/effessdev/indexes-quickstart-using-postgresql-min-read-55ee

## Related notes
- [[2026-02-28-clustered-vs-non-clustered-index-in-sqlcomplete-guide-with-examples]]
- [[2026-05-10-why-where-phone-null-returns-nothing-in-sql]]
- [[2026-04-24-sql-like-and-wildcards-pattern-matching-made-simple]]
- [[2026-04-11-master-mysql-views-and-window-functions-advanced-query-optimization-guide]]
- [[2026-04-29-postgresql-subquery-and-cte-optimization]]
- [[2026-02-27-sql-query-optimization-15-techniques-to-speed-up-your-database-2026]]
