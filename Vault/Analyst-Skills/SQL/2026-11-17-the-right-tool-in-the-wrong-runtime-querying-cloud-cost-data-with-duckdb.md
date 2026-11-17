---
title: 'The Right Tool in the Wrong Runtime: Querying Cloud Cost Data with DuckDB'
date: '2026-11-17'
source: https://dev.to/v4nd1t/the-right-tool-in-the-wrong-runtime-querying-cloud-cost-data-with-duckdb-4604
domain: SQL
relevance: 🟡
tags:
- '#ai'
- '#best-practice'
- '#feature'
- '#library'
- '#python'
- '#sql'
- '#tool'
- '#tutorial'
related:
- '[[2026-09-14-duckdb-in-production-what-its-actually-good-at-and-what-it-isnt]]'
- '[[2026-06-25-duckdb-for-data-engineering-in-process-olap-local-etl-parquet-first-workflows]]'
- '[[2026-09-17-one-ai-assistant-many-databases-wiring-up-multiple-data-sources-with-mcp]]'
- '[[2026-07-06-your-postgres-already-knows-why-its-slow-you-just-have-to-ask-it]]'
- '[[2026-04-22-sql-set-operators-union-intersect-and-except-explained-simply]]'
- '[[2026-09-16-the-data-modeling-concepts-nobody-mentions-after-star-schema-101]]'
status: unread
---

> **TL;DR:** Here's a task that sounds boring and turned into the most useful infrastructure lesson I learned all year: let people ask questions about our cloud bill. Not "what's the total," the finance dashboard does that. Questions…

## What’s new and why it matters
Here's a task that sounds boring and turned into the most useful infrastructure lesson I learned all year: let people ask questions about our cloud bill. Not "what's the total," the finance dashboard does that. Questions like "which service, in which compartment, drove last month's spike, broken down by day." That means querying the raw, itemized billing data, and cloud billing data is genuinely large: one row per resource per hour, dozens of columns, dumped as a pile of compressed CSV files into object storage. I went through three architectures to serve those queries. The interesting part is…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Write the query in a scratchpad and run EXPLAIN/QUERY PLAN to verify performance.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/v4nd1t/the-right-tool-in-the-wrong-runtime-querying-cloud-cost-data-with-duckdb-4604

## Related notes
- [[2026-09-14-duckdb-in-production-what-its-actually-good-at-and-what-it-isnt]]
- [[2026-06-25-duckdb-for-data-engineering-in-process-olap-local-etl-parquet-first-workflows]]
- [[2026-09-17-one-ai-assistant-many-databases-wiring-up-multiple-data-sources-with-mcp]]
- [[2026-07-06-your-postgres-already-knows-why-its-slow-you-just-have-to-ask-it]]
- [[2026-04-22-sql-set-operators-union-intersect-and-except-explained-simply]]
- [[2026-09-16-the-data-modeling-concepts-nobody-mentions-after-star-schema-101]]
