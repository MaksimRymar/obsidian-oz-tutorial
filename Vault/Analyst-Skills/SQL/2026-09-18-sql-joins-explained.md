---
title: SQL Joins Explained.
date: '2026-09-18'
source: https://dev.to/josephine_mackylah_d6b31f/joins-explained-nei
domain: SQL
relevance: 🟡
tags:
- '#ai'
- '#sql'
- '#tool'
related:
- '[[2026-09-16-sql-joins-with-examples-of-each]]'
- '[[2026-09-09-sql-joins]]'
- '[[2026-09-15-sql-joins-explained]]'
- '[[2026-09-10-sql-joins-combining-data-across-tables]]'
- '[[2026-04-21-sql-joins-and-window-functions-a-practical-guide]]'
- '[[2026-09-18-understanding-sql-joins]]'
status: unread
---

> **TL;DR:** How Sunrise Supermarket connects its tables Sunrise Supermarket's database isn't one giant table it's four: customers , products , orders , and order_items . Each one holds its own piece of the story. Customers live in o…

## What’s new and why it matters
How Sunrise Supermarket connects its tables Sunrise Supermarket's database isn't one giant table it's four: customers , products , orders , and order_items . Each one holds its own piece of the story. Customers live in one table, products in another, and every order plus what was actually bought in it is split across orders and order_items . That's good design, but it means the information you actually want ("which customer bought what") is scattered across all four. Joins are how you bring them back together. What Are Joins? A join combines rows from two or more tables based on a column they…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Write the query in a scratchpad and run EXPLAIN/QUERY PLAN to verify performance.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/josephine_mackylah_d6b31f/joins-explained-nei

## Related notes
- [[2026-09-16-sql-joins-with-examples-of-each]]
- [[2026-09-09-sql-joins]]
- [[2026-09-15-sql-joins-explained]]
- [[2026-09-10-sql-joins-combining-data-across-tables]]
- [[2026-04-21-sql-joins-and-window-functions-a-practical-guide]]
- [[2026-09-18-understanding-sql-joins]]
