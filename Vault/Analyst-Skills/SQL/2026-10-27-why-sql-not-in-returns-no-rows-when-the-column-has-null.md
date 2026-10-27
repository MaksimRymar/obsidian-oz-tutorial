---
title: Why SQL NOT IN returns no rows when the column has NULL
date: '2026-10-27'
source: https://dev.to/realdev9868/why-sql-not-in-returns-no-rows-when-the-column-has-null-5h2m
domain: SQL
relevance: 🟡
tags:
- '#best-practice'
- '#career'
- '#python'
- '#sql'
- '#tool'
- '#zendesk'
related:
- '[[2026-10-16-an-ai-explained-sql-group-by-in-four-lines-one-of-them-is-wrong]]'
- '[[2026-10-16-one-null-in-the-subquery-and-your-not-in-returned-nothing]]'
- '[[2026-10-24-how-to-find-missing-ids-between-two-lists-and-get-the-sql-for-free]]'
- '[[2026-10-15-sql-joins-explained-with-one-tiny-dataset-plus-5-interview-questions]]'
- '[[2026-09-29-the-not-in-trap-why-your-sql-query-returns-zero-rows]]'
- '[[2026-07-02-dont-use-not-in]]'
status: unread
---

> **TL;DR:** You write a query to drop a few blocked customers. The blocked list has two real ids and one NULL. You expect everyone else. You get nothing. That is the NOT IN plus NULL trap. It shows up in interviews and in production…

## What’s new and why it matters
You write a query to drop a few blocked customers. The blocked list has two real ids and one NULL. You expect everyone else. You get nothing. That is the NOT IN plus NULL trap. It shows up in interviews and in production reports. Here it is on a small SQLite dataset, with every result taken from a real run on Python 3.13's sqlite3. The tiny dataset Five customers. One of them has no city yet. SELECT id , name , city FROM customers ORDER BY id ; 1 | Asha | Pune 2 | Ravi | Delhi 3 | Meera | NULL 4 | Kabir | Pune 5 | Neha | Mumbai A blocked list. Two real ids, and one NULL (a bad import, a left j…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Write the query in a scratchpad and run EXPLAIN/QUERY PLAN to verify performance.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/realdev9868/why-sql-not-in-returns-no-rows-when-the-column-has-null-5h2m

## Related notes
- [[2026-10-16-an-ai-explained-sql-group-by-in-four-lines-one-of-them-is-wrong]]
- [[2026-10-16-one-null-in-the-subquery-and-your-not-in-returned-nothing]]
- [[2026-10-24-how-to-find-missing-ids-between-two-lists-and-get-the-sql-for-free]]
- [[2026-10-15-sql-joins-explained-with-one-tiny-dataset-plus-5-interview-questions]]
- [[2026-09-29-the-not-in-trap-why-your-sql-query-returns-zero-rows]]
- [[2026-07-02-dont-use-not-in]]
