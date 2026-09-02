---
title: Keep an ER diagram of your database, updated on every push
date: '2026-09-01'
source: https://dev.to/patu/keep-an-er-diagram-of-your-database-updated-on-every-push-3994
domain: SQL
relevance: 🟡
tags:
- '#sql'
- '#tool'
related:
- '[[2026-08-11-sql-aliases-how-to-read-a-query-out-loud]]'
- '[[2026-08-22-where-to-get-a-sample-database-to-practice-sql-and-how-to-check-it-loaded]]'
- '[[2026-08-31-subquery-vs-cte-in-sql-same-logic-one-you-can-check]]'
- '[[2026-06-28-how-to-generate-a-sql-schema-from-a-csv-file-without-hand-writing-every-column-type]]'
- '[[2026-08-21-column-comments-in-postgresql-and-mysql-how-to-document-columns-without-a-migration]]'
- '[[2026-08-06-drawsql-alternative-an-offline-desktop-erd-tool-with-no-table-limits]]'
status: unread
---

> **TL;DR:** Paste a SQL schema, get an interactive entity-relationship diagram on a stable link. Wire it into CI and the diagram regenerates itself every time the schema changes: no diagram to draw, ever again. The problem with hand…

## What’s new and why it matters
Paste a SQL schema, get an interactive entity-relationship diagram on a stable link. Wire it into CI and the diagram regenerates itself every time the schema changes: no diagram to draw, ever again. The problem with hand-drawn diagrams A database diagram is out of date the moment someone adds a column. You draw it once for the onboarding doc, and three migrations later it lies. mcdview takes the opposite route: the schema file is the source of truth. Point it at your schema.sql and it generates the diagram: a single self-contained HTML page, no runtime, no database connection. What the diagram…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Write the query in a scratchpad and run EXPLAIN/QUERY PLAN to verify performance.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/patu/keep-an-er-diagram-of-your-database-updated-on-every-push-3994

## Related notes
- [[2026-08-11-sql-aliases-how-to-read-a-query-out-loud]]
- [[2026-08-22-where-to-get-a-sample-database-to-practice-sql-and-how-to-check-it-loaded]]
- [[2026-08-31-subquery-vs-cte-in-sql-same-logic-one-you-can-check]]
- [[2026-06-28-how-to-generate-a-sql-schema-from-a-csv-file-without-hand-writing-every-column-type]]
- [[2026-08-21-column-comments-in-postgresql-and-mysql-how-to-document-columns-without-a-migration]]
- [[2026-08-06-drawsql-alternative-an-offline-desktop-erd-tool-with-no-table-limits]]
