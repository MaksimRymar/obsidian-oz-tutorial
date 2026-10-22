---
title: Convert Time Columns into Rows and Pivot into a New Cross Table
date: '2026-10-22'
source: https://dev.to/esproc_spl/convert-time-columns-into-rows-and-pivot-into-a-new-cross-table-3im2
domain: SQL
relevance: 🟡
tags:
- '#sql'
- '#tool'
related:
- '[[2026-09-15-sql-joins-explained]]'
- '[[2026-09-07-like-in-sql-explained-for-beginners]]'
- '[[2026-08-04-sqlazymerge-multiple-tables-into-single-rows-by-common-id]]'
- '[[2026-07-23-btree-height-after-delete-postgresql-fast-root]]'
- '[[2026-09-16-sql-joins-with-examples-of-each]]'
- '[[2026-10-15-the-list-shows-two-numbers-so-the-query-digs-them-out-of-the-json-instead-of-loading-a-hundred-attempts]]'
status: unread
---

> **TL;DR:** Problem Description The table tb can be seen as a cross table: the combination of the ID and PartNum fields forms the row header, the three field names EnteredOn, PickedTime and DeliveredTime form the column header, and…

## What’s new and why it matters
Problem Description The table tb can be seen as a cross table: the combination of the ID and PartNum fields forms the row header, the three field names EnteredOn, PickedTime and DeliveredTime form the column header, and the cells hold time points. Neither the content nor the number of the row headers is fixed. Now the table has to be turned around: the original cells (the time points) become the row header of the new table, the original row header (the combination of PartNum and ID) becomes the column header of the new table, and the original three column headers are replaced by the strings EN…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Write the query in a scratchpad and run EXPLAIN/QUERY PLAN to verify performance.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/esproc_spl/convert-time-columns-into-rows-and-pivot-into-a-new-cross-table-3im2

## Related notes
- [[2026-09-15-sql-joins-explained]]
- [[2026-09-07-like-in-sql-explained-for-beginners]]
- [[2026-08-04-sqlazymerge-multiple-tables-into-single-rows-by-common-id]]
- [[2026-07-23-btree-height-after-delete-postgresql-fast-root]]
- [[2026-09-16-sql-joins-with-examples-of-each]]
- [[2026-10-15-the-list-shows-two-numbers-so-the-query-digs-them-out-of-the-json-instead-of-loading-a-hundred-attempts]]
