---
title: JSONB vs columns in PostgreSQL, measured on 2 million rows
date: '2026-11-10'
source: https://dev.to/importstatic/jsonb-vs-columns-in-postgresql-measured-on-2-million-rows-39ee
domain: SQL
relevance: 🟡
tags:
- '#ai'
- '#sql'
- '#tool'
related:
- '[[2026-09-16-sql-joins-with-examples-of-each]]'
- '[[2026-08-31-temp-table-vs-view-in-sql-a-saved-answer-or-a-saved-question]]'
- '[[2026-10-26-sql-joins-explained-inner-left-right-and-full-with-examples]]'
- '[[2026-11-09-sql-where-vs-having-differences-execution-order-and-when-to-use-each-tested-examples]]'
- '[[2026-10-15-the-list-shows-two-numbers-so-the-query-digs-them-out-of-the-json-instead-of-loading-a-hundred-attempts]]'
- '[[2026-11-09-my-latest-20-issues-query-read-200000-rows-even-with-an-index-on-projectid]]'
status: unread
---

> **TL;DR:** Originally published on ImportStatic . Storing rows as a jsonb document in PostgreSQL instead of typed columns costs a lot in storage and updates and little in indexed lookups, and a GIN index beats a single-column btree…

## What’s new and why it matters
Originally published on ImportStatic . Storing rows as a jsonb document in PostgreSQL instead of typed columns costs a lot in storage and updates and little in indexed lookups, and a GIN index beats a single-column btree when a query combines keys. Those are the results of loading the same 2 million orders into both layouts on PostgreSQL 18.6 and comparing storage, filters, aggregates, indexes, planner estimates and updates. The question came from a Hacker News thread about shredding JSON columns , which asked how much difference remains in Postgres once the JSON is properly indexed. The plann…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Write the query in a scratchpad and run EXPLAIN/QUERY PLAN to verify performance.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/importstatic/jsonb-vs-columns-in-postgresql-measured-on-2-million-rows-39ee

## Related notes
- [[2026-09-16-sql-joins-with-examples-of-each]]
- [[2026-08-31-temp-table-vs-view-in-sql-a-saved-answer-or-a-saved-question]]
- [[2026-10-26-sql-joins-explained-inner-left-right-and-full-with-examples]]
- [[2026-11-09-sql-where-vs-having-differences-execution-order-and-when-to-use-each-tested-examples]]
- [[2026-10-15-the-list-shows-two-numbers-so-the-query-digs-them-out-of-the-json-instead-of-loading-a-hundred-attempts]]
- [[2026-11-09-my-latest-20-issues-query-read-200000-rows-even-with-an-index-on-projectid]]
