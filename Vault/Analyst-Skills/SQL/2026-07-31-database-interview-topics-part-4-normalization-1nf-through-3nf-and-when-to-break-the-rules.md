---
title: 'Database Interview Topics Part 4: Normalization, 1NF Through 3NF, and When
  to Break the Rules'
date: '2026-07-31'
source: https://dev.to/manoharij/database-interview-topics-part-4-normalization-1nf-through-3nf-and-when-to-break-the-rules-4c0f
domain: SQL
relevance: 🟡
tags:
- '#ai'
- '#career'
- '#sql'
- '#tool'
- '#zendesk'
related:
- '[[2026-07-24-database-interview-topics-part-1-sql-joins-explained-with-examples]]'
- '[[2026-07-23-btree-height-after-delete-postgresql-fast-root]]'
- '[[2026-04-19-sql-joins-explained-simply---a-beginners-guide]]'
- '[[2026-07-29-database-interview-topics-part-3-stored-procedures-views-and-transactions]]'
- '[[2026-03-05-learning-sql-join-and-window-functions]]'
- '[[2026-04-21-sql-joins-and-window-functions-a-practical-guide]]'
status: unread
---

> **TL;DR:** Part 1 of this series covered joins. Part 2 covered indexing. Part 3 covered stored procedures, views, and transactions. This closing part covers normalization - and rather than abstract rule definitions, it takes one ge…

## What’s new and why it matters
Part 1 of this series covered joins. Part 2 covered indexing. Part 3 covered stored procedures, views, and transactions. This closing part covers normalization - and rather than abstract rule definitions, it takes one genuinely messy sample table and fixes it one normal form at a time, so each rule is visible in an actual before and after rather than just described. The Messy Starting Table OrderId CustomerName CustomerPhones ProductNames CityId CityName 1 Alex Kim 555-1234, 555-5678 Mouse, Keyboard 10 Chicago 2 Priya Shah 555-9999 Monitor 20 Denver 3 Alex Kim 555-1234, 555-5678 Webcam 10 Chic…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Write the query in a scratchpad and run EXPLAIN/QUERY PLAN to verify performance.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/manoharij/database-interview-topics-part-4-normalization-1nf-through-3nf-and-when-to-break-the-rules-4c0f

## Related notes
- [[2026-07-24-database-interview-topics-part-1-sql-joins-explained-with-examples]]
- [[2026-07-23-btree-height-after-delete-postgresql-fast-root]]
- [[2026-04-19-sql-joins-explained-simply---a-beginners-guide]]
- [[2026-07-29-database-interview-topics-part-3-stored-procedures-views-and-transactions]]
- [[2026-03-05-learning-sql-join-and-window-functions]]
- [[2026-04-21-sql-joins-and-window-functions-a-practical-guide]]
