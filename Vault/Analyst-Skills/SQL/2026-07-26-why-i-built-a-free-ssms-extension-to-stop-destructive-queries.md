---
title: Why I Built a Free SSMS Extension to Stop Destructive Queries
date: '2026-07-26'
source: https://dev.to/manuelenzo/why-i-built-a-free-ssms-extension-to-stop-destructive-queries-npo
domain: SQL
relevance: 🟡
tags:
- '#best-practice'
- '#sql'
- '#tool'
related:
- '[[2026-05-09-how-i-built-a-real-time-postgresql-wal-reader-in-go]]'
- '[[2026-05-12-10-sql-changes-one-took-30-seconds-it-cut-query-time-by-85]]'
- '[[2026-04-21-sql-nulls-demystified-what-they-are-and-how-to-handle-them]]'
- '[[2026-04-03-i-got-tired-of-watching-my-terminal-so-i-built-guga]]'
- '[[2026-03-15-easy-query-the-most-powerful-orm-for-java]]'
- '[[2026-04-13-how-i-learned-sql-by-creating-a-simple-school-database]]'
status: unread
---

> **TL;DR:** The moment that started it A colleague of mine was cleaning up some old records in a staging environment. Same query he'd run a dozen times before, except this time he was connected to production. He hit F5. No WHERE cla…

## What’s new and why it matters
The moment that started it A colleague of mine was cleaning up some old records in a staging environment. Same query he'd run a dozen times before, except this time he was connected to production. He hit F5. No WHERE clause. 47,000 rows gone in milliseconds . We recovered from a backup, lost about two hours, and nobody got fired. But it stuck with me:** SSMS will let you delete an entire production table with the same amount of friction as running a SELECT 1**. No pause, no confirmation, nothing. The tool that DBAs and backend developers spend all day in has zero built-in protection against th…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Write the query in a scratchpad and run EXPLAIN/QUERY PLAN to verify performance.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/manuelenzo/why-i-built-a-free-ssms-extension-to-stop-destructive-queries-npo

## Related notes
- [[2026-05-09-how-i-built-a-real-time-postgresql-wal-reader-in-go]]
- [[2026-05-12-10-sql-changes-one-took-30-seconds-it-cut-query-time-by-85]]
- [[2026-04-21-sql-nulls-demystified-what-they-are-and-how-to-handle-them]]
- [[2026-04-03-i-got-tired-of-watching-my-terminal-so-i-built-guga]]
- [[2026-03-15-easy-query-the-most-powerful-orm-for-java]]
- [[2026-04-13-how-i-learned-sql-by-creating-a-simple-school-database]]
