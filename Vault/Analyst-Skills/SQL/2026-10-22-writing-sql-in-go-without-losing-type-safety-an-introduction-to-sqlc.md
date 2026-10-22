---
title: 'Writing SQL in Go Without Losing Type Safety: An Introduction to sqlc'
date: '2026-10-22'
source: https://dev.to/jlamka/writing-sql-in-go-without-losing-type-safety-an-introduction-to-sqlc-11d8
domain: SQL
relevance: 🟡
tags:
- '#sql'
- '#tool'
related:
- '[[2026-09-29-sql-joins-how-to-combine-tables-the-right-way]]'
- '[[2026-09-15-sql-joins-explained]]'
- '[[2026-05-03-i-built-a-sast-scanner-from-scratch-heres-every-design-decision-i-made]]'
- '[[2026-03-09-mastering-sql-joins-and-window-functions-with-real-examples]]'
- '[[2026-05-18-top-orm-tools-practical-comparison]]'
- '[[2026-09-09-when-one-query-isnt-enough-a-love-letter-to-ctes-and-subqueries-in-postgresql]]'
status: unread
---

> **TL;DR:** One thing I've been exploring after GopherCon Africa 2026 is how Go developers work with databases. That's where I came across sqlc, a tool that makes writing database code in Go a little more interesting. So, what does…

## What’s new and why it matters
One thing I've been exploring after GopherCon Africa 2026 is how Go developers work with databases. That's where I came across sqlc, a tool that makes writing database code in Go a little more interesting. So, what does it actually do? What is sqlc? When building an application, you might write SQL queries to fetch or insert data into a database. You then need Go code to execute those queries and work with the results. Usually, this means writing some extra code to connect the two. sqlc generates Go code from your SQL queries, allowing you to write the SQL yourself while getting generated Go f…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Write the query in a scratchpad and run EXPLAIN/QUERY PLAN to verify performance.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/jlamka/writing-sql-in-go-without-losing-type-safety-an-introduction-to-sqlc-11d8

## Related notes
- [[2026-09-29-sql-joins-how-to-combine-tables-the-right-way]]
- [[2026-09-15-sql-joins-explained]]
- [[2026-05-03-i-built-a-sast-scanner-from-scratch-heres-every-design-decision-i-made]]
- [[2026-03-09-mastering-sql-joins-and-window-functions-with-real-examples]]
- [[2026-05-18-top-orm-tools-practical-comparison]]
- [[2026-09-09-when-one-query-isnt-enough-a-love-letter-to-ctes-and-subqueries-in-postgresql]]
