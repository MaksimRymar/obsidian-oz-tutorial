---
title: 'CUDA Rust: What the Two GPU Kernel Tracks Actually Guarantee'
date: '2026-09-17'
source: https://dev.to/chenyuan20509/cuda-rust-what-the-two-gpu-kernel-tracks-actually-guarantee-22f0
domain: SQL
relevance: 🟡
tags:
- '#ai'
- '#best-practice'
- '#feature'
- '#python'
- '#sql'
- '#tool'
related:
- '[[2026-09-04-i-built-an-offline-document-indexer-and-ollama-taught-me-two-things-i-did-not-expect]]'
- '[[2026-09-01-i-raced-six-models-against-each-other-on-digitalocean-inference-the-cheapest-one-won]]'
- '[[2026-08-07-my-mcp-tools-docstring-promised-limit-1-100-passing--1-returned-almost-everything-not-nothing]]'
- '[[2026-08-27-partitioning-clustering-and-bi-engine-measuring-what-each-one-saves-in-bigquery]]'
- '[[2026-07-23-btree-height-after-delete-postgresql-fast-root]]'
- '[[2026-08-14-schema-linting-vs-migration-linting-which-database-problems-each-one-can-see]]'
status: unread
---

> **TL;DR:** On September 8, 2026, NVIDIA published a technical blog post that introduced CUDA Rust, a pair of projects that let developers write GPU kernels in Rust and compile them natively to PTX. The first, cuda-oxide, is a custo…

## What’s new and why it matters
On September 8, 2026, NVIDIA published a technical blog post that introduced CUDA Rust, a pair of projects that let developers write GPU kernels in Rust and compile them natively to PTX. The first, cuda-oxide, is a custom rustc codegen backend that routes kernel functions through Rust MIR, the Pliron IR framework and LLVM before handing everything else to the standard backend. The second, cutile-rs, is published on crates.io, runs on stable Rust 1.89 or newer, and JIT-compiles tile-based kernels through CUDA Tile IR. Neither project is production-ready, and NVIDIA describes both as work that w…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Write the query in a scratchpad and run EXPLAIN/QUERY PLAN to verify performance.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/chenyuan20509/cuda-rust-what-the-two-gpu-kernel-tracks-actually-guarantee-22f0

## Related notes
- [[2026-09-04-i-built-an-offline-document-indexer-and-ollama-taught-me-two-things-i-did-not-expect]]
- [[2026-09-01-i-raced-six-models-against-each-other-on-digitalocean-inference-the-cheapest-one-won]]
- [[2026-08-07-my-mcp-tools-docstring-promised-limit-1-100-passing--1-returned-almost-everything-not-nothing]]
- [[2026-08-27-partitioning-clustering-and-bi-engine-measuring-what-each-one-saves-in-bigquery]]
- [[2026-07-23-btree-height-after-delete-postgresql-fast-root]]
- [[2026-08-14-schema-linting-vs-migration-linting-which-database-problems-each-one-can-see]]
