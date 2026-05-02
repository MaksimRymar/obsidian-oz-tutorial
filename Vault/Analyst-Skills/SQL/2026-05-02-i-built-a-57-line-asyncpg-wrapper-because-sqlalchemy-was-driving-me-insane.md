---
title: I built a 57-line asyncpg wrapper because SQLAlchemy was driving me insane
date: '2026-05-02'
source: https://dev.to/kernz/i-built-a-57-line-asyncpg-wrapper-because-sqlalchemy-was-driving-me-insane-16jg
domain: SQL
relevance: 🟡
tags:
- '#feature'
- '#python'
- '#sql'
- '#support-analytics'
- '#tool'
- '#tutorial'
related:
- '[[2026-02-24-database-decoded-navigating-queries-in-fastapi-django-orm-vs-raw-sql]]'
- '[[2026-02-20-how-i-built-an-advanced-sql-tutorial-and-self-hosted-it-on-my-own-nas]]'
- '[[2026-03-12-sql-join-tutorial-inner-left-right-full-outer-explained]]'
- '[[2026-04-15-how-to-build-a-strong-foundation-in-sql-and-databases-step-by-step]]'
- '[[2026-04-24-the-sql-query-mistakes-that-cost-me-points-in-my-database-assignment]]'
- '[[2026-03-26-sqlite-is-enough-for-your-side-project-full-text-search-json-and-wal-mode-included]]'
status: unread
---

> **TL;DR:** I came from Rust where I used sqlx — you write raw SQL, you get typed structs back. Simple, honest, fast. Then I had to write Python and reached for SQLAlchemy. Big mistake. Suddenly I was learning a DSL on top of SQL. D…

## What’s new and why it matters
I came from Rust where I used sqlx — you write raw SQL, you get typed structs back. Simple, honest, fast. Then I had to write Python and reached for SQLAlchemy. Big mistake. Suddenly I was learning a DSL on top of SQL. Debugging what ORM decided to generate behind my back. Fighting N+1 queries I didn't even know were happening. Writing text() to escape into raw SQL anyway. So I built EzQL. What is it? A minimal wrapper around asyncpg. You write SQL. You get typed Pydantic models back. That's literally it. The entire core is 57 lines of code. How it works Define your model: from pydantic import…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Write the query in a scratchpad and run EXPLAIN/QUERY PLAN to verify performance.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/kernz/i-built-a-57-line-asyncpg-wrapper-because-sqlalchemy-was-driving-me-insane-16jg

## Related notes
- [[2026-02-24-database-decoded-navigating-queries-in-fastapi-django-orm-vs-raw-sql]]
- [[2026-02-20-how-i-built-an-advanced-sql-tutorial-and-self-hosted-it-on-my-own-nas]]
- [[2026-03-12-sql-join-tutorial-inner-left-right-full-outer-explained]]
- [[2026-04-15-how-to-build-a-strong-foundation-in-sql-and-databases-step-by-step]]
- [[2026-04-24-the-sql-query-mistakes-that-cost-me-points-in-my-database-assignment]]
- [[2026-03-26-sqlite-is-enough-for-your-side-project-full-text-search-json-and-wal-mode-included]]
