---
title: 'arrayJoin in ClickHouse: Why Your Rows Are Duplicating (and How to Control
  It)'
date: '2026-04-28'
source: https://dev.to/mohhddhassan/arrayjoin-in-clickhouse-why-your-rows-are-duplicating-and-how-to-control-it-5862
domain: SQL
relevance: 🟡
tags:
- '#sql'
- '#tableau'
- '#tool'
- '#tutorial'
related:
- '[[2026-04-23-a-beginners-pocket-guide-to-sql-data-analysis]]'
- '[[2026-04-22-sql-set-operators-union-intersect-and-except-explained-simply]]'
- '[[2026-04-21-how-i-started-thinking-in-sql-not-just-writing-queries]]'
- '[[2026-03-09-sql-window-functions-dont-have-to-be-scary]]'
- '[[2026-04-21-sql-joins-and-window-functions-a-practical-guide]]'
- '[[2026-04-15-how-to-build-a-strong-foundation-in-sql-and-databases-step-by-step]]'
status: unread
---

> **TL;DR:** When working with arrays in ClickHouse, arrayJoin feels straightforward. Until your query suddenly returns far more rows than expected. The Use Case Let’s say you have a table like this: CREATE TABLE events ( user_id UIn…

## What’s new and why it matters
When working with arrays in ClickHouse, arrayJoin feels straightforward. Until your query suddenly returns far more rows than expected. The Use Case Let’s say you have a table like this: CREATE TABLE events ( user_id UInt32 , actions Array ( String ) ) ENGINE = MergeTree ORDER BY user_id ; Example row: user_id : 1 actions : [ ' click' , ' scroll' , ' purchase' ] Now you want each action as a separate row. The Tool: arrayJoin SELECT user_id , arrayJoin ( actions ) AS action FROM events ; Output: 1 click 1 scroll 1 purchase So far, everything looks correct. Where Things Go Wrong Now let’s say yo…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Write the query in a scratchpad and run EXPLAIN/QUERY PLAN to verify performance.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/mohhddhassan/arrayjoin-in-clickhouse-why-your-rows-are-duplicating-and-how-to-control-it-5862

## Related notes
- [[2026-04-23-a-beginners-pocket-guide-to-sql-data-analysis]]
- [[2026-04-22-sql-set-operators-union-intersect-and-except-explained-simply]]
- [[2026-04-21-how-i-started-thinking-in-sql-not-just-writing-queries]]
- [[2026-03-09-sql-window-functions-dont-have-to-be-scary]]
- [[2026-04-21-sql-joins-and-window-functions-a-practical-guide]]
- [[2026-04-15-how-to-build-a-strong-foundation-in-sql-and-databases-step-by-step]]
