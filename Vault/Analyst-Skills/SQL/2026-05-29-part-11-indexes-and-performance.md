---
title: 'Part 11: Indexes and Performance'
date: '2026-05-29'
source: https://dev.to/edriso/part-11-indexes-and-performance-44h2
domain: SQL
relevance: 🟡
tags:
- '#sql'
- '#tool'
related:
- '[[2026-03-30-database-indexing-explained-whats-actually-happening-under-the-hood]]'
- '[[2026-05-29-part-12-transactions]]'
- '[[2026-03-02-database-indexing-explained-how-to-make-your-queries-1000x-faster]]'
- '[[2026-02-28-database-indexing-made-easy-sql-vs-mongodb]]'
- '[[2026-05-27-why-your-sql-looks-like-a-mess-and-how-to-fix-it-in-seconds]]'
- '[[2026-04-15-sql-limit-and-offset-paginate-your-query-results-like-a-pro]]'
status: unread
---

> **TL;DR:** Part of the "SQL: Zero to Ninja" series, written for junior web devs. Your app worked great with 200 users. Then it got popular, hit a million rows, and one page started taking 8 whole seconds to load. Same query, same c…

## What’s new and why it matters
Part of the "SQL: Zero to Ninja" series, written for junior web devs. Your app worked great with 200 users. Then it got popular, hit a million rows, and one page started taking 8 whole seconds to load. Same query, same code, nothing changed. So what happened? Your database was quietly reading every single row, every single time. Let's fix that with indexes, and then squash the sneaky N+1 bug that haunts almost every ORM app. The idea in one line An index is a sorted shortcut that lets the database jump straight to the rows you want, instead of reading the whole table to find them. The metaphor…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Write the query in a scratchpad and run EXPLAIN/QUERY PLAN to verify performance.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/edriso/part-11-indexes-and-performance-44h2

## Related notes
- [[2026-03-30-database-indexing-explained-whats-actually-happening-under-the-hood]]
- [[2026-05-29-part-12-transactions]]
- [[2026-03-02-database-indexing-explained-how-to-make-your-queries-1000x-faster]]
- [[2026-02-28-database-indexing-made-easy-sql-vs-mongodb]]
- [[2026-05-27-why-your-sql-looks-like-a-mess-and-how-to-fix-it-in-seconds]]
- [[2026-04-15-sql-limit-and-offset-paginate-your-query-results-like-a-pro]]
