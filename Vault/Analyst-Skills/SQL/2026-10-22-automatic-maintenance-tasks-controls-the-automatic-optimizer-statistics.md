---
title: Automatic maintenance tasks controls the automatic optimizer statistics
date: '2026-10-22'
source: https://dev.to/dbcasefiles/automatic-maintenance-tasks-controls-the-automatic-optimizer-statistics-31ja
domain: SQL
relevance: 🟡
tags:
- '#sql'
- '#tool'
related:
- '[[2026-10-19-joins-window-functions-ctes-and-subqueries]]'
- '[[2026-08-12-sql-foundations-start-to-finish]]'
- '[[2026-08-30-dataform-for-bigquery-google-native-transformation-assertions-cicd]]'
- '[[2026-10-17-joins-in-sql]]'
- '[[2026-08-29-i-broke-production-with-a-plsql-loop-here-are-the-10-steps-i-skipped]]'
- '[[2026-08-21-how-to-find-duplicate-rows-in-sql-and-decide-what-counts-as-one]]'
status: unread
---

> **TL;DR:** Query to check the current state of jobs in CDB_AUTOTASK_CLIENT of the database, auto optimizer stats collection job is disabled in PDBs. SELECT COALESCE ( p . name , ( SELECT name FROM v $ database )) AS DATABASE , CASE…

## What’s new and why it matters
Query to check the current state of jobs in CDB_AUTOTASK_CLIENT of the database, auto optimizer stats collection job is disabled in PDBs. SELECT COALESCE ( p . name , ( SELECT name FROM v $ database )) AS DATABASE , CASE WHEN c . con_id = 1 THEN 'CDB' WHEN c . con_id = 2 THEN 'SEED' ELSE 'PDB' END AS type_db , c . client_name , c . status , c . attributes FROM cdb_autotask_client c LEFT JOIN v $ pdbs p ON c . con_id = p . con_id ORDER BY type_db , client_name ; DATABASE TYPE_DB CLIENT_NAME STATUS ATTRIBUTES _______________ __________ __________________________________ __________ ______________…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Write the query in a scratchpad and run EXPLAIN/QUERY PLAN to verify performance.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/dbcasefiles/automatic-maintenance-tasks-controls-the-automatic-optimizer-statistics-31ja

## Related notes
- [[2026-10-19-joins-window-functions-ctes-and-subqueries]]
- [[2026-08-12-sql-foundations-start-to-finish]]
- [[2026-08-30-dataform-for-bigquery-google-native-transformation-assertions-cicd]]
- [[2026-10-17-joins-in-sql]]
- [[2026-08-29-i-broke-production-with-a-plsql-loop-here-are-the-10-steps-i-skipped]]
- [[2026-08-21-how-to-find-duplicate-rows-in-sql-and-decide-what-counts-as-one]]
