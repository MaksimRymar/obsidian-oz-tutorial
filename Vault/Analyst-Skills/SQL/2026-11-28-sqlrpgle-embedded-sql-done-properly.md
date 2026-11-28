---
title: 'SQLRPGLE: embedded SQL done properly'
date: '2026-11-28'
source: https://dev.to/rainierio-dev/sqlrpgle-embedded-sql-done-properly-2obi
domain: SQL
relevance: 🔴
tags:
- '#ai'
- '#best-practice'
- '#feature'
- '#library'
- '#sql'
- '#tool'
related:
- '[[2026-09-01-i-raced-six-models-against-each-other-on-digitalocean-inference-the-cheapest-one-won]]'
- '[[2026-10-03-hiding-the-table-is-not-enough-your-llm-can-still-see-the-salary-column]]'
- '[[2026-09-16-sql-joins-with-examples-of-each]]'
- '[[2026-10-16-an-ai-explained-sql-group-by-in-four-lines-one-of-them-is-wrong]]'
- '[[2026-10-26-sql-joins-explained-inner-left-right-and-full-with-examples]]'
- '[[2026-11-09-sql-where-vs-having-differences-execution-order-and-when-to-use-each-tested-examples]]'
status: unread
---

> **TL;DR:** SQLRPGLE: embedded SQL done properly Embedded SQL in RPG is the default way to access Db2 for i in new code. It is also where I most often see sloppy code: no status checks, SELECT * , and cursors left open. This article…

## What’s new and why it matters
SQLRPGLE: embedded SQL done properly Embedded SQL in RPG is the default way to access Db2 for i in new code. It is also where I most often see sloppy code: no status checks, SELECT * , and cursors left open. This article gives a pattern you can paste into a real program. Syntax in **FREE SQL statements start with exec sql and end with a semicolon, and can span lines. The source member type is SQLRPGLE. **free exec sql set option commit = *none, closqlcsr = *endmod, datfmt = *iso; Same program in fixed format (what you will meet in most shops): C/EXEC SQL C+ SET OPTION COMMIT = *NONE, CLOSQLCSR…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Write the query in a scratchpad and run EXPLAIN/QUERY PLAN to verify performance.
- Add a short note: what changed in your workflow?

## Relevance
🔴

## Source
https://dev.to/rainierio-dev/sqlrpgle-embedded-sql-done-properly-2obi

## Related notes
- [[2026-09-01-i-raced-six-models-against-each-other-on-digitalocean-inference-the-cheapest-one-won]]
- [[2026-10-03-hiding-the-table-is-not-enough-your-llm-can-still-see-the-salary-column]]
- [[2026-09-16-sql-joins-with-examples-of-each]]
- [[2026-10-16-an-ai-explained-sql-group-by-in-four-lines-one-of-them-is-wrong]]
- [[2026-10-26-sql-joins-explained-inner-left-right-and-full-with-examples]]
- [[2026-11-09-sql-where-vs-having-differences-execution-order-and-when-to-use-each-tested-examples]]
