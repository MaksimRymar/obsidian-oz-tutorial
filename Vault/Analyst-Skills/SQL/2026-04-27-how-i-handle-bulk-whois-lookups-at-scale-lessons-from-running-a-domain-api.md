---
title: 'How I handle bulk WHOIS lookups at scale: lessons from running a domain API'
date: '2026-04-27'
source: https://dev.to/whoisjson/how-i-handle-bulk-whois-lookups-at-scale-lessons-from-running-a-domain-api-3lfe
domain: SQL
relevance: 🟡
tags:
- '#python'
- '#sql'
- '#tool'
related:
- '[[2026-04-17-maybe-this-is-how-open-source-apps-are-born]]'
- '[[2026-04-08-how-building-a-streaming-sql-api-in-nodejs-changed-my-approach-to-real-time-data]]'
- '[[2026-04-02-how-to-turn-any-webpage-into-structured-data-for-your-llm]]'
- '[[2026-03-13-you-dont-need-a-framework-building-reliable-ai-agents-from-first-principles]]'
- '[[2026-02-24-stop-using-any-the-wrong-way-in-rails]]'
- '[[2026-04-21-what-happens-to-your-mutual-fund-between-9-am-and-9-pm]]'
status: unread
---

> **TL;DR:** I've been running a WHOIS API since 2016. For a long time, most users were doing one-off lookups, maybe a few hundred a day. Then at some point customers started showing up with different needs entirely. Threat intel pip…

## What’s new and why it matters
I've been running a WHOIS API since 2016. For a long time, most users were doing one-off lookups, maybe a few hundred a day. Then at some point customers started showing up with different needs entirely. Threat intel pipelines, domain portfolio audits, registrant enrichment at scale. One customer hit 30 million requests in a single month. That's a different problem from building a WHOIS wrapper. And most of the articles I found when dealing with it were either too basic or skipped the parts that actually bite you in production. So here's what I've learned. Rate limits are the easy part The obv…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Write the query in a scratchpad and run EXPLAIN/QUERY PLAN to verify performance.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/whoisjson/how-i-handle-bulk-whois-lookups-at-scale-lessons-from-running-a-domain-api-3lfe

## Related notes
- [[2026-04-17-maybe-this-is-how-open-source-apps-are-born]]
- [[2026-04-08-how-building-a-streaming-sql-api-in-nodejs-changed-my-approach-to-real-time-data]]
- [[2026-04-02-how-to-turn-any-webpage-into-structured-data-for-your-llm]]
- [[2026-03-13-you-dont-need-a-framework-building-reliable-ai-agents-from-first-principles]]
- [[2026-02-24-stop-using-any-the-wrong-way-in-rails]]
- [[2026-04-21-what-happens-to-your-mutual-fund-between-9-am-and-9-pm]]
