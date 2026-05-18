---
title: Three memory-leak patterns in long-running scrapers (and how I caught them
  after 968 Trustpilot runs)
date: '2026-05-18'
source: https://dev.to/0012303/three-memory-leak-patterns-in-long-running-scrapers-and-how-i-caught-them-after-968-trustpilot-5202
domain: Productivity
relevance: 🟡
tags:
- '#best-practice'
- '#productivity'
- '#python'
- '#tool'
- '#zendesk'
related:
- '[[2026-04-02-how-to-stop-your-ai-agent-from-burning-400month-on-api-calls]]'
- '[[2026-03-16-build-your-first-multi-agent-system-in-python-3-patterns-that-scale]]'
- '[[2026-03-30-database-indexing-explained-whats-actually-happening-under-the-hood]]'
- '[[2026-04-12-how-i-built-a-code-review-agent-that-gets-smarter-every-time-a-developer-hits-accept]]'
- '[[2026-05-09-how-instagram-blocks-scrapers-in-2026-and-what-actually-gets-around-it]]'
- '[[2026-04-11-i-trusted-the-code-ai-wrote-for-me-my-data-was-silently-broken-the-whole-time]]'
status: unread
---

> **TL;DR:** Memory leaks in scrapers do not crash the run. They quietly bump the Apify Memory limit from 1 GB to 2 GB to 4 GB, double the per-run cost, and only get spotted weeks later on a compute-unit invoice. After 968 Trustpilot…

## What’s new and why it matters
Memory leaks in scrapers do not crash the run. They quietly bump the Apify Memory limit from 1 GB to 2 GB to 4 GB, double the per-run cost, and only get spotted weeks later on a compute-unit invoice. After 968 Trustpilot runs (~80–300 review pages each, ~150k page hits cumulative), I started sampling RSS every 1,000 pages. The growth pattern told a different story than the logs. Below are the three patterns that account for ~90% of the leaks I have seen across my 32 published Apify actors. 1. The unbounded asyncio queue The most common pattern. A producer coroutine fetches URLs faster than the…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/0012303/three-memory-leak-patterns-in-long-running-scrapers-and-how-i-caught-them-after-968-trustpilot-5202

## Related notes
- [[2026-04-02-how-to-stop-your-ai-agent-from-burning-400month-on-api-calls]]
- [[2026-03-16-build-your-first-multi-agent-system-in-python-3-patterns-that-scale]]
- [[2026-03-30-database-indexing-explained-whats-actually-happening-under-the-hood]]
- [[2026-04-12-how-i-built-a-code-review-agent-that-gets-smarter-every-time-a-developer-hits-accept]]
- [[2026-05-09-how-instagram-blocks-scrapers-in-2026-and-what-actually-gets-around-it]]
- [[2026-04-11-i-trusted-the-code-ai-wrote-for-me-my-data-was-silently-broken-the-whole-time]]
