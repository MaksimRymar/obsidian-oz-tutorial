---
title: 'Getting only the new DOIs from the Crossref API every day: dates, cursors
  and rate limits'
date: '2026-11-01'
source: https://dev.to/fecklesspleb/getting-only-the-new-dois-from-the-crossref-api-every-day-dates-cursors-and-rate-limits-354
domain: SQL
relevance: 🟡
tags:
- '#ai'
- '#library'
- '#python'
- '#sql'
- '#tool'
related:
- '[[2026-10-16-an-ai-explained-sql-group-by-in-four-lines-one-of-them-is-wrong]]'
- '[[2026-08-30-sql-date-functions-how-to-group-by-month-without-losing-one]]'
- '[[2026-08-11-sql-aliases-how-to-read-a-query-out-loud]]'
- '[[2026-08-21-how-to-find-duplicate-rows-in-sql-and-decide-what-counts-as-one]]'
- '[[2026-06-15-day-01-of-learning-data-engineering-step1-sql-joins-and-set-operators]]'
- '[[2026-04-03-i-got-tired-of-watching-my-terminal-so-i-built-guga]]'
status: unread
---

> **TL;DR:** AI disclosure: this post was drafted with AI assistance. I ran every request and every number below myself against the live Crossref REST API on November 1, 2026, and checked the code and tests before publishing. I wante…

## What’s new and why it matters
AI disclosure: this post was drafted with AI assistance. I ran every request and every number below myself against the live Crossref REST API on November 1, 2026, and checked the code and tests before publishing. I wanted a boring thing: every morning, a CSV of the journal articles that got a DOI since yesterday, for a handful of journals, and never the same DOI twice. Crossref's REST API is free, needs no key, and held 188,319,891 records when I asked, so it should be one request. It is close, but it took me a few wrong turns. Here are the ones worth knowing about. The finished script is abou…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Write the query in a scratchpad and run EXPLAIN/QUERY PLAN to verify performance.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/fecklesspleb/getting-only-the-new-dois-from-the-crossref-api-every-day-dates-cursors-and-rate-limits-354

## Related notes
- [[2026-10-16-an-ai-explained-sql-group-by-in-four-lines-one-of-them-is-wrong]]
- [[2026-08-30-sql-date-functions-how-to-group-by-month-without-losing-one]]
- [[2026-08-11-sql-aliases-how-to-read-a-query-out-loud]]
- [[2026-08-21-how-to-find-duplicate-rows-in-sql-and-decide-what-counts-as-one]]
- [[2026-06-15-day-01-of-learning-data-engineering-step1-sql-joins-and-set-operators]]
- [[2026-04-03-i-got-tired-of-watching-my-terminal-so-i-built-guga]]
