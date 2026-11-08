---
title: Fifteen Chinese cities have more sights than beds — and that is a feature,
  not a gap
date: '2026-11-08'
source: https://dev.to/sinostay/fifteen-chinese-cities-have-more-sights-than-beds-and-that-is-a-feature-not-a-gap-2bm4
domain: SQL
relevance: 🟡
tags:
- '#ai'
- '#feature'
- '#sql'
related:
- '[[2026-08-21-how-to-find-duplicate-rows-in-sql-and-decide-what-counts-as-one]]'
- '[[2026-10-29-teaching-yourself-sql-when-your-job-is-ops]]'
- '[[2026-10-16-an-ai-explained-sql-group-by-in-four-lines-one-of-them-is-wrong]]'
- '[[2026-08-31-running-total-in-sql-the-window-frame-that-decides-the-answer]]'
- '[[2026-08-26-redb-371-props-search-up-to-100x-faster-an-alternative-to-ef-core-or-a-companion-to-it]]'
- '[[2026-09-07-like-in-sql-explained-for-beginners]]'
status: unread
---

> **TL;DR:** We run a small travel dataset: hotels in China that state they accept foreign guests, attractions with English names and opening hours, both matched by city. Every city page on the site has a floor of eight verified hote…

## What’s new and why it matters
We run a small travel dataset: hotels in China that state they accept foreign guests, attractions with English names and opening hours, both matched by city. Every city page on the site has a floor of eight verified hotels. Below eight, the city gets the nearest larger city instead of a page. Eighteen cities sit exactly on that floor. Fifteen of them have at least six attractions. That number is the whole post. Here is what it means and how we got it. The query Two aggregates, one join: SELECT a . city_slug , a . n AS spots , h . n AS hotels FROM ( SELECT city_slug , COUNT ( * ) n FROM attract…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Write the query in a scratchpad and run EXPLAIN/QUERY PLAN to verify performance.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/sinostay/fifteen-chinese-cities-have-more-sights-than-beds-and-that-is-a-feature-not-a-gap-2bm4

## Related notes
- [[2026-08-21-how-to-find-duplicate-rows-in-sql-and-decide-what-counts-as-one]]
- [[2026-10-29-teaching-yourself-sql-when-your-job-is-ops]]
- [[2026-10-16-an-ai-explained-sql-group-by-in-four-lines-one-of-them-is-wrong]]
- [[2026-08-31-running-total-in-sql-the-window-frame-that-decides-the-answer]]
- [[2026-08-26-redb-371-props-search-up-to-100x-faster-an-alternative-to-ef-core-or-a-companion-to-it]]
- [[2026-09-07-like-in-sql-explained-for-beginners]]
