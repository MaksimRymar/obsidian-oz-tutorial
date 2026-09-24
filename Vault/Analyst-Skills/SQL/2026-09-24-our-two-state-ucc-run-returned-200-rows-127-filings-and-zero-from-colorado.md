---
title: Our two-state UCC run returned 200 rows, 127 filings, and zero from Colorado
date: '2026-09-24'
source: https://dev.to/devil_scrapes/our-two-state-ucc-run-returned-200-rows-127-filings-and-zero-from-colorado-12l4
domain: SQL
relevance: 🟡
tags:
- '#sql'
- '#tool'
related:
- '[[2026-08-26-redb-371-props-search-up-to-100x-faster-an-alternative-to-ef-core-or-a-companion-to-it]]'
- '[[2026-08-31-running-total-in-sql-the-window-frame-that-decides-the-answer]]'
- '[[2026-07-15-i-built-with-both-apis-as-a-bootcamp-grad-heres-what-actually-matters]]'
- '[[2026-09-16-sql-joins-with-examples-of-each]]'
- '[[2026-08-31-subquery-vs-cte-in-sql-same-logic-one-you-can-check]]'
- '[[2026-08-21-how-to-find-duplicate-rows-in-sql-and-decide-what-counts-as-one]]'
status: unread
---

> **TL;DR:** Quick answer Before the UCC Lien Filing Scraper ever went public, a deep cloud run asked it for Connecticut and Colorado filings from the last 120 days, capped at 200 rows. The run came back SUCCEEDED with 200 rows. Ever…

## What’s new and why it matters
Quick answer Before the UCC Lien Filing Scraper ever went public, a deep cloud run asked it for Connecticut and Colorado filings from the last 120 days, capped at 200 rows. The run came back SUCCEEDED with 200 rows. Every one of them was from Connecticut. Colorado — which had real filings in that exact window — contributed zero. And those 200 rows described only 127 distinct filings. Both numbers were telling us something. One was a bug. The other was the data being honest about its own shape, and the fix there was to our copy, not our code. How does a two-state run return rows from only one s…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Write the query in a scratchpad and run EXPLAIN/QUERY PLAN to verify performance.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/devil_scrapes/our-two-state-ucc-run-returned-200-rows-127-filings-and-zero-from-colorado-12l4

## Related notes
- [[2026-08-26-redb-371-props-search-up-to-100x-faster-an-alternative-to-ef-core-or-a-companion-to-it]]
- [[2026-08-31-running-total-in-sql-the-window-frame-that-decides-the-answer]]
- [[2026-07-15-i-built-with-both-apis-as-a-bootcamp-grad-heres-what-actually-matters]]
- [[2026-09-16-sql-joins-with-examples-of-each]]
- [[2026-08-31-subquery-vs-cte-in-sql-same-logic-one-you-can-check]]
- [[2026-08-21-how-to-find-duplicate-rows-in-sql-and-decide-what-counts-as-one]]
