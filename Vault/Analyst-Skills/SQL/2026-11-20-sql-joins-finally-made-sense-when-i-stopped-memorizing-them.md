---
title: SQL JOINs finally made sense when I stopped memorizing them
date: '2026-11-20'
source: https://dev.to/stackcraftstudio/sql-joins-finally-made-sense-when-i-stopped-memorizing-them-577h
domain: SQL
relevance: 🟡
tags:
- '#sql'
- '#tool'
related:
- '[[2026-10-26-sql-joins-explained-inner-left-right-and-full-with-examples]]'
- '[[2026-11-04-sql-window-functions-clicked-when-i-stopped-collapsing-rows]]'
- '[[2026-09-16-sql-joins-with-examples-of-each]]'
- '[[2026-10-10-sql-indexes-explained-for-people-who-just-got-yelled-at-by-a-slow-dashboard]]'
- '[[2026-05-01-joins-combining-tables-without-losing-your-mind]]'
- '[[2026-11-05-sql-inner-join-vs-left-join-vs-right-join-vs-full-outer-join-differences-with-examples-tested-in-mysql-84-and-sqlite]]'
status: unread
---

> **TL;DR:** I spent an embarrassing amount of my first year writing SQL by vibes. JOIN especially. INNER JOIN? LEFT JOIN? I had memorized the Venn diagrams like they were multiplication tables, and I still froze every time a query n…

## What’s new and why it matters
I spent an embarrassing amount of my first year writing SQL by vibes. JOIN especially. INNER JOIN? LEFT JOIN? I had memorized the Venn diagrams like they were multiplication tables, and I still froze every time a query needed more than one table. What fixed it was stopping memorization entirely and thinking about one question instead: which table keeps all its rows? The only question that matters Every JOIN is just: match rows from table A with rows from table B on some key. The join type answers one thing - who survives when there is no match? INNER JOIN - nobody survives without a match. Onl…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Write the query in a scratchpad and run EXPLAIN/QUERY PLAN to verify performance.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/stackcraftstudio/sql-joins-finally-made-sense-when-i-stopped-memorizing-them-577h

## Related notes
- [[2026-10-26-sql-joins-explained-inner-left-right-and-full-with-examples]]
- [[2026-11-04-sql-window-functions-clicked-when-i-stopped-collapsing-rows]]
- [[2026-09-16-sql-joins-with-examples-of-each]]
- [[2026-10-10-sql-indexes-explained-for-people-who-just-got-yelled-at-by-a-slow-dashboard]]
- [[2026-05-01-joins-combining-tables-without-losing-your-mind]]
- [[2026-11-05-sql-inner-join-vs-left-join-vs-right-join-vs-full-outer-join-differences-with-examples-tested-in-mysql-84-and-sqlite]]
