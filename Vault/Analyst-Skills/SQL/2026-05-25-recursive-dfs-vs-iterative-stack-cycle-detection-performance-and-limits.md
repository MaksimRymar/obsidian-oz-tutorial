---
title: 'Recursive DFS vs Iterative Stack: Cycle Detection Performance and Limits'
date: '2026-05-25'
source: https://dev.to/tildalice/recursive-dfs-vs-iterative-stack-cycle-detection-performance-and-limits-4l0l
domain: SQL
relevance: 🟡
tags:
- '#career'
- '#library'
- '#python'
- '#sql'
- '#tool'
- '#zendesk'
related:
- '[[2026-03-03-advanced-numpy-the-performance-tricks-that-separate-pros-from-beginners]]'
- '[[2026-04-30-your-mcp-servers-are-flying-blind-heres-how-to-fix-it]]'
- '[[2026-04-16-duckdb-in-the-wild-what-6-minutes-of-benchmarking-across-4-machines-taught-me-about-real-world-performance]]'
- '[[2026-03-14-the-ai-engineering-stack-in-2026-what-to-learn-first]]'
- '[[2026-05-11-data-analyst-interview-questions-2026-what-actually-shows-up-across-all-three-rounds]]'
- '[[2026-03-30-build-a-productionready-sql-evaluation-engine-for-llms]]'
status: unread
---

> **TL;DR:** The Stack Overflow That Shouldn't Have Happened A cycle detection function crashed on a graph with 12,000 nodes. Not a million. Twelve thousand. The recursive DFS worked fine in local tests with synthetic graphs of 500-1…

## What’s new and why it matters
The Stack Overflow That Shouldn't Have Happened A cycle detection function crashed on a graph with 12,000 nodes. Not a million. Twelve thousand. The recursive DFS worked fine in local tests with synthetic graphs of 500-1000 nodes. But the production graph — a dependency tree from a package manager audit — hit Python's recursion limit ( RecursionError: maximum recursion depth exceeded ) at around 10,000 frames. The fix everyone suggests? Switch to an iterative approach with an explicit stack. But does it actually run faster, or just avoid the crash? Here's what the benchmarks show when you pit…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Write the query in a scratchpad and run EXPLAIN/QUERY PLAN to verify performance.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/tildalice/recursive-dfs-vs-iterative-stack-cycle-detection-performance-and-limits-4l0l

## Related notes
- [[2026-03-03-advanced-numpy-the-performance-tricks-that-separate-pros-from-beginners]]
- [[2026-04-30-your-mcp-servers-are-flying-blind-heres-how-to-fix-it]]
- [[2026-04-16-duckdb-in-the-wild-what-6-minutes-of-benchmarking-across-4-machines-taught-me-about-real-world-performance]]
- [[2026-03-14-the-ai-engineering-stack-in-2026-what-to-learn-first]]
- [[2026-05-11-data-analyst-interview-questions-2026-what-actually-shows-up-across-all-three-rounds]]
- [[2026-03-30-build-a-productionready-sql-evaluation-engine-for-llms]]
