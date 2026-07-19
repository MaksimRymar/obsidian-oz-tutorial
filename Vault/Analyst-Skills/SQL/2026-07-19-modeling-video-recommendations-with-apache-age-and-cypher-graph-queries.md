---
title: Modeling Video Recommendations With Apache AGE and Cypher Graph Queries
date: '2026-07-19'
source: https://dev.to/ahmet_gedik778845/modeling-video-recommendations-with-apache-age-and-cypher-graph-queries-5516
domain: SQL
relevance: 🟡
tags:
- '#ai'
- '#best-practice'
- '#feature'
- '#library'
- '#python'
- '#sql'
- '#tool'
- '#zendesk'
related:
- '[[2026-04-21-sql-window-functions-and-ctes]]'
- '[[2026-06-24-building-graph-based-video-relationship-queries-with-apache-age]]'
- '[[2026-04-29-postgresql-subquery-and-cte-optimization]]'
- '[[2026-07-18-building-my-first-real-database-what-a-weekend-sql-assignment-taught-me-about-postgres-and-git]]'
- '[[2026-06-10-sql-for-data-analysis-the-10-query-patterns-that-matter]]'
- '[[2026-06-28-one-query-language-for-sql-mongo-and-the-browser-the-case-for-forge]]'
status: unread
---

> **TL;DR:** The recursive join that killed our recommendation endpoint Our "related videos" sidebar started as three lines of SQL. A video belongs to categories, shares tags with other videos, and appears in the same regional trend…

## What’s new and why it matters
The recursive join that killed our recommendation endpoint Our "related videos" sidebar started as three lines of SQL. A video belongs to categories, shares tags with other videos, and appears in the same regional trend windows. Rank by overlap, return the top eight. Fine. Then product asked for something that sounds simple and is not: "Show videos two hops away — things that co-trend with videos that co-trend with this one, but that the viewer has not already been recommended this week." That is a graph traversal wearing a relational costume. In SQLite it became a self-join stacked on a self-…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Write the query in a scratchpad and run EXPLAIN/QUERY PLAN to verify performance.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/ahmet_gedik778845/modeling-video-recommendations-with-apache-age-and-cypher-graph-queries-5516

## Related notes
- [[2026-04-21-sql-window-functions-and-ctes]]
- [[2026-06-24-building-graph-based-video-relationship-queries-with-apache-age]]
- [[2026-04-29-postgresql-subquery-and-cte-optimization]]
- [[2026-07-18-building-my-first-real-database-what-a-weekend-sql-assignment-taught-me-about-postgres-and-git]]
- [[2026-06-10-sql-for-data-analysis-the-10-query-patterns-that-matter]]
- [[2026-06-28-one-query-language-for-sql-mongo-and-the-browser-the-case-for-forge]]
