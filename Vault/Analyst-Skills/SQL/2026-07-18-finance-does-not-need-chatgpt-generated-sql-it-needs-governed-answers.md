---
title: Finance does not need ChatGPT-generated SQL. It needs governed answers
date: '2026-07-18'
source: https://dev.to/mads_hansen_27b33ebfee4c9/finance-does-not-need-chatgpt-generated-sql-it-needs-governed-answers-3j98
domain: SQL
relevance: 🟡
tags:
- '#ai'
- '#sql'
- '#tool'
related:
- '[[2026-07-16-natural-language-sql-needs-guardrails-not-just-better-prompts]]'
- '[[2026-05-13-ai-database-agents-need-result-contracts-not-just-rows]]'
- '[[2026-03-16-how-i-turned-approved-sql-into-governed-business-kpis]]'
- '[[2026-06-16-building-a-natural-language-query-interface-for-your-database-a-developers-blueprint]]'
- '[[2026-06-10-sql-for-data-analysis-the-10-query-patterns-that-matter]]'
- '[[2026-07-02-building-an-ai-sql-validation-agent-with-codex-and-a-rest-api]]'
status: unread
---

> **TL;DR:** The finance team asks: Why did recurring revenue move this month? The database contains the answer. But a raw ChatGPT-to-SQL connection does not contain the business definition. It may not know: which subscriptions count…

## What’s new and why it matters
The finance team asks: Why did recurring revenue move this month? The database contains the answer. But a raw ChatGPT-to-SQL connection does not contain the business definition. It may not know: which subscriptions count how refunds are treated which timezone closes the month which legal entity is in scope whether the number is month-to-date or final whether a backfill changed yesterday's result For finance reporting, the hard part is not generating SQL. It is keeping the metric definition attached to the answer. A production workflow should use: an approved finance view or semantic layer a de…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Write the query in a scratchpad and run EXPLAIN/QUERY PLAN to verify performance.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/mads_hansen_27b33ebfee4c9/finance-does-not-need-chatgpt-generated-sql-it-needs-governed-answers-3j98

## Related notes
- [[2026-07-16-natural-language-sql-needs-guardrails-not-just-better-prompts]]
- [[2026-05-13-ai-database-agents-need-result-contracts-not-just-rows]]
- [[2026-03-16-how-i-turned-approved-sql-into-governed-business-kpis]]
- [[2026-06-16-building-a-natural-language-query-interface-for-your-database-a-developers-blueprint]]
- [[2026-06-10-sql-for-data-analysis-the-10-query-patterns-that-matter]]
- [[2026-07-02-building-an-ai-sql-validation-agent-with-codex-and-a-rest-api]]
