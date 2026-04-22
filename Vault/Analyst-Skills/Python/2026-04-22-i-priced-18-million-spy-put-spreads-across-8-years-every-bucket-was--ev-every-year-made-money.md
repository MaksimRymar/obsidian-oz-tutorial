---
title: I Priced 18 Million SPY Put Spreads Across 8 Years. Every Bucket Was -EV. Every
  Year Made Money.
date: '2026-04-22'
source: https://dev.to/tomasz_dobrowolski_35d32c/i-priced-18-million-spy-put-spreads-across-8-years-every-bucket-was-ev-every-year-made-money-4i3k
domain: Python
relevance: 🟡
tags:
- '#ai'
- '#library'
- '#python'
- '#sql'
- '#tool'
related:
- '[[2026-04-02-how-to-stop-your-ai-agent-from-burning-400month-on-api-calls]]'
- '[[2026-04-11-7-free-defi-apis-every-developer-should-know-in-2026-with-code-examples]]'
- '[[2026-04-21-what-happens-to-your-mutual-fund-between-9-am-and-9-pm]]'
- '[[2026-02-26-choosing-an-agent-framework-in-2026-a-data-driven-decision-guide]]'
- '[[2026-03-30-database-indexing-explained-whats-actually-happening-under-the-hood]]'
- '[[2026-04-13-python-314-free-threading-real-benchmarks-real-breakage-real-code]]'
status: unread
---

> **TL;DR:** When a blog post tells you "sell 30-delta puts at 45 DTE with a 50% profit take," you have no way to know whether that rule is near-optimal, arbitrary, or picked because it happens to look good in the author's sample. Th…

## What’s new and why it matters
When a blog post tells you "sell 30-delta puts at 45 DTE with a 50% profit take," you have no way to know whether that rule is near-optimal, arbitrary, or picked because it happens to look good in the author's sample. The only cure for cherry-picking is not to pick — compute the full surface and show where the edge actually lives. So I did. For every trading day from 2018-04-16 to 2026-04-02, for every SPY expiry with a usable SVI fit, for every short-strike delta in [0.05, 0.40] and every width in {1, 2, 3, 5, 10, 20} , I priced the theoretical credit spread under Black-Scholes with surface-c…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Reproduce the example in a notebook; then refactor into a reusable function.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/tomasz_dobrowolski_35d32c/i-priced-18-million-spy-put-spreads-across-8-years-every-bucket-was-ev-every-year-made-money-4i3k

## Related notes
- [[2026-04-02-how-to-stop-your-ai-agent-from-burning-400month-on-api-calls]]
- [[2026-04-11-7-free-defi-apis-every-developer-should-know-in-2026-with-code-examples]]
- [[2026-04-21-what-happens-to-your-mutual-fund-between-9-am-and-9-pm]]
- [[2026-02-26-choosing-an-agent-framework-in-2026-a-data-driven-decision-guide]]
- [[2026-03-30-database-indexing-explained-whats-actually-happening-under-the-hood]]
- [[2026-04-13-python-314-free-threading-real-benchmarks-real-breakage-real-code]]
