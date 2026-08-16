---
title: 'Qdrant Recall Inconsistency: It Took 300 Test Runs to Discover the Index Wasn''t
  Refreshed'
date: '2026-08-16'
source: https://dev.to/_eb7f2a654e97a60ae9f96e/qdrant-recall-inconsistency-it-took-300-test-runs-to-discover-the-index-wasnt-refreshed-3agf
domain: SQL
relevance: 🟡
tags:
- '#ai'
- '#python'
- '#sql'
related:
- '[[2026-05-08-from-2-hours-to-3-minutes-eliminating-missed-tests-in-ai-memory-consistency-testing]]'
- '[[2026-07-19-one-missed-test-case-cost-me-8-hours-how-i-built-a-zero-regression-memory-test-suite-with-pytest-docker]]'
- '[[2026-08-13-cutting-ai-agent-memory-testing-from-40-minutes-to-3-with-pytest-docker]]'
- '[[2026-05-02-uncovering-8-indexeddb-data-loss-after-browser-crashes-with-playwright]]'
- '[[2026-06-15-day-01-of-learning-data-engineering-step1-sql-joins-and-set-operators]]'
- '[[2026-08-13-contract-testing-vector-db-memory-storage-with-pytest-allure-60-fewer-regression-incidents]]'
status: unread
---

> **TL;DR:** At 2 AM, a user reported that the AI Agent suddenly forgot details of a project we discussed yesterday. I groggily opened Grafana and saw the memory recall rate had dropped from 98% to 60%. My first thought was the embed…

## What’s new and why it matters
At 2 AM, a user reported that the AI Agent suddenly forgot details of a project we discussed yesterday. I groggily opened Grafana and saw the memory recall rate had dropped from 98% to 60%. My first thought was the embedding model acting up again, but after digging through logs, I found a "time gap" between Qdrant writes and queries—data was upserted, yet queries intermittently returned nothing. This wasn't the first time, so I decided to automate recall consistency testing with pytest + Qdrant, and discovered the pitfalls were deeper than expected. Problem Breakdown The AI Agent's memory stor…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Write the query in a scratchpad and run EXPLAIN/QUERY PLAN to verify performance.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/_eb7f2a654e97a60ae9f96e/qdrant-recall-inconsistency-it-took-300-test-runs-to-discover-the-index-wasnt-refreshed-3agf

## Related notes
- [[2026-05-08-from-2-hours-to-3-minutes-eliminating-missed-tests-in-ai-memory-consistency-testing]]
- [[2026-07-19-one-missed-test-case-cost-me-8-hours-how-i-built-a-zero-regression-memory-test-suite-with-pytest-docker]]
- [[2026-08-13-cutting-ai-agent-memory-testing-from-40-minutes-to-3-with-pytest-docker]]
- [[2026-05-02-uncovering-8-indexeddb-data-loss-after-browser-crashes-with-playwright]]
- [[2026-06-15-day-01-of-learning-data-engineering-step1-sql-joins-and-set-operators]]
- [[2026-08-13-contract-testing-vector-db-memory-storage-with-pytest-allure-60-fewer-regression-incidents]]
