---
title: Store the Wall Time, Not the UTC Instant — Morocco's 2026 Time Change
date: '2026-11-26'
source: https://dev.to/wozo/store-the-wall-time-not-the-utc-instant-moroccos-2026-time-change-38m1
domain: SQL
relevance: 🔴
tags:
- '#ai'
- '#feature'
- '#library'
- '#python'
- '#sql'
- '#support-analytics'
- '#tool'
related:
- '[[2026-08-26-redb-371-props-search-up-to-100x-faster-an-alternative-to-ef-core-or-a-companion-to-it]]'
- '[[2026-09-26-26-of-45-shops-had-no-way-to-reach-them-heres-the-script-i-added]]'
- '[[2026-11-11-five-security-tests-for-mcp-servers-and-agents-in-173-lines-of-python]]'
- '[[2026-06-12-build-a-rag-chatbot-from-scratch-in-about-40-lines-of-python]]'
- '[[2026-09-07-like-in-sql-explained-for-beginners]]'
- '[[2026-10-05-how-to-get-a-transcript-of-any-spotify-podcast-episode-3-ways-with-and-without-code]]'
status: unread
---

> **TL;DR:** We've all heard "store everything in UTC." For a timestamp that already happened, that's the right default. For a meeting that has not happened yet, it can quietly go wrong. The time you actually promised is a civil time…

## What’s new and why it matters
We've all heard "store everything in UTC." For a timestamp that already happened, that's the right default. For a meeting that has not happened yet, it can quietly go wrong. The time you actually promised is a civil time in a city — 10:00 in Casablanca on 15 October 2026 — and that city's offset can still change after you save the event. Morocco did exactly that this year. What changed On Sunday, 20 September 2026, at 02:00, clocks in Morocco went back 60 minutes. Decree No. 2.26.530, adopted on 25 June 2026 and published in Bulletin Officiel No. 7521 on 29 June, returned legal time to Greenwi…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Write the query in a scratchpad and run EXPLAIN/QUERY PLAN to verify performance.
- Add a short note: what changed in your workflow?

## Relevance
🔴

## Source
https://dev.to/wozo/store-the-wall-time-not-the-utc-instant-moroccos-2026-time-change-38m1

## Related notes
- [[2026-08-26-redb-371-props-search-up-to-100x-faster-an-alternative-to-ef-core-or-a-companion-to-it]]
- [[2026-09-26-26-of-45-shops-had-no-way-to-reach-them-heres-the-script-i-added]]
- [[2026-11-11-five-security-tests-for-mcp-servers-and-agents-in-173-lines-of-python]]
- [[2026-06-12-build-a-rag-chatbot-from-scratch-in-about-40-lines-of-python]]
- [[2026-09-07-like-in-sql-explained-for-beginners]]
- [[2026-10-05-how-to-get-a-transcript-of-any-spotify-podcast-episode-3-ways-with-and-without-code]]
