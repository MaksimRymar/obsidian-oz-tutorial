---
title: 'Python Without the GIL: Is It Actually Faster? I Measured It'
date: '2026-11-21'
source: https://dev.to/refactorly/python-without-the-gil-is-it-actually-faster-i-measured-it-55oo
domain: SQL
relevance: 🔴
tags:
- '#ai'
- '#feature'
- '#python'
- '#sql'
- '#tool'
related:
- '[[2026-04-13-python-314-free-threading-real-benchmarks-real-breakage-real-code]]'
- '[[2026-08-19-a-local-video-dubber-fully-running-in-about-ten-minutes]]'
- '[[2026-11-05-your-ai-says-fixed-would-a-test-notice-if-it-wasnt]]'
- '[[2026-08-06-find-your-worst-postgres-query-in-15-minutes-with-pgstatstatements]]'
- '[[2026-08-12-sql-ctes-how-to-build-a-query-in-steps-you-can-check]]'
- '[[2026-06-15-day-01-of-learning-data-engineering-step1-sql-joins-and-set-operators]]'
status: unread
---

> **TL;DR:** For about thirty years, Python threads couldn't run Python code in parallel. Now there's an official build of Python without that limit: the free-threaded build. So I measured it: the same code on the same Mac, with the…

## What’s new and why it matters
For about thirty years, Python threads couldn't run Python code in parallel. Now there's an official build of Python without that limit: the free-threaded build. So I measured it: the same code on the same Mac, with the GIL and without it. Short version: about 3× faster on 8 threads for CPU-heavy code, no change for code that mostly waits, slightly slower single-threaded, and it exposes race conditions the GIL was hiding. Video version: What is the GIL? The Global Interpreter Lock lets only one thread run Python bytecode at a time. Threads still help when your code waits (network, files, datab…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Write the query in a scratchpad and run EXPLAIN/QUERY PLAN to verify performance.
- Add a short note: what changed in your workflow?

## Relevance
🔴

## Source
https://dev.to/refactorly/python-without-the-gil-is-it-actually-faster-i-measured-it-55oo

## Related notes
- [[2026-04-13-python-314-free-threading-real-benchmarks-real-breakage-real-code]]
- [[2026-08-19-a-local-video-dubber-fully-running-in-about-ten-minutes]]
- [[2026-11-05-your-ai-says-fixed-would-a-test-notice-if-it-wasnt]]
- [[2026-08-06-find-your-worst-postgres-query-in-15-minutes-with-pgstatstatements]]
- [[2026-08-12-sql-ctes-how-to-build-a-query-in-steps-you-can-check]]
- [[2026-06-15-day-01-of-learning-data-engineering-step1-sql-joins-and-set-operators]]
