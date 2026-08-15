---
title: LIMIT 20 is not a sampling strategy
date: '2026-08-15'
source: https://dev.to/mads_hansen_27b33ebfee4c9/limit-20-is-not-a-sampling-strategy-1o04
domain: SQL
relevance: 🟡
tags:
- '#ai'
- '#best-practice'
- '#sql'
- '#tool'
- '#tutorial'
related:
- '[[2026-07-22-before-chatgpt-queries-your-sql-database-define-the-answer-contract]]'
- '[[2026-05-02-why-standard-indexes-fail-the-architecture-of-the-covering-index]]'
- '[[2026-05-13-ai-database-agents-need-result-contracts-not-just-rows]]'
- '[[2026-08-08-a-valid-sql-query-is-not-proof-that-the-question-was-answerable]]'
- '[[2026-05-30-sqlite-is-all-you-need-for-durable-workflows]]'
- '[[2026-06-30-how-to-implement-rbac-in-go]]'
status: unread
---

> **TL;DR:** “Show me twenty examples” sounds harmless. The generated SQL adds LIMIT 20 without a stable order. The database returns whichever rows happen to arrive first. The assistant finds a pattern, and the team treats that patte…

## What’s new and why it matters
“Show me twenty examples” sounds harmless. The generated SQL adds LIMIT 20 without a stable order. The database returns whichever rows happen to arrive first. The assistant finds a pattern, and the team treats that pattern as evidence. But a row limit is not a sample design. Physical layout, indexes, query plans, parallel workers, recent inserts, and cache state can all change which rows appear. Before examples support a conclusion, define: the population and cutoff authorization scope the sampling method stable row identity seed and algorithm version strata and weights redaction what the samp…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Write the query in a scratchpad and run EXPLAIN/QUERY PLAN to verify performance.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/mads_hansen_27b33ebfee4c9/limit-20-is-not-a-sampling-strategy-1o04

## Related notes
- [[2026-07-22-before-chatgpt-queries-your-sql-database-define-the-answer-contract]]
- [[2026-05-02-why-standard-indexes-fail-the-architecture-of-the-covering-index]]
- [[2026-05-13-ai-database-agents-need-result-contracts-not-just-rows]]
- [[2026-08-08-a-valid-sql-query-is-not-proof-that-the-question-was-answerable]]
- [[2026-05-30-sqlite-is-all-you-need-for-durable-workflows]]
- [[2026-06-30-how-to-implement-rbac-in-go]]
