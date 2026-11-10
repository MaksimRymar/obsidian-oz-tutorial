---
title: Why SQL UNIQUE Constraints Allow Duplicate NULLs
date: '2026-11-10'
source: https://dev.to/doogal/why-sql-unique-constraints-allow-duplicate-nulls-56n
domain: SQL
relevance: 🟡
tags:
- '#ai'
- '#library'
- '#sql'
- '#tool'
- '#zendesk'
related:
- '[[2026-08-21-null-in-sql-why-null-finds-nothing-and-what-to-write-instead]]'
- '[[2026-10-05-sqljam-move-tables-across-databases-with-schema-data-and-all]]'
- '[[2026-10-27-sql-not-in-vs-not-exists-handling-null-values-safely]]'
- '[[2026-07-02-dont-use-not-in]]'
- '[[2026-08-21-how-to-find-duplicate-rows-in-sql-and-decide-what-counts-as-one]]'
- '[[2026-06-21-postgresql-23502-error-causes-and-solutions-complete-guide]]'
status: unread
---

> **TL;DR:** Quick Answer: In SQL, unique constraints permit multiple NULL values because NULL represents an unknown state rather than an empty value, meaning two NULLs are never equal ( NULL = NULL evaluates to UNKNOWN ). While this…

## What’s new and why it matters
Quick Answer: In SQL, unique constraints permit multiple NULL values because NULL represents an unknown state rather than an empty value, meaning two NULLs are never equal ( NULL = NULL evaluates to UNKNOWN ). While this prevents unintended collisions on optional single columns, it silently compromises composite keys unless you explicitly configure your index with NULLS NOT DISTINCT . Imagine running a migration to enforce strict uniqueness on a database column, only to look at your production data a week later and find twenty rows that appear identical. Your initial instinct might be to suspe…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Write the query in a scratchpad and run EXPLAIN/QUERY PLAN to verify performance.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/doogal/why-sql-unique-constraints-allow-duplicate-nulls-56n

## Related notes
- [[2026-08-21-null-in-sql-why-null-finds-nothing-and-what-to-write-instead]]
- [[2026-10-05-sqljam-move-tables-across-databases-with-schema-data-and-all]]
- [[2026-10-27-sql-not-in-vs-not-exists-handling-null-values-safely]]
- [[2026-07-02-dont-use-not-in]]
- [[2026-08-21-how-to-find-duplicate-rows-in-sql-and-decide-what-counts-as-one]]
- [[2026-06-21-postgresql-23502-error-causes-and-solutions-complete-guide]]
