---
title: '# SQL Window Functions: The Part That Took Me a While to Understand'
date: '2026-09-14'
source: https://dev.to/feddy_mwanjumwa_e4047cf0c/-sql-window-functions-the-part-that-took-me-a-while-to-understand-5d96
domain: SQL
relevance: 🟡
tags:
- '#sql'
- '#tool'
related:
- '[[2026-03-09-sql-window-functions-dont-have-to-be-scary]]'
- '[[2026-08-12-sql-window-functions-how-to-get-the-top-row-per-group]]'
- '[[2026-06-13-select-final-and-optimize-final-are-not-the-same-thing]]'
- '[[2026-08-31-running-total-in-sql-the-window-frame-that-decides-the-answer]]'
- '[[2026-09-09-sql-functions]]'
- '[[2026-09-08-write-code-once-use-it-forever-python-functions-explained]]'
status: unread
---

> **TL;DR:** SQL Window Functions: The Part That Took Me a While to Understand Window functions were one of those SQL topics that looked much more complicated than they actually were. What finally helped me understand them was realis…

## What’s new and why it matters
SQL Window Functions: The Part That Took Me a While to Understand Window functions were one of those SQL topics that looked much more complicated than they actually were. What finally helped me understand them was realising that they let me calculate something across related rows without removing the individual rows. That is the big difference from GROUP BY. What are window functions? A window function performs a calculation across a set of related rows while still keeping each row in the result. For example, suppose I have sales data: Amina | Nairobi | 50000 Brian | Nairobi | 35000 Faith | Mo…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Write the query in a scratchpad and run EXPLAIN/QUERY PLAN to verify performance.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/feddy_mwanjumwa_e4047cf0c/-sql-window-functions-the-part-that-took-me-a-while-to-understand-5d96

## Related notes
- [[2026-03-09-sql-window-functions-dont-have-to-be-scary]]
- [[2026-08-12-sql-window-functions-how-to-get-the-top-row-per-group]]
- [[2026-06-13-select-final-and-optimize-final-are-not-the-same-thing]]
- [[2026-08-31-running-total-in-sql-the-window-frame-that-decides-the-answer]]
- [[2026-09-09-sql-functions]]
- [[2026-09-08-write-code-once-use-it-forever-python-functions-explained]]
