---
title: Your BigQuery bill is a query-shape problem. We cut one 72% in three weeks.
date: '2026-07-27'
source: https://dev.to/votiakov/your-bigquery-bill-is-a-query-shape-problem-we-cut-one-72-in-three-weeks-3mnh
domain: SQL
relevance: 🔴
tags:
- '#sql'
- '#support-analytics'
- '#tool'
related:
- '[[2026-06-28-how-to-generate-a-sql-schema-from-a-csv-file-without-hand-writing-every-column-type]]'
- '[[2026-07-06-your-postgres-already-knows-why-its-slow-you-just-have-to-ask-it]]'
- '[[2026-07-09-dashboards-dont-get-opened-building-a-weekly-lapse-risk-pipeline-that-pushes-work-instead-of-waiting-for-logins]]'
- '[[2026-06-08-running-real-sql-on-dynamodb-how-it-actually-works]]'
- '[[2026-07-04-why-your-database-index-gets-ignored-and-how-to-design-one-that-isnt]]'
- '[[2026-07-27-track-new-job-postings-the-week-they-appear-with-a-scheduled-scraper-and-a-diff]]'
status: unread
---

> **TL;DR:** BigQuery doesn't charge you for having data. It charges you for touching it. On-demand pricing bills per byte scanned, which means your bill isn't a data-size problem or a traffic problem. It's a query-shape problem, and…

## What’s new and why it matters
BigQuery doesn't charge you for having data. It charges you for touching it. On-demand pricing bills per byte scanned, which means your bill isn't a data-size problem or a traffic problem. It's a query-shape problem, and query shape is fixable in an afternoon per table. A recent client was a textbook case. Dashboards running SELECT * over an unpartitioned events table, so every refresh scanned the full history back to 2019. Plus a pile of scheduled queries feeding tables nobody read anymore. Three weeks of work cut the bill 72%, about £2K a month, and the queries got faster. That last part sur…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Write the query in a scratchpad and run EXPLAIN/QUERY PLAN to verify performance.
- Add a short note: what changed in your workflow?

## Relevance
🔴

## Source
https://dev.to/votiakov/your-bigquery-bill-is-a-query-shape-problem-we-cut-one-72-in-three-weeks-3mnh

## Related notes
- [[2026-06-28-how-to-generate-a-sql-schema-from-a-csv-file-without-hand-writing-every-column-type]]
- [[2026-07-06-your-postgres-already-knows-why-its-slow-you-just-have-to-ask-it]]
- [[2026-07-09-dashboards-dont-get-opened-building-a-weekly-lapse-risk-pipeline-that-pushes-work-instead-of-waiting-for-logins]]
- [[2026-06-08-running-real-sql-on-dynamodb-how-it-actually-works]]
- [[2026-07-04-why-your-database-index-gets-ignored-and-how-to-design-one-that-isnt]]
- [[2026-07-27-track-new-job-postings-the-week-they-appear-with-a-scheduled-scraper-and-a-diff]]
