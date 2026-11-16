---
title: Finding negative stock with a running balance - SUM() OVER in a Uniface service
date: '2026-11-16'
source: https://dev.to/f345345dfg/finding-negative-stock-with-a-running-balance-sum-over-in-a-uniface-service-26o3
domain: SQL
relevance: 🟡
tags:
- '#python'
- '#sql'
- '#tool'
related:
- '[[2026-11-16-checking-vat-id-format-with-glob-in-sqlite---from-a-uniface-service]]'
- '[[2026-11-16-validating-free-form-field-values-in-sqlite---glob-patterns-and-a-date-surprise]]'
- '[[2026-11-16-customer-hierarchies-with-with-recursive---finding-cycles-and-group-totals-in-a-uniface-service]]'
- '[[2026-09-01-seeding-fixtures-realistic-test-data-for-warehouse-integration-tests]]'
- '[[2026-09-16-sql-joins-with-examples-of-each]]'
- '[[2026-09-03-how-to-run-generative-ai-on-sql-tables-with-snowflake-cortex]]'
status: unread
---

> **TL;DR:** A customer app built in Uniface 10 keeps stock as movements: one row per receipt, delivery, transfer or correction in the table STOCK_MOVE , with a signed quantity. The current stock of a product in a warehouse is the su…

## What’s new and why it matters
A customer app built in Uniface 10 keeps stock as movements: one row per receipt, delivery, transfer or correction in the table STOCK_MOVE , with a signed quantity. The current stock of a product in a warehouse is the sum of its movements. A check "stock below zero" on that sum misses the interesting case: a delivery booked before the receipt, corrected a week later. At the end everything adds up, but for a week the books said -5. Tested with Rocket Uniface 10.4.03 Community Edition (10.4.03.021) on Windows, November 2026. The app uses SQLite through the SLE driver (SQLite 3.50.2). The data Qu…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Write the query in a scratchpad and run EXPLAIN/QUERY PLAN to verify performance.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/f345345dfg/finding-negative-stock-with-a-running-balance-sum-over-in-a-uniface-service-26o3

## Related notes
- [[2026-11-16-checking-vat-id-format-with-glob-in-sqlite---from-a-uniface-service]]
- [[2026-11-16-validating-free-form-field-values-in-sqlite---glob-patterns-and-a-date-surprise]]
- [[2026-11-16-customer-hierarchies-with-with-recursive---finding-cycles-and-group-totals-in-a-uniface-service]]
- [[2026-09-01-seeding-fixtures-realistic-test-data-for-warehouse-integration-tests]]
- [[2026-09-16-sql-joins-with-examples-of-each]]
- [[2026-09-03-how-to-run-generative-ai-on-sql-tables-with-snowflake-cortex]]
