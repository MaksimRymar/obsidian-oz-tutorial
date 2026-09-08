---
title: '''Column Must Appear in the GROUP BY Clause'' — Why SQL Won''t Let You Do
  That'
date: '2026-09-08'
source: https://dev.to/systemcraftdev/column-must-appear-in-the-group-by-clause-why-sql-wont-let-you-do-that-124a
domain: SQL
relevance: 🟡
tags:
- '#sql'
- '#tool'
- '#tutorial'
related:
- '[[2026-09-07-like-in-sql-explained-for-beginners]]'
- '[[2026-03-09-sql-window-functions-dont-have-to-be-scary]]'
- '[[2026-09-07-why-adding-an-index-wont-fix-your-slow-count-in-postgresql]]'
- '[[2026-04-21-sql-window-functions-and-ctes]]'
- '[[2026-07-22-when-to-trust-ai-generated-sql-and-when-not-to]]'
- '[[2026-06-19-oracle-ora-00934-error-causes-and-solutions-complete-guide]]'
status: unread
---

> **TL;DR:** It isn't a syntax error and it isn't arbitrary. SQL is asking a question it genuinely can't answer on its own — and once you see that, the fix is obvious. Adapted from the SQL Essentials Companion Guide . You add one mor…

## What’s new and why it matters
It isn't a syntax error and it isn't arbitrary. SQL is asking a question it genuinely can't answer on its own — and once you see that, the fix is obvious. Adapted from the SQL Essentials Companion Guide . You add one more column to a GROUP BY query, run it, and get this instead of results: ERROR : column "products.name" must appear in the GROUP BY clause or be used in an aggregate function The query looked reasonable. Nothing is misspelled. But SQL is refusing to run it at all — not returning wrong data, just flatly declining. That refusal is the whole story: SQL isn't confused about syntax, i…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Write the query in a scratchpad and run EXPLAIN/QUERY PLAN to verify performance.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/systemcraftdev/column-must-appear-in-the-group-by-clause-why-sql-wont-let-you-do-that-124a

## Related notes
- [[2026-09-07-like-in-sql-explained-for-beginners]]
- [[2026-03-09-sql-window-functions-dont-have-to-be-scary]]
- [[2026-09-07-why-adding-an-index-wont-fix-your-slow-count-in-postgresql]]
- [[2026-04-21-sql-window-functions-and-ctes]]
- [[2026-07-22-when-to-trust-ai-generated-sql-and-when-not-to]]
- [[2026-06-19-oracle-ora-00934-error-causes-and-solutions-complete-guide]]
