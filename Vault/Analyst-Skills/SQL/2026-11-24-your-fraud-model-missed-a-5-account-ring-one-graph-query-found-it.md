---
title: Your Fraud Model Missed a 5-Account Ring. One Graph Query Found It.
date: '2026-11-24'
source: https://dev.to/synapcores/your-fraud-model-missed-a-5-account-ring-one-graph-query-found-it-6dc
domain: SQL
relevance: 🟡
tags:
- '#ai'
- '#best-practice'
- '#feature'
- '#sql'
- '#tool'
related:
- '[[2026-11-12-ai-brand-tracking-a-practical-check-you-can-run-today-by-yourself]]'
- '[[2026-09-16-sql-joins-with-examples-of-each]]'
- '[[2026-10-26-sql-joins-explained-inner-left-right-and-full-with-examples]]'
- '[[2026-10-06-i-scanned-1152-dbt-models-for-joins-that-inflate-sum-here-is-what-i-found]]'
- '[[2026-08-31-running-total-in-sql-the-window-frame-that-decides-the-answer]]'
- '[[2026-11-13-5-sql-mistakes-that-return-the-wrong-number-with-no-error-reproduce-each-one-in-postgres]]'
status: unread
---

> **TL;DR:** Fraud models have a blind spot built into how they work: they score one row at a time . That's exactly right for the lone fraudster, whose payments are huge, at 3am, from abroad. It does nothing against a fraud ring : fi…

## What’s new and why it matters
Fraud models have a blind spot built into how they work: they score one row at a time . That's exactly right for the lone fraudster, whose payments are huge, at 3am, from abroad. It does nothing against a fraud ring : five accounts that each spend like a normal customer but share one phone and a couple of stolen card numbers. The ring isn't in any row. It's in the connections between rows . Here's a worked example with real numbers. I re-ran every query below this morning on a fresh install, and the data, model and queries are all in a recipe you can run yourself. The setup: 40 ordinary accoun…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Write the query in a scratchpad and run EXPLAIN/QUERY PLAN to verify performance.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/synapcores/your-fraud-model-missed-a-5-account-ring-one-graph-query-found-it-6dc

## Related notes
- [[2026-11-12-ai-brand-tracking-a-practical-check-you-can-run-today-by-yourself]]
- [[2026-09-16-sql-joins-with-examples-of-each]]
- [[2026-10-26-sql-joins-explained-inner-left-right-and-full-with-examples]]
- [[2026-10-06-i-scanned-1152-dbt-models-for-joins-that-inflate-sum-here-is-what-i-found]]
- [[2026-08-31-running-total-in-sql-the-window-frame-that-decides-the-answer]]
- [[2026-11-13-5-sql-mistakes-that-return-the-wrong-number-with-no-error-reproduce-each-one-in-postgres]]
