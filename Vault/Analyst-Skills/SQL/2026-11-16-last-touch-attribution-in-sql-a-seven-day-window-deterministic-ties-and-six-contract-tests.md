---
title: 'Last-Touch Attribution in SQL: A Seven-Day Window, Deterministic Ties, and
  Six Contract Tests'
date: '2026-11-16'
source: https://dev.to/rupak_kulkarni_08b45c5846/last-touch-attribution-in-sql-a-seven-day-window-deterministic-ties-and-six-contract-tests-2d4h
domain: SQL
relevance: 🟡
tags:
- '#ai'
- '#python'
- '#sql'
- '#tool'
related:
- '[[2026-06-10-sql-for-data-analysis-the-10-query-patterns-that-matter]]'
- '[[2026-10-06-i-scanned-1152-dbt-models-for-joins-that-inflate-sum-here-is-what-i-found]]'
- '[[2026-10-26-sql-joins-explained-inner-left-right-and-full-with-examples]]'
- '[[2026-04-27-sql-group-by-having-the-beginners-guide-to-summarizing-data-like-a-pro]]'
- '[[2026-03-03-sql-joins-window-functions-the-skills-that-separate-analysts-from-beginners]]'
- '[[2026-09-15-sql-joins-explained]]'
status: unread
---

> **TL;DR:** A retail-media dashboard can show perfectly plausible revenue numbers while answering the wrong question. If the same order follows a search click, a social click, and another search click, which campaign receives credit…

## What’s new and why it matters
A retail-media dashboard can show perfectly plausible revenue numbers while answering the wrong question. If the same order follows a search click, a social click, and another search click, which campaign receives credit? A recent public commit in my retail-media analytics pipeline adds a deterministic seven-day last-touch attribution model and six SQLite contract tests. This walkthrough explains the actual implementation, the edge cases it covers, and the important business questions it does not answer. The contract before the query We start with two synthetic tables: orders(order_id, custome…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Write the query in a scratchpad and run EXPLAIN/QUERY PLAN to verify performance.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/rupak_kulkarni_08b45c5846/last-touch-attribution-in-sql-a-seven-day-window-deterministic-ties-and-six-contract-tests-2d4h

## Related notes
- [[2026-06-10-sql-for-data-analysis-the-10-query-patterns-that-matter]]
- [[2026-10-06-i-scanned-1152-dbt-models-for-joins-that-inflate-sum-here-is-what-i-found]]
- [[2026-10-26-sql-joins-explained-inner-left-right-and-full-with-examples]]
- [[2026-04-27-sql-group-by-having-the-beginners-guide-to-summarizing-data-like-a-pro]]
- [[2026-03-03-sql-joins-window-functions-the-skills-that-separate-analysts-from-beginners]]
- [[2026-09-15-sql-joins-explained]]
