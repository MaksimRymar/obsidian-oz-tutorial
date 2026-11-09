---
title: 'SQL WHERE vs HAVING: Differences, Execution Order and When to Use Each (Tested
  Examples)'
date: '2026-11-09'
source: https://dev.to/mfaysaldev/sql-where-vs-having-differences-execution-order-and-when-to-use-each-tested-examples-59af
domain: SQL
relevance: 🟡
tags:
- '#ai'
- '#sql'
- '#tool'
- '#tutorial'
related:
- '[[2026-10-16-an-ai-explained-sql-group-by-in-four-lines-one-of-them-is-wrong]]'
- '[[2026-06-10-sql-for-data-analysis-the-10-query-patterns-that-matter]]'
- '[[2026-10-26-sql-joins-explained-inner-left-right-and-full-with-examples]]'
- '[[2026-10-15-sql-joins-explained-with-one-tiny-dataset-plus-5-interview-questions]]'
- '[[2026-11-05-sql-inner-join-vs-left-join-vs-right-join-vs-full-outer-join-differences-with-examples-tested-in-mysql-84-and-sqlite]]'
- '[[2026-08-21-how-to-find-duplicate-rows-in-sql-and-decide-what-counts-as-one]]'
status: unread
---

> **TL;DR:** WHERE filters individual rows before they are grouped, and HAVING filters whole groups after GROUP BY has run. That's why only HAVING can use aggregate functions such as SUM() , COUNT() and AVG() . Use WHERE for conditio…

## What’s new and why it matters
WHERE filters individual rows before they are grouped, and HAVING filters whole groups after GROUP BY has run. That's why only HAVING can use aggregate functions such as SUM() , COUNT() and AVG() . Use WHERE for conditions on plain columns, like status = 'paid' , and HAVING for conditions on totals, like SUM(amount) > 100 . You can use both in one query, and WHERE always runs first. The PostgreSQL SELECT reference puts it in one line: WHERE filters individual rows before GROUP BY is applied, while HAVING filters group rows created by GROUP BY. The rest of this guide shows what that means in pr…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Write the query in a scratchpad and run EXPLAIN/QUERY PLAN to verify performance.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/mfaysaldev/sql-where-vs-having-differences-execution-order-and-when-to-use-each-tested-examples-59af

## Related notes
- [[2026-10-16-an-ai-explained-sql-group-by-in-four-lines-one-of-them-is-wrong]]
- [[2026-06-10-sql-for-data-analysis-the-10-query-patterns-that-matter]]
- [[2026-10-26-sql-joins-explained-inner-left-right-and-full-with-examples]]
- [[2026-10-15-sql-joins-explained-with-one-tiny-dataset-plus-5-interview-questions]]
- [[2026-11-05-sql-inner-join-vs-left-join-vs-right-join-vs-full-outer-join-differences-with-examples-tested-in-mysql-84-and-sqlite]]
- [[2026-08-21-how-to-find-duplicate-rows-in-sql-and-decide-what-counts-as-one]]
