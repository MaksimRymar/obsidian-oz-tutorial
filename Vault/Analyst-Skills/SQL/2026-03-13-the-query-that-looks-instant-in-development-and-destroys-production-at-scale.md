---
title: The Query That Looks Instant in Development and Destroys Production at Scale
date: '2026-03-13'
source: https://dev.to/makroumi/the-query-that-looks-instant-in-development-and-destroys-production-at-scale-5h6l
domain: SQL
relevance: 🔴
tags:
- '#best-practice'
- '#sql'
- '#tool'
related:
- '[[2026-03-13-7-sql-patterns-that-look-fine-in-review-and-destroy-you-in-production]]'
- '[[2026-03-09-the-sql-query-that-ruined-my-weekend-and-what-i-built-to-prevent-it]]'
- '[[2026-02-25-partition-and-organize-data-for-performance]]'
- '[[2026-03-01-stop-writing-slow-sql-7-query-optimization-tricks-every-developer-should-know]]'
- '[[2026-03-02-database-indexing-explained-how-to-make-your-queries-1000x-faster]]'
- '[[2026-03-11-why-production-databases-break-normalization-and-why-thats-okay]]'
status: unread
---

> **TL;DR:** Originally published at makroumi.hashnode.dev You push the code on Friday afternoon. Tests pass. Staging looks fine. You deploy and go home. At 2am your phone rings. Response times are 8 seconds. Users are abandoning. Th…

## What’s new and why it matters
Originally published at makroumi.hashnode.dev You push the code on Friday afternoon. Tests pass. Staging looks fine. You deploy and go home. At 2am your phone rings. Response times are 8 seconds. Users are abandoning. The on-call engineer is staring at a dashboard full of red. And somewhere in the codebase is a query that ran in 4 milliseconds in development and is now bringing down production on a table with 50 million rows. This is not a rare story. It happens every week at companies of every size. The query was never dangerous in development because development doesn't look like production.…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Write the query in a scratchpad and run EXPLAIN/QUERY PLAN to verify performance.
- Add a short note: what changed in your workflow?

## Relevance
🔴

## Source
https://dev.to/makroumi/the-query-that-looks-instant-in-development-and-destroys-production-at-scale-5h6l

## Related notes
- [[2026-03-13-7-sql-patterns-that-look-fine-in-review-and-destroy-you-in-production]]
- [[2026-03-09-the-sql-query-that-ruined-my-weekend-and-what-i-built-to-prevent-it]]
- [[2026-02-25-partition-and-organize-data-for-performance]]
- [[2026-03-01-stop-writing-slow-sql-7-query-optimization-tricks-every-developer-should-know]]
- [[2026-03-02-database-indexing-explained-how-to-make-your-queries-1000x-faster]]
- [[2026-03-11-why-production-databases-break-normalization-and-why-thats-okay]]
