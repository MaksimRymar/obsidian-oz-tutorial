---
title: Tracking Tableau Server Storage Over Time with PostgreSQL
date: '2026-07-29'
source: https://dev.to/jungalung/tracking-tableau-server-storage-over-time-with-postgresql-33fn
domain: SQL
relevance: 🟡
tags:
- '#ai'
- '#sql'
- '#tableau'
- '#zendesk'
related:
- '[[2026-03-09-sql-window-functions-dont-have-to-be-scary]]'
- '[[2026-04-27-sql-group-by-having-the-beginners-guide-to-summarizing-data-like-a-pro]]'
- '[[2026-04-09-sql-aggregate-functions-stop-guessing-start-calculating]]'
- '[[2026-06-09-pandas-vs-sql-when-to-use-each]]'
- '[[2026-07-24-you-dont-need-a-backend-to-store-form-submissions-you-need-a-place-to-ask-how-many]]'
- '[[2026-07-28-how-i-made-sure-you-cant-like-and-dislike-the-same-post-at-once]]'
status: unread
---

> **TL;DR:** Tableau's admin views show you storage at a single point in time, but they don't give you a trend line. If you want to know whether your server's footprint is growing, shrinking, or holding steady, you need to snapshot i…

## What’s new and why it matters
Tableau's admin views show you storage at a single point in time, but they don't give you a trend line. If you want to know whether your server's footprint is growing, shrinking, or holding steady, you need to snapshot it yourself. Here's the query I run daily to do that. The SQL SELECT CURRENT_DATE AS snapshot_date , ROUND ( SUM ( CASE WHEN content_type = 'Workbook' THEN size ELSE 0 END ) / 1000 . 0 ^ 3 , 2 ) AS workbook_storage_gb , ROUND ( SUM ( CASE WHEN content_type = 'Datasource' THEN size ELSE 0 END ) / 1000 . 0 ^ 3 , 2 ) AS datasource_storage_gb , ROUND ( SUM ( size ) / 1000 . 0 ^ 3 ,…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Write the query in a scratchpad and run EXPLAIN/QUERY PLAN to verify performance.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/jungalung/tracking-tableau-server-storage-over-time-with-postgresql-33fn

## Related notes
- [[2026-03-09-sql-window-functions-dont-have-to-be-scary]]
- [[2026-04-27-sql-group-by-having-the-beginners-guide-to-summarizing-data-like-a-pro]]
- [[2026-04-09-sql-aggregate-functions-stop-guessing-start-calculating]]
- [[2026-06-09-pandas-vs-sql-when-to-use-each]]
- [[2026-07-24-you-dont-need-a-backend-to-store-form-submissions-you-need-a-place-to-ask-how-many]]
- [[2026-07-28-how-i-made-sure-you-cant-like-and-dislike-the-same-post-at-once]]
