---
title: 'AWS Glue Deep Dive: Crawlers, Job Bookmarks, DynamicFrames & Spark Tuning'
date: '2026-08-24'
source: https://dev.to/gowthampotureddi/aws-glue-deep-dive-crawlers-job-bookmarks-dynamicframes-spark-tuning-47af
domain: SQL
relevance: 🟡
tags:
- '#ai'
- '#best-practice'
- '#career'
- '#feature'
- '#library'
- '#python'
- '#sql'
- '#tableau'
- '#tool'
- '#tutorial'
- '#zendesk'
related:
- '[[2026-06-27-spark-tuning-cheat-sheet-shuffle-partitions-skew-broadcast-persist-memory-fractions]]'
- '[[2026-06-02-sql-data-types-deep-dive-int-numeric-varchar-json-array-timestamp]]'
- '[[2026-06-10-sql-for-data-analysis-the-10-query-patterns-that-matter]]'
- '[[2026-08-23-apache-hive-deep-dive-for-data-engineers-metastore-partitions-orc-tez-vs-mapreduce]]'
- '[[2026-08-21-how-to-find-duplicate-rows-in-sql-and-decide-what-counts-as-one]]'
- '[[2026-08-21-null-in-sql-why-null-finds-nothing-and-what-to-write-instead]]'
status: unread
---

> **TL;DR:** AWS Glue is the service that most data engineers reach for the moment "we need serverless Spark ETL on AWS" enters a conversation — and it is also the service that quietly triples a bill or silently re-processes yesterda…

## What’s new and why it matters
AWS Glue is the service that most data engineers reach for the moment "we need serverless Spark ETL on AWS" enters a conversation — and it is also the service that quietly triples a bill or silently re-processes yesterday's data because four of its abstractions do not behave the way a plain Spark job would. A crawler infers a schema and writes it into the Glue Data Catalog ; a Glue job runs Spark against that catalog; a job bookmark remembers which files it already read so the next run is incremental; and a DynamicFrame carries records whose schema was never fixed up front. Get any one of thos…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Write the query in a scratchpad and run EXPLAIN/QUERY PLAN to verify performance.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/gowthampotureddi/aws-glue-deep-dive-crawlers-job-bookmarks-dynamicframes-spark-tuning-47af

## Related notes
- [[2026-06-27-spark-tuning-cheat-sheet-shuffle-partitions-skew-broadcast-persist-memory-fractions]]
- [[2026-06-02-sql-data-types-deep-dive-int-numeric-varchar-json-array-timestamp]]
- [[2026-06-10-sql-for-data-analysis-the-10-query-patterns-that-matter]]
- [[2026-08-23-apache-hive-deep-dive-for-data-engineers-metastore-partitions-orc-tez-vs-mapreduce]]
- [[2026-08-21-how-to-find-duplicate-rows-in-sql-and-decide-what-counts-as-one]]
- [[2026-08-21-null-in-sql-why-null-finds-nothing-and-what-to-write-instead]]
