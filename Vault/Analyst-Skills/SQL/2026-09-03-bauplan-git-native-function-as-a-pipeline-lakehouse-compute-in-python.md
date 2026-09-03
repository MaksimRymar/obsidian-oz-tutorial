---
title: 'Bauplan: Git-Native, Function-as-a-Pipeline Lakehouse Compute in Python'
date: '2026-09-03'
source: https://dev.to/gowthampotureddi/bauplan-git-native-function-as-a-pipeline-lakehouse-compute-in-python-5fo9
domain: SQL
relevance: 🔴
tags:
- '#ai'
- '#best-practice'
- '#career'
- '#feature'
- '#library'
- '#python'
- '#sql'
- '#support-analytics'
- '#tool'
- '#tutorial'
- '#zendesk'
related:
- '[[2026-09-01-i-raced-six-models-against-each-other-on-digitalocean-inference-the-cheapest-one-won]]'
- '[[2026-08-21-how-to-find-duplicate-rows-in-sql-and-decide-what-counts-as-one]]'
- '[[2026-06-10-sql-for-data-analysis-the-10-query-patterns-that-matter]]'
- '[[2026-08-30-dataform-for-bigquery-google-native-transformation-assertions-cicd]]'
- '[[2026-08-31-subquery-vs-cte-in-sql-same-logic-one-you-can-check]]'
- '[[2026-08-31-how-to-reconcile-two-tables-in-sql-when-the-row-counts-match]]'
status: unread
---

> **TL;DR:** Bauplan is what you get when someone looks at the modern data stack — a Spark cluster for compute, dbt for transformations, a separate catalog like Nessie or lakeFS for data version control, an orchestrator to wire it al…

## What’s new and why it matters
Bauplan is what you get when someone looks at the modern data stack — a Spark cluster for compute, dbt for transformations, a separate catalog like Nessie or lakeFS for data version control, an orchestrator to wire it all together — and decides to collapse the whole assembly into a single programmable runtime. You write your pipeline as ordinary Python functions, each function a node in a directed acyclic graph, and the platform runs them serverless over Iceberg tables in your own object storage. There is no cluster to size, no separate transformation framework to learn, and no bolt-on version…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Write the query in a scratchpad and run EXPLAIN/QUERY PLAN to verify performance.
- Add a short note: what changed in your workflow?

## Relevance
🔴

## Source
https://dev.to/gowthampotureddi/bauplan-git-native-function-as-a-pipeline-lakehouse-compute-in-python-5fo9

## Related notes
- [[2026-09-01-i-raced-six-models-against-each-other-on-digitalocean-inference-the-cheapest-one-won]]
- [[2026-08-21-how-to-find-duplicate-rows-in-sql-and-decide-what-counts-as-one]]
- [[2026-06-10-sql-for-data-analysis-the-10-query-patterns-that-matter]]
- [[2026-08-30-dataform-for-bigquery-google-native-transformation-assertions-cicd]]
- [[2026-08-31-subquery-vs-cte-in-sql-same-logic-one-you-can-check]]
- [[2026-08-31-how-to-reconcile-two-tables-in-sql-when-the-row-counts-match]]
