---
title: 'Alpaca partial fills: count 7 shares, not 10'
date: '2026-10-24'
source: https://dev.to/stratcorealpha/alpaca-partial-fills-do-not-add-3-and-7-188g
domain: SQL
relevance: 🟡
tags:
- '#ai'
- '#library'
- '#python'
- '#sql'
- '#tool'
related:
- '[[2026-10-23-a-good-price-is-not-yet-a-trade]]'
- '[[2026-10-05-how-to-get-a-transcript-of-any-spotify-podcast-episode-3-ways-with-and-without-code]]'
- '[[2026-08-31-running-total-in-sql-the-window-frame-that-decides-the-answer]]'
- '[[2026-09-21-how-to-build-a-creator-emails-pipeline-in-one-python-call]]'
- '[[2026-10-14-43-days-17040-ai-signals-four-things-the-data-says-that-trend-lists-wont-tell-you]]'
- '[[2026-10-22-i-was-tired-of-letting-the-oom-killer-do-my-vram-math-so-i-wrote-a-one-file-cli]]'
status: unread
---

> **TL;DR:** Your bot should count 7 filled shares after totals of 3 and 7, not 10. In my small local check, adding both totals overstated the order by three shares. That is enough to give you the wrong view of how much of an order r…

## What’s new and why it matters
Your bot should count 7 filled shares after totals of 3 and 7, not 10. In my small local check, adding both totals overstated the order by three shares. That is enough to give you the wrong view of how much of an order remains open. In A Good Price Is Not Yet a Trade , Sergei B asks: "Which orders went into the count?" His post separates orders with some filled volume from orders with none. That distinction also matters when you read a bot's filled quantity. A good fill price says little if the quantity beside it has been counted twice. This example uses invented quantities. It does not use Se…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Write the query in a scratchpad and run EXPLAIN/QUERY PLAN to verify performance.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/stratcorealpha/alpaca-partial-fills-do-not-add-3-and-7-188g

## Related notes
- [[2026-10-23-a-good-price-is-not-yet-a-trade]]
- [[2026-10-05-how-to-get-a-transcript-of-any-spotify-podcast-episode-3-ways-with-and-without-code]]
- [[2026-08-31-running-total-in-sql-the-window-frame-that-decides-the-answer]]
- [[2026-09-21-how-to-build-a-creator-emails-pipeline-in-one-python-call]]
- [[2026-10-14-43-days-17040-ai-signals-four-things-the-data-says-that-trend-lists-wont-tell-you]]
- [[2026-10-22-i-was-tired-of-letting-the-oom-killer-do-my-vram-math-so-i-wrote-a-one-file-cli]]
