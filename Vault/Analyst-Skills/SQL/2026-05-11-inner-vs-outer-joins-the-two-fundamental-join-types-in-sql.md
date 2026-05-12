---
title: 'Inner vs Outer Joins: The Two Fundamental Join Types in SQL'
date: '2026-05-11'
source: https://dev.to/michaelfv/inner-vs-outer-joins-the-two-fundamental-join-types-in-sql-2jf5
domain: SQL
relevance: 🟡
tags:
- '#ai'
- '#sql'
- '#tool'
related:
- '[[2026-03-01-sql-joins]]'
- '[[2026-03-05-joins-and-window-functions-in-sql]]'
- '[[2026-03-10-joins-window-functions]]'
- '[[2026-03-02-simple-guides-to-table-joins-and-window-functions-in-sql]]'
- '[[2026-03-02-joins-and-window-functions-in-sql]]'
- '[[2026-04-19-sql-joins-explained-simply---a-beginners-guide]]'
status: unread
---

> **TL;DR:** SQL joins fall into two fundamental categories — inner joins and outer joins — while LEFT , RIGHT , and FULL joins are subclasses of the outer join. This hierarchy is defined by the logical principle of "which rows are i…

## What’s new and why it matters
SQL joins fall into two fundamental categories — inner joins and outer joins — while LEFT , RIGHT , and FULL joins are subclasses of the outer join. This hierarchy is defined by the logical principle of "which rows are included in the result set" and "which table's unmatched rows are preserved". The Two Fundamental Types Type Core Logic Result Set INNER JOIN "Match only — discard what doesn't match" Returns only rows that satisfy the join condition in both tables. OUTER JOIN "Keep one side as the base — pad NULLs where no match exists" Returns all rows from one (or both) tables, filling in NUL…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Write the query in a scratchpad and run EXPLAIN/QUERY PLAN to verify performance.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/michaelfv/inner-vs-outer-joins-the-two-fundamental-join-types-in-sql-2jf5

## Related notes
- [[2026-03-01-sql-joins]]
- [[2026-03-05-joins-and-window-functions-in-sql]]
- [[2026-03-10-joins-window-functions]]
- [[2026-03-02-simple-guides-to-table-joins-and-window-functions-in-sql]]
- [[2026-03-02-joins-and-window-functions-in-sql]]
- [[2026-04-19-sql-joins-explained-simply---a-beginners-guide]]
