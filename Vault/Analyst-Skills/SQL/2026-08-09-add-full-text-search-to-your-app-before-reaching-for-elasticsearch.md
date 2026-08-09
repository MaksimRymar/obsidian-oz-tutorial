---
title: Add Full-Text Search to Your App Before Reaching for Elasticsearch
date: '2026-08-09'
source: https://dev.to/libme/add-full-text-search-to-your-app-before-reaching-for-elasticsearch-lmc
domain: SQL
relevance: 🟡
tags:
- '#ai'
- '#best-practice'
- '#feature'
- '#sql'
- '#tool'
- '#zendesk'
related:
- '[[2026-03-30-database-indexing-explained-whats-actually-happening-under-the-hood]]'
- '[[2026-03-13-you-dont-need-a-framework-building-reliable-ai-agents-from-first-principles]]'
- '[[2026-06-28-how-to-generate-a-sql-schema-from-a-csv-file-without-hand-writing-every-column-type]]'
- '[[2026-06-21-product-analytics-with-sql-tracking-what-actually-matters]]'
- '[[2026-05-20-how-to-prompt-ai-tools-to-write-accurate-sql-queries-and-why-most-developers-get-this-wrong]]'
- '[[2026-04-17-i-tested-postgresql-on-5-million-rows-heres-what-actually-makes-queries-fast]]'
status: unread
---

> **TL;DR:** If your app already runs on Postgres and you need "search that finds the right rows when someone types a few words," you almost certainly do not need Elasticsearch yet. Postgres has had built-in full-text search for over…

## What’s new and why it matters
If your app already runs on Postgres and you need "search that finds the right rows when someone types a few words," you almost certainly do not need Elasticsearch yet. Postgres has had built-in full-text search for over a decade — stemming, ranking, and a GIN index that keeps queries fast — and for most apps under a few million rows it is fast enough, accurate enough, and one fewer service to operate. Reach for a dedicated search engine when you hit its real limits, not by default. I keep watching teams stand up an Elasticsearch or OpenSearch cluster for what is, in practice, a search box ove…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Write the query in a scratchpad and run EXPLAIN/QUERY PLAN to verify performance.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/libme/add-full-text-search-to-your-app-before-reaching-for-elasticsearch-lmc

## Related notes
- [[2026-03-30-database-indexing-explained-whats-actually-happening-under-the-hood]]
- [[2026-03-13-you-dont-need-a-framework-building-reliable-ai-agents-from-first-principles]]
- [[2026-06-28-how-to-generate-a-sql-schema-from-a-csv-file-without-hand-writing-every-column-type]]
- [[2026-06-21-product-analytics-with-sql-tracking-what-actually-matters]]
- [[2026-05-20-how-to-prompt-ai-tools-to-write-accurate-sql-queries-and-why-most-developers-get-this-wrong]]
- [[2026-04-17-i-tested-postgresql-on-5-million-rows-heres-what-actually-makes-queries-fast]]
