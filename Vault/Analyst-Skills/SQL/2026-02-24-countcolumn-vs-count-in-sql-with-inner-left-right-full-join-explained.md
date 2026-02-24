---
title: COUNT(column) vs COUNT(*) in SQL — With INNER, LEFT, RIGHT & FULL JOIN Explained
date: '2026-02-24'
source: https://dev.to/deko39/countcolumn-vs-count-in-sql-with-inner-left-right-full-join-explained-1a1f
domain: SQL
relevance: 🟡
tags:
- '#ai'
- '#sql'
- '#tool'
related:
- '[[2026-02-20-how-i-built-an-advanced-sql-tutorial-and-self-hosted-it-on-my-own-nas]]'
- '[[2026-02-23-flask-vs-nodejs-choosing-the-right-backend-framework-for-2026]]'
- '[[2026-02-24-database-decoded-navigating-queries-in-fastapi-django-orm-vs-raw-sql]]'
- '[[2026-02-23-distributed-locking-in-python]]'
- '[[2026-02-22-5-most-asked-sql-interview-questions]]'
- '[[2026-02-22-stop-wiring-dependencies-by-hand---meet-injectq-python-di-done-right]]'
status: unread
---

> **TL;DR:** Counting seems simple in SQL… until joins enter the picture. One of the most common bugs in reporting queries comes from misunderstanding: COUNT(*) vs COUNT(column) 1. The Core Rule ✅ COUNT(*) -> Counts rows ✅ COUNT(colu…

## What’s new and why it matters
Counting seems simple in SQL… until joins enter the picture. One of the most common bugs in reporting queries comes from misunderstanding: COUNT(*) vs COUNT(column) 1. The Core Rule ✅ COUNT(*) -> Counts rows ✅ COUNT(column) -> Counts non-NULL values in that column That’s it. But joins create NULLs — and that’s where things change. 2. Example setup Customer id name 1 Alice 2 Bob 3 Carol Orders id customer_id 10 1 11 1 12 2 a. INNER JOIN SELECT c.id, COUNT(*), COUNT(o.id) FROM customers c INNER JOIN orders o ON c.id = o.customer_id GROUP BY c.id; id COUNT(*) COUNT(o.id) 1 2 2 2 1 1 Why? INNER JO…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Write the query in a scratchpad and run EXPLAIN/QUERY PLAN to verify performance.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/deko39/countcolumn-vs-count-in-sql-with-inner-left-right-full-join-explained-1a1f

## Related notes
- [[2026-02-20-how-i-built-an-advanced-sql-tutorial-and-self-hosted-it-on-my-own-nas]]
- [[2026-02-23-flask-vs-nodejs-choosing-the-right-backend-framework-for-2026]]
- [[2026-02-24-database-decoded-navigating-queries-in-fastapi-django-orm-vs-raw-sql]]
- [[2026-02-23-distributed-locking-in-python]]
- [[2026-02-22-5-most-asked-sql-interview-questions]]
- [[2026-02-22-stop-wiring-dependencies-by-hand---meet-injectq-python-di-done-right]]
