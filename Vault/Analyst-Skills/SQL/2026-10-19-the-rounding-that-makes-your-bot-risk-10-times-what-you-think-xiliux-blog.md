---
title: The rounding that makes your bot risk 10 times what you think | Xiliux Blog
date: '2026-10-19'
source: https://dev.to/isazajuancarlos/the-rounding-that-makes-your-bot-risk-10-times-what-you-think-xiliux-blog-4lhj
domain: SQL
relevance: 🔴
tags:
- '#best-practice'
- '#feature'
- '#library'
- '#python'
- '#sql'
- '#tool'
related:
- '[[2026-07-22-the-backfill-pattern-adding-required-columns-without-downtime]]'
- '[[2026-09-06-exit-code-0-is-a-lie-7-ways-my-unattended-automation-silently-did-nothing]]'
- '[[2026-02-24-stop-using-any-the-wrong-way-in-rails]]'
- '[[2026-09-14-agents-for-humans-an-agent-that-refuses-to-guess-what-your-letter-says]]'
- '[[2026-10-04-analytics-engineer-the-job-that-didnt-exist-5-years-ago-and-why-it-does-now]]'
- '[[2026-09-21-building-a-market-aware-execution-engine-for-polymarket-bots-with-python]]'
status: unread
---

> **TL;DR:** Almost every trading bot has one line that decides how much to buy . It usually looks trivial: if I risk 1% of my balance and my stop is 1000 dollars away, the quantity comes out of a division. The arithmetic is grade-sc…

## What’s new and why it matters
Almost every trading bot has one line that decides how much to buy . It usually looks trivial: if I risk 1% of my balance and my stop is 1000 dollars away, the quantity comes out of a division. The arithmetic is grade-school. What isn't grade-school is making that number fit the exchange's constraints . That's where money is lost, and in ways that don't show up in the logs. The pattern that multiplies your risk This is in countless bots, and was in one of mine: cantidad = max ( 1 , int ( cantidad_teorica / contract_size )) The intent is defensive: "never let it come out zero". The effect is th…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Write the query in a scratchpad and run EXPLAIN/QUERY PLAN to verify performance.
- Add a short note: what changed in your workflow?

## Relevance
🔴

## Source
https://dev.to/isazajuancarlos/the-rounding-that-makes-your-bot-risk-10-times-what-you-think-xiliux-blog-4lhj

## Related notes
- [[2026-07-22-the-backfill-pattern-adding-required-columns-without-downtime]]
- [[2026-09-06-exit-code-0-is-a-lie-7-ways-my-unattended-automation-silently-did-nothing]]
- [[2026-02-24-stop-using-any-the-wrong-way-in-rails]]
- [[2026-09-14-agents-for-humans-an-agent-that-refuses-to-guess-what-your-letter-says]]
- [[2026-10-04-analytics-engineer-the-job-that-didnt-exist-5-years-ago-and-why-it-does-now]]
- [[2026-09-21-building-a-market-aware-execution-engine-for-polymarket-bots-with-python]]
