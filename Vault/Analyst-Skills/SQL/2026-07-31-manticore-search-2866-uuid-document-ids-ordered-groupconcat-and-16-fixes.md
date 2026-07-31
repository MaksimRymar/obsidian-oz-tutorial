---
title: 'Manticore Search 28.6.6: UUID document IDs, ordered GROUP_CONCAT(), and 16
  fixes'
date: '2026-07-31'
source: https://dev.to/sanikolaev/manticore-search-2866-uuid-document-ids-ordered-groupconcat-and-16-fixes-12ch
domain: SQL
relevance: 🔴
tags:
- '#feature'
- '#library'
- '#sql'
- '#support-analytics'
- '#tool'
- '#tutorial'
related:
- '[[2026-04-22-sql-set-operators-union-intersect-and-except-explained-simply]]'
- '[[2026-05-18-top-orm-tools-practical-comparison]]'
- '[[2026-03-03-sql-joins-window-functions-the-skills-that-separate-analysts-from-beginners]]'
- '[[2026-06-10-sql-for-data-analysis-the-10-query-patterns-that-matter]]'
- '[[2026-03-14-demystifying-sql-joins-window-functions]]'
- '[[2026-04-09-postgresql-foreign-data-wrappers-cross-database-queries-explained]]'
status: unread
---

> **TL;DR:** Manticore Search 28.6.6 has been released. The headline additions are UUID document IDs for real-time tables and ordered, limited GROUP_CONCAT() for grouped queries. The release also includes 16 fixes for backups, replic…

## What’s new and why it matters
Manticore Search 28.6.6 has been released. The headline additions are UUID document IDs for real-time tables and ordered, limited GROUP_CONCAT() for grouped queries. The release also includes 16 fixes for backups, replication, query processing, SQL compatibility, and secondary indexes. This post covers everything shipped from 28.4.5 through 28.6.6 . Upgrade notes There are no new mandatory data migrations in this release. UUID IDs are an opt-in table definition: existing numeric-ID tables keep working as they are. If you want UUID identifiers, create a real-time table with id uuid ; ALTER TABL…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Write the query in a scratchpad and run EXPLAIN/QUERY PLAN to verify performance.
- Add a short note: what changed in your workflow?

## Relevance
🔴

## Source
https://dev.to/sanikolaev/manticore-search-2866-uuid-document-ids-ordered-groupconcat-and-16-fixes-12ch

## Related notes
- [[2026-04-22-sql-set-operators-union-intersect-and-except-explained-simply]]
- [[2026-05-18-top-orm-tools-practical-comparison]]
- [[2026-03-03-sql-joins-window-functions-the-skills-that-separate-analysts-from-beginners]]
- [[2026-06-10-sql-for-data-analysis-the-10-query-patterns-that-matter]]
- [[2026-03-14-demystifying-sql-joins-window-functions]]
- [[2026-04-09-postgresql-foreign-data-wrappers-cross-database-queries-explained]]
