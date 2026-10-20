---
title: When ClickHouse merges change your query results
date: '2026-10-20'
source: https://dev.to/maksim-gr/when-clickhouse-merges-change-your-query-results-5d99
domain: SQL
relevance: 🟡
tags:
- '#ai'
- '#best-practice'
- '#sql'
- '#tool'
- '#tutorial'
- '#zendesk'
related:
- '[[2026-09-25-5-sql-patterns-that-run-fine-and-still-return-the-wrong-answer]]'
- '[[2026-07-23-btree-height-after-delete-postgresql-fast-root]]'
- '[[2026-09-16-sql-joins-with-examples-of-each]]'
- '[[2026-08-31-running-total-in-sql-the-window-frame-that-decides-the-answer]]'
- '[[2026-08-21-how-to-find-duplicate-rows-in-sql-and-decide-what-counts-as-one]]'
- '[[2026-09-01-i-raced-six-models-against-each-other-on-digitalocean-inference-the-cheapest-one-won]]'
status: unread
---

> **TL;DR:** In Part 1 I followed an order from INSERT through a merge. That answered two questions that came up during coffee breaks at work. This post tackles the third: "Why doesn't my SELECT show the values I expect?" I usually h…

## What’s new and why it matters
In Part 1 I followed an order from INSERT through a merge. That answered two questions that came up during coffee breaks at work. This post tackles the third: "Why doesn't my SELECT show the values I expect?" I usually hear this question from people using SummingMergeTree , AggregatingMergeTree , or CollapsingMergeTree . In these engines, a merge can change the rows themselves: it sums them, collapses them, or removes them. As a result, the same query can return different results depending on how many merges have occurred. If you skipped Part 1, three things from it matter here. Each inserted…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Write the query in a scratchpad and run EXPLAIN/QUERY PLAN to verify performance.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/maksim-gr/when-clickhouse-merges-change-your-query-results-5d99

## Related notes
- [[2026-09-25-5-sql-patterns-that-run-fine-and-still-return-the-wrong-answer]]
- [[2026-07-23-btree-height-after-delete-postgresql-fast-root]]
- [[2026-09-16-sql-joins-with-examples-of-each]]
- [[2026-08-31-running-total-in-sql-the-window-frame-that-decides-the-answer]]
- [[2026-08-21-how-to-find-duplicate-rows-in-sql-and-decide-what-counts-as-one]]
- [[2026-09-01-i-raced-six-models-against-each-other-on-digitalocean-inference-the-cheapest-one-won]]
