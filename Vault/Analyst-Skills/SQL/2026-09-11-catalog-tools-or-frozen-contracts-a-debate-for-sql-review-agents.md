---
title: 'Catalog Tools or Frozen Contracts: A Debate for SQL Review Agents'
date: '2026-09-11'
source: https://dev.to/dataio_4921/catalog-tools-or-frozen-contracts-a-debate-for-sql-review-agents-5400
domain: SQL
relevance: 🟡
tags:
- '#ai'
- '#library'
- '#python'
- '#sql'
- '#tool'
related:
- '[[2026-09-04-when-index-hit-stats-go-stale-two-positions-for-sql-review-agents]]'
- '[[2026-09-05-a-frozen-test-is-not-coverage-a-merge-gate-for-agent-patches]]'
- '[[2026-09-09-pick-agent-compute-by-blast-radius-not-by-the-price-tag]]'
- '[[2026-09-05-how-query-optimizers-work-statistics-cardinality-join-order]]'
- '[[2026-09-08-charge-wait-time-to-the-same-job]]'
- '[[2026-08-14-schema-linting-vs-migration-linting-which-database-problems-each-one-can-see]]'
status: unread
---

> **TL;DR:** A pull request added a reporting query that joined orders, order_items, products, and a new promo_windows table. The SQL review agent still carried last week's schema dump inside its prompt context window. It treated pro…

## What’s new and why it matters
A pull request added a reporting query that joined orders, order_items, products, and a new promo_windows table. The SQL review agent still carried last week's schema dump inside its prompt context window. It treated promo_windows as missing and opened a false-positive finding against a table that already existed. A second run queried information_schema.columns during review and accepted the join, but that path needed a live database session in CI. That fork is the subject of this debate: on-demand catalog tools versus versioned schema contracts. The problem both sides are trying to bound SQL…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Write the query in a scratchpad and run EXPLAIN/QUERY PLAN to verify performance.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/dataio_4921/catalog-tools-or-frozen-contracts-a-debate-for-sql-review-agents-5400

## Related notes
- [[2026-09-04-when-index-hit-stats-go-stale-two-positions-for-sql-review-agents]]
- [[2026-09-05-a-frozen-test-is-not-coverage-a-merge-gate-for-agent-patches]]
- [[2026-09-09-pick-agent-compute-by-blast-radius-not-by-the-price-tag]]
- [[2026-09-05-how-query-optimizers-work-statistics-cardinality-join-order]]
- [[2026-09-08-charge-wait-time-to-the-same-job]]
- [[2026-08-14-schema-linting-vs-migration-linting-which-database-problems-each-one-can-see]]
