---
title: 'Immutable predictions: a schema for grading model output you can''t quietly
  rewrite'
date: '2026-11-09'
source: https://dev.to/soccerdream_ai/immutable-predictions-a-schema-for-grading-model-output-you-cant-quietly-rewrite-2o82
domain: SQL
relevance: 🟡
tags:
- '#ai'
- '#python'
- '#sql'
- '#tool'
related:
- '[[2026-08-21-how-to-find-duplicate-rows-in-sql-and-decide-what-counts-as-one]]'
- '[[2026-10-15-free-draft-volume-or-paid-first-passes-a-debate-for-agent-sql-budgets]]'
- '[[2026-10-30-count-accepted-jobs-not-successful-api-calls-when-comparing-ai-workflows]]'
- '[[2026-08-31-running-total-in-sql-the-window-frame-that-decides-the-answer]]'
- '[[2026-09-29-the-not-in-trap-why-your-sql-query-returns-zero-rows]]'
- '[[2026-08-13-3-testing-habits-that-caught-bugs-before-my-users-did]]'
status: unread
---

> **TL;DR:** Every model evaluation I've ever seen has the same hole in it: the predictions are stored in a table someone can edit. Not maliciously, usually. Someone reruns a pipeline, a backfill overwrites yesterday's rows, a "fix"…

## What’s new and why it matters
Every model evaluation I've ever seen has the same hole in it: the predictions are stored in a table someone can edit. Not maliciously, usually. Someone reruns a pipeline, a backfill overwrites yesterday's rows, a "fix" recomputes an output with the model that was retrained this morning, and suddenly your 30-day accuracy number describes a model that never existed. The evaluation looks better, the model is not better, and nobody can tell the difference because there's no evidence trail. I build a football analytics platform where a few hundred independent models publish probability estimates b…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Write the query in a scratchpad and run EXPLAIN/QUERY PLAN to verify performance.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/soccerdream_ai/immutable-predictions-a-schema-for-grading-model-output-you-cant-quietly-rewrite-2o82

## Related notes
- [[2026-08-21-how-to-find-duplicate-rows-in-sql-and-decide-what-counts-as-one]]
- [[2026-10-15-free-draft-volume-or-paid-first-passes-a-debate-for-agent-sql-budgets]]
- [[2026-10-30-count-accepted-jobs-not-successful-api-calls-when-comparing-ai-workflows]]
- [[2026-08-31-running-total-in-sql-the-window-frame-that-decides-the-answer]]
- [[2026-09-29-the-not-in-trap-why-your-sql-query-returns-zero-rows]]
- [[2026-08-13-3-testing-habits-that-caught-bugs-before-my-users-did]]
