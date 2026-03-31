---
title: Why I stopped using flat $/kWh to size commercial battery storage.
date: '2026-03-31'
source: https://dev.to/tinashe_/why-i-stopped-using-flat-kwh-to-size-commercial-battery-storage-2a0a
domain: SQL
relevance: 🟡
tags:
- '#ai'
- '#python'
- '#sql'
- '#tool'
related:
- '[[2026-03-13-you-dont-need-a-framework-building-reliable-ai-agents-from-first-principles]]'
- '[[2026-03-25-i-built-a-job-alert-bot-that-texts-me-new-remote-jobs-every-hour-python-telegram]]'
- '[[2026-03-23-the-reason-your-live-ai-demo-spins-has-nothing-to-do-with-your-model]]'
- '[[2026-03-02-your-ai-forgot-everything-you-told-it-yesterday-mine-didnt]]'
- '[[2026-03-14-176-trades-on-polymarket-what-my-bot-actually-made-its-not-what-you-think]]'
- '[[2026-03-28-soul-engine]]'
status: unread
---

> **TL;DR:** I've been building energy APIs for about four years. The thing that kept bothering me wasn't the code — it was watching tools I respected give completely wrong BESS cost estimates because they multiplied system size by a…

## What’s new and why it matters
I've been building energy APIs for about four years. The thing that kept bothering me wasn't the code — it was watching tools I respected give completely wrong BESS cost estimates because they multiplied system size by a flat dollars-per-kilowatt-hour figure. That's not how battery storage costs work. And it matters a lot when someone is deciding whether to spend $800,000 on a system. The problem with flat $/kWh Most BESS calculators I've seen do something like this: # What most tools do — this is wrong system_cost = capacity_kwh * cost_per_kwh # e.g. 500 kWh * $400 = $200,000 The issue is tha…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Write the query in a scratchpad and run EXPLAIN/QUERY PLAN to verify performance.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/tinashe_/why-i-stopped-using-flat-kwh-to-size-commercial-battery-storage-2a0a

## Related notes
- [[2026-03-13-you-dont-need-a-framework-building-reliable-ai-agents-from-first-principles]]
- [[2026-03-25-i-built-a-job-alert-bot-that-texts-me-new-remote-jobs-every-hour-python-telegram]]
- [[2026-03-23-the-reason-your-live-ai-demo-spins-has-nothing-to-do-with-your-model]]
- [[2026-03-02-your-ai-forgot-everything-you-told-it-yesterday-mine-didnt]]
- [[2026-03-14-176-trades-on-polymarket-what-my-bot-actually-made-its-not-what-you-think]]
- [[2026-03-28-soul-engine]]
