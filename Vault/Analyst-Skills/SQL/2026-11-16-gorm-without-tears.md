---
title: GORM Without Tears
date: '2026-11-16'
source: https://dev.to/jtonny490/gorm-without-tears-15oj
domain: SQL
relevance: 🟡
tags:
- '#best-practice'
- '#feature'
- '#sql'
- '#support-analytics'
- '#tool'
related:
- '[[2026-05-20-learning-sql-as-if-you-built-it-yourself]]'
- '[[2026-09-25-5-sql-patterns-that-run-fine-and-still-return-the-wrong-answer]]'
- '[[2026-11-13-5-sql-mistakes-that-return-the-wrong-number-with-no-error-reproduce-each-one-in-postgres]]'
- '[[2026-03-30-database-indexing-explained-whats-actually-happening-under-the-hood]]'
- '[[2026-09-15-sql-joins-explained]]'
- '[[2026-08-28-stop-writing-raw-sql-in-your-migrations-most-of-the-time]]'
status: unread
---

> **TL;DR:** Models, Migrations, and Relationships There is a moment in every Go developer's life when they stare at a raw SQL string spread across four lines, with a fifth line of rows.Scan(&a, &b, &c, &d, &e, &f) , and think: surel…

## What’s new and why it matters
Models, Migrations, and Relationships There is a moment in every Go developer's life when they stare at a raw SQL string spread across four lines, with a fifth line of rows.Scan(&a, &b, &c, &d, &e, &f) , and think: surely there's a better way. There is. It's called an ORM, and in the Go world the popular one is GORM . It translates between the world of Go structs and the world of database tables, so you can say "save this user" instead of hand-writing an INSERT statement and wrangling columns. But GORM is also a tool with sharp corners. Used well, it saves hours. Used carelessly, it produces t…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Write the query in a scratchpad and run EXPLAIN/QUERY PLAN to verify performance.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/jtonny490/gorm-without-tears-15oj

## Related notes
- [[2026-05-20-learning-sql-as-if-you-built-it-yourself]]
- [[2026-09-25-5-sql-patterns-that-run-fine-and-still-return-the-wrong-answer]]
- [[2026-11-13-5-sql-mistakes-that-return-the-wrong-number-with-no-error-reproduce-each-one-in-postgres]]
- [[2026-03-30-database-indexing-explained-whats-actually-happening-under-the-hood]]
- [[2026-09-15-sql-joins-explained]]
- [[2026-08-28-stop-writing-raw-sql-in-your-migrations-most-of-the-time]]
