---
title: After 3 Years of Redis, We Were Testing AI Agent Memory Expiry Wrong
date: '2026-08-18'
source: https://dev.to/_eb7f2a654e97a60ae9f96e/after-3-years-of-redis-we-were-testing-ai-agent-memory-expiry-wrong-3ko0
domain: SQL
relevance: 🟡
tags:
- '#ai'
- '#python'
- '#sql'
- '#tool'
related:
- '[[2026-05-08-from-2-hours-to-3-minutes-eliminating-missed-tests-in-ai-memory-consistency-testing]]'
- '[[2026-07-18-llm-memory-consistency-testing-3-pitfalls-with-playwright-pytest-and-8-hours-of-debugging]]'
- '[[2026-08-13-contract-testing-vector-db-memory-storage-with-pytest-allure-60-fewer-regression-incidents]]'
- '[[2026-06-22-from-45-minutes-to-3-automated-testing-for-ai-agent-memory]]'
- '[[2026-08-17-from-30-minutes-to-5-seconds-testing-agent-memory-with-pytest-sqlite]]'
- '[[2026-07-12-from-2-hour-manual-regression-to-8-minutes-doubling-accuracy-in-llm-memory-testing]]'
status: unread
---

> **TL;DR:** I was woken up at 2 AM by an on-call alert. A user complained that the AI Agent carried over shopping preferences from the previous session into a new one. My first instinct: did the Redis cache fail to isolate? I opened…

## What’s new and why it matters
I was woken up at 2 AM by an on-call alert. A user complained that the AI Agent carried over shopping preferences from the previous session into a new one. My first instinct: did the Redis cache fail to isolate? I opened redis-cli and found memory:agent:123:session:456 had existed for 12 hours, with TTL of -1 — this key should have expired after 10 minutes. That's when I realized: after years of using Redis for AI Agent memory storage, our manual tests never truly covered the expiration boundary. Problem breakdown AI Agent memory storage has two hard requirements: isolation and expiration poli…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Write the query in a scratchpad and run EXPLAIN/QUERY PLAN to verify performance.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/_eb7f2a654e97a60ae9f96e/after-3-years-of-redis-we-were-testing-ai-agent-memory-expiry-wrong-3ko0

## Related notes
- [[2026-05-08-from-2-hours-to-3-minutes-eliminating-missed-tests-in-ai-memory-consistency-testing]]
- [[2026-07-18-llm-memory-consistency-testing-3-pitfalls-with-playwright-pytest-and-8-hours-of-debugging]]
- [[2026-08-13-contract-testing-vector-db-memory-storage-with-pytest-allure-60-fewer-regression-incidents]]
- [[2026-06-22-from-45-minutes-to-3-automated-testing-for-ai-agent-memory]]
- [[2026-08-17-from-30-minutes-to-5-seconds-testing-agent-memory-with-pytest-sqlite]]
- [[2026-07-12-from-2-hour-manual-regression-to-8-minutes-doubling-accuracy-in-llm-memory-testing]]
