---
title: I made FLUX 1.16 faster on an M5 Max. Then I found out my quality gate was
  measuring the wrong thing.
date: '2026-07-16'
source: https://dev.to/kkjcodes/i-made-flux-116x-faster-on-an-m5-max-then-i-found-out-my-quality-gate-was-measuring-the-wrong-3ci4
domain: SQL
relevance: 🟡
tags:
- '#ai'
- '#python'
- '#sql'
- '#tool'
related:
- '[[2026-04-17-maybe-this-is-how-open-source-apps-are-born]]'
- '[[2026-07-01-one-big-table-vs-the-star-schema-i-think-everyones-arguing-about-the-wrong-thing]]'
- '[[2026-06-09-how-i-messed-up-ai-streaming-and-how-you-can-avoid-it]]'
- '[[2026-06-14-i-wish-i-knew-ai-speech-to-text-sooner-heres-the-full-breakdown]]'
- '[[2026-05-12-10-sql-changes-one-took-30-seconds-it-cut-query-time-by-85]]'
- '[[2026-07-15-i-built-with-both-apis-as-a-bootcamp-grad-heres-what-actually-matters]]'
status: unread
---

> **TL;DR:** I spent a few weeks benchmarking training-free block-residual caching for FLUX.1-dev on an Apple M5 Max. The timing result was real: a stable ~1.16× speedup, tight variance, reproducible across prompts. Then the quality…

## What’s new and why it matters
I spent a few weeks benchmarking training-free block-residual caching for FLUX.1-dev on an Apple M5 Max. The timing result was real: a stable ~1.16× speedup, tight variance, reproducible across prompts. Then the quality sweep came back and every policy failed my gate. Median PSNR of 14.27 dB against a gate of 30 dB. Decisive failure. I almost published that as "block-residual caching doesn't preserve quality on Apple Silicon." That would have been wrong — not because the numbers were wrong, but because PSNR wasn't measuring what I thought it was measuring . This post is about the speedup, the…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Write the query in a scratchpad and run EXPLAIN/QUERY PLAN to verify performance.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/kkjcodes/i-made-flux-116x-faster-on-an-m5-max-then-i-found-out-my-quality-gate-was-measuring-the-wrong-3ci4

## Related notes
- [[2026-04-17-maybe-this-is-how-open-source-apps-are-born]]
- [[2026-07-01-one-big-table-vs-the-star-schema-i-think-everyones-arguing-about-the-wrong-thing]]
- [[2026-06-09-how-i-messed-up-ai-streaming-and-how-you-can-avoid-it]]
- [[2026-06-14-i-wish-i-knew-ai-speech-to-text-sooner-heres-the-full-breakdown]]
- [[2026-05-12-10-sql-changes-one-took-30-seconds-it-cut-query-time-by-85]]
- [[2026-07-15-i-built-with-both-apis-as-a-bootcamp-grad-heres-what-actually-matters]]
