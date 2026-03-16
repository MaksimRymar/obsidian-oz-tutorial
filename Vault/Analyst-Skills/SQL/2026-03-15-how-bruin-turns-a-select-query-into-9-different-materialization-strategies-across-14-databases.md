---
title: How Bruin turns a SELECT query into 9 different materialization strategies
  across 14 databases
date: '2026-03-15'
source: https://dev.to/terzioglub/how-bruin-turns-a-select-query-into-9-different-materialization-strategies-across-14-databases-34dk
domain: SQL
relevance: 🟡
tags:
- '#ai'
- '#best-practice'
- '#feature'
- '#library'
- '#python'
- '#sql'
- '#tool'
related:
- '[[2026-03-01-sql-joins]]'
- '[[2026-03-08-understanding-group-by-in-sql]]'
- '[[2026-03-01-joins-and-windows-functions-in-sql]]'
- '[[2026-03-12-sql-join-tutorial-inner-left-right-full-outer-explained]]'
- '[[2026-03-03-sql-joins-window-functions-the-skills-that-separate-analysts-from-beginners]]'
- '[[2026-02-24-stop-using-any-the-wrong-way-in-rails]]'
status: unread
---

> **TL;DR:** You write SELECT * FROM orders WHERE dt > '2024-01-01' . But that query alone doesn't create a table, update a partition, or merge with existing records. Something has to wrap your SQL in the right DDL/DML for your speci…

## What’s new and why it matters
You write SELECT * FROM orders WHERE dt > '2024-01-01' . But that query alone doesn't create a table, update a partition, or merge with existing records. Something has to wrap your SQL in the right DDL/DML for your specific database, strategy, and context. In Bruin, that something is the materialization system. It takes your query, looks at your config, and generates the exact SQL needed to materialize the result. Pure string manipulation with a clear purpose. I want to walk through how it actually works, because the architecture is simpler than you'd expect for something that handles 9 strate…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Write the query in a scratchpad and run EXPLAIN/QUERY PLAN to verify performance.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/terzioglub/how-bruin-turns-a-select-query-into-9-different-materialization-strategies-across-14-databases-34dk

## Related notes
- [[2026-03-01-sql-joins]]
- [[2026-03-08-understanding-group-by-in-sql]]
- [[2026-03-01-joins-and-windows-functions-in-sql]]
- [[2026-03-12-sql-join-tutorial-inner-left-right-full-outer-explained]]
- [[2026-03-03-sql-joins-window-functions-the-skills-that-separate-analysts-from-beginners]]
- [[2026-02-24-stop-using-any-the-wrong-way-in-rails]]
