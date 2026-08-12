---
title: How to Grade Search Relevance Before You Touch the Ranking Weights
date: '2026-08-11'
source: https://dev.to/libme/how-to-grade-search-relevance-before-you-touch-the-ranking-weights-3554
domain: SQL
relevance: 🟡
tags:
- '#ai'
- '#feature'
- '#python'
- '#sql'
- '#tool'
- '#tutorial'
related:
- '[[2026-08-11-how-to-test-search-relevance-before-you-ship-a-ranking-change]]'
- '[[2026-05-20-learning-sql-as-if-you-built-it-yourself]]'
- '[[2026-07-27-top-n-per-group-is-the-query-limit-cant-write]]'
- '[[2026-03-30-database-indexing-explained-whats-actually-happening-under-the-hood]]'
- '[[2026-04-21-sql-window-functions-and-ctes]]'
- '[[2026-08-09-why-your-python-search-cant-find-c-c-or-rd-and-how-to-fix-it]]'
status: unread
---

> **TL;DR:** Before you change a single ts_rank weight, freeze your corpus and score the current ranking against a set of graded judgments. Otherwise you are comparing two moving targets — new weights and new documents — and you will…

## What’s new and why it matters
Before you change a single ts_rank weight, freeze your corpus and score the current ranking against a set of graded judgments. Otherwise you are comparing two moving targets — new weights and new documents — and you will never know which one moved the needle. A relevance regression harness turns "search feels worse since Tuesday" into a number you can diff, the same way a test suite turns "the code feels broken" into a red check. I wrote earlier about load-testing a Postgres full-text index and pinning down relevance. A commenter on that post sharpened the key point: if you tune weights agains…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Write the query in a scratchpad and run EXPLAIN/QUERY PLAN to verify performance.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/libme/how-to-grade-search-relevance-before-you-touch-the-ranking-weights-3554

## Related notes
- [[2026-08-11-how-to-test-search-relevance-before-you-ship-a-ranking-change]]
- [[2026-05-20-learning-sql-as-if-you-built-it-yourself]]
- [[2026-07-27-top-n-per-group-is-the-query-limit-cant-write]]
- [[2026-03-30-database-indexing-explained-whats-actually-happening-under-the-hood]]
- [[2026-04-21-sql-window-functions-and-ctes]]
- [[2026-08-09-why-your-python-search-cant-find-c-c-or-rd-and-how-to-fix-it]]
