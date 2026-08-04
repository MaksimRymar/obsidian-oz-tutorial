---
title: 'Optimizing an 18 TB Azure SQL Hyperscale Database — Part 3: The Real Cost
  of Indexes'
date: '2026-08-04'
source: https://dev.to/kostyabartashevich/optimizing-an-18-tb-azure-sql-hyperscale-database-part-3-the-real-cost-of-indexes-5500
domain: SQL
relevance: 🟡
tags:
- '#ai'
- '#sql'
- '#tool'
related:
- '[[2026-06-15-day-01-of-learning-data-engineering-step1-sql-joins-and-set-operators]]'
- '[[2026-07-06-your-postgres-already-knows-why-its-slow-you-just-have-to-ask-it]]'
- '[[2026-07-21-my-gitignore-had-a-blanket-rule-one-file-broke-it-and-no-pattern-would-have-caught-that]]'
- '[[2026-07-24-long-running-sql-queries-a-sample-exploration]]'
- '[[2026-03-30-database-indexing-explained-whats-actually-happening-under-the-hood]]'
- '[[2026-06-23-aws-glue-or-airflow-youre-probably-paying-for-both-to-do-one-job]]'
status: unread
---

> **TL;DR:** Previously: we halved compute by understanding a spiky load profile. Cutting CPU was only half the picture — the database's size and its indexes were the other half. Two things about fragmentation stood out early. First,…

## What’s new and why it matters
Previously: we halved compute by understanding a spiky load profile. Cutting CPU was only half the picture — the database's size and its indexes were the other half. Two things about fragmentation stood out early. First, there was no regular index maintenance job at all, so fragmentation simply accumulated. Second — and more fundamental — several of the largest, busiest tables used a random uniqueidentifier (GUID) as their clustered primary key . Here's why that matters, briefly. A clustered index defines the physical order in which rows are stored. With a random GUID, new rows don't land at t…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Write the query in a scratchpad and run EXPLAIN/QUERY PLAN to verify performance.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/kostyabartashevich/optimizing-an-18-tb-azure-sql-hyperscale-database-part-3-the-real-cost-of-indexes-5500

## Related notes
- [[2026-06-15-day-01-of-learning-data-engineering-step1-sql-joins-and-set-operators]]
- [[2026-07-06-your-postgres-already-knows-why-its-slow-you-just-have-to-ask-it]]
- [[2026-07-21-my-gitignore-had-a-blanket-rule-one-file-broke-it-and-no-pattern-would-have-caught-that]]
- [[2026-07-24-long-running-sql-queries-a-sample-exploration]]
- [[2026-03-30-database-indexing-explained-whats-actually-happening-under-the-hood]]
- [[2026-06-23-aws-glue-or-airflow-youre-probably-paying-for-both-to-do-one-job]]
