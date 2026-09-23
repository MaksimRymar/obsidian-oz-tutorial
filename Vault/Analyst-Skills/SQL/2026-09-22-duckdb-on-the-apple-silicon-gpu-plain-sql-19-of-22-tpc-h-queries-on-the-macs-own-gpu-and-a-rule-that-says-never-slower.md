---
title: 'DuckDB on the Apple Silicon GPU: Plain SQL, 19 of 22 TPC-H Queries on the
  Mac''s Own GPU, and a Rule That Says Never Slower'
date: '2026-09-22'
source: https://dev.to/aiexplore369zoho/duckdb-on-the-apple-silicon-gpu-plain-sql-19-of-22-tpc-h-queries-on-the-macs-own-gpu-and-a-rule-44l6
domain: SQL
relevance: 🔴
tags:
- '#ai'
- '#feature'
- '#library'
- '#python'
- '#sql'
- '#tool'
- '#zendesk'
related:
- '[[2026-08-21-how-to-find-duplicate-rows-in-sql-and-decide-what-counts-as-one]]'
- '[[2026-08-31-running-total-in-sql-the-window-frame-that-decides-the-answer]]'
- '[[2026-04-21-sql-window-functions-and-ctes]]'
- '[[2026-08-26-redb-371-props-search-up-to-100x-faster-an-alternative-to-ef-core-or-a-companion-to-it]]'
- '[[2026-08-11-sql-aliases-how-to-read-a-query-out-loud]]'
- '[[2026-09-07-like-in-sql-explained-for-beginners]]'
status: unread
---

> **TL;DR:** DuckDB has no GPU backend of its own, and the GPU engines built for it need an NVIDIA card. Your Mac already has a GPU sitting on the same chip as the CPU, sharing the same memory, doing nothing while DuckDB works. gpudb…

## What’s new and why it matters
DuckDB has no GPU backend of its own, and the GPU engines built for it need an NVIDIA card. Your Mac already has a GPU sitting on the same chip as the CPU, sharing the same memory, doing nothing while DuckDB works. gpudb 0.7 , released on 20 September 2026, is an Apache-2.0 DuckDB extension for that GPU — Apple silicon through Metal, and NVIDIA through CUDA — and from this version you reach it by writing plain DuckDB SQL. Every result in the new gpudb shell ends with one line saying where the statement ran and why: GPU (topk: the resident GROUP BY) · 38.8 ms DuckDB (threshold: 6 groups < 1000)…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Write the query in a scratchpad and run EXPLAIN/QUERY PLAN to verify performance.
- Add a short note: what changed in your workflow?

## Relevance
🔴

## Source
https://dev.to/aiexplore369zoho/duckdb-on-the-apple-silicon-gpu-plain-sql-19-of-22-tpc-h-queries-on-the-macs-own-gpu-and-a-rule-44l6

## Related notes
- [[2026-08-21-how-to-find-duplicate-rows-in-sql-and-decide-what-counts-as-one]]
- [[2026-08-31-running-total-in-sql-the-window-frame-that-decides-the-answer]]
- [[2026-04-21-sql-window-functions-and-ctes]]
- [[2026-08-26-redb-371-props-search-up-to-100x-faster-an-alternative-to-ef-core-or-a-companion-to-it]]
- [[2026-08-11-sql-aliases-how-to-read-a-query-out-loud]]
- [[2026-09-07-like-in-sql-explained-for-beginners]]
