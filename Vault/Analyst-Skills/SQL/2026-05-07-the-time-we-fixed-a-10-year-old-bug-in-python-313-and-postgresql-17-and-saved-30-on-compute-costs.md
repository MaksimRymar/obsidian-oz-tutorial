---
title: The Time We Fixed a 10-Year-Old Bug in Python 3.13 and PostgreSQL 17 and Saved
  30% on Compute Costs
date: '2026-05-07'
source: https://dev.to/johalputt/the-time-we-fixed-a-10-year-old-bug-in-python-313-and-postgresql-17-and-saved-30-on-compute-costs-2j9k
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
- '#zendesk'
related:
- '[[2026-05-03-how-to-use-python-314s-new-pattern-matching-with-fastapi-0115-for-api-routing]]'
- '[[2026-05-06-how-to-use-python-313s-new-async-features-for-1m-io-operations-40-faster-execution]]'
- '[[2026-04-02-how-to-stop-your-ai-agent-from-burning-400month-on-api-calls]]'
- '[[2026-05-06-how-to-use-python-313-for-building-ai-scripts-with-langchain-03-and-pytorch-25]]'
- '[[2026-03-28-finding-slow-queries-in-postgresql-without-guessing]]'
- '[[2026-05-04-python-313-vs-pypy-74-jit-compilation-speed-for-data-pipeline-workloads]]'
status: unread
---

> **TL;DR:** In Q3 2024, our team stumbled on a decade-old interaction bug between Python 3.13’s asyncio event loop and PostgreSQL 17’s new parallel query executor that was silently wasting 30% of our production compute budget—and we…

## What’s new and why it matters
In Q3 2024, our team stumbled on a decade-old interaction bug between Python 3.13’s asyncio event loop and PostgreSQL 17’s new parallel query executor that was silently wasting 30% of our production compute budget—and we fixed it in 14 lines of patch code. For context: we run a 12-service e-commerce backend processing 40k orders per second, with a monthly compute spend of $210k across 3 AWS regions. When we upgraded to Python 3.13 and PostgreSQL 17 in July 2024, we expected a 5-7% performance boost from the new features—instead, our p99 latency spiked by 40%, and our AWS bill jumped by $63k th…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Write the query in a scratchpad and run EXPLAIN/QUERY PLAN to verify performance.
- Add a short note: what changed in your workflow?

## Relevance
🔴

## Source
https://dev.to/johalputt/the-time-we-fixed-a-10-year-old-bug-in-python-313-and-postgresql-17-and-saved-30-on-compute-costs-2j9k

## Related notes
- [[2026-05-03-how-to-use-python-314s-new-pattern-matching-with-fastapi-0115-for-api-routing]]
- [[2026-05-06-how-to-use-python-313s-new-async-features-for-1m-io-operations-40-faster-execution]]
- [[2026-04-02-how-to-stop-your-ai-agent-from-burning-400month-on-api-calls]]
- [[2026-05-06-how-to-use-python-313-for-building-ai-scripts-with-langchain-03-and-pytorch-25]]
- [[2026-03-28-finding-slow-queries-in-postgresql-without-guessing]]
- [[2026-05-04-python-313-vs-pypy-74-jit-compilation-speed-for-data-pipeline-workloads]]
