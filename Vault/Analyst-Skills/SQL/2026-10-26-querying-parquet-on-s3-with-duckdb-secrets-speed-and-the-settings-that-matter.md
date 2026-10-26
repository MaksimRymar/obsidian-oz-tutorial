---
title: 'Querying Parquet on S3 with DuckDB: secrets, speed and the settings that matter'
date: '2026-10-26'
source: https://dev.to/mohammed_arshadansari_f2/querying-parquet-on-s3-with-duckdb-secrets-speed-and-the-settings-that-matter-3gij
domain: SQL
relevance: 🟡
tags:
- '#ai'
- '#python'
- '#sql'
- '#tool'
related:
- '[[2026-07-20-building-a-right-click-query-this-file-workflow-in-vs-code-with-duckdb]]'
- '[[2026-10-05-how-to-get-a-transcript-of-any-spotify-podcast-episode-3-ways-with-and-without-code]]'
- '[[2026-08-21-which-sql-database-should-you-install]]'
- '[[2026-10-22-i-was-tired-of-letting-the-oom-killer-do-my-vram-math-so-i-wrote-a-one-file-cli]]'
- '[[2026-10-03-turn-database-docs-into-agent-ready-knowledge-okf-series-part-3]]'
- '[[2026-08-21-how-to-find-duplicate-rows-in-sql-and-decide-what-counts-as-one]]'
status: unread
---

> **TL;DR:** DuckDB reads Parquet on S3 in one line, and that part is not the problem. The problem shows up a month later, when a query that took two seconds on your laptop takes forty against the bucket and nobody can say why. The a…

## What’s new and why it matters
DuckDB reads Parquet on S3 in one line, and that part is not the problem. The problem shows up a month later, when a query that took two seconds on your laptop takes forty against the bucket and nobody can say why. The answer is almost never bandwidth. It is the number of requests. Object storage charges you a round trip for every file you open and every column chunk you fetch. A layout that costs nothing on local disk can mean tens of thousands of round trips on S3. This post covers credentials first, because they are what people search for, and then the layout and settings that decide speed.…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Write the query in a scratchpad and run EXPLAIN/QUERY PLAN to verify performance.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/mohammed_arshadansari_f2/querying-parquet-on-s3-with-duckdb-secrets-speed-and-the-settings-that-matter-3gij

## Related notes
- [[2026-07-20-building-a-right-click-query-this-file-workflow-in-vs-code-with-duckdb]]
- [[2026-10-05-how-to-get-a-transcript-of-any-spotify-podcast-episode-3-ways-with-and-without-code]]
- [[2026-08-21-which-sql-database-should-you-install]]
- [[2026-10-22-i-was-tired-of-letting-the-oom-killer-do-my-vram-math-so-i-wrote-a-one-file-cli]]
- [[2026-10-03-turn-database-docs-into-agent-ready-knowledge-okf-series-part-3]]
- [[2026-08-21-how-to-find-duplicate-rows-in-sql-and-decide-what-counts-as-one]]
