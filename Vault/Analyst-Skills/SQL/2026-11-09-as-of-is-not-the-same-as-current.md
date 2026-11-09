---
title: as-of is not the same as current
date: '2026-11-09'
source: https://dev.to/shrouwoods/as-of-is-not-the-same-as-current-4m5h
domain: SQL
relevance: 🟡
tags:
- '#best-practice'
- '#sql'
- '#tool'
- '#tutorial'
related:
- '[[2026-06-10-sql-for-data-analysis-the-10-query-patterns-that-matter]]'
- '[[2026-08-31-how-to-reconcile-two-tables-in-sql-when-the-row-counts-match]]'
- '[[2026-07-02-dbt-snapshots-scd-2-without-writing-a-single-merge-statement]]'
- '[[2026-10-13-snowflake-sql-patterns-for-revenue-reporting]]'
- '[[2026-09-12-amazon-kinesis-deep-dive-data-streams-firehose-analytics]]'
- '[[2026-08-21-how-to-find-duplicate-rows-in-sql-and-decide-what-counts-as-one]]'
status: unread
---

> **TL;DR:** quick answer current means "what is true right now." as-of means "what was true at a specific timestamp or calendar date." if you filter to the current row when the business question is historical, you will ship wrong me…

## What’s new and why it matters
quick answer current means "what is true right now." as-of means "what was true at a specific timestamp or calendar date." if you filter to the current row when the business question is historical, you will ship wrong metrics that still pass compile and sometimes still pass naive row-count tests. fix the time question first, then pick one of three patterns: filter on a validity interval, pass an as-of parameter into the query, or pre-resolve the correct row in a cte before you join. who this is for audience: analysts, analytics engineers, and backend developers who build reports or models over…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Write the query in a scratchpad and run EXPLAIN/QUERY PLAN to verify performance.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/shrouwoods/as-of-is-not-the-same-as-current-4m5h

## Related notes
- [[2026-06-10-sql-for-data-analysis-the-10-query-patterns-that-matter]]
- [[2026-08-31-how-to-reconcile-two-tables-in-sql-when-the-row-counts-match]]
- [[2026-07-02-dbt-snapshots-scd-2-without-writing-a-single-merge-statement]]
- [[2026-10-13-snowflake-sql-patterns-for-revenue-reporting]]
- [[2026-09-12-amazon-kinesis-deep-dive-data-streams-firehose-analytics]]
- [[2026-08-21-how-to-find-duplicate-rows-in-sql-and-decide-what-counts-as-one]]
