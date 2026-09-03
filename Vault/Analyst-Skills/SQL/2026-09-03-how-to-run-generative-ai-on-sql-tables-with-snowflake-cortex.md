---
title: How to run generative AI on SQL tables with Snowflake Cortex
date: '2026-09-03'
source: https://dev.to/laura_cristinachicovisd/how-to-run-generative-ai-on-sql-tables-with-snowflake-cortex-5gh6
domain: SQL
relevance: 🔴
tags:
- '#ai'
- '#feature'
- '#sql'
- '#tool'
- '#tutorial'
related:
- '[[2026-06-10-sql-for-data-analysis-the-10-query-patterns-that-matter]]'
- '[[2026-08-31-running-total-in-sql-the-window-frame-that-decides-the-answer]]'
- '[[2026-09-01-seeding-fixtures-realistic-test-data-for-warehouse-integration-tests]]'
- '[[2026-08-11-the-text-to-sql-demo-takes-an-afternoon-the-other-90-is-why-you-should-buy-it]]'
- '[[2026-08-22-where-to-get-a-sample-database-to-practice-sql-and-how-to-check-it-loaded]]'
- '[[2026-08-12-sql-foundations-start-to-finish]]'
status: unread
---

> **TL;DR:** The question that decides whether Cortex belongs in your stack is not what it can do. It is what it costs once the table has millions of rows instead of five. That question exists because the model call is an ordinary SQ…

## What’s new and why it matters
The question that decides whether Cortex belongs in your stack is not what it can do. It is what it costs once the table has millions of rows instead of five. That question exists because the model call is an ordinary SQL function. It sits inside a SELECT , composes with WHERE , JOIN and GROUP BY , and runs once per row. So this walkthrough goes in that order. Access first, then the functions on a small slice, then the credit consumption before anything scales up. Before you start A Snowflake account on Standard edition or above, in a region where Cortex is available. A running warehouse. The…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Write the query in a scratchpad and run EXPLAIN/QUERY PLAN to verify performance.
- Add a short note: what changed in your workflow?

## Relevance
🔴

## Source
https://dev.to/laura_cristinachicovisd/how-to-run-generative-ai-on-sql-tables-with-snowflake-cortex-5gh6

## Related notes
- [[2026-06-10-sql-for-data-analysis-the-10-query-patterns-that-matter]]
- [[2026-08-31-running-total-in-sql-the-window-frame-that-decides-the-answer]]
- [[2026-09-01-seeding-fixtures-realistic-test-data-for-warehouse-integration-tests]]
- [[2026-08-11-the-text-to-sql-demo-takes-an-afternoon-the-other-90-is-why-you-should-buy-it]]
- [[2026-08-22-where-to-get-a-sample-database-to-practice-sql-and-how-to-check-it-loaded]]
- [[2026-08-12-sql-foundations-start-to-finish]]
