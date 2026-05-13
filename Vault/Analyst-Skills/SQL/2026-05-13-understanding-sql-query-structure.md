---
title: Understanding SQL query structure
date: '2026-05-13'
source: https://dev.to/weenaithdev/understanding-sql-query-structure-4hei
domain: SQL
relevance: 🟡
tags:
- '#ai'
- '#sql'
related:
- '[[2026-03-19-i-built-visual-execution-tools-for-sql-and-python---heres-why]]'
- '[[2026-04-15-how-to-build-a-strong-foundation-in-sql-and-databases-step-by-step]]'
- '[[2026-03-08-understanding-group-by-in-sql]]'
- '[[2026-04-27-from-chaos-to-clarity-how-sql-transforms-raw-data-into-powerful-stories]]'
- '[[2026-04-07-writing-sql-that-doesnt-come-back-to-haunt-you]]'
- '[[2026-04-29-aggregations-counting-summing-and-averaging-your-data]]'
status: unread
---

> **TL;DR:** This is basically SQL’s version of BODMAS/PEDMAS. We write SQL one way… but SQL executes it differently. The golden rule: F/JWGBHSOL/O Looks gibberish at first. Actually very important. How SQL Executes Queries F/J → FRO…

## What’s new and why it matters
This is basically SQL’s version of BODMAS/PEDMAS. We write SQL one way… but SQL executes it differently. The golden rule: F/JWGBHSOL/O Looks gibberish at first. Actually very important. How SQL Executes Queries F/J → FROM / JOIN Build the dataset. FROM → grab the main table JOIN → combine other tables W → WHERE First filter. Removes rows that don’t match conditions. GB → GROUP BY Create groups from rows. Turns row-level data into grouped data. H → HAVING Second filter. But this time for groups, not rows. S → SELECT Pick the final columns/results to display. O → ORDER BY Sort the final output.…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Write the query in a scratchpad and run EXPLAIN/QUERY PLAN to verify performance.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/weenaithdev/understanding-sql-query-structure-4hei

## Related notes
- [[2026-03-19-i-built-visual-execution-tools-for-sql-and-python---heres-why]]
- [[2026-04-15-how-to-build-a-strong-foundation-in-sql-and-databases-step-by-step]]
- [[2026-03-08-understanding-group-by-in-sql]]
- [[2026-04-27-from-chaos-to-clarity-how-sql-transforms-raw-data-into-powerful-stories]]
- [[2026-04-07-writing-sql-that-doesnt-come-back-to-haunt-you]]
- [[2026-04-29-aggregations-counting-summing-and-averaging-your-data]]
