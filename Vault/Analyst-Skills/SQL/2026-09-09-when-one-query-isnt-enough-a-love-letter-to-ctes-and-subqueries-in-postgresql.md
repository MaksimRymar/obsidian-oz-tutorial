---
title: 'When One Query Isn''t Enough: A Love Letter to CTEs and Subqueries in PostgreSQL'
date: '2026-09-09'
source: https://dev.to/datawithian/when-one-query-isnt-enough-a-love-letter-to-ctes-and-subqueries-in-postgresql-2oj3
domain: SQL
relevance: 🟡
tags:
- '#ai'
- '#sql'
- '#tableau'
- '#tool'
- '#zendesk'
related:
- '[[2026-04-30-subqueries-vs-ctes-in-sql-master-nested-queries-and-write-cleaner-smarter-code]]'
- '[[2026-09-07-subqueries-ctes-in-sql-what-they-are-and-when-to-use-each]]'
- '[[2026-04-22-understanding-subqueries-vs-ctes-in-sql-with-examples]]'
- '[[2026-09-08-subqueries-vs-ctes-the-sql-showdown-you-didnt-know-you-needed]]'
- '[[2026-04-21-sql-subqueries-vs-ctes-a-guide-to-writing-better-queries]]'
- '[[2026-03-03-sql-joins-window-functions-the-skills-that-separate-analysts-from-beginners]]'
status: unread
---

> **TL;DR:** Introduction If you've spent enough time writing SQL, you've probably reached that point where a query starts simple and then somehow turns into a monster. You begin with: SELECT * FROM trips ; Then someone asks, "Can we…

## What’s new and why it matters
Introduction If you've spent enough time writing SQL, you've probably reached that point where a query starts simple and then somehow turns into a monster. You begin with: SELECT * FROM trips ; Then someone asks, "Can we find the drivers whose average fare is above the overall average?" No problem. You add an AVG() . Then they ask, "Only include drivers who have completed at least five trips." You add a COUNT() . Then comes, "And their average rating should be below 3." Before you know it, you're staring at a query with nested queries inside nested queries, wondering whether you wrote SQL or a…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Write the query in a scratchpad and run EXPLAIN/QUERY PLAN to verify performance.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/datawithian/when-one-query-isnt-enough-a-love-letter-to-ctes-and-subqueries-in-postgresql-2oj3

## Related notes
- [[2026-04-30-subqueries-vs-ctes-in-sql-master-nested-queries-and-write-cleaner-smarter-code]]
- [[2026-09-07-subqueries-ctes-in-sql-what-they-are-and-when-to-use-each]]
- [[2026-04-22-understanding-subqueries-vs-ctes-in-sql-with-examples]]
- [[2026-09-08-subqueries-vs-ctes-the-sql-showdown-you-didnt-know-you-needed]]
- [[2026-04-21-sql-subqueries-vs-ctes-a-guide-to-writing-better-queries]]
- [[2026-03-03-sql-joins-window-functions-the-skills-that-separate-analysts-from-beginners]]
