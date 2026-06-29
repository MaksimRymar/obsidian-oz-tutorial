---
title: 'Data Analysis SQL: Asking the right questions and using the right tools'
date: '2026-06-28'
source: https://dev.to/lulij/data-analysis-sql-asking-the-right-questions-and-using-the-right-tools-2a5o
domain: SQL
relevance: 🟡
tags:
- '#ai'
- '#career'
- '#sql'
- '#support-analytics'
- '#tool'
related:
- '[[2026-05-10-why-where-phone-null-returns-nothing-in-sql]]'
- '[[2026-03-30-database-indexing-explained-whats-actually-happening-under-the-hood]]'
- '[[2026-04-19-sql-deep-dive-subqueries-vs-ctes-which-one-should-you-use]]'
- '[[2026-04-30-subqueries-vs-ctes-in-sql-master-nested-queries-and-write-cleaner-smarter-code]]'
- '[[2026-05-11-five-sql-patterns-ai-agents-get-wrong-and-how-to-fix-them]]'
- '[[2026-03-09-sql-window-functions-dont-have-to-be-scary]]'
status: unread
---

> **TL;DR:** If you've ever practiced SQL interview questions, you have almost certainly crossed paths with this classic prompt: “Find the second highest salary in the company.” When the problem lands on the table, your first instinc…

## What’s new and why it matters
If you've ever practiced SQL interview questions, you have almost certainly crossed paths with this classic prompt: “Find the second highest salary in the company.” When the problem lands on the table, your first instinct is usually to smile, open your editor, and type this in four seconds: SELECT salary FROM employees ORDER BY salary DESC LIMIT 1 OFFSET 1 ; And just like that, you are probably out of the interview. Not because the syntax is broken—that runs perfectly in PostgreSQL—but because you just committed the cardinal sin of data engineering: you dove right into the code before understa…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Write the query in a scratchpad and run EXPLAIN/QUERY PLAN to verify performance.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/lulij/data-analysis-sql-asking-the-right-questions-and-using-the-right-tools-2a5o

## Related notes
- [[2026-05-10-why-where-phone-null-returns-nothing-in-sql]]
- [[2026-03-30-database-indexing-explained-whats-actually-happening-under-the-hood]]
- [[2026-04-19-sql-deep-dive-subqueries-vs-ctes-which-one-should-you-use]]
- [[2026-04-30-subqueries-vs-ctes-in-sql-master-nested-queries-and-write-cleaner-smarter-code]]
- [[2026-05-11-five-sql-patterns-ai-agents-get-wrong-and-how-to-fix-them]]
- [[2026-03-09-sql-window-functions-dont-have-to-be-scary]]
