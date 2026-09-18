---
title: 'How to Optimize Slow dbt Models: Incremental Models, DAGs, and Query Performance'
date: '2026-09-18'
source: https://dev.to/harulmozhi/how-to-optimize-slow-dbt-models-incremental-models-dags-and-query-performance-4l0
domain: SQL
relevance: 🟡
tags:
- '#ai'
- '#best-practice'
- '#sql'
- '#support-analytics'
- '#tool'
- '#tutorial'
- '#zendesk'
related:
- '[[2026-04-02-how-to-stop-your-ai-agent-from-burning-400month-on-api-calls]]'
- '[[2026-09-01-i-raced-six-models-against-each-other-on-digitalocean-inference-the-cheapest-one-won]]'
- '[[2026-09-07-subqueries-ctes-in-sql-what-they-are-and-when-to-use-each]]'
- '[[2026-03-15-data-quality-testing-how-bruin-and-dbt-take-different-paths-to-the-same-goal]]'
- '[[2026-08-30-sqlmesh-vs-dbt-virtual-data-environments-column-level-lineage-blue-green-deploys]]'
- '[[2026-08-20-a-benchmark-is-only-as-good-as-the-model-you-use-to-grade-it]]'
status: unread
---

> **TL;DR:** If a dbt project has slow models, where should an engineering team actually start? Not with the model that takes the longest to build. That is the intuitive place to look, and it is usually the wrong one. dbt model optim…

## What’s new and why it matters
If a dbt project has slow models, where should an engineering team actually start? Not with the model that takes the longest to build. That is the intuitive place to look, and it is usually the wrong one. dbt model optimization done well starts with the DAG, because the DAG tells you something query-level profiling cannot: how much of the pipeline is waiting on any single model to finish. A model that takes six minutes and has forty downstream dependents is a bigger problem than a model that takes twenty minutes and has none. This piece walks through the order that actually works, based on how…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Write the query in a scratchpad and run EXPLAIN/QUERY PLAN to verify performance.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/harulmozhi/how-to-optimize-slow-dbt-models-incremental-models-dags-and-query-performance-4l0

## Related notes
- [[2026-04-02-how-to-stop-your-ai-agent-from-burning-400month-on-api-calls]]
- [[2026-09-01-i-raced-six-models-against-each-other-on-digitalocean-inference-the-cheapest-one-won]]
- [[2026-09-07-subqueries-ctes-in-sql-what-they-are-and-when-to-use-each]]
- [[2026-03-15-data-quality-testing-how-bruin-and-dbt-take-different-paths-to-the-same-goal]]
- [[2026-08-30-sqlmesh-vs-dbt-virtual-data-environments-column-level-lineage-blue-green-deploys]]
- [[2026-08-20-a-benchmark-is-only-as-good-as-the-model-you-use-to-grade-it]]
