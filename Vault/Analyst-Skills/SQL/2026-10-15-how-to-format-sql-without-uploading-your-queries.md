---
title: How to format SQL without uploading your queries
date: '2026-10-15'
source: https://dev.to/aniruddh_kawle_294f0f38b1/how-to-format-sql-without-uploading-your-queries-13dg
domain: SQL
relevance: 🟡
tags:
- '#sql'
- '#tool'
- '#tutorial'
related:
- '[[2026-03-30-i-stopped-pasting-ddl-into-random-chatbots-heres-the-local-windows-db-client-i-use]]'
- '[[2026-07-22-when-to-trust-ai-generated-sql-and-when-not-to]]'
- '[[2026-06-28-data-analysis-sql-asking-the-right-questions-and-using-the-right-tools]]'
- '[[2026-09-18-the-dialect-trap-why-ai-writes-sql-your-database-refuses-to-run]]'
- '[[2026-06-10-sql-for-data-analysis-the-10-query-patterns-that-matter]]'
- '[[2026-06-28-our-sql-server-loop-kept-writing-the-previous-rows-value]]'
status: unread
---

> **TL;DR:** Pasting a production query into a random "SQL formatter" website is a habit most of us have, and a quiet risk. Queries contain table names, column names and sometimes literal values you'd rather not hand to a server you…

## What’s new and why it matters
Pasting a production query into a random "SQL formatter" website is a habit most of us have, and a quiet risk. Queries contain table names, column names and sometimes literal values you'd rather not hand to a server you can't inspect. Here's how to check whether a tool really stays local, and what to watch for by dialect. Check a tool before you paste Open your browser's DevTools, go to the Network tab, paste a query and run the formatter. If a request fires that includes your SQL in its payload, the tool sends it to a server. If nothing happens when you format, the work is happening in your t…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Write the query in a scratchpad and run EXPLAIN/QUERY PLAN to verify performance.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/aniruddh_kawle_294f0f38b1/how-to-format-sql-without-uploading-your-queries-13dg

## Related notes
- [[2026-03-30-i-stopped-pasting-ddl-into-random-chatbots-heres-the-local-windows-db-client-i-use]]
- [[2026-07-22-when-to-trust-ai-generated-sql-and-when-not-to]]
- [[2026-06-28-data-analysis-sql-asking-the-right-questions-and-using-the-right-tools]]
- [[2026-09-18-the-dialect-trap-why-ai-writes-sql-your-database-refuses-to-run]]
- [[2026-06-10-sql-for-data-analysis-the-10-query-patterns-that-matter]]
- [[2026-06-28-our-sql-server-loop-kept-writing-the-previous-rows-value]]
