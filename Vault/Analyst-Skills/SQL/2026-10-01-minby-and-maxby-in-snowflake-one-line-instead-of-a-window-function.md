---
title: 'MIN_BY and MAX_BY in Snowflake: One Line Instead of a Window Function'
date: '2026-10-01'
source: https://medium.com/@karthikrajashekaran/min-by-and-max-by-in-snowflake-one-line-instead-of-a-window-function-93fb96c5ba92?source=rss------sql-5
domain: SQL
relevance: 🟡
tags:
- '#sql'
related:
- '[[2026-06-15-window-functions-are-the-line-between-a-reporting-analyst-and-an-analytics-engineer]]'
- '[[2026-08-21-6-sql-window-function-tricks-that-replace-200-lines-of-application-code]]'
- '[[2026-06-04-parker-shamblin-java-backend-project-jdbc-oracle-sql-and-tomcat]]'
- '[[2026-07-16-row-level-security-rls-in-power-bi-secure-your-data-without-duplicating-reports]]'
- '[[2026-05-14-spark-iceberg-and-the-lineage-trap-why-our-250000-row-pipeline-took-80-minutes-to-plan]]'
- '[[2026-09-24-sql-window-functions-explained-rownumber-rank-denserank-lag-lead-in-mysql]]'
status: unread
---

> **TL;DR:** They replace the QUALIFY ROW_NUMBER() dance with a single call. They also hand back three different kinds of NULL and an arbitrary winner… Continue reading on Medium »

## What’s new and why it matters
They replace the QUALIFY ROW_NUMBER() dance with a single call. They also hand back three different kinds of NULL and an arbitrary winner… Continue reading on Medium »

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Write the query in a scratchpad and run EXPLAIN/QUERY PLAN to verify performance.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://medium.com/@karthikrajashekaran/min-by-and-max-by-in-snowflake-one-line-instead-of-a-window-function-93fb96c5ba92?source=rss------sql-5

## Related notes
- [[2026-06-15-window-functions-are-the-line-between-a-reporting-analyst-and-an-analytics-engineer]]
- [[2026-08-21-6-sql-window-function-tricks-that-replace-200-lines-of-application-code]]
- [[2026-06-04-parker-shamblin-java-backend-project-jdbc-oracle-sql-and-tomcat]]
- [[2026-07-16-row-level-security-rls-in-power-bi-secure-your-data-without-duplicating-reports]]
- [[2026-05-14-spark-iceberg-and-the-lineage-trap-why-our-250000-row-pipeline-took-80-minutes-to-plan]]
- [[2026-09-24-sql-window-functions-explained-rownumber-rank-denserank-lag-lead-in-mysql]]
