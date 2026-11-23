---
title: 'MapReduce, Hive and Spark SQL on the same 7 jobs: Spark won by 1.5x, but 58%
  of its time was start-up'
date: '2026-11-23'
source: https://dev.to/protechscacademy/mapreduce-hive-and-spark-sql-on-the-same-7-jobs-spark-won-by-15x-but-58-of-its-time-was-4ikp
domain: Python
relevance: 🟡
tags:
- '#ai'
- '#python'
- '#sql'
- '#tool'
- '#tutorial'
related:
- '[[2026-08-31-subquery-vs-cte-in-sql-same-logic-one-you-can-check]]'
- '[[2026-10-27-ai-agents-can-run-sql-now-where-should-database-teams-draw-the-line]]'
- '[[2026-04-21-sql-window-functions-and-ctes]]'
- '[[2026-07-06-your-postgres-already-knows-why-its-slow-you-just-have-to-ask-it]]'
- '[[2026-09-05-what-actually-happens-in-a-database-index-and-why-half-of-them-do-nothing]]'
- '[[2026-11-03-im-an-ai-character-my-youtube-shorts-stats-misled-me-three-times-in-one-night]]'
status: unread
---

> **TL;DR:** How much did each generation of the Hadoop-era tools actually change? We wrote the same seven analyses three times and ran them on the same files: Generation 1: hand-written Java MapReduce jobs Generation 2: HiveQL on Hi…

## What’s new and why it matters
How much did each generation of the Hadoop-era tools actually change? We wrote the same seven analyses three times and ran them on the same files: Generation 1: hand-written Java MapReduce jobs Generation 2: HiveQL on Hive 4.2.1 with its MapReduce engine Generation 3: Spark SQL 4.3.0 on YARN plus Spark in local mode as an ablation. The setup Data: NASA web-server logs of 1995 and generated TPC-H tables, at two sizes: sf1 (1.34 GB) and sf3 (4.06 GB). Jobs: word count, requests per day and top 10 URLs over the logs; TPC-H Q1, Q6, Q3 and Q12 . Same everything: the same files in HDFS (Hadoop 3.5.0…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Reproduce the example in a notebook; then refactor into a reusable function.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/protechscacademy/mapreduce-hive-and-spark-sql-on-the-same-7-jobs-spark-won-by-15x-but-58-of-its-time-was-4ikp

## Related notes
- [[2026-08-31-subquery-vs-cte-in-sql-same-logic-one-you-can-check]]
- [[2026-10-27-ai-agents-can-run-sql-now-where-should-database-teams-draw-the-line]]
- [[2026-04-21-sql-window-functions-and-ctes]]
- [[2026-07-06-your-postgres-already-knows-why-its-slow-you-just-have-to-ask-it]]
- [[2026-09-05-what-actually-happens-in-a-database-index-and-why-half-of-them-do-nothing]]
- [[2026-11-03-im-an-ai-character-my-youtube-shorts-stats-misled-me-three-times-in-one-night]]
