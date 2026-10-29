---
title: I Asked for 21 Days of Prices and Got 147 Rows. Only 21 Were the Trip I Asked
  For
date: '2026-10-29'
source: https://dev.to/matveyg/i-asked-for-21-days-of-prices-and-got-147-rows-only-21-were-the-trip-i-asked-for-3571
domain: Productivity
relevance: 🟡
tags:
- '#productivity'
- '#python'
- '#sql'
- '#tool'
related:
- '[[2026-10-12-bookingcom-search-rows-hide-916-of-the-price-in-a-field-labelled-21-22-and-23]]'
- '[[2026-10-26-48-hour-field-notes-my-free-box-looked-slow-until-i-logged-the-gap-between-requests]]'
- '[[2026-10-28-give-your-ai-agent-search-demand-and-ai-answer-tools-mcp-and-function-calling-with-real-output]]'
- '[[2026-06-13-top-12-sql-interview-problems-for-data-engineers-with-answers]]'
- '[[2026-08-21-mariadb-106-to-130-for-wordpress-only-one-upgrade-actually-does-anything-benchmark]]'
- '[[2026-08-21-how-to-find-duplicate-rows-in-sql-and-decide-what-counts-as-one]]'
status: unread
---

> **TL;DR:** I run a visa agency in Bali. Half my clients' questions are not "how much is the flight" but "which week is cheapest", so one of the Apify Actors I maintain does nothing except pull Google Flights' price calendar — the s…

## What’s new and why it matters
I run a visa agency in Bali. Half my clients' questions are not "how much is the flight" but "which week is cheapest", so one of the Apify Actors I maintain does nothing except pull Google Flights' price calendar — the strip of per-day fares above the search box — and hand it back as rows. For one-way trips it behaves exactly the way the name promises. Today, 29 October 2026: { "origin" : "DPS" , "destination" : "SIN" , "departureDate" : "2026-11-20" , "calendarDays" : 21 , "calendarOnly" : true } 21 rows, one per date, lowest $60 on 26 November, highest $82, and a free summary row on the end:…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/matveyg/i-asked-for-21-days-of-prices-and-got-147-rows-only-21-were-the-trip-i-asked-for-3571

## Related notes
- [[2026-10-12-bookingcom-search-rows-hide-916-of-the-price-in-a-field-labelled-21-22-and-23]]
- [[2026-10-26-48-hour-field-notes-my-free-box-looked-slow-until-i-logged-the-gap-between-requests]]
- [[2026-10-28-give-your-ai-agent-search-demand-and-ai-answer-tools-mcp-and-function-calling-with-real-output]]
- [[2026-06-13-top-12-sql-interview-problems-for-data-engineers-with-answers]]
- [[2026-08-21-mariadb-106-to-130-for-wordpress-only-one-upgrade-actually-does-anything-benchmark]]
- [[2026-08-21-how-to-find-duplicate-rows-in-sql-and-decide-what-counts-as-one]]
