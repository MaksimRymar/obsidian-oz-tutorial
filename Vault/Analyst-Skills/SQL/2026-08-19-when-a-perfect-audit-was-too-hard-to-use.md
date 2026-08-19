---
title: When a perfect audit was too hard to use
date: '2026-08-19'
source: https://dev.to/islamov/when-a-perfect-audit-was-too-hard-to-use-hjb
domain: SQL
relevance: 🔴
tags:
- '#ai'
- '#feature'
- '#sql'
- '#support-analytics'
- '#tool'
related:
- '[[2026-04-23-i-built-a-browser-only-sql-practice-tool-because-installing-dbeaver-is-a-productivity-tax]]'
- '[[2026-07-24-ai-generated-sql-has-a-silent-failure-problem-heres-a-way-to-catch-it]]'
- '[[2026-07-06-your-postgres-already-knows-why-its-slow-you-just-have-to-ask-it]]'
- '[[2026-07-23-btree-height-after-delete-postgresql-fast-root]]'
- '[[2026-06-15-day-01-of-learning-data-engineering-step1-sql-joins-and-set-operators]]'
- '[[2026-03-30-your-sql-client-is-a-relic-heres-what-a-duckdb-native-ide-looks-like]]'
status: unread
---

> **TL;DR:** There are tasks in the database world that engineers genuinely enjoy: query optimization, petabyte-scale sharding, or designing highly available clusters. And then there are tasks you do because you must — security audit…

## What’s new and why it matters
There are tasks in the database world that engineers genuinely enjoy: query optimization, petabyte-scale sharding, or designing highly available clusters. And then there are tasks you do because you must — security auditing is one of them. This article tells the story of how the PostgreSQL audit extension pg_proaudit was redesigned: from a technically brilliant but barely usable tool into something administrators actually want to use. The story is told by Mikhail Gribkov, senior developer at Postgres Professional. If you’ve ever worked with security teams, this scenario will feel familiar. The…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Write the query in a scratchpad and run EXPLAIN/QUERY PLAN to verify performance.
- Add a short note: what changed in your workflow?

## Relevance
🔴

## Source
https://dev.to/islamov/when-a-perfect-audit-was-too-hard-to-use-hjb

## Related notes
- [[2026-04-23-i-built-a-browser-only-sql-practice-tool-because-installing-dbeaver-is-a-productivity-tax]]
- [[2026-07-24-ai-generated-sql-has-a-silent-failure-problem-heres-a-way-to-catch-it]]
- [[2026-07-06-your-postgres-already-knows-why-its-slow-you-just-have-to-ask-it]]
- [[2026-07-23-btree-height-after-delete-postgresql-fast-root]]
- [[2026-06-15-day-01-of-learning-data-engineering-step1-sql-joins-and-set-operators]]
- [[2026-03-30-your-sql-client-is-a-relic-heres-what-a-duckdb-native-ide-looks-like]]
