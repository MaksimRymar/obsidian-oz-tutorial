---
title: Filter the CFTC COT report for WHEAT and you get three different markets
date: '2026-09-24'
source: https://dev.to/devil_scrapes/filter-the-cftc-cot-report-for-wheat-and-you-get-three-different-markets-3l7n
domain: SQL
relevance: 🟡
tags:
- '#ai'
- '#python'
- '#sql'
- '#tool'
related:
- '[[2026-08-21-null-in-sql-why-null-finds-nothing-and-what-to-write-instead]]'
- '[[2026-09-18-how-we-grade-hundreds-of-sports-picks-a-day-in-public]]'
- '[[2026-09-23-one-real-scan-counts-a-hundred-ranking-a-curation-queue-by-your-own-users]]'
- '[[2026-09-16-sql-joins-with-examples-of-each]]'
- '[[2026-09-17-i-fact-checked-5-viral-my-ai-bot-made-money-posts-against-primary-data-none-survived]]'
- '[[2026-08-26-redb-371-props-search-up-to-100x-faster-an-alternative-to-ef-core-or-a-companion-to-it]]'
status: unread
---

> **TL;DR:** Quick answer Ask the CFTC's Commitments of Traders data for commodity_name = 'WHEAT' on the 2026-09-15 report and you don't get one market back. You get three: soft red winter wheat on the Chicago Board of Trade, hard re…

## What’s new and why it matters
Quick answer Ask the CFTC's Commitments of Traders data for commodity_name = 'WHEAT' on the 2026-09-15 report and you don't get one market back. You get three: soft red winter wheat on the Chicago Board of Trade, hard red winter wheat on the same exchange, and hard red spring wheat on the MIAX Futures Exchange. They are different contracts with different open interest and different traders, and speculators can be positioned in opposite directions in them. Add them up and you get a number that describes no real market. The CFTC Commitments of Traders Scraper pulls the COT reports straight from…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Write the query in a scratchpad and run EXPLAIN/QUERY PLAN to verify performance.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/devil_scrapes/filter-the-cftc-cot-report-for-wheat-and-you-get-three-different-markets-3l7n

## Related notes
- [[2026-08-21-null-in-sql-why-null-finds-nothing-and-what-to-write-instead]]
- [[2026-09-18-how-we-grade-hundreds-of-sports-picks-a-day-in-public]]
- [[2026-09-23-one-real-scan-counts-a-hundred-ranking-a-curation-queue-by-your-own-users]]
- [[2026-09-16-sql-joins-with-examples-of-each]]
- [[2026-09-17-i-fact-checked-5-viral-my-ai-bot-made-money-posts-against-primary-data-none-survived]]
- [[2026-08-26-redb-371-props-search-up-to-100x-faster-an-alternative-to-ef-core-or-a-companion-to-it]]
