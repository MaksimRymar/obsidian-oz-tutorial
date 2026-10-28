---
title: ROW VS PAGE VS COLUMNSTORE VS ARHIVE DATA COMPRESSION on SQLServer
date: '2026-10-27'
source: https://dev.to/abeamar/row-vs-page-vs-columnstore-vs-arhive-data-compression-on-sqlserver-1nlo
domain: SQL
relevance: 🟡
tags:
- '#ai'
- '#sql'
- '#support-analytics'
- '#tool'
related:
- '[[2026-03-03-sql-joins-window-functions-the-skills-that-separate-analysts-from-beginners]]'
- '[[2026-06-10-sql-for-data-analysis-the-10-query-patterns-that-matter]]'
- '[[2026-06-12-indexes-quickstart-using-postgresql-15-sec-read]]'
- '[[2026-08-21-how-to-find-duplicate-rows-in-sql-and-decide-what-counts-as-one]]'
- '[[2026-04-11-master-mysql-views-and-window-functions-advanced-query-optimization-guide]]'
- '[[2026-08-31-running-total-in-sql-the-window-frame-that-decides-the-answer]]'
status: unread
---

> **TL;DR:** Storage and the size of your database can become a real danger if you don't actively monitor your table sizes, archive old data, and implement compression. Left unchecked, a table won't just eat up your disk space it wil…

## What’s new and why it matters
Storage and the size of your database can become a real danger if you don't actively monitor your table sizes, archive old data, and implement compression. Left unchecked, a table won't just eat up your disk space it will choke your backups, impact buffer pool, drag down query speeds. Moving from lowest to highest storage savings, you can start from ROW compression for active OLTP tables, to PAGE compression for read heavy tables, to COLUMNSTORE for data Warehouses, and finally to COLUMNSTORE ARCHIVE for rarely accessed data. Keep in mind that savings vary heavily by table structure, uniform v…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Write the query in a scratchpad and run EXPLAIN/QUERY PLAN to verify performance.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/abeamar/row-vs-page-vs-columnstore-vs-arhive-data-compression-on-sqlserver-1nlo

## Related notes
- [[2026-03-03-sql-joins-window-functions-the-skills-that-separate-analysts-from-beginners]]
- [[2026-06-10-sql-for-data-analysis-the-10-query-patterns-that-matter]]
- [[2026-06-12-indexes-quickstart-using-postgresql-15-sec-read]]
- [[2026-08-21-how-to-find-duplicate-rows-in-sql-and-decide-what-counts-as-one]]
- [[2026-04-11-master-mysql-views-and-window-functions-advanced-query-optimization-guide]]
- [[2026-08-31-running-total-in-sql-the-window-frame-that-decides-the-answer]]
