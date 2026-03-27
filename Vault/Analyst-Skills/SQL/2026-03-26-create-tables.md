---
title: Create Tables
date: '2026-03-26'
source: https://dev.to/sandhya_steffym_4872a8be/create-tables-3gc9
domain: SQL
relevance: 🟡
tags:
- '#ai'
- '#sql'
- '#tool'
related:
- '[[2026-03-05-learning-sql-join-and-window-functions]]'
- '[[2026-03-26-alter-table]]'
- '[[2026-03-26-design-a-reliable-wallet-transfer-system-with-acid-guarantees-pt---1-atomicity]]'
- '[[2026-03-20-postgresql-constraints]]'
- '[[2026-03-25-isolation]]'
- '[[2026-03-25-consistency]]'
status: unread
---

> **TL;DR:** Today I learned how to create tables in SQL and how to apply different constraints. At first, it felt confusing, but when I understood the purpose behind each rule, it became much easier. Let me explain each task in a si…

## What’s new and why it matters
Today I learned how to create tables in SQL and how to apply different constraints. At first, it felt confusing, but when I understood the purpose behind each rule, it became much easier. Let me explain each task in a simple way. Creating a Students Table First, I created a table called students. Each student should have an id, name, and age. The important thing here is that id must be unique, so we use a PRIMARY KEY. CREATE TABLE students ( id SERIAL PRIMARY KEY, name VARCHAR(100), age INT ); Here, PRIMARY KEY ensures that no two students will have the same id. Employees Table with Required F…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Write the query in a scratchpad and run EXPLAIN/QUERY PLAN to verify performance.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/sandhya_steffym_4872a8be/create-tables-3gc9

## Related notes
- [[2026-03-05-learning-sql-join-and-window-functions]]
- [[2026-03-26-alter-table]]
- [[2026-03-26-design-a-reliable-wallet-transfer-system-with-acid-guarantees-pt---1-atomicity]]
- [[2026-03-20-postgresql-constraints]]
- [[2026-03-25-isolation]]
- [[2026-03-25-consistency]]
