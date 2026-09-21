---
title: percentile_cont, a 20,000 row window, and the difference between skipped and
  failed
date: '2026-09-21'
source: https://dev.to/daniel_pertu/percentilecont-a-20000-row-window-and-the-difference-between-skipped-and-failed-gek
domain: SQL
relevance: 🟡
tags:
- '#sql'
- '#tool'
related:
- '[[2026-09-05-what-actually-happens-in-a-database-index-and-why-half-of-them-do-nothing]]'
- '[[2026-08-31-subquery-vs-cte-in-sql-same-logic-one-you-can-check]]'
- '[[2026-08-25-pgcancelbackend-returned-true-the-queue-didnt-move]]'
- '[[2026-08-13-cohort-retention-analysis-in-sql-the-query-that-tells-you-if-your-product-is-actually-sticky]]'
- '[[2026-06-10-sql-for-data-analysis-the-10-query-patterns-that-matter]]'
- '[[2026-09-01-i-raced-six-models-against-each-other-on-digitalocean-inference-the-cheapest-one-won]]'
status: unread
---

> **TL;DR:** Every score in CogniPrep is reported as a percentile, because a raw 74 out of 100 tells a candidate nothing. To do that you need a population distribution per game, and to keep that distribution current you need a job. T…

## What’s new and why it matters
Every score in CogniPrep is reported as a percentile, because a raw 74 out of 100 tells a candidate nothing. To do that you need a population distribution per game, and to keep that distribution current you need a job. The first version of the job did what most first versions do: select the rows, compute in Node. const sessions = await db . select (). from ( gameSessionsTable ). where ( eq ( gameSessionsTable . game_id , gameId )); const scores = sessions . map (( s ) => s . raw_score ); // mean, median, stdDev, percentiles in JS That selects every column, including a metrics jsonb blob that c…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Write the query in a scratchpad and run EXPLAIN/QUERY PLAN to verify performance.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/daniel_pertu/percentilecont-a-20000-row-window-and-the-difference-between-skipped-and-failed-gek

## Related notes
- [[2026-09-05-what-actually-happens-in-a-database-index-and-why-half-of-them-do-nothing]]
- [[2026-08-31-subquery-vs-cte-in-sql-same-logic-one-you-can-check]]
- [[2026-08-25-pgcancelbackend-returned-true-the-queue-didnt-move]]
- [[2026-08-13-cohort-retention-analysis-in-sql-the-query-that-tells-you-if-your-product-is-actually-sticky]]
- [[2026-06-10-sql-for-data-analysis-the-10-query-patterns-that-matter]]
- [[2026-09-01-i-raced-six-models-against-each-other-on-digitalocean-inference-the-cheapest-one-won]]
