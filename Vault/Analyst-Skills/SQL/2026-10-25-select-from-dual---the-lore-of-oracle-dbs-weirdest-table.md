---
title: '`SELECT * FROM DUAL` - The Lore of Oracle DB''s Weirdest Table'
date: '2026-10-25'
source: https://dev.to/shikarisohan/select-from-dual-the-lore-of-oracle-dbs-weirdest-table-4bdk
domain: SQL
relevance: 🔴
tags:
- '#career'
- '#feature'
- '#sql'
- '#tool'
- '#tutorial'
related:
- '[[2026-06-15-day-01-of-learning-data-engineering-step1-sql-joins-and-set-operators]]'
- '[[2026-09-09-still-writing-slow-sql-queries-10-ways-to-improve-performance]]'
- '[[2026-04-22-sql-set-operators-union-intersect-and-except-explained-simply]]'
- '[[2026-10-18-introduction-to-databases-and-sql-with-postgresql-window-functions-joins-ctes-and-subqueries-on-a-simple-hospital-databa]]'
- '[[2026-10-15-sql-joins-explained-with-one-tiny-dataset-plus-5-interview-questions]]'
- '[[2026-05-31-i-didnt-have-a-pc-for-my-database-class-so-i-built-my-own-t-sql-sandbox-in-the-browser]]'
status: unread
---

> **TL;DR:** If you've ever written Oracle SQL, you've probably typed this: SELECT SYSDATE FROM DUAL ; I use DUAL constantly. Billing queries, rate validations, migration scripts. Yet for months, I never stopped to ask: why does this…

## What’s new and why it matters
If you've ever written Oracle SQL, you've probably typed this: SELECT SYSDATE FROM DUAL ; I use DUAL constantly. Billing queries, rate validations, migration scripts. Yet for months, I never stopped to ask: why does this table even exist? Then one afternoon, I ran: SELECT * FROM DUAL ; DUMMY ----- X One column. One row. The letter X . That's it. So I went down the rabbit hole. The Man Behind DUAL The story goes back to Oracle's early days and an engineer named Charles "Chuck" Weiss . DUAL was originally created as an internal object in Oracle's data dictionary. Weiss explained its purpose in O…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Write the query in a scratchpad and run EXPLAIN/QUERY PLAN to verify performance.
- Add a short note: what changed in your workflow?

## Relevance
🔴

## Source
https://dev.to/shikarisohan/select-from-dual-the-lore-of-oracle-dbs-weirdest-table-4bdk

## Related notes
- [[2026-06-15-day-01-of-learning-data-engineering-step1-sql-joins-and-set-operators]]
- [[2026-09-09-still-writing-slow-sql-queries-10-ways-to-improve-performance]]
- [[2026-04-22-sql-set-operators-union-intersect-and-except-explained-simply]]
- [[2026-10-18-introduction-to-databases-and-sql-with-postgresql-window-functions-joins-ctes-and-subqueries-on-a-simple-hospital-databa]]
- [[2026-10-15-sql-joins-explained-with-one-tiny-dataset-plus-5-interview-questions]]
- [[2026-05-31-i-didnt-have-a-pc-for-my-database-class-so-i-built-my-own-t-sql-sandbox-in-the-browser]]
