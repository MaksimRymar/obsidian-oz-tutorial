---
title: 'Zero-Disk Streaming Database Backup: 8 GB Dump Processed with Only ~119 MB
  RAM!'
date: '2026-08-03'
source: https://dev.to/indhifarhandika/zero-disk-streaming-database-backup-8-gb-dump-processed-with-only-119-mb-ram-4c8h
domain: SQL
relevance: 🟡
tags:
- '#ai'
- '#sql'
related:
- '[[2026-07-14-python-memory-profiling-tracemalloc-scalene-py-spy-for-long-running-pipelines]]'
- '[[2026-07-06-how-to-identify-and-kill-mysql-queries-using-command-line]]'
- '[[2026-03-07-stop-sending-health-data-to-the-cloud-build-a-privacy-first-symptom-checker-with-webgpu]]'
- '[[2026-07-14-polars-streaming-engine-deep-dive-out-of-core-joins-groupby-window]]'
- '[[2026-06-28-ad-hoc-video-analytics-with-duckdb-on-parquet-exports-from-production-sqlite]]'
- '[[2026-05-30-master-mysql-views-and-window-functions-advanced-query-optimization-guide]]'
status: unread
---

> **TL;DR:** When managing database backups, key pain points on entry-level servers are memory spikes (Out of Memory crashes) and running out of disk space due to temporary dump files. To validate the efficiency of LunarDump (a zero-…

## What’s new and why it matters
When managing database backups, key pain points on entry-level servers are memory spikes (Out of Memory crashes) and running out of disk space due to temporary dump files. To validate the efficiency of LunarDump (a zero-disk streaming backup solution), I conducted a benchmark & memory profiling using Memray across a multi-cloud setup based in Jakarta. 🖥️ Test Environment Setup: Server A (Database): Tencent Cloud (Jakarta) — Ubuntu 24.04, 2 vCPU, 2 GB RAM, 40 GB SSD Server B (LunarDump Engine): Cloudeka (Jakarta) — Ubuntu 24.04, 1 vCPU, 1 GB RAM, 20 GB SSD Destina tion Storage: Google Cloud Sto…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Write the query in a scratchpad and run EXPLAIN/QUERY PLAN to verify performance.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/indhifarhandika/zero-disk-streaming-database-backup-8-gb-dump-processed-with-only-119-mb-ram-4c8h

## Related notes
- [[2026-07-14-python-memory-profiling-tracemalloc-scalene-py-spy-for-long-running-pipelines]]
- [[2026-07-06-how-to-identify-and-kill-mysql-queries-using-command-line]]
- [[2026-03-07-stop-sending-health-data-to-the-cloud-build-a-privacy-first-symptom-checker-with-webgpu]]
- [[2026-07-14-polars-streaming-engine-deep-dive-out-of-core-joins-groupby-window]]
- [[2026-06-28-ad-hoc-video-analytics-with-duckdb-on-parquet-exports-from-production-sqlite]]
- [[2026-05-30-master-mysql-views-and-window-functions-advanced-query-optimization-guide]]
