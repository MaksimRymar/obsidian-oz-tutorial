---
title: SQL vs NoSQL on AWS (Aurora, RDS or DynamoDB)
date: '2026-11-15'
source: https://dev.to/aws/sql-vs-nosql-on-aws-aurora-rds-or-dynamodb-3kp3
domain: SQL
relevance: 🟡
tags:
- '#ai'
- '#best-practice'
- '#feature'
- '#sql'
- '#tool'
- '#tutorial'
- '#zendesk'
related:
- '[[2026-08-21-how-to-find-duplicate-rows-in-sql-and-decide-what-counts-as-one]]'
- '[[2026-06-04-why-we-built-an-sql-layer-for-dynamodb]]'
- '[[2026-09-16-sql-joins-with-examples-of-each]]'
- '[[2026-11-11-i-built-generaterealdata-a-test-data-generator-where-keys-totals-and-rules-hold-across-tables]]'
- '[[2026-09-08-cassandra-scylladb-wide-column-data-modeling-done-right]]'
- '[[2026-09-08-dynamodb-for-data-engineers-single-table-design-streams-s3-export]]'
status: unread
---

> **TL;DR:** Intro A database is one of the few architecture decisions that can be expensive to reverse. Pipelines can get replaced and caches get swapped easily, but by the time you know whether the database choice was right, you al…

## What’s new and why it matters
Intro A database is one of the few architecture decisions that can be expensive to reverse. Pipelines can get replaced and caches get swapped easily, but by the time you know whether the database choice was right, you already have a schema, query layer and production data that must move together. Consider our working example: You're a software engineer at REXTECH, a company that operates public EV charging stations across the United States and you've been handed the next version of their platform along with ownership of the data layer. The platform does three jobs: Drivers open an app to find…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Write the query in a scratchpad and run EXPLAIN/QUERY PLAN to verify performance.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/aws/sql-vs-nosql-on-aws-aurora-rds-or-dynamodb-3kp3

## Related notes
- [[2026-08-21-how-to-find-duplicate-rows-in-sql-and-decide-what-counts-as-one]]
- [[2026-06-04-why-we-built-an-sql-layer-for-dynamodb]]
- [[2026-09-16-sql-joins-with-examples-of-each]]
- [[2026-11-11-i-built-generaterealdata-a-test-data-generator-where-keys-totals-and-rules-hold-across-tables]]
- [[2026-09-08-cassandra-scylladb-wide-column-data-modeling-done-right]]
- [[2026-09-08-dynamodb-for-data-engineers-single-table-design-streams-s3-export]]
