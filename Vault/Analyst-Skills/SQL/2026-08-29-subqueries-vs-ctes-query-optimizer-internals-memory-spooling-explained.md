---
title: 'Subqueries vs CTEs: Query Optimizer Internals & Memory Spooling Explained'
date: '2026-08-29'
source: https://dev.to/arpitmbangre/subqueries-vs-ctes-query-optimizer-internals-memory-spooling-explained-4mlm
domain: SQL
relevance: 🟡
tags:
- '#best-practice'
- '#sql'
- '#tool'
- '#zendesk'
related:
- '[[2026-04-26-sql-subqueries-vs-ctes-a-complete-guide-for-data-analysts-published]]'
- '[[2026-04-02-ctes-vs-subqueries-in-sql-which-one-should-you-use]]'
- '[[2026-06-02-5-sql-queries-developers-always-have-to-look-up-with-copy-paste-answers]]'
- '[[2026-05-11-five-sql-patterns-ai-agents-get-wrong-and-how-to-fix-them]]'
- '[[2026-06-13-top-12-sql-interview-problems-for-data-engineers-with-answers]]'
- '[[2026-05-03-claudemd-for-postgresql-13-rules-that-make-ai-write-safe-production-ready-sql]]'
status: unread
---

> **TL;DR:** Many engineers believe Common Table Expressions ( CTEs ) are always faster than subqueries . In modern SQL Server ( and PostgreSQL ), ** that is a myth ** . Here is what actually happens under the hood : ### 1 . Inlining…

## What’s new and why it matters
Many engineers believe Common Table Expressions ( CTEs ) are always faster than subqueries . In modern SQL Server ( and PostgreSQL ), ** that is a myth ** . Here is what actually happens under the hood : ### 1 . Inlining & The Query Optimizer By default , the SQL optimizer treats standard CTEs and derived tables ( subqueries ) almost identically : - The engine expands both into the same relational tree . - They generate the ** exact same execution plan and I / O cost ** . sql -- Pattern A: Derived Table (Subquery) SELECT DeptID, EmpName, Salary FROM ( SELECT DeptID, EmpName, Salary, DENSE_RANK…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Write the query in a scratchpad and run EXPLAIN/QUERY PLAN to verify performance.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/arpitmbangre/subqueries-vs-ctes-query-optimizer-internals-memory-spooling-explained-4mlm

## Related notes
- [[2026-04-26-sql-subqueries-vs-ctes-a-complete-guide-for-data-analysts-published]]
- [[2026-04-02-ctes-vs-subqueries-in-sql-which-one-should-you-use]]
- [[2026-06-02-5-sql-queries-developers-always-have-to-look-up-with-copy-paste-answers]]
- [[2026-05-11-five-sql-patterns-ai-agents-get-wrong-and-how-to-fix-them]]
- [[2026-06-13-top-12-sql-interview-problems-for-data-engineers-with-answers]]
- [[2026-05-03-claudemd-for-postgresql-13-rules-that-make-ai-write-safe-production-ready-sql]]
