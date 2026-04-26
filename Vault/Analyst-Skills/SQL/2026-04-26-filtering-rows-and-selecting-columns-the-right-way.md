---
title: Filtering Rows and Selecting Columns (The Right Way)
date: '2026-04-26'
source: https://dev.to/yakhilesh/filtering-rows-and-selecting-columns-the-right-way-2d30
domain: SQL
relevance: 🟡
tags:
- '#ai'
- '#best-practice'
- '#python'
- '#sql'
- '#tool'
related:
- '[[2026-04-22-sql-set-operators-union-intersect-and-except-explained-simply]]'
- '[[2026-04-20-up-down-or-down-up-understanding-subqueries-and-ctes-in-sql-a-comprehensive-guide]]'
- '[[2026-04-24-sql-like-and-wildcards-pattern-matching-made-simple]]'
- '[[2026-04-25-6-essential-sql-concepts-every-beginner-should-master]]'
- '[[2026-04-09-sql-where-clause-the-complete-guide-to-filtering-data]]'
- '[[2026-04-23-i-built-a-browser-only-sql-practice-tool-because-installing-dbeaver-is-a-productivity-tax]]'
status: unread
---

> **TL;DR:** You know df["column"] selects a column. You know df.head() shows the top rows. But in real analysis, you need surgical precision. Give me rows 50 through 200 where salary is above the median and department is not Sales,…

## What’s new and why it matters
You know df["column"] selects a column. You know df.head() shows the top rows. But in real analysis, you need surgical precision. Give me rows 50 through 200 where salary is above the median and department is not Sales, and only show me the name, age, and salary columns. That sentence is one Pandas expression when you know what you are doing. Three nested loops when you do not. This post is about knowing what you are doing. Two Ways to Select: loc and iloc These are the two main selectors. They look similar but they think differently. iloc thinks in positions. Row 0 is the first row. Column 2…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Write the query in a scratchpad and run EXPLAIN/QUERY PLAN to verify performance.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/yakhilesh/filtering-rows-and-selecting-columns-the-right-way-2d30

## Related notes
- [[2026-04-22-sql-set-operators-union-intersect-and-except-explained-simply]]
- [[2026-04-20-up-down-or-down-up-understanding-subqueries-and-ctes-in-sql-a-comprehensive-guide]]
- [[2026-04-24-sql-like-and-wildcards-pattern-matching-made-simple]]
- [[2026-04-25-6-essential-sql-concepts-every-beginner-should-master]]
- [[2026-04-09-sql-where-clause-the-complete-guide-to-filtering-data]]
- [[2026-04-23-i-built-a-browser-only-sql-practice-tool-because-installing-dbeaver-is-a-productivity-tax]]
