---
title: dbt snapshots are not an audit log
date: '2026-11-03'
source: https://dev.to/aniketsoni/dbt-snapshots-are-not-an-audit-log-1m4c
domain: SQL
relevance: 🟡
tags:
- '#ai'
- '#best-practice'
- '#sql'
- '#support-analytics'
- '#tool'
related:
- '[[2026-04-23-i-built-a-browser-only-sql-practice-tool-because-installing-dbeaver-is-a-productivity-tax]]'
- '[[2026-05-20-learning-sql-as-if-you-built-it-yourself]]'
- '[[2026-06-28-data-analysis-sql-asking-the-right-questions-and-using-the-right-tools]]'
- '[[2026-03-30-build-a-productionready-sql-evaluation-engine-for-llms]]'
- '[[2026-09-24-factless-fact-tables-modeling-events-coverage-eligibility-without-measures]]'
- '[[2026-06-13-top-12-sql-interview-problems-for-data-engineers-with-answers]]'
status: unread
---

> **TL;DR:** The persistent myth that dbt snapshots act as a foolproof audit log is a dangerous misunderstanding of how slowly changing dimensions (SCDs) function in modern data warehouses. Many engineers treat snapshots as a catch-a…

## What’s new and why it matters
The persistent myth that dbt snapshots act as a foolproof audit log is a dangerous misunderstanding of how slowly changing dimensions (SCDs) function in modern data warehouses. Many engineers treat snapshots as a catch-all solution for "tracking changes." If a table changes, they point a dbt snapshot at it and assume they have a perfect history of every state transition. However, dbt snapshots are designed to track the current state of a dimension over time, not to capture the high-frequency event stream required for an audit. What happened In 2022, the engineering team at Monzo shared a postm…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Write the query in a scratchpad and run EXPLAIN/QUERY PLAN to verify performance.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/aniketsoni/dbt-snapshots-are-not-an-audit-log-1m4c

## Related notes
- [[2026-04-23-i-built-a-browser-only-sql-practice-tool-because-installing-dbeaver-is-a-productivity-tax]]
- [[2026-05-20-learning-sql-as-if-you-built-it-yourself]]
- [[2026-06-28-data-analysis-sql-asking-the-right-questions-and-using-the-right-tools]]
- [[2026-03-30-build-a-productionready-sql-evaluation-engine-for-llms]]
- [[2026-09-24-factless-fact-tables-modeling-events-coverage-eligibility-without-measures]]
- [[2026-06-13-top-12-sql-interview-problems-for-data-engineers-with-answers]]
