---
title: 1.1.3 Optimizable vs Utility
date: '2026-05-05'
source: https://dev.to/joonghyukshin/113-optimizable-vs-utility-51bl
domain: SQL
relevance: 🟡
tags:
- '#ai'
- '#best-practice'
- '#feature'
- '#sql'
- '#tool'
related:
- '[[2026-04-22-sql-set-operators-union-intersect-and-except-explained-simply]]'
- '[[2026-04-02-ctes-vs-subqueries-in-sql-which-one-should-you-use]]'
- '[[2026-04-23-i-built-a-browser-only-sql-practice-tool-because-installing-dbeaver-is-a-productivity-tax]]'
- '[[2026-04-21-sql-window-functions-and-ctes]]'
- '[[2026-04-30-subqueries-vs-ctes-in-sql-master-nested-queries-and-write-cleaner-smarter-code]]'
- '[[2026-04-22-understanding-subqueries-vs-ctes-in-sql-with-examples]]'
status: unread
---

> **TL;DR:** Inside the five-stage pipeline from 1.1.1, there is another fork right after the parser. PostgreSQL classifies every SQL command into one of two camps. One side holds the optimizable queries, the other holds the utility…

## What’s new and why it matters
Inside the five-stage pipeline from 1.1.1, there is another fork right after the parser. PostgreSQL classifies every SQL command into one of two camps. One side holds the optimizable queries, the other holds the utility commands. The classification is decided by a single field on the Query node, commandType , and from that point on the two camps travel completely different paths . One goes through the rewriter, the planner, and the executor. The other bypasses all three. This fork was a single line in the 1.1.1 picture, but it shapes the entire internal structure of PostgreSQL, so it earns its…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Write the query in a scratchpad and run EXPLAIN/QUERY PLAN to verify performance.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/joonghyukshin/113-optimizable-vs-utility-51bl

## Related notes
- [[2026-04-22-sql-set-operators-union-intersect-and-except-explained-simply]]
- [[2026-04-02-ctes-vs-subqueries-in-sql-which-one-should-you-use]]
- [[2026-04-23-i-built-a-browser-only-sql-practice-tool-because-installing-dbeaver-is-a-productivity-tax]]
- [[2026-04-21-sql-window-functions-and-ctes]]
- [[2026-04-30-subqueries-vs-ctes-in-sql-master-nested-queries-and-write-cleaner-smarter-code]]
- [[2026-04-22-understanding-subqueries-vs-ctes-in-sql-with-examples]]
