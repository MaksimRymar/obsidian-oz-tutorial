---
title: EXPLAIN PLAN as a Lint for LLM-Generated SQL
date: '2026-08-06'
source: https://dev.to/nunc/explain-plan-as-a-lint-for-llm-generated-sql-4mg8
domain: SQL
relevance: 🟡
tags:
- '#ai'
- '#library'
- '#python'
- '#sql'
- '#tool'
- '#zendesk'
related:
- '[[2026-03-30-database-indexing-explained-whats-actually-happening-under-the-hood]]'
- '[[2026-06-15-day-01-of-learning-data-engineering-step1-sql-joins-and-set-operators]]'
- '[[2026-06-05-your-postgres-is-failing-quietly-7-sql-checks-that-catch-it-before-grafana-does]]'
- '[[2026-06-19-how-to-embed-a-sql-dashboard-into-your-saas-app-without-building-everything-from-scratch]]'
- '[[2026-05-03-claudemd-for-postgresql-13-rules-that-make-ai-write-safe-production-ready-sql]]'
- '[[2026-05-15-oracle-fusion-vs-ebs-7-sql-patterns-every-bip-report-developer-needs]]'
status: unread
---

> **TL;DR:** My AI agents write Oracle SQL all day: fix scripts, diagnostics, one-off reports for a 2.3M-line legacy system. Their most common failure isn't bad logic. It is SQL that references a table or column that almost exists. O…

## What’s new and why it matters
My AI agents write Oracle SQL all day: fix scripts, diagnostics, one-off reports for a 2.3M-line legacy system. Their most common failure isn't bad logic. It is SQL that references a table or column that almost exists. Oracle has had the fix for decades, it costs one statement per query, and it never executes anything: EXPLAIN PLAN . The failure mode: names that almost exist A language model doesn't know your schema. It knows what schemas usually look like. So on a 20-year-old database with thousands of tables, it produces names that are plausible instead of real: POLICY_STATUS when the column…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Write the query in a scratchpad and run EXPLAIN/QUERY PLAN to verify performance.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/nunc/explain-plan-as-a-lint-for-llm-generated-sql-4mg8

## Related notes
- [[2026-03-30-database-indexing-explained-whats-actually-happening-under-the-hood]]
- [[2026-06-15-day-01-of-learning-data-engineering-step1-sql-joins-and-set-operators]]
- [[2026-06-05-your-postgres-is-failing-quietly-7-sql-checks-that-catch-it-before-grafana-does]]
- [[2026-06-19-how-to-embed-a-sql-dashboard-into-your-saas-app-without-building-everything-from-scratch]]
- [[2026-05-03-claudemd-for-postgresql-13-rules-that-make-ai-write-safe-production-ready-sql]]
- [[2026-05-15-oracle-fusion-vs-ebs-7-sql-patterns-every-bip-report-developer-needs]]
