---
title: My first SQL lesson learned the hard way
date: '2026-11-14'
source: https://dev.to/dewton_97927134e207/my-first-sql-lesson-learned-the-hard-way-1di3
domain: SQL
relevance: 🟡
tags:
- '#sql'
related:
- '[[2026-11-11-mastering-sql-anti-joins-finding-missing-records-with-left-join-and-is-null]]'
- '[[2026-10-29-filtering-data-in-sql-a-beginners-guide-to-where-and-like-and-friends]]'
- '[[2026-10-29-two-requests-one-rule-two-rows-fixing-the-insert-where-not-exists-race-in-postgresql]]'
- '[[2026-05-23-insert-update-delete-in-sql-safe-crud-patterns-for-data-engineers]]'
- '[[2026-04-06-the-sql-mistake-everyone-makes-writing-vs-execution-order]]'
- '[[2026-10-25-why-your-sql-query-returns-the-wrong-rows-and-how-where-and-order-by-fix-it]]'
status: unread
---

> **TL;DR:** I forgot the WHERE clause on my first UPDATE while practising and changed every row in my test table. Lesson: write the SELECT with the same WHERE first, check the rows, then run the UPDATE. What’s your beginner SQL mist…

## What’s new and why it matters
I forgot the WHERE clause on my first UPDATE while practising and changed every row in my test table. Lesson: write the SELECT with the same WHERE first, check the rows, then run the UPDATE. What’s your beginner SQL mistake?

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Write the query in a scratchpad and run EXPLAIN/QUERY PLAN to verify performance.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/dewton_97927134e207/my-first-sql-lesson-learned-the-hard-way-1di3

## Related notes
- [[2026-11-11-mastering-sql-anti-joins-finding-missing-records-with-left-join-and-is-null]]
- [[2026-10-29-filtering-data-in-sql-a-beginners-guide-to-where-and-like-and-friends]]
- [[2026-10-29-two-requests-one-rule-two-rows-fixing-the-insert-where-not-exists-race-in-postgresql]]
- [[2026-05-23-insert-update-delete-in-sql-safe-crud-patterns-for-data-engineers]]
- [[2026-04-06-the-sql-mistake-everyone-makes-writing-vs-execution-order]]
- [[2026-10-25-why-your-sql-query-returns-the-wrong-rows-and-how-where-and-order-by-fix-it]]
