---
title: Top N per group is the query `LIMIT` can't write
date: '2026-07-27'
source: https://dev.to/omer_hochman/top-n-per-group-is-the-query-limit-cant-write-57eb
domain: SQL
relevance: 🟡
tags:
- '#presentations'
- '#sql'
- '#tool'
related:
- '[[2026-06-20-select-the-first-row-per-group-in-supabase-postgres]]'
- '[[2026-07-22-when-to-trust-ai-generated-sql-and-when-not-to]]'
- '[[2026-05-29-part-14-window-functions-ninja-mode]]'
- '[[2026-04-02-ctes-vs-subqueries-in-sql-which-one-should-you-use]]'
- '[[2026-05-18-wrong-answer-is-the-worst-feedback-you-can-give-a-sql-learner-so-i-built-something-better]]'
- '[[2026-06-09-pandas-vs-sql-when-to-use-each]]'
status: unread
---

> **TL;DR:** Originally published at nlqdb.com/blog You want the top 3 best-selling products in each category . Or the most recent order per customer . Or the highest-scoring attempt per user . The English is so plain it feels like i…

## What’s new and why it matters
Originally published at nlqdb.com/blog You want the top 3 best-selling products in each category . Or the most recent order per customer . Or the highest-scoring attempt per user . The English is so plain it feels like it should compile to something you already know — ORDER BY revenue DESC LIMIT 3 — and that is exactly the trap. LIMIT caps the whole result set . Ask it for the top 3 and it hands you the 3 best rows across every category combined, not 3 per category. The word "per" quietly moved the query somewhere LIMIT cannot follow. -- What you wrote (wrong): 3 rows total, not 3 per category…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Write the query in a scratchpad and run EXPLAIN/QUERY PLAN to verify performance.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/omer_hochman/top-n-per-group-is-the-query-limit-cant-write-57eb

## Related notes
- [[2026-06-20-select-the-first-row-per-group-in-supabase-postgres]]
- [[2026-07-22-when-to-trust-ai-generated-sql-and-when-not-to]]
- [[2026-05-29-part-14-window-functions-ninja-mode]]
- [[2026-04-02-ctes-vs-subqueries-in-sql-which-one-should-you-use]]
- [[2026-05-18-wrong-answer-is-the-worst-feedback-you-can-give-a-sql-learner-so-i-built-something-better]]
- [[2026-06-09-pandas-vs-sql-when-to-use-each]]
