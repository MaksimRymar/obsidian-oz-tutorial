---
title: DDP Is Not Always Faster
date: '2026-05-16'
source: https://dev.to/thokozani_buthelezi_2cd41/ddp-is-not-always-faster-23mh
domain: SQL
relevance: 🟡
tags:
- '#ai'
- '#best-practice'
- '#python'
- '#sql'
- '#tool'
related:
- '[[2026-03-30-database-indexing-explained-whats-actually-happening-under-the-hood]]'
- '[[2026-04-11-i-trusted-the-code-ai-wrote-for-me-my-data-was-silently-broken-the-whole-time]]'
- '[[2026-03-15-easy-query-the-most-powerful-orm-for-java]]'
- '[[2026-03-14-176-trades-on-polymarket-what-my-bot-actually-made-its-not-what-you-think]]'
- '[[2026-04-16-duckdb-in-the-wild-what-6-minutes-of-benchmarking-across-4-machines-taught-me-about-real-world-performance]]'
- '[[2026-03-28-fine-tuning-ai-for-free-kaggle-qlora-hands-on-guide]]'
status: unread
---

> **TL;DR:** That is the result of this experiment, and it is the most important thing to understand about distributed training before you reach for it. I ran my nanoGPT implementation, a 4M parameter character-level transformer acro…

## What’s new and why it matters
That is the result of this experiment, and it is the most important thing to understand about distributed training before you reach for it. I ran my nanoGPT implementation, a 4M parameter character-level transformer across two T4 GPUs on Kaggle using PyTorch's DistributedDataParallel. The single GPU baseline ran at 22ms per step. The DDP run across two GPUs ran at 26ms per step. Adding a second GPU made training slower. How DDP Works DDP splits each batch across GPUs, each GPU sees a different subset of the data via DistributedSampler . Each GPU runs its own forward and backward pass independe…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Write the query in a scratchpad and run EXPLAIN/QUERY PLAN to verify performance.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/thokozani_buthelezi_2cd41/ddp-is-not-always-faster-23mh

## Related notes
- [[2026-03-30-database-indexing-explained-whats-actually-happening-under-the-hood]]
- [[2026-04-11-i-trusted-the-code-ai-wrote-for-me-my-data-was-silently-broken-the-whole-time]]
- [[2026-03-15-easy-query-the-most-powerful-orm-for-java]]
- [[2026-03-14-176-trades-on-polymarket-what-my-bot-actually-made-its-not-what-you-think]]
- [[2026-04-16-duckdb-in-the-wild-what-6-minutes-of-benchmarking-across-4-machines-taught-me-about-real-world-performance]]
- [[2026-03-28-fine-tuning-ai-for-free-kaggle-qlora-hands-on-guide]]
