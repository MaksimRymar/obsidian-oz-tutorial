---
title: Extracting Column Lineage from Flink SQL Without Running a Cluster
date: '2026-11-18'
source: https://dev.to/jarred0214/extracting-column-lineage-from-flink-sql-without-running-a-cluster-2ajp
domain: SQL
relevance: 🟡
tags:
- '#ai'
- '#sql'
- '#tool'
related:
- '[[2026-05-01-i-built-a-vs-code-extension-to-debug-mysql-queries-step-by-step]]'
- '[[2026-09-15-sql-joins-explained]]'
- '[[2026-11-18-how-to-find-out-what-1000-websites-are-built-with-and-what-you-cant-see-from-outside]]'
- '[[2026-06-28-how-to-generate-a-sql-schema-from-a-csv-file-without-hand-writing-every-column-type]]'
- '[[2026-08-21-how-to-find-duplicate-rows-in-sql-and-decide-what-counts-as-one]]'
- '[[2026-05-10-why-where-phone-null-returns-nothing-in-sql]]'
status: unread
---

> **TL;DR:** Before dropping a source column, I want to know which downstream columns depend on it. Searching SQL files helps find direct references, but a temporary view can hide the connection between the source column and the fina…

## What’s new and why it matters
Before dropping a source column, I want to know which downstream columns depend on it. Searching SQL files helps find direct references, but a temporary view can hide the connection between the source column and the final write. I built LineSQL to extract those relationships from SQL scripts. This Flink example runs locally with Java and curl. curl -fsSL \ https://repo.maven.apache.org/maven2/io/github/jarredhj0214/linesql-cli/1.3.0/linesql-cli-1.3.0.jar \ -o linesql.jar && java -jar linesql.jar --dialect FLINK " CREATE TEMPORARY VIEW active_users AS SELECT id FROM ods.users WHERE status = 'AC…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Write the query in a scratchpad and run EXPLAIN/QUERY PLAN to verify performance.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/jarred0214/extracting-column-lineage-from-flink-sql-without-running-a-cluster-2ajp

## Related notes
- [[2026-05-01-i-built-a-vs-code-extension-to-debug-mysql-queries-step-by-step]]
- [[2026-09-15-sql-joins-explained]]
- [[2026-11-18-how-to-find-out-what-1000-websites-are-built-with-and-what-you-cant-see-from-outside]]
- [[2026-06-28-how-to-generate-a-sql-schema-from-a-csv-file-without-hand-writing-every-column-type]]
- [[2026-08-21-how-to-find-duplicate-rows-in-sql-and-decide-what-counts-as-one]]
- [[2026-05-10-why-where-phone-null-returns-nothing-in-sql]]
