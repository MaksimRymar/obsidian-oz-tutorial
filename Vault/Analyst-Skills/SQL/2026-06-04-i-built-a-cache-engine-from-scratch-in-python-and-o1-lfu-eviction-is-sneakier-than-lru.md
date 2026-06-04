---
title: I Built a Cache Engine from Scratch in Python — and O(1) LFU Eviction Is Sneakier
  Than LRU
date: '2026-06-04'
source: https://dev.to/hajirufai/i-built-a-cache-engine-from-scratch-in-python-and-o1-lfu-eviction-is-sneakier-than-lru-28m7
domain: SQL
relevance: 🟡
tags:
- '#best-practice'
- '#career'
- '#python'
- '#sql'
- '#tool'
related:
- '[[2026-04-17-maybe-this-is-how-open-source-apps-are-born]]'
- '[[2026-02-24-stop-using-any-the-wrong-way-in-rails]]'
- '[[2026-04-22-i-kept-forgetting-to-delete-my-venvs-so-i-built-a-gui-for-it]]'
- '[[2026-03-13-you-dont-need-a-framework-building-reliable-ai-agents-from-first-principles]]'
- '[[2026-03-23-the-reason-your-live-ai-demo-spins-has-nothing-to-do-with-your-model]]'
- '[[2026-03-15-easy-query-the-most-powerful-orm-for-java]]'
status: unread
---

> **TL;DR:** When you call cache.get("user:123") and the cache is full, something has to go. That decision — which key gets thrown out to make room — is the whole game in caching. Get it right and your hit rate stays high. Get it wro…

## What’s new and why it matters
When you call cache.get("user:123") and the cache is full, something has to go. That decision — which key gets thrown out to make room — is the whole game in caching. Get it right and your hit rate stays high. Get it wrong and you're constantly evicting the one thing you were about to ask for again. I'd used functools.lru_cache and Redis for years without really knowing what happens in that moment. So I built CacheLite: an in-memory cache engine in pure Python, no dependencies, where I had to write every eviction policy by hand. LRU, LFU, FIFO, Random — plus TTL expiry, a reader-writer lock, s…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Write the query in a scratchpad and run EXPLAIN/QUERY PLAN to verify performance.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/hajirufai/i-built-a-cache-engine-from-scratch-in-python-and-o1-lfu-eviction-is-sneakier-than-lru-28m7

## Related notes
- [[2026-04-17-maybe-this-is-how-open-source-apps-are-born]]
- [[2026-02-24-stop-using-any-the-wrong-way-in-rails]]
- [[2026-04-22-i-kept-forgetting-to-delete-my-venvs-so-i-built-a-gui-for-it]]
- [[2026-03-13-you-dont-need-a-framework-building-reliable-ai-agents-from-first-principles]]
- [[2026-03-23-the-reason-your-live-ai-demo-spins-has-nothing-to-do-with-your-model]]
- [[2026-03-15-easy-query-the-most-powerful-orm-for-java]]
