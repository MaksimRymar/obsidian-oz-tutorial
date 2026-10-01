---
title: 'Your Demo Dashboard Is Not a Funnel: Auditing Synthetic Events in ClickHouse'
date: '2026-10-01'
source: https://dev.to/sensorflow/your-demo-dashboard-is-not-a-funnel-auditing-synthetic-events-in-clickhouse-527f
domain: SQL
relevance: 🟡
tags:
- '#feature'
- '#sql'
- '#tableau'
- '#tool'
related:
- '[[2026-08-21-how-to-find-duplicate-rows-in-sql-and-decide-what-counts-as-one]]'
- '[[2026-08-05-reconstructing-wallet-journeys-across-dex-frontends-one-chain-at-a-time]]'
- '[[2026-09-01-seeding-fixtures-realistic-test-data-for-warehouse-integration-tests]]'
- '[[2026-07-23-the-3-user-personas-that-determine-the-success-of-an-enterprise-data-platform]]'
- '[[2026-08-11-the-text-to-sql-demo-takes-an-afternoon-the-other-90-is-why-you-should-buy-it]]'
- '[[2026-06-13-top-12-sql-interview-problems-for-data-engineers-with-answers]]'
status: unread
---

> **TL;DR:** A newly installed analytics stack can show a convincing sequence of "app open → product view → add to cart → purchase" before it has ingested a single real user event. That is useful for testing whether the database and…

## What’s new and why it matters
A newly installed analytics stack can show a convincing sequence of "app open → product view → add to cart → purchase" before it has ingested a single real user event. That is useful for testing whether the database and dashboard start, but it is not evidence of conversion. Four non-empty bars may represent four disjoint groups of users. This is a practical audit of SensorFlow's public demo-data generator . SensorFlow is an independent, open-source, self-hosted event pipeline built around an existing Sensors Data SDK integration, a Go receiver, ClickHouse, and Apache Superset. It does not clai…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Write the query in a scratchpad and run EXPLAIN/QUERY PLAN to verify performance.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/sensorflow/your-demo-dashboard-is-not-a-funnel-auditing-synthetic-events-in-clickhouse-527f

## Related notes
- [[2026-08-21-how-to-find-duplicate-rows-in-sql-and-decide-what-counts-as-one]]
- [[2026-08-05-reconstructing-wallet-journeys-across-dex-frontends-one-chain-at-a-time]]
- [[2026-09-01-seeding-fixtures-realistic-test-data-for-warehouse-integration-tests]]
- [[2026-07-23-the-3-user-personas-that-determine-the-success-of-an-enterprise-data-platform]]
- [[2026-08-11-the-text-to-sql-demo-takes-an-afternoon-the-other-90-is-why-you-should-buy-it]]
- [[2026-06-13-top-12-sql-interview-problems-for-data-engineers-with-answers]]
