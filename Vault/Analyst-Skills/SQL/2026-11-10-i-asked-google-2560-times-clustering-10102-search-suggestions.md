---
title: 'I asked Google 2,560 times: clustering 10,102 search suggestions'
date: '2026-11-10'
source: https://dev.to/sinostay/i-asked-google-2560-times-clustering-10102-search-suggestions-543d
domain: SQL
relevance: 🟡
tags:
- '#ai'
- '#python'
- '#sql'
- '#tool'
related:
- '[[2026-10-05-how-to-get-a-transcript-of-any-spotify-podcast-episode-3-ways-with-and-without-code]]'
- '[[2026-10-14-our-free-plan-hides-creators-with-a-window-function-and-the-locked-count-is-the-same-predicate-with-a-not-in-front]]'
- '[[2026-06-28-how-to-generate-a-sql-schema-from-a-csv-file-without-hand-writing-every-column-type]]'
- '[[2026-09-04-i-built-an-offline-document-indexer-and-ollama-taught-me-two-things-i-did-not-expect]]'
- '[[2026-06-15-day-01-of-learning-data-engineering-step1-sql-joins-and-set-operators]]'
- '[[2026-08-12-sql-foundations-start-to-finish]]'
status: unread
---

> **TL;DR:** I wanted to know what people actually type before a trip to China. Not what I assumed, and not what travel blogs cover — what goes into the box. Google does not sell that data cheaply. But it does hand out its autocomple…

## What’s new and why it matters
I wanted to know what people actually type before a trip to China. Not what I assumed, and not what travel blogs cover — what goes into the box. Google does not sell that data cheaply. But it does hand out its autocomplete endpoint for free, and that endpoint returns the phrases real people typed, ordered by how often they type them. So I scraped my own question into it. The harvest Three layers, about 2,560 requests: # 1. seed phrases SEEDS = [ 'china' , 'china travel' , 'china visa' , 'china hotel' , 'china sim card' , . . . ] # 2. question prefixes — this is where intent lives PREFIXES = […

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Write the query in a scratchpad and run EXPLAIN/QUERY PLAN to verify performance.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/sinostay/i-asked-google-2560-times-clustering-10102-search-suggestions-543d

## Related notes
- [[2026-10-05-how-to-get-a-transcript-of-any-spotify-podcast-episode-3-ways-with-and-without-code]]
- [[2026-10-14-our-free-plan-hides-creators-with-a-window-function-and-the-locked-count-is-the-same-predicate-with-a-not-in-front]]
- [[2026-06-28-how-to-generate-a-sql-schema-from-a-csv-file-without-hand-writing-every-column-type]]
- [[2026-09-04-i-built-an-offline-document-indexer-and-ollama-taught-me-two-things-i-did-not-expect]]
- [[2026-06-15-day-01-of-learning-data-engineering-step1-sql-joins-and-set-operators]]
- [[2026-08-12-sql-foundations-start-to-finish]]
