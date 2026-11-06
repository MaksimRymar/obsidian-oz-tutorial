---
title: Reconcile a dashboard number with the source table in SQL
date: '2026-11-06'
source: https://dev.to/refaeldakar/reconcile-a-dashboard-number-with-the-source-table-in-sql-14oj
domain: SQL
relevance: 🟡
tags:
- '#sql'
- '#tool'
related:
- '[[2026-06-10-sql-for-data-analysis-the-10-query-patterns-that-matter]]'
- '[[2026-10-16-an-ai-explained-sql-group-by-in-four-lines-one-of-them-is-wrong]]'
- '[[2026-10-06-i-scanned-1152-dbt-models-for-joins-that-inflate-sum-here-is-what-i-found]]'
- '[[2026-08-31-how-to-reconcile-two-tables-in-sql-when-the-row-counts-match]]'
- '[[2026-11-03-null-rate-data-quality-check-in-sql-per-column]]'
- '[[2026-11-05-cost-first-or-sample-first-a-debate-over-how-agent-sql-loops-handle-unknown-table-sizes]]'
status: unread
---

> **TL;DR:** "The dashboard says 349 and finance says 312." Nobody knows which is right, and the argument usually lasts longer than the fix. A reconciliation check ends it: compute the number again from the source, line it up day by…

## What’s new and why it matters
"The dashboard says 349 and finance says 312." Nobody knows which is right, and the argument usually lasts longer than the fix. A reconciliation check ends it: compute the number again from the source, line it up day by day against what the dashboard shows, and look only at the rows that disagree. Plain Postgres SQL below. The full write-up is on my blog. The query WITH src AS ( SELECT created_at :: date AS day , sum ( amount ) AS src_total FROM orders WHERE status = 'paid' AND created_at >= current_date - 7 AND created_at < current_date GROUP BY 1 ), shown AS ( SELECT day , revenue AS shown_t…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Write the query in a scratchpad and run EXPLAIN/QUERY PLAN to verify performance.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/refaeldakar/reconcile-a-dashboard-number-with-the-source-table-in-sql-14oj

## Related notes
- [[2026-06-10-sql-for-data-analysis-the-10-query-patterns-that-matter]]
- [[2026-10-16-an-ai-explained-sql-group-by-in-four-lines-one-of-them-is-wrong]]
- [[2026-10-06-i-scanned-1152-dbt-models-for-joins-that-inflate-sum-here-is-what-i-found]]
- [[2026-08-31-how-to-reconcile-two-tables-in-sql-when-the-row-counts-match]]
- [[2026-11-03-null-rate-data-quality-check-in-sql-per-column]]
- [[2026-11-05-cost-first-or-sample-first-a-debate-over-how-agent-sql-loops-handle-unknown-table-sizes]]
