---
title: 'Open-source tool: Cross-database universal "field-level" data lineage analysis
  and visualization (Part 2 of 3)'
date: '2026-09-17'
source: https://dev.to/zgl20053779/open-source-tool-cross-database-universal-field-level-data-lineage-analysis-and-visualization-1jle
domain: SQL
relevance: 🟡
tags:
- '#python'
- '#sql'
- '#tool'
- '#zendesk'
related:
- '[[2026-07-21-from-tables-to-insights-a-beginners-journey-into-sql]]'
- '[[2026-09-16-sql-joins-with-examples-of-each]]'
- '[[2026-06-10-sql-for-data-analysis-the-10-query-patterns-that-matter]]'
- '[[2026-09-15-sql-joins-explained]]'
- '[[2026-03-15-sql-for-generating-test-data-in-mysql]]'
- '[[2026-03-02-designing-efficient-queries-with-sql-joins-and-window-functions]]'
status: unread
---

> **TL;DR:** This article is Part 2. In the previous step, we obtained "primary lineage annotation information". In this step, we will obtain complete field-level lineage data and save it into three tables in the MYSQL database. The…

## What’s new and why it matters
This article is Part 2. In the previous step, we obtained "primary lineage annotation information". In this step, we will obtain complete field-level lineage data and save it into three tables in the MYSQL database. The names and functions of these three tables are as follows: sql_table_struct_info : Save table structure information for tables, views, and functions (possibly) sql_table2table_info : Save the relationships between tables in the script, such as target table, source table, table alias, table association method, association filtering conditions, and other related information sql_ta…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Write the query in a scratchpad and run EXPLAIN/QUERY PLAN to verify performance.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/zgl20053779/open-source-tool-cross-database-universal-field-level-data-lineage-analysis-and-visualization-1jle

## Related notes
- [[2026-07-21-from-tables-to-insights-a-beginners-journey-into-sql]]
- [[2026-09-16-sql-joins-with-examples-of-each]]
- [[2026-06-10-sql-for-data-analysis-the-10-query-patterns-that-matter]]
- [[2026-09-15-sql-joins-explained]]
- [[2026-03-15-sql-for-generating-test-data-in-mysql]]
- [[2026-03-02-designing-efficient-queries-with-sql-joins-and-window-functions]]
