---
title: SQL UNION vs UNION ALL vs INTERSECT vs EXCEPT
date: '2026-05-23'
source: https://dev.to/gowthampotureddi/sql-union-vs-union-all-vs-intersect-vs-except-ih0
domain: SQL
relevance: 🟡
tags:
- '#ai'
- '#best-practice'
- '#career'
- '#library'
- '#sql'
- '#tool'
- '#tutorial'
- '#zendesk'
related:
- '[[2026-04-22-sql-set-operators-union-intersect-and-except-explained-simply]]'
- '[[2026-05-11-postgresql-sql-data-types-practical-column-type-guide]]'
- '[[2026-04-19-sql-deep-dive-subqueries-vs-ctes-which-one-should-you-use]]'
- '[[2026-03-01-sql-joins]]'
- '[[2026-03-12-sql-join-tutorial-inner-left-right-full-outer-explained]]'
- '[[2026-04-23-i-built-a-browser-only-sql-practice-tool-because-installing-dbeaver-is-a-productivity-tax]]'
status: unread
---

> **TL;DR:** sql set operations stitch two or more result sets together along the row axis: union sql stacks rows and drops duplicates, union all sql stacks rows and keeps every duplicate, intersect sql keeps only rows that appear in…

## What’s new and why it matters
sql set operations stitch two or more result sets together along the row axis: union sql stacks rows and drops duplicates, union all sql stacks rows and keeps every duplicate, intersect sql keeps only rows that appear in both inputs, and except sql (called minus sql in Oracle) keeps rows from the left input that do not appear in the right. These four operators answer the bulk of the sql interview questions in the "combine result sets" cluster, and the union vs union all distinction alone trips up more candidates than almost any other shape on a SQL whiteboard. This guide walks through every op…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Write the query in a scratchpad and run EXPLAIN/QUERY PLAN to verify performance.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/gowthampotureddi/sql-union-vs-union-all-vs-intersect-vs-except-ih0

## Related notes
- [[2026-04-22-sql-set-operators-union-intersect-and-except-explained-simply]]
- [[2026-05-11-postgresql-sql-data-types-practical-column-type-guide]]
- [[2026-04-19-sql-deep-dive-subqueries-vs-ctes-which-one-should-you-use]]
- [[2026-03-01-sql-joins]]
- [[2026-03-12-sql-join-tutorial-inner-left-right-full-outer-explained]]
- [[2026-04-23-i-built-a-browser-only-sql-practice-tool-because-installing-dbeaver-is-a-productivity-tax]]
