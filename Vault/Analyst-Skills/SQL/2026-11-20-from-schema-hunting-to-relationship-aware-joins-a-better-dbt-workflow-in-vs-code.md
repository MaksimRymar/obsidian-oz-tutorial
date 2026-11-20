---
title: 'From Schema Hunting to Relationship-Aware JOINs: A Better dbt Workflow in
  VS Code'
date: '2026-11-20'
source: https://dev.to/arisyn/from-schema-hunting-to-relationship-aware-joins-a-better-dbt-workflow-in-vs-code-2po7
domain: SQL
relevance: 🟡
tags:
- '#ai'
- '#sql'
- '#support-analytics'
- '#tool'
- '#zendesk'
related:
- '[[2026-11-16-how-intalink-for-dbt-understands-joins-relationship-discovery-lineage-inheritance-and-fanout-detection]]'
- '[[2026-09-09-sql-joins]]'
- '[[2026-09-16-sql-joins-with-examples-of-each]]'
- '[[2026-04-19-sql-joins-explained-simply---a-beginners-guide]]'
- '[[2026-09-29-sql-joins-how-to-combine-tables-the-right-way]]'
- '[[2026-09-09-when-one-query-isnt-enough-a-love-letter-to-ctes-and-subqueries-in-postgresql]]'
status: unread
---

> **TL;DR:** How to discover related tables, suggest JOIN conditions, and inspect relationship evidence without constantly leaving your SQL editor. Writing a JOIN in SQL is easy. Finding the right JOIN in an unfamiliar database is a…

## What’s new and why it matters
How to discover related tables, suggest JOIN conditions, and inspect relationship evidence without constantly leaving your SQL editor. Writing a JOIN in SQL is easy. Finding the right JOIN in an unfamiliar database is a different story. If you work with dbt, you've probably spent time searching through schemas, inspecting column names, tracing existing models, or asking colleagues how two tables are connected. This becomes particularly frustrating when: Foreign keys are missing or incomplete. Different systems use inconsistent column names. Several tables contain similar identifiers. Relations…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Write the query in a scratchpad and run EXPLAIN/QUERY PLAN to verify performance.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/arisyn/from-schema-hunting-to-relationship-aware-joins-a-better-dbt-workflow-in-vs-code-2po7

## Related notes
- [[2026-11-16-how-intalink-for-dbt-understands-joins-relationship-discovery-lineage-inheritance-and-fanout-detection]]
- [[2026-09-09-sql-joins]]
- [[2026-09-16-sql-joins-with-examples-of-each]]
- [[2026-04-19-sql-joins-explained-simply---a-beginners-guide]]
- [[2026-09-29-sql-joins-how-to-combine-tables-the-right-way]]
- [[2026-09-09-when-one-query-isnt-enough-a-love-letter-to-ctes-and-subqueries-in-postgresql]]
