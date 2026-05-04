---
title: 'Python 3.13 no‑GIL scaling on 64 cores: faster than 3.12 multiprocessing for
  our data pipeline?'
date: '2026-05-04'
source: https://dev.to/johalputt/python-313-no-gil-scaling-on-64-cores-faster-than-312-multiprocessing-for-our-data-pipeline-2c5o
domain: SQL
relevance: 🟡
tags:
- '#ai'
- '#python'
- '#sql'
related:
- '[[2026-04-13-python-314-free-threading-real-benchmarks-real-breakage-real-code]]'
- '[[2026-02-23-my-aws-lambda-runs-faster-than-yours-heres-how-to-optimize-lambda-cold-starts-with-snapstart]]'
- '[[2026-02-25-what-is-the-difference-between-multithreading-and-multiprocessing-in-python]]'
- '[[2026-03-05-efficient-parallelism-in-python-a-practical-guide-to-concurrentfutures-module]]'
- '[[2026-02-22-a-beginners-guide-to-making-data-web-applications-using-python-with-streamlit]]'
- '[[2026-04-06-pydantic-ai-tutorial-how-i-build-type-safe-ai-agents-that-actually-work-in-production]]'
status: unread
---

> **TL;DR:** Python 3.13 No-GIL Scaling on 64 Cores: Faster Than 3.12 Multiprocessing for Data Pipelines? Python’s Global Interpreter Lock (GIL) has long been a bottleneck for multi-core scaling, forcing developers to rely on multipr…

## What’s new and why it matters
Python 3.13 No-GIL Scaling on 64 Cores: Faster Than 3.12 Multiprocessing for Data Pipelines? Python’s Global Interpreter Lock (GIL) has long been a bottleneck for multi-core scaling, forcing developers to rely on multiprocessing or alternative runtimes for CPU-bound workloads. With Python 3.13’s experimental no-GIL mode (PEP 703), we tested whether removing the GIL delivers better scaling for a real-world data pipeline on 64 cores than Python 3.12’s standard multiprocessing module. Our Test Setup We used a bare-metal server with 64 AMD EPYC cores, 256GB RAM, running Ubuntu 22.04 LTS. The test…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Write the query in a scratchpad and run EXPLAIN/QUERY PLAN to verify performance.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/johalputt/python-313-no-gil-scaling-on-64-cores-faster-than-312-multiprocessing-for-our-data-pipeline-2c5o

## Related notes
- [[2026-04-13-python-314-free-threading-real-benchmarks-real-breakage-real-code]]
- [[2026-02-23-my-aws-lambda-runs-faster-than-yours-heres-how-to-optimize-lambda-cold-starts-with-snapstart]]
- [[2026-02-25-what-is-the-difference-between-multithreading-and-multiprocessing-in-python]]
- [[2026-03-05-efficient-parallelism-in-python-a-practical-guide-to-concurrentfutures-module]]
- [[2026-02-22-a-beginners-guide-to-making-data-web-applications-using-python-with-streamlit]]
- [[2026-04-06-pydantic-ai-tutorial-how-i-build-type-safe-ai-agents-that-actually-work-in-production]]
