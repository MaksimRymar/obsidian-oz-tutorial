---
title: SELECT FINAL and OPTIMIZE FINAL Are Not the Same Thing
date: '2026-06-13'
source: https://dev.to/mohhddhassan/select-final-and-optimize-final-are-not-the-same-thing-7ak
domain: SQL
relevance: 🟡
tags:
- '#ai'
- '#best-practice'
- '#sql'
- '#tool'
related:
- '[[2026-04-22-sql-set-operators-union-intersect-and-except-explained-simply]]'
- '[[2026-03-03-sql-joins-window-functions-the-skills-that-separate-analysts-from-beginners]]'
- '[[2026-04-21-sql-joins-and-window-functions-a-practical-guide]]'
- '[[2026-06-10-how-to-scrape-google-search-results-without-building-your-own-scraper]]'
- '[[2026-04-23-i-built-a-browser-only-sql-practice-tool-because-installing-dbeaver-is-a-productivity-tax]]'
- '[[2026-03-15-why-i-as-someone-who-likes-mysql-now-want-to-recommend-postgresql]]'
status: unread
---

> **TL;DR:** One thing that confused me when I first started learning ClickHouse was the word FINAL . Because eventually you'll come across both: SELECT * FROM events FINAL ; and: OPTIMIZE TABLE events FINAL ; At first glance, they s…

## What’s new and why it matters
One thing that confused me when I first started learning ClickHouse was the word FINAL . Because eventually you'll come across both: SELECT * FROM events FINAL ; and: OPTIMIZE TABLE events FINAL ; At first glance, they sound like they should do roughly the same thing. After all, both contain the word FINAL . But they actually solve two completely different problems. One affects query results. The other affects how data is physically stored. Understanding this distinction can save a lot of confusion when working with MergeTree tables. Why This Confusion Happens Most people encounter FINAL while…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Write the query in a scratchpad and run EXPLAIN/QUERY PLAN to verify performance.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/mohhddhassan/select-final-and-optimize-final-are-not-the-same-thing-7ak

## Related notes
- [[2026-04-22-sql-set-operators-union-intersect-and-except-explained-simply]]
- [[2026-03-03-sql-joins-window-functions-the-skills-that-separate-analysts-from-beginners]]
- [[2026-04-21-sql-joins-and-window-functions-a-practical-guide]]
- [[2026-06-10-how-to-scrape-google-search-results-without-building-your-own-scraper]]
- [[2026-04-23-i-built-a-browser-only-sql-practice-tool-because-installing-dbeaver-is-a-productivity-tax]]
- [[2026-03-15-why-i-as-someone-who-likes-mysql-now-want-to-recommend-postgresql]]
