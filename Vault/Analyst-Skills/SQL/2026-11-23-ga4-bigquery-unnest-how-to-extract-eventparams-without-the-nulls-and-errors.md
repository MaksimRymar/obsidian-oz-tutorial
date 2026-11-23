---
title: 'GA4 BigQuery UNNEST: How to Extract event_params Without the NULLs and Errors'
date: '2026-11-23'
source: https://dev.to/logicalweb/ga4-bigquery-unnest-how-to-extract-eventparams-without-the-nulls-and-errors-2k4k
domain: SQL
relevance: 🟡
tags:
- '#best-practice'
- '#sql'
- '#tool'
- '#tutorial'
- '#zendesk'
related:
- '[[2026-08-21-how-to-find-duplicate-rows-in-sql-and-decide-what-counts-as-one]]'
- '[[2026-10-26-sql-joins-explained-inner-left-right-and-full-with-examples]]'
- '[[2026-09-16-sql-joins-with-examples-of-each]]'
- '[[2026-10-16-an-ai-explained-sql-group-by-in-four-lines-one-of-them-is-wrong]]'
- '[[2026-09-28-group-by-aggregate-functions-explained-the-where-vs-having-mistake-almost-everyone-makes]]'
- '[[2026-06-10-sql-for-data-analysis-the-10-query-patterns-that-matter]]'
status: unread
---

> **TL;DR:** GA4 BigQuery UNNEST: How to Extract event_params Without the NULLs and Errors If you have exported GA4 to BigQuery, you have probably hit this moment: you open the events_* table, find the column that should hold the pag…

## What’s new and why it matters
GA4 BigQuery UNNEST: How to Extract event_params Without the NULLs and Errors If you have exported GA4 to BigQuery, you have probably hit this moment: you open the events_* table, find the column that should hold the page URL or the session ID… and it's not a column at all. It's a nested, repeated record called event_params , and almost everything you actually want to analyse is buried inside it. This is the single biggest reason people stall with the GA4 BigQuery export. The data is all there — page locations, session IDs, engagement time, campaign values, your custom parameters — but none of…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Write the query in a scratchpad and run EXPLAIN/QUERY PLAN to verify performance.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/logicalweb/ga4-bigquery-unnest-how-to-extract-eventparams-without-the-nulls-and-errors-2k4k

## Related notes
- [[2026-08-21-how-to-find-duplicate-rows-in-sql-and-decide-what-counts-as-one]]
- [[2026-10-26-sql-joins-explained-inner-left-right-and-full-with-examples]]
- [[2026-09-16-sql-joins-with-examples-of-each]]
- [[2026-10-16-an-ai-explained-sql-group-by-in-four-lines-one-of-them-is-wrong]]
- [[2026-09-28-group-by-aggregate-functions-explained-the-where-vs-having-mistake-almost-everyone-makes]]
- [[2026-06-10-sql-for-data-analysis-the-10-query-patterns-that-matter]]
