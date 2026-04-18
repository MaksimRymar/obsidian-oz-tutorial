---
title: Published a SQL Linter to PyPI Because I Was Tired of Bad Queries Hitting Production
date: '2026-04-18'
source: https://dev.to/pawan_singhkapkoti_ea8a0/published-a-sql-linter-to-pypi-because-i-was-tired-of-bad-queries-hitting-production-18o0
domain: SQL
relevance: 🟡
tags:
- '#ai'
- '#best-practice'
- '#feature'
- '#library'
- '#python'
- '#sql'
- '#tool'
related:
- '[[2026-03-03-sql-joins-window-functions-the-skills-that-separate-analysts-from-beginners]]'
- '[[2026-03-09-how-to-build-and-publish-a-python-package-to-pypi-with-a-real-project]]'
- '[[2026-03-26-finding-the-missing-indexes-your-queries-are-begging-for]]'
- '[[2026-03-13-test-your-ai-agent-like-a-senior-engineer-4-patterns-that-work]]'
- '[[2026-03-30-database-indexing-explained-whats-actually-happening-under-the-hood]]'
- '[[2026-03-21-postgresql-performance-10-queries-youre-writing-wrong-2026-edition]]'
status: unread
---

> **TL;DR:** Food manufacturing ERPs run on SQL Server. SSRS reports, stored procedures, ad-hoc queries — often written by people who learned SQL from Stack Overflow. A DELETE without WHERE against a staging table is a wake-up call.…

## What’s new and why it matters
Food manufacturing ERPs run on SQL Server. SSRS reports, stored procedures, ad-hoc queries — often written by people who learned SQL from Stack Overflow. A DELETE without WHERE against a staging table is a wake-up call. sql-sop catches these patterns before they reach the database. sql-sop: 18 rules, 55 tests, 0.08 seconds pip install sql-sop sql-sop check . That is it. Point it at a directory and it scans every .sql file in 0.08 seconds. No config file needed. No database connection. Just pattern matching against compiled regex and sqlparse AST analysis. The rules 5 errors (block commits): Ru…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Write the query in a scratchpad and run EXPLAIN/QUERY PLAN to verify performance.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/pawan_singhkapkoti_ea8a0/published-a-sql-linter-to-pypi-because-i-was-tired-of-bad-queries-hitting-production-18o0

## Related notes
- [[2026-03-03-sql-joins-window-functions-the-skills-that-separate-analysts-from-beginners]]
- [[2026-03-09-how-to-build-and-publish-a-python-package-to-pypi-with-a-real-project]]
- [[2026-03-26-finding-the-missing-indexes-your-queries-are-begging-for]]
- [[2026-03-13-test-your-ai-agent-like-a-senior-engineer-4-patterns-that-work]]
- [[2026-03-30-database-indexing-explained-whats-actually-happening-under-the-hood]]
- [[2026-03-21-postgresql-performance-10-queries-youre-writing-wrong-2026-edition]]
