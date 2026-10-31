---
title: 'The last month is always a lie: lessons from querying 1 billion rows of Brazilian
  crime data'
date: '2026-10-30'
source: https://dev.to/crime_brasil/the-last-month-is-always-a-lie-lessons-from-querying-1-billion-rows-of-brazilian-crime-data-2bhn
domain: SQL
relevance: 🔴
tags:
- '#ai'
- '#python'
- '#sql'
- '#tool'
- '#zendesk'
related:
- '[[2026-08-30-sql-date-functions-how-to-group-by-month-without-losing-one]]'
- '[[2026-08-21-how-to-find-duplicate-rows-in-sql-and-decide-what-counts-as-one]]'
- '[[2026-08-31-how-to-reconcile-two-tables-in-sql-when-the-row-counts-match]]'
- '[[2026-08-22-where-to-get-a-sample-database-to-practice-sql-and-how-to-check-it-loaded]]'
- '[[2026-08-30-funnel-conversion-in-sql-and-the-step-that-shows-100]]'
- '[[2026-08-31-running-total-in-sql-the-window-frame-that-decides-the-answer]]'
status: unread
---

> **TL;DR:** We run Crime Brasil , a site that turns official Brazilian public-safety data into maps and rankings for every neighbourhood and municipality in the country. Under the hood that is about 1 billion rows: police reports fr…

## What’s new and why it matters
We run Crime Brasil , a site that turns official Brazilian public-safety data into maps and rankings for every neighbourhood and municipality in the country. Under the hood that is about 1 billion rows: police reports from state security departments, health-ministry mortality records, court and prison data, traffic and more. Most of the hard problems are not about scale. They are about data that looks right and isn't. Here are two rules we now apply before any number leaves the database, plus what they say about São Paulo in 2026. Rule 1: the last month in the file is always incomplete State p…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Write the query in a scratchpad and run EXPLAIN/QUERY PLAN to verify performance.
- Add a short note: what changed in your workflow?

## Relevance
🔴

## Source
https://dev.to/crime_brasil/the-last-month-is-always-a-lie-lessons-from-querying-1-billion-rows-of-brazilian-crime-data-2bhn

## Related notes
- [[2026-08-30-sql-date-functions-how-to-group-by-month-without-losing-one]]
- [[2026-08-21-how-to-find-duplicate-rows-in-sql-and-decide-what-counts-as-one]]
- [[2026-08-31-how-to-reconcile-two-tables-in-sql-when-the-row-counts-match]]
- [[2026-08-22-where-to-get-a-sample-database-to-practice-sql-and-how-to-check-it-loaded]]
- [[2026-08-30-funnel-conversion-in-sql-and-the-step-that-shows-100]]
- [[2026-08-31-running-total-in-sql-the-window-frame-that-decides-the-answer]]
