---
title: Your Python rate limiter is lying to you the moment you add a second server
date: '2026-06-29'
source: https://dev.to/annamareemorris/your-python-rate-limiter-is-lying-to-you-the-moment-you-add-a-second-server-2df5
domain: SQL
relevance: 🟡
tags:
- '#library'
- '#python'
- '#sql'
- '#tool'
- '#tutorial'
related:
- '[[2026-03-13-you-dont-need-a-framework-building-reliable-ai-agents-from-first-principles]]'
- '[[2026-02-24-stop-using-any-the-wrong-way-in-rails]]'
- '[[2026-06-04-i-built-a-cache-engine-from-scratch-in-python-and-o1-lfu-eviction-is-sneakier-than-lru]]'
- '[[2026-04-22-your-pytest-retries-are-lying-to-you-the-hidden-cost-of---reruns-and-the-plugin-i-wrote-so-i-could-actually-see-what-my-]]'
- '[[2026-03-30-database-indexing-explained-whats-actually-happening-under-the-hood]]'
- '[[2026-04-30-the-database-is-where-ai-agents-in-production-get-weird]]'
status: unread
---

> **TL;DR:** Most rate-limiter tutorials show you a tidy little token bucket that works perfectly — on one machine. Then you deploy to production, where you're running three copies of your app behind a load balancer, and the limiter…

## What’s new and why it matters
Most rate-limiter tutorials show you a tidy little token bucket that works perfectly — on one machine. Then you deploy to production, where you're running three copies of your app behind a load balancer, and the limiter quietly stops doing its job. Nobody gets an error. Nothing crashes. Your "100 requests per minute" just silently becomes 300, and you don't find out until something downstream falls over. This post is about why that happens, a small demo you can run to see it, and the one change that fixes it. The limiter that works on your laptop Here's a textbook in-memory token bucket. The m…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Write the query in a scratchpad and run EXPLAIN/QUERY PLAN to verify performance.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/annamareemorris/your-python-rate-limiter-is-lying-to-you-the-moment-you-add-a-second-server-2df5

## Related notes
- [[2026-03-13-you-dont-need-a-framework-building-reliable-ai-agents-from-first-principles]]
- [[2026-02-24-stop-using-any-the-wrong-way-in-rails]]
- [[2026-06-04-i-built-a-cache-engine-from-scratch-in-python-and-o1-lfu-eviction-is-sneakier-than-lru]]
- [[2026-04-22-your-pytest-retries-are-lying-to-you-the-hidden-cost-of---reruns-and-the-plugin-i-wrote-so-i-could-actually-see-what-my-]]
- [[2026-03-30-database-indexing-explained-whats-actually-happening-under-the-hood]]
- [[2026-04-30-the-database-is-where-ai-agents-in-production-get-weird]]
