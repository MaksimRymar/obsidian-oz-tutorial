---
title: Craton Bolt — The Open-Source JIT-Compiled GPU SQL Engine That Compiles SQL
  to NVIDIA PTX at Runtime
date: '2026-08-18'
source: https://dev.to/tekmag/craton-bolt-the-open-source-jit-compiled-gpu-sql-engine-that-compiles-sql-to-nvidia-ptx-at-runtime-4c6l
domain: SQL
relevance: 🟡
tags:
- '#ai'
- '#feature'
- '#library'
- '#python'
- '#sql'
- '#tool'
- '#zendesk'
related:
- '[[2026-04-22-sql-set-operators-union-intersect-and-except-explained-simply]]'
- '[[2026-04-19-sql-deep-dive-subqueries-vs-ctes-which-one-should-you-use]]'
- '[[2026-06-10-sql-for-data-analysis-the-10-query-patterns-that-matter]]'
- '[[2026-03-01-joins-and-windows-functions-in-sql]]'
- '[[2026-08-04-apache-arrow-for-data-engineers-zero-copy-columnar-memory-across-the-whole-stack]]'
- '[[2026-03-12-sql-join-tutorial-inner-left-right-full-outer-explained]]'
status: unread
---

> **TL;DR:** Craton Bolt is a SQL execution engine written in pure Rust that compiles each query into a fresh NVIDIA PTX kernel at runtime, loads it via the CUDA driver, and runs it on the GPU. There is no C++ shim, no precompiled ke…

## What’s new and why it matters
Craton Bolt is a SQL execution engine written in pure Rust that compiles each query into a fresh NVIDIA PTX kernel at runtime, loads it via the CUDA driver, and runs it on the GPU. There is no C++ shim, no precompiled kernel library, and no FFI to a third-party query engine. The full pipeline — parse, plan, codegen, launch — is Rust on top of the raw CUDA driver API. The project comes from Craton, a nearshore engineering shop based in Buenos Aires, and sits at github.com/craton-co/craton-bolt under the Apache 2.0 license. It is currently at version 0.7.0 and is actively developed. The authors…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Write the query in a scratchpad and run EXPLAIN/QUERY PLAN to verify performance.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/tekmag/craton-bolt-the-open-source-jit-compiled-gpu-sql-engine-that-compiles-sql-to-nvidia-ptx-at-runtime-4c6l

## Related notes
- [[2026-04-22-sql-set-operators-union-intersect-and-except-explained-simply]]
- [[2026-04-19-sql-deep-dive-subqueries-vs-ctes-which-one-should-you-use]]
- [[2026-06-10-sql-for-data-analysis-the-10-query-patterns-that-matter]]
- [[2026-03-01-joins-and-windows-functions-in-sql]]
- [[2026-08-04-apache-arrow-for-data-engineers-zero-copy-columnar-memory-across-the-whole-stack]]
- [[2026-03-12-sql-join-tutorial-inner-left-right-full-outer-explained]]
