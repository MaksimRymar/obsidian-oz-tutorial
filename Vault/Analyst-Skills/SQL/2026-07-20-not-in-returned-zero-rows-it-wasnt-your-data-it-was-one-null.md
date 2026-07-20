---
title: NOT IN returned zero rows. It wasn't your data — it was one NULL.
date: '2026-07-20'
source: https://dev.to/omer_hochman/not-in-returned-zero-rows-it-wasnt-your-data-it-was-one-null-4inj
domain: SQL
relevance: 🟡
tags:
- '#sql'
related:
- '[[2026-07-02-dont-use-not-in]]'
- '[[2026-06-10-sql-for-data-analysis-the-10-query-patterns-that-matter]]'
- '[[2026-06-13-top-12-sql-interview-problems-for-data-engineers-with-answers]]'
- '[[2026-07-09-why-one-sql-join-returns-5-rows-and-another-returns-12]]'
- '[[2026-04-21-two-sql-null-traps-missing-join-rows-and-unique-constraints-that-do-nothing]]'
- '[[2026-05-20-learning-sql-as-if-you-built-it-yourself]]'
status: unread
---

> **TL;DR:** Originally published at nlqdb.com/blog "Which customers never placed an order?" is a question you ask constantly — products never sold, users with no login this month, invoices with no payment. It's a set difference, and…

## What’s new and why it matters
Originally published at nlqdb.com/blog "Which customers never placed an order?" is a question you ask constantly — products never sold, users with no login this month, invoices with no payment. It's a set difference, and the obvious query is a quiet trap: SELECT * FROM customers WHERE id NOT IN ( SELECT customer_id FROM orders ); -- returns nothing. why? If a single customer_id in that subquery is NULL, you get zero rows — no error, no warning. Here's why: NOT IN (a, b, NULL) expands to id <> a AND id <> b AND id <> NULL . That last comparison is never true — comparing anything to NULL is unkn…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Write the query in a scratchpad and run EXPLAIN/QUERY PLAN to verify performance.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/omer_hochman/not-in-returned-zero-rows-it-wasnt-your-data-it-was-one-null-4inj

## Related notes
- [[2026-07-02-dont-use-not-in]]
- [[2026-06-10-sql-for-data-analysis-the-10-query-patterns-that-matter]]
- [[2026-06-13-top-12-sql-interview-problems-for-data-engineers-with-answers]]
- [[2026-07-09-why-one-sql-join-returns-5-rows-and-another-returns-12]]
- [[2026-04-21-two-sql-null-traps-missing-join-rows-and-unique-constraints-that-do-nothing]]
- [[2026-05-20-learning-sql-as-if-you-built-it-yourself]]
