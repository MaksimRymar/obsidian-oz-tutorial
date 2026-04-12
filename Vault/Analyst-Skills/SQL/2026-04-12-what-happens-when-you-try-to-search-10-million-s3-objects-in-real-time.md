---
title: What happens when you try to search 10 million S3 objects in real-time
date: '2026-04-12'
source: https://dev.to/ashwath_stephen_2f5e1eef0/what-happens-when-you-try-to-search-10-million-s3-objects-in-real-time-9d4
domain: SQL
relevance: 🔴
tags:
- '#ai'
- '#best-practice'
- '#sql'
- '#tool'
related:
- '[[2026-03-30-database-indexing-explained-whats-actually-happening-under-the-hood]]'
- '[[2026-03-26-sqlite-is-enough-for-your-side-project-full-text-search-json-and-wal-mode-included]]'
- '[[2026-04-08-how-building-a-streaming-sql-api-in-nodejs-changed-my-approach-to-real-time-data]]'
- '[[2026-03-30-your-sql-client-is-a-relic-heres-what-a-duckdb-native-ide-looks-like]]'
- '[[2026-03-30-i-stopped-pasting-ddl-into-random-chatbots-heres-the-local-windows-db-client-i-use]]'
- '[[2026-03-31-ai-agent-for-data-analysis-automate-reports-dashboards-amp-insights-2026]]'
status: unread
---

> **TL;DR:** run about 170TB of data across 10 buckets on S3-compatible storage. Data pipelines dump Druid segments, Kafka flat events, Prometheus TSDB blocks — millions of objects, growing daily. Nobody on the team could answer basi…

## What’s new and why it matters
run about 170TB of data across 10 buckets on S3-compatible storage. Data pipelines dump Druid segments, Kafka flat events, Prometheus TSDB blocks — millions of objects, growing daily. Nobody on the team could answer basic questions: How much is this costing us? What's the oldest data in that bucket? Which folder grew 40TB last month? AWS Console times out on large buckets. Cyberduck crashes. MinIO Console doesn't have search. s3cmd gives you a wall of text you can't do anything with. So I built what I needed. The first attempt broke Started simple — a Flask app that called ListObjectsV2, cache…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Write the query in a scratchpad and run EXPLAIN/QUERY PLAN to verify performance.
- Add a short note: what changed in your workflow?

## Relevance
🔴

## Source
https://dev.to/ashwath_stephen_2f5e1eef0/what-happens-when-you-try-to-search-10-million-s3-objects-in-real-time-9d4

## Related notes
- [[2026-03-30-database-indexing-explained-whats-actually-happening-under-the-hood]]
- [[2026-03-26-sqlite-is-enough-for-your-side-project-full-text-search-json-and-wal-mode-included]]
- [[2026-04-08-how-building-a-streaming-sql-api-in-nodejs-changed-my-approach-to-real-time-data]]
- [[2026-03-30-your-sql-client-is-a-relic-heres-what-a-duckdb-native-ide-looks-like]]
- [[2026-03-30-i-stopped-pasting-ddl-into-random-chatbots-heres-the-local-windows-db-client-i-use]]
- [[2026-03-31-ai-agent-for-data-analysis-automate-reports-dashboards-amp-insights-2026]]
