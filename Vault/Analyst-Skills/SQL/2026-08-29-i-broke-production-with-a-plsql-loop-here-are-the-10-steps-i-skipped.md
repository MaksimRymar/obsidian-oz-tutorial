---
title: I Broke Production with a PL/SQL Loop. Here Are the 10 Steps I Skipped
date: '2026-08-29'
source: https://dev.to/wassim_bensaida_c33234dc/i-broke-production-with-a-plsql-loop-here-are-the-10-steps-i-skipped-35ng
domain: SQL
relevance: 🟡
tags:
- '#ai'
- '#career'
- '#library'
- '#sql'
- '#tableau'
- '#tool'
- '#tutorial'
- '#zendesk'
related:
- '[[2026-04-02-ctes-vs-subqueries-in-sql-which-one-should-you-use]]'
- '[[2026-06-10-sql-for-data-analysis-the-10-query-patterns-that-matter]]'
- '[[2026-08-21-how-to-find-duplicate-rows-in-sql-and-decide-what-counts-as-one]]'
- '[[2026-08-21-null-in-sql-why-null-finds-nothing-and-what-to-write-instead]]'
- '[[2026-08-12-sql-foundations-start-to-finish]]'
- '[[2026-08-12-sql-window-functions-how-to-get-the-top-row-per-group]]'
status: unread
---

> **TL;DR:** The job was supposed to run for four minutes. At 7:40 the next morning it was still running, half the rows were updated, and I couldn't roll any of it back. Here is the shape of what I wrote — simplified, but not by much…

## What’s new and why it matters
The job was supposed to run for four minutes. At 7:40 the next morning it was still running, half the rows were updated, and I couldn't roll any of it back. Here is the shape of what I wrote — simplified, but not by much: BEGIN FOR r IN ( SELECT item_id , qty FROM stock_lines ) LOOP UPDATE stock_summary SET qty = qty + r . qty WHERE item_id = r . item_id ; COMMIT ; -- "so it doesn't fill the undo" END LOOP ; END ; / It looks harmless. It is not. Three separate mistakes are stacked in those nine lines, and each one maps to a fundamental I had skipped: One UPDATE per row. 400,000 rows meant 400,…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Write the query in a scratchpad and run EXPLAIN/QUERY PLAN to verify performance.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/wassim_bensaida_c33234dc/i-broke-production-with-a-plsql-loop-here-are-the-10-steps-i-skipped-35ng

## Related notes
- [[2026-04-02-ctes-vs-subqueries-in-sql-which-one-should-you-use]]
- [[2026-06-10-sql-for-data-analysis-the-10-query-patterns-that-matter]]
- [[2026-08-21-how-to-find-duplicate-rows-in-sql-and-decide-what-counts-as-one]]
- [[2026-08-21-null-in-sql-why-null-finds-nothing-and-what-to-write-instead]]
- [[2026-08-12-sql-foundations-start-to-finish]]
- [[2026-08-12-sql-window-functions-how-to-get-the-top-row-per-group]]
