---
title: Real-Time Data Classification with Generated Columns
date: '2026-08-26'
source: https://dev.to/crate/real-time-data-classification-with-generated-columns-15ip
domain: SQL
relevance: 🟡
tags:
- '#feature'
- '#sql'
- '#tool'
- '#zendesk'
related:
- '[[2026-08-21-how-to-find-duplicate-rows-in-sql-and-decide-what-counts-as-one]]'
- '[[2026-08-11-sql-joins-how-to-join-two-tables-without-losing-or-doubling-rows]]'
- '[[2026-08-11-the-text-to-sql-demo-takes-an-afternoon-the-other-90-is-why-you-should-buy-it]]'
- '[[2026-08-11-sql-aliases-how-to-read-a-query-out-loud]]'
- '[[2026-04-08-how-building-a-streaming-sql-api-in-nodejs-changed-my-approach-to-real-time-data]]'
- '[[2026-08-12-can-you-run-hybrid-search-on-one-database-yes-heres-how-cratedb-does-it]]'
status: unread
---

> **TL;DR:** Traditionally, there have been two ways to process data: Load it exactly as is, then figure out how to clean it up. This implies an extra round of processing and means there will be a lag between data arriving and it bei…

## What’s new and why it matters
Traditionally, there have been two ways to process data: Load it exactly as is, then figure out how to clean it up. This implies an extra round of processing and means there will be a lag between data arriving and it being usable. Treat it with the greatest suspicion and only load it after an elaborate sanity check. It’s the same work but done earlier. But sometimes there’s a ‘middle way’. CrateDB’s generated columns allow you to categorize and index data as it arrives. While a very simple feature, it can be remarkably useful, as the database applies it on every insert, no matter who is doing…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Write the query in a scratchpad and run EXPLAIN/QUERY PLAN to verify performance.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/crate/real-time-data-classification-with-generated-columns-15ip

## Related notes
- [[2026-08-21-how-to-find-duplicate-rows-in-sql-and-decide-what-counts-as-one]]
- [[2026-08-11-sql-joins-how-to-join-two-tables-without-losing-or-doubling-rows]]
- [[2026-08-11-the-text-to-sql-demo-takes-an-afternoon-the-other-90-is-why-you-should-buy-it]]
- [[2026-08-11-sql-aliases-how-to-read-a-query-out-loud]]
- [[2026-04-08-how-building-a-streaming-sql-api-in-nodejs-changed-my-approach-to-real-time-data]]
- [[2026-08-12-can-you-run-hybrid-search-on-one-database-yes-heres-how-cratedb-does-it]]
