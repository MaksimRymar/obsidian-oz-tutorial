---
title: How to Optimize Python 3.12 Code with Cython 3 and Rust 1.85 Bindings for 10x
  Speedups
date: '2026-05-02'
source: https://dev.to/johalputt/how-to-optimize-python-312-code-with-cython-3-and-rust-185-bindings-for-10x-speedups-1706
domain: SQL
relevance: 🔴
tags:
- '#ai'
- '#best-practice'
- '#feature'
- '#library'
- '#python'
- '#sql'
- '#tool'
- '#tutorial'
related:
- '[[2026-04-13-python-314-free-threading-real-benchmarks-real-breakage-real-code]]'
- '[[2026-02-22-a-beginners-guide-to-making-data-web-applications-using-python-with-streamlit]]'
- '[[2026-03-13-you-dont-need-a-framework-building-reliable-ai-agents-from-first-principles]]'
- '[[2026-05-02-uncovering-8-indexeddb-data-loss-after-browser-crashes-with-playwright]]'
- '[[2026-04-03-i-got-tired-of-watching-my-terminal-so-i-built-guga]]'
- '[[2026-02-23-my-aws-lambda-runs-faster-than-yours-heres-how-to-optimize-lambda-cold-starts-with-snapstart]]'
status: unread
---

> **TL;DR:** Python’s global interpreter lock (GIL) and dynamic typing make it 10–100x slower than compiled languages for CPU-bound workloads. In 2024 benchmarks, a naive Python 3.12 matrix multiplication function took 12.7 seconds t…

## What’s new and why it matters
Python’s global interpreter lock (GIL) and dynamic typing make it 10–100x slower than compiled languages for CPU-bound workloads. In 2024 benchmarks, a naive Python 3.12 matrix multiplication function took 12.7 seconds to process 1000x1000 float arrays, while a Cython 3-optimized version ran in 1.4 seconds, and a Rust 1.85 binding dropped that to 0.89 seconds — a 14.3x speedup over pure Python, with zero Python code changes for the Rust path. 🔴 Live Ecosystem Stats ⭐ rust-lang/rust — 112,466 stars, 14,875 forks ⭐ python/cpython — 72,543 stars, 34,529 forks Data pulled live from GitHub and npm.…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Write the query in a scratchpad and run EXPLAIN/QUERY PLAN to verify performance.
- Add a short note: what changed in your workflow?

## Relevance
🔴

## Source
https://dev.to/johalputt/how-to-optimize-python-312-code-with-cython-3-and-rust-185-bindings-for-10x-speedups-1706

## Related notes
- [[2026-04-13-python-314-free-threading-real-benchmarks-real-breakage-real-code]]
- [[2026-02-22-a-beginners-guide-to-making-data-web-applications-using-python-with-streamlit]]
- [[2026-03-13-you-dont-need-a-framework-building-reliable-ai-agents-from-first-principles]]
- [[2026-05-02-uncovering-8-indexeddb-data-loss-after-browser-crashes-with-playwright]]
- [[2026-04-03-i-got-tired-of-watching-my-terminal-so-i-built-guga]]
- [[2026-02-23-my-aws-lambda-runs-faster-than-yours-heres-how-to-optimize-lambda-cold-starts-with-snapstart]]
