---
title: It passed every constraint. It was still wrong.
date: '2026-10-29'
source: https://dev.to/generaterealdata/it-passed-every-constraint-it-was-still-wrong-187f
domain: SQL
relevance: 🔴
tags:
- '#ai'
- '#best-practice'
- '#python'
- '#sql'
- '#tool'
- '#zendesk'
related:
- '[[2026-08-21-how-to-find-duplicate-rows-in-sql-and-decide-what-counts-as-one]]'
- '[[2026-10-06-i-scanned-1152-dbt-models-for-joins-that-inflate-sum-here-is-what-i-found]]'
- '[[2026-09-01-seeding-fixtures-realistic-test-data-for-warehouse-integration-tests]]'
- '[[2026-08-31-running-total-in-sql-the-window-frame-that-decides-the-answer]]'
- '[[2026-08-18-the-duplicate-rows-query-you-re-google-every-six-weeks]]'
- '[[2026-10-16-an-ai-explained-sql-group-by-in-four-lines-one-of-them-is-wrong]]'
status: unread
---

> **TL;DR:** My first generated test database loaded without a single error. Every foreign key resolved. Row counts matched. The first twenty rows of every table looked right: sensible names, dates and prices. Then I asked it one que…

## What’s new and why it matters
My first generated test database loaded without a single error. Every foreign key resolved. Row counts matched. The first twenty rows of every table looked right: sensible names, dates and prices. Then I asked it one question: how many cancelled orders have a shipment? The answer was not zero. No constraint had complained, because no constraint could. This post is the method I've used since to prove a multi-table dataset is consistent. It needs nothing but SQL, and it works on any data: generated, sampled from production, or produced by a pipeline you're testing. Quick quiz before you scroll W…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Write the query in a scratchpad and run EXPLAIN/QUERY PLAN to verify performance.
- Add a short note: what changed in your workflow?

## Relevance
🔴

## Source
https://dev.to/generaterealdata/it-passed-every-constraint-it-was-still-wrong-187f

## Related notes
- [[2026-08-21-how-to-find-duplicate-rows-in-sql-and-decide-what-counts-as-one]]
- [[2026-10-06-i-scanned-1152-dbt-models-for-joins-that-inflate-sum-here-is-what-i-found]]
- [[2026-09-01-seeding-fixtures-realistic-test-data-for-warehouse-integration-tests]]
- [[2026-08-31-running-total-in-sql-the-window-frame-that-decides-the-answer]]
- [[2026-08-18-the-duplicate-rows-query-you-re-google-every-six-weeks]]
- [[2026-10-16-an-ai-explained-sql-group-by-in-four-lines-one-of-them-is-wrong]]
