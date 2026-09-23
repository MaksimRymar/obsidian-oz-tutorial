---
title: 'Fact Table Patterns: Transaction, Periodic Snapshot & Accumulating Snapshot
  Facts'
date: '2026-09-23'
source: https://dev.to/gowthampotureddi/fact-table-patterns-transaction-periodic-snapshot-accumulating-snapshot-facts-1o93
domain: SQL
relevance: 🟡
tags:
- '#ai'
- '#best-practice'
- '#career'
- '#presentations'
- '#sql'
- '#tool'
- '#tutorial'
- '#zendesk'
related:
- '[[2026-08-31-how-to-reconcile-two-tables-in-sql-when-the-row-counts-match]]'
- '[[2026-09-23-special-dimensions-junk-degenerate-role-playing-conformed-dimensions]]'
- '[[2026-09-16-the-data-modeling-concepts-nobody-mentions-after-star-schema-101]]'
- '[[2026-06-10-sql-for-data-analysis-the-10-query-patterns-that-matter]]'
- '[[2026-09-16-sql-joins-with-examples-of-each]]'
- '[[2026-08-31-running-total-in-sql-the-window-frame-that-decides-the-answer]]'
status: unread
---

> **TL;DR:** fact table patterns are the three shapes every measurement table in a dimensional model can take — and choosing the right one is not a stylistic preference, it is a correctness decision that determines whether your SUM r…

## What’s new and why it matters
fact table patterns are the three shapes every measurement table in a dimensional model can take — and choosing the right one is not a stylistic preference, it is a correctness decision that determines whether your SUM returns a number a business will trust. A fact table is the centre of a star schema: a wide, mostly-numeric table whose columns are foreign keys to dimensions plus the numeric measures you actually aggregate. But "one fact table" hides a fork in the road. Are you recording each individual event as it happens? Sampling a balance at the end of every day? Or tracking a single order…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Write the query in a scratchpad and run EXPLAIN/QUERY PLAN to verify performance.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/gowthampotureddi/fact-table-patterns-transaction-periodic-snapshot-accumulating-snapshot-facts-1o93

## Related notes
- [[2026-08-31-how-to-reconcile-two-tables-in-sql-when-the-row-counts-match]]
- [[2026-09-23-special-dimensions-junk-degenerate-role-playing-conformed-dimensions]]
- [[2026-09-16-the-data-modeling-concepts-nobody-mentions-after-star-schema-101]]
- [[2026-06-10-sql-for-data-analysis-the-10-query-patterns-that-matter]]
- [[2026-09-16-sql-joins-with-examples-of-each]]
- [[2026-08-31-running-total-in-sql-the-window-frame-that-decides-the-answer]]
