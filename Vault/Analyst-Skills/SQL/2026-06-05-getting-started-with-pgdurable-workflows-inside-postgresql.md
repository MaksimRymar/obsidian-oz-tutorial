---
title: 'Getting Started with pg_durable: Workflows Inside PostgreSQL'
date: '2026-06-05'
source: https://dev.to/franckpachot/getting-started-with-pgdurable-durable-workflows-inside-postgresql-3980
domain: SQL
relevance: 🟡
tags:
- '#ai'
- '#feature'
- '#library'
- '#sql'
- '#tool'
related:
- '[[2026-03-03-sql-joins-window-functions-the-skills-that-separate-analysts-from-beginners]]'
- '[[2026-06-05-i-got-tired-of-writing-the-same-history-table-boilerplate-so-i-built-a-postgres-extension]]'
- '[[2026-05-29-one-practical-sql-trigger-example-you-can-actually-use]]'
- '[[2026-04-22-understanding-subqueries-vs-ctes-in-sql-with-examples]]'
- '[[2026-04-10-sql-case-expressions-write-smarter-queries-with-conditional-logic]]'
- '[[2026-04-30-subqueries-vs-ctes-in-sql-master-nested-queries-and-write-cleaner-smarter-code]]'
status: unread
---

> **TL;DR:** Modern applications demand long‑lasting workflows that can withstand crashes, restarts, and failures, often relying on external platforms. pg_durable integrates durable workflow orchestration directly into PostgreSQL, en…

## What’s new and why it matters
Modern applications demand long‑lasting workflows that can withstand crashes, restarts, and failures, often relying on external platforms. pg_durable integrates durable workflow orchestration directly into PostgreSQL, enabling workflows to be created in SQL and reliably executed, monitored, inspected, and recovered from disruptions. This tool is particularly useful for ETL processes, data pipelines, background tasks, scheduled jobs, long‑running business procedures, and internal workflow management. To truly grasp its capabilities, the best approach is to try it yourself. I did so by building…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Write the query in a scratchpad and run EXPLAIN/QUERY PLAN to verify performance.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/franckpachot/getting-started-with-pgdurable-durable-workflows-inside-postgresql-3980

## Related notes
- [[2026-03-03-sql-joins-window-functions-the-skills-that-separate-analysts-from-beginners]]
- [[2026-06-05-i-got-tired-of-writing-the-same-history-table-boilerplate-so-i-built-a-postgres-extension]]
- [[2026-05-29-one-practical-sql-trigger-example-you-can-actually-use]]
- [[2026-04-22-understanding-subqueries-vs-ctes-in-sql-with-examples]]
- [[2026-04-10-sql-case-expressions-write-smarter-queries-with-conditional-logic]]
- [[2026-04-30-subqueries-vs-ctes-in-sql-master-nested-queries-and-write-cleaner-smarter-code]]
