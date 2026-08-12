---
title: Can You Run Hybrid Search on One Database? Yes! Here's How CrateDB Does It
date: '2026-08-12'
source: https://dev.to/srmadscience/can-you-run-hybrid-search-on-one-database-yes-heres-how-cratedb-does-it-42i
domain: AI-Tools
relevance: 🟡
tags:
- '#ai'
- '#best-practice'
- '#python'
- '#sql'
- '#support-analytics'
- '#tool'
- '#zendesk'
related:
- '[[2026-04-29-aggregations-counting-summing-and-averaging-your-data]]'
- '[[2026-06-08-running-real-sql-on-dynamodb-how-it-actually-works]]'
- '[[2026-08-11-sql-joins-how-to-join-two-tables-without-losing-or-doubling-rows]]'
- '[[2026-04-19-sql-joins-explained-simply---a-beginners-guide]]'
- '[[2026-04-15-sql-limit-and-offset-paginate-your-query-results-like-a-pro]]'
- '[[2026-06-28-how-to-generate-a-sql-schema-from-a-csv-file-without-hand-writing-every-column-type]]'
status: unread
---

> **TL;DR:** Search has got more powerful, but also more complicated It used to be that database queries were simple enough. Either you had an index, or you didn't, and either way you had some kind of optimizer (cost or rule) that tu…

## What’s new and why it matters
Search has got more powerful, but also more complicated It used to be that database queries were simple enough. Either you had an index, or you didn't, and either way you had some kind of optimizer (cost or rule) that turned your SQL statement into a viable plan for finding and returning your data. We now live in a world where in addition to the Boolean logic of traditional RDBMS queries, we also have: Geospatial queries Full text search queries, using BM25 . Vector Search And if that weren't enough, we have to consider that instead of a traditional application issuing the query, it might be a…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Reproduce the example in a notebook; then refactor into a reusable function.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/srmadscience/can-you-run-hybrid-search-on-one-database-yes-heres-how-cratedb-does-it-42i

## Related notes
- [[2026-04-29-aggregations-counting-summing-and-averaging-your-data]]
- [[2026-06-08-running-real-sql-on-dynamodb-how-it-actually-works]]
- [[2026-08-11-sql-joins-how-to-join-two-tables-without-losing-or-doubling-rows]]
- [[2026-04-19-sql-joins-explained-simply---a-beginners-guide]]
- [[2026-04-15-sql-limit-and-offset-paginate-your-query-results-like-a-pro]]
- [[2026-06-28-how-to-generate-a-sql-schema-from-a-csv-file-without-hand-writing-every-column-type]]
