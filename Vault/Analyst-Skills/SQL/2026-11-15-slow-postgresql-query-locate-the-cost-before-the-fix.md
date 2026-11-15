---
title: Slow PostgreSQL Query? Locate the Cost Before the Fix
date: '2026-11-15'
source: https://dev.to/alimoradi/slow-postgresql-query-locate-the-cost-before-the-fix-214g
domain: SQL
relevance: 🟡
tags:
- '#sql'
- '#tool'
- '#tutorial'
related:
- '[[2026-08-13-3-testing-habits-that-caught-bugs-before-my-users-did]]'
- '[[2026-11-04-how-to-read-postgresql-explain-output]]'
- '[[2026-04-16-duckdb-in-the-wild-what-6-minutes-of-benchmarking-across-4-machines-taught-me-about-real-world-performance]]'
- '[[2026-03-12-query-planning-overhead-with-many-chunks-and-how-to-fix-it]]'
- '[[2026-10-17-why-did-ls-sort-clip10-before-clip1-three-orders-for-one-folder-of-numbered-clips]]'
- '[[2026-08-26-redb-371-props-search-up-to-100x-faster-an-alternative-to-ef-core-or-a-companion-to-it]]'
status: unread
---

> **TL;DR:** A slow query needs a diagnosis before it needs a fix. In one PostgreSQL investigation, a recorded production plan showed 2,070.4 ms of execution time . JIT compilation consumed 2,023.5 ms within that total: 97.7% . The o…

## What’s new and why it matters
A slow query needs a diagnosis before it needs a fix. In one PostgreSQL investigation, a recorded production plan showed 2,070.4 ms of execution time . JIT compilation consumed 2,023.5 ms within that total: 97.7% . The operator-supplied audit summary also reported shared-buffer hits, with zero shared reads or temporary blocks in that sample. Compilation was the dominant measured cost. That gave us a hypothesis to test. The diagnostic workflow. Turning JIT off tests the explanation; broader workload evidence guides a permanent change. Test the diagnosis A separate local comparison ran the servi…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Write the query in a scratchpad and run EXPLAIN/QUERY PLAN to verify performance.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/alimoradi/slow-postgresql-query-locate-the-cost-before-the-fix-214g

## Related notes
- [[2026-08-13-3-testing-habits-that-caught-bugs-before-my-users-did]]
- [[2026-11-04-how-to-read-postgresql-explain-output]]
- [[2026-04-16-duckdb-in-the-wild-what-6-minutes-of-benchmarking-across-4-machines-taught-me-about-real-world-performance]]
- [[2026-03-12-query-planning-overhead-with-many-chunks-and-how-to-fix-it]]
- [[2026-10-17-why-did-ls-sort-clip10-before-clip1-three-orders-for-one-folder-of-numbered-clips]]
- [[2026-08-26-redb-371-props-search-up-to-100x-faster-an-alternative-to-ef-core-or-a-companion-to-it]]
