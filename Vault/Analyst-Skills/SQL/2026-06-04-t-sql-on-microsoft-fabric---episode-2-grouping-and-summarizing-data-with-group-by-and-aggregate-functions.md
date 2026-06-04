---
title: 'T-SQL on Microsoft Fabric - Episode 2: Grouping and Summarizing Data with
  GROUP BY and Aggregate Functions'
date: '2026-06-04'
source: https://dev.to/lamkhac/t-sql-on-microsoft-fabric-episode-2-grouping-and-summarizing-data-with-group-by-and-aggregate-4bjm
domain: SQL
relevance: 🟡
tags:
- '#ai'
- '#feature'
- '#sql'
- '#tableau'
- '#tool'
related:
- '[[2026-04-29-aggregations-counting-summing-and-averaging-your-data]]'
- '[[2026-02-22-5-most-asked-sql-interview-questions]]'
- '[[2026-06-02-t-sql-on-microsoft-fabric--episode-1-t-sql-basics-in-microsoft-fabric-warehouse-select-where-and-order-by]]'
- '[[2026-04-21-sql-window-functions-and-ctes]]'
- '[[2026-03-20-postgresqlaggregative-functions]]'
- '[[2026-05-22-group-by-and-having-in-sql-aggregation-patterns-for-interviews]]'
status: unread
---

> **TL;DR:** Learning Goals In this lesson, you will learn how to: Understand aggregate functions in T-SQL Use SUM() to calculate totals Use COUNT() to count rows and distinct values Use AVG() to calculate averages Use MIN() and MAX(…

## What’s new and why it matters
Learning Goals In this lesson, you will learn how to: Understand aggregate functions in T-SQL Use SUM() to calculate totals Use COUNT() to count rows and distinct values Use AVG() to calculate averages Use MIN() and MAX() to find the lowest and highest values Group data with GROUP BY Filter grouped results with HAVING These are some of the most frequently used SQL features in Data Warehouses, Power BI models, and Microsoft Fabric. 1. Prepare the Data Create the schema: CREATE SCHEMA sales ; Create the table: CREATE TABLE sales . Orders ( OrderID INT , CustomerID INT , ProductName VARCHAR ( 100…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Write the query in a scratchpad and run EXPLAIN/QUERY PLAN to verify performance.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/lamkhac/t-sql-on-microsoft-fabric-episode-2-grouping-and-summarizing-data-with-group-by-and-aggregate-4bjm

## Related notes
- [[2026-04-29-aggregations-counting-summing-and-averaging-your-data]]
- [[2026-02-22-5-most-asked-sql-interview-questions]]
- [[2026-06-02-t-sql-on-microsoft-fabric--episode-1-t-sql-basics-in-microsoft-fabric-warehouse-select-where-and-order-by]]
- [[2026-04-21-sql-window-functions-and-ctes]]
- [[2026-03-20-postgresqlaggregative-functions]]
- [[2026-05-22-group-by-and-having-in-sql-aggregation-patterns-for-interviews]]
