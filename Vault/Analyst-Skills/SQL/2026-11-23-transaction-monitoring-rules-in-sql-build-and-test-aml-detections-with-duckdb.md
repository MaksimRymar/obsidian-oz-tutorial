---
title: 'Transaction Monitoring Rules in SQL: Build and Test AML Detections with DuckDB'
date: '2026-11-23'
source: https://dev.to/audrey_xu/transaction-monitoring-rules-in-sql-build-and-test-aml-detections-with-duckdb-1jji
domain: SQL
relevance: 🟡
tags:
- '#ai'
- '#best-practice'
- '#python'
- '#sql'
- '#support-analytics'
- '#tool'
related:
- '[[2026-08-31-running-total-in-sql-the-window-frame-that-decides-the-answer]]'
- '[[2026-09-24-my-alert-fired-7-times-across-1963-pairs-i-assumed-the-thresholds-were-too-high-they-were-and-it-didnt-matter]]'
- '[[2026-08-23-sql-window-frames-explained-how-unbounded-preceding-creates-a-running-total]]'
- '[[2026-10-06-i-scanned-1152-dbt-models-for-joins-that-inflate-sum-here-is-what-i-found]]'
- '[[2026-09-01-seeding-fixtures-realistic-test-data-for-warehouse-integration-tests]]'
- '[[2026-10-16-an-ai-explained-sql-group-by-in-four-lines-one-of-them-is-wrong]]'
status: unread
---

> **TL;DR:** Banks track transaction patterns in real time to flag unusual activity, such as a sudden large withdrawal in another city or several quick purchases in a row. In AML transaction monitoring, most of that flagging still st…

## What’s new and why it matters
Banks track transaction patterns in real time to flag unusual activity, such as a sudden large withdrawal in another city or several quick purchases in a row. In AML transaction monitoring, most of that flagging still starts with rules: “three cash deposits just under $10,000 in a week”, “money in, money out within two days”, “a silent account suddenly moving five figures”. Rules are easy to explain to an auditor, which matters: US examiners expect a bank to document its filtering criteria and thresholds and explain them. They are also easy to get subtly wrong. A window that counts rows instea…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Write the query in a scratchpad and run EXPLAIN/QUERY PLAN to verify performance.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/audrey_xu/transaction-monitoring-rules-in-sql-build-and-test-aml-detections-with-duckdb-1jji

## Related notes
- [[2026-08-31-running-total-in-sql-the-window-frame-that-decides-the-answer]]
- [[2026-09-24-my-alert-fired-7-times-across-1963-pairs-i-assumed-the-thresholds-were-too-high-they-were-and-it-didnt-matter]]
- [[2026-08-23-sql-window-frames-explained-how-unbounded-preceding-creates-a-running-total]]
- [[2026-10-06-i-scanned-1152-dbt-models-for-joins-that-inflate-sum-here-is-what-i-found]]
- [[2026-09-01-seeding-fixtures-realistic-test-data-for-warehouse-integration-tests]]
- [[2026-10-16-an-ai-explained-sql-group-by-in-four-lines-one-of-them-is-wrong]]
