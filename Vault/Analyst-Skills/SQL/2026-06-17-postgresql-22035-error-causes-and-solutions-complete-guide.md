---
title: 'PostgreSQL 22035 Error: Causes and Solutions Complete Guide'
date: '2026-06-17'
source: https://dev.to/dbmserror/postgresql-22035-error-causes-and-solutions-complete-guide-26pg
domain: SQL
relevance: 🟡
tags:
- '#sql'
- '#tool'
- '#tutorial'
related:
- '[[2026-06-15-oracle-ora-00904-error-causes-and-solutions-complete-guide]]'
- '[[2026-06-12-postgresql-2200h-error-causes-and-solutions-complete-guide]]'
- '[[2026-06-17-postgresql-22032-error-causes-and-solutions-complete-guide]]'
- '[[2026-06-04-postgresql-2202e-error-causes-and-solutions-complete-guide]]'
- '[[2026-06-16-oracle-ora-00909-error-causes-and-solutions-complete-guide]]'
- '[[2026-06-16-oracle-ora-00913-error-causes-and-solutions-complete-guide]]'
status: unread
---

> **TL;DR:** PostgreSQL Error 22035: no_sql_json_item PostgreSQL error code 22035 ( no_sql_json_item ) occurs when a SQL/JSON path expression fails to find a matching item within the target JSON document. This typically happens when…

## What’s new and why it matters
PostgreSQL Error 22035: no_sql_json_item PostgreSQL error code 22035 ( no_sql_json_item ) occurs when a SQL/JSON path expression fails to find a matching item within the target JSON document. This typically happens when using JSON path functions like jsonb_path_value() or jsonb_path_query() with a path that doesn't exist in the given JSON data. It is most commonly triggered in strict mode or when mandatory single-value returns are expected. Top 3 Causes 1. Accessing a Non-Existent JSON Key Referencing a key or nested path that simply does not exist in the JSON document is the most frequent cau…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Write the query in a scratchpad and run EXPLAIN/QUERY PLAN to verify performance.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/dbmserror/postgresql-22035-error-causes-and-solutions-complete-guide-26pg

## Related notes
- [[2026-06-15-oracle-ora-00904-error-causes-and-solutions-complete-guide]]
- [[2026-06-12-postgresql-2200h-error-causes-and-solutions-complete-guide]]
- [[2026-06-17-postgresql-22032-error-causes-and-solutions-complete-guide]]
- [[2026-06-04-postgresql-2202e-error-causes-and-solutions-complete-guide]]
- [[2026-06-16-oracle-ora-00909-error-causes-and-solutions-complete-guide]]
- [[2026-06-16-oracle-ora-00913-error-causes-and-solutions-complete-guide]]
