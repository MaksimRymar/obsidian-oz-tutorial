---
title: Why Healthy P99 Latency Can Hide Async Runtime Collapse in Python
date: '2026-05-17'
source: https://dev.to/priyanshu-systems/why-healthy-p99-latency-can-hide-async-runtime-collapse-in-python-1ibm
domain: SQL
relevance: 🟡
tags:
- '#python'
- '#sql'
- '#support-analytics'
- '#tool'
- '#zendesk'
related:
- '[[2026-04-20-i-tracked-every-llm-api-call-for-a-week-65-were-unnecessary]]'
- '[[2026-03-01-fastapi-under-load-5-production-issues-most-teams-discover-too-late]]'
- '[[2026-04-11-when-an-api-stopped-returning-json-i-switched-to-selenium-and-added-ai-summaries]]'
- '[[2026-03-05-building-an-ai-prediction-api-with-fastapi-lessons-from-an-open-source-project]]'
- '[[2026-04-17-beyond-the-brain-exposing-ai-modules-to-rest-grpc-and-graphql]]'
- '[[2026-05-16-automated-domain-investing-with-hard-budget-walls-and-an-ai-council-that-has-to-agree-before-any-money-moves]]'
status: unread
---

> **TL;DR:** Most observability dashboards focus heavily on request-facing metrics: latency throughput error rate CPU and memory usage Those metrics are important, but while stress-testing async FastAPI services under concurrent load…

## What’s new and why it matters
Most observability dashboards focus heavily on request-facing metrics: latency throughput error rate CPU and memory usage Those metrics are important, but while stress-testing async FastAPI services under concurrent load, I noticed they were not always enough to explain what the runtime was actually experiencing internally. In one test setup, requests were still returning 200 OK , P99 latency had increased but was still within survivable limits, and CPU usage looked fairly normal. At the same time, the asyncio event loop was already struggling badly. Other endpoints became inconsistent, execut…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Write the query in a scratchpad and run EXPLAIN/QUERY PLAN to verify performance.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/priyanshu-systems/why-healthy-p99-latency-can-hide-async-runtime-collapse-in-python-1ibm

## Related notes
- [[2026-04-20-i-tracked-every-llm-api-call-for-a-week-65-were-unnecessary]]
- [[2026-03-01-fastapi-under-load-5-production-issues-most-teams-discover-too-late]]
- [[2026-04-11-when-an-api-stopped-returning-json-i-switched-to-selenium-and-added-ai-summaries]]
- [[2026-03-05-building-an-ai-prediction-api-with-fastapi-lessons-from-an-open-source-project]]
- [[2026-04-17-beyond-the-brain-exposing-ai-modules-to-rest-grpc-and-graphql]]
- [[2026-05-16-automated-domain-investing-with-hard-budget-walls-and-an-ai-council-that-has-to-agree-before-any-money-moves]]
