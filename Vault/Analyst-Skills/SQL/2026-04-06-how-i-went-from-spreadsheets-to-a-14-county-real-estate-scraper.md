---
title: How I Went From Spreadsheets to a 14-County Real Estate Scraper
date: '2026-04-06'
source: https://dev.to/domoniqueluchin/how-i-went-from-spreadsheets-to-a-14-county-real-estate-scraper-5cnb
domain: SQL
relevance: 🟡
tags:
- '#sql'
- '#tool'
related:
- '[[2026-04-06-i-scraped-14-texas-counties-every-night-to-find-distressed-properties]]'
- '[[2026-03-26-sqlite-is-enough-for-your-side-project-full-text-search-json-and-wal-mode-included]]'
- '[[2026-03-08-understanding-group-by-in-sql]]'
- '[[2026-03-11-i-thought-my-rails-query-was-fine-until-null-ate-my-data]]'
- '[[2026-03-28-kysely-has-a-free-api-type-safe-sql-query-builder-for-typescript]]'
- '[[2026-02-28-ai-data-analysis-tools-i-actually-use-daily]]'
status: unread
---

> **TL;DR:** Six months ago my lead list was a Google Sheet with 300 rows I updated manually. Now five edge functions scrape 14 Texas counties every night and score 125+ leads automatically. Here is the full build. What I Scrape Four…

## What’s new and why it matters
Six months ago my lead list was a Google Sheet with 300 rows I updated manually. Now five edge functions scrape 14 Texas counties every night and score 125+ leads automatically. Here is the full build. What I Scrape Four data sources per county: Foreclosure filings — Properties where the owner is behind on their mortgage Delinquent tax rolls — Properties with unpaid property taxes Code violations — Properties with open city violations 311 complaints — Nuisance complaints filed by neighbors Each one is a signal of seller motivation. Stack all four on one address and you have a highly distressed…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Write the query in a scratchpad and run EXPLAIN/QUERY PLAN to verify performance.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/domoniqueluchin/how-i-went-from-spreadsheets-to-a-14-county-real-estate-scraper-5cnb

## Related notes
- [[2026-04-06-i-scraped-14-texas-counties-every-night-to-find-distressed-properties]]
- [[2026-03-26-sqlite-is-enough-for-your-side-project-full-text-search-json-and-wal-mode-included]]
- [[2026-03-08-understanding-group-by-in-sql]]
- [[2026-03-11-i-thought-my-rails-query-was-fine-until-null-ate-my-data]]
- [[2026-03-28-kysely-has-a-free-api-type-safe-sql-query-builder-for-typescript]]
- [[2026-02-28-ai-data-analysis-tools-i-actually-use-daily]]
