---
title: How to auto-grade SQL exercises against a real SQLite database
date: '2026-11-14'
source: https://dev.to/ashwin31/how-to-auto-grade-sql-exercises-against-a-real-sqlite-database-f0
domain: SQL
relevance: 🟡
tags:
- '#ai'
- '#library'
- '#python'
- '#sql'
- '#tool'
- '#tutorial'
related:
- '[[2026-08-31-running-total-in-sql-the-window-frame-that-decides-the-answer]]'
- '[[2026-11-09-sql-where-vs-having-differences-execution-order-and-when-to-use-each-tested-examples]]'
- '[[2026-11-11-your-unique-constraint-in-postgresql-lets-duplicates-through-here-is-how-to-find-every-one]]'
- '[[2026-08-11-sql-aliases-how-to-read-a-query-out-loud]]'
- '[[2026-10-17-server-side-sorting-and-filtering-for-a-react-data-grid-and-five-places-your-sql-quietly-disagree]]'
- '[[2026-08-21-which-sql-database-should-you-install]]'
status: unread
---

> **TL;DR:** If you teach SQL, you've probably tried grading by comparing a student's query with your own. It doesn't work, because two correct queries rarely look alike. All three of these answer the same question, and all three pas…

## What’s new and why it matters
If you teach SQL, you've probably tried grading by comparing a student's query with your own. It doesn't work, because two correct queries rarely look alike. All three of these answer the same question, and all three pass the grader in this post: SELECT member , SUM ( days ) FROM loans GROUP BY member HAVING SUM ( days ) >= CAST ( readfile ( 'input' ) AS INTEGER ) ; SELECT member , total FROM ( SELECT member , SUM ( days ) AS total FROM loans GROUP BY member ) WHERE total >= CAST ( readfile ( 'input' ) AS INTEGER ) ; WITH totals AS ( SELECT member , SUM ( days ) AS total FROM loans GROUP BY me…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Write the query in a scratchpad and run EXPLAIN/QUERY PLAN to verify performance.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/ashwin31/how-to-auto-grade-sql-exercises-against-a-real-sqlite-database-f0

## Related notes
- [[2026-08-31-running-total-in-sql-the-window-frame-that-decides-the-answer]]
- [[2026-11-09-sql-where-vs-having-differences-execution-order-and-when-to-use-each-tested-examples]]
- [[2026-11-11-your-unique-constraint-in-postgresql-lets-duplicates-through-here-is-how-to-find-every-one]]
- [[2026-08-11-sql-aliases-how-to-read-a-query-out-loud]]
- [[2026-10-17-server-side-sorting-and-filtering-for-a-react-data-grid-and-five-places-your-sql-quietly-disagree]]
- [[2026-08-21-which-sql-database-should-you-install]]
