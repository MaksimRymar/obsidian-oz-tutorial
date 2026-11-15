---
title: 'Grade once, prove it forever: 46,756 settled calls and the case for an append-only
  grading ledger'
date: '2026-11-15'
source: https://dev.to/soccerdream_ai/grade-once-prove-it-forever-46756-settled-calls-and-the-case-for-an-append-only-grading-ledger-1m8l
domain: SQL
relevance: 🟡
tags:
- '#ai'
- '#python'
- '#sql'
- '#tool'
related:
- '[[2026-10-16-an-ai-explained-sql-group-by-in-four-lines-one-of-them-is-wrong]]'
- '[[2026-08-21-how-to-find-duplicate-rows-in-sql-and-decide-what-counts-as-one]]'
- '[[2026-06-16-sql-or-python-the-line-is-sharper-than-you-think-with-code]]'
- '[[2026-08-05-reconstructing-wallet-journeys-across-dex-frontends-one-chain-at-a-time]]'
- '[[2026-08-31-how-to-reconcile-two-tables-in-sql-when-the-row-counts-match]]'
- '[[2026-08-31-temp-table-vs-view-in-sql-a-saved-answer-or-a-saved-question]]'
status: unread
---

> **TL;DR:** Every prediction system eventually makes a promise like this: "our hit rate is 57%." That is a claim about the past, and it is only meaningful if the past cannot be edited. In almost every system I have audited, the grad…

## What’s new and why it matters
Every prediction system eventually makes a promise like this: "our hit rate is 57%." That is a claim about the past, and it is only meaningful if the past cannot be edited. In almost every system I have audited, the grade is a mutable boolean on the same row as the prediction, updated by whatever job ran last. The row is not a record. It is a cache of the most recent writer's opinion. The case study: a production system with 46,969 prediction rows, 46,756 of them settled. All figures come from the live database. What a grade actually contains A grade is not a boolean. It is a tuple: the frozen…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Write the query in a scratchpad and run EXPLAIN/QUERY PLAN to verify performance.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/soccerdream_ai/grade-once-prove-it-forever-46756-settled-calls-and-the-case-for-an-append-only-grading-ledger-1m8l

## Related notes
- [[2026-10-16-an-ai-explained-sql-group-by-in-four-lines-one-of-them-is-wrong]]
- [[2026-08-21-how-to-find-duplicate-rows-in-sql-and-decide-what-counts-as-one]]
- [[2026-06-16-sql-or-python-the-line-is-sharper-than-you-think-with-code]]
- [[2026-08-05-reconstructing-wallet-journeys-across-dex-frontends-one-chain-at-a-time]]
- [[2026-08-31-how-to-reconcile-two-tables-in-sql-when-the-row-counts-match]]
- [[2026-08-31-temp-table-vs-view-in-sql-a-saved-answer-or-a-saved-question]]
