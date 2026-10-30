---
title: I changed the rows. PostgreSQL's statistics still remembered them.
date: '2026-10-30'
source: https://dev.to/panditshivam/i-changed-the-rows-postgresqls-statistics-still-remembered-them-4k38
domain: SQL
relevance: 🔴
tags:
- '#ai'
- '#feature'
- '#sql'
- '#tool'
- '#zendesk'
related:
- '[[2026-09-30-a-stored-procedure-can-compile-and-still-change-its-meaning]]'
- '[[2026-08-12-sql-ctes-how-to-build-a-query-in-steps-you-can-check]]'
- '[[2026-08-21-null-in-sql-why-null-finds-nothing-and-what-to-write-instead]]'
- '[[2026-10-30-count-accepted-jobs-not-successful-api-calls-when-comparing-ai-workflows]]'
- '[[2026-09-17-no-introspection-no-allowlist-reconstructing-whatnots-graphql-queries-from-a-compiled-ast]]'
- '[[2026-08-21-how-to-find-duplicate-rows-in-sql-and-decide-what-counts-as-one]]'
status: unread
---

> **TL;DR:** The table had zero canary rows. Its planner statistics still named the canary. That is the result of a small PostgreSQL test I built after reading the Anonymizer 3.3 security release. The release describes several fixes,…

## What’s new and why it matters
The table had zero canary rows. Its planner statistics still named the canary. That is the result of a small PostgreSQL test I built after reading the Anonymizer 3.3 security release. The release describes several fixes, including an issue involving authentic values left in statistics after static masking.[1] I wanted to make the underlying metadata surface visible without pretending to reproduce the extension's vulnerability. So I used plain PostgreSQL 16.11, a disposable cluster and 100 synthetic rows. No extension. No real personal data. Just a deliberately memorable string: SYNTHETIC_CANAR…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Write the query in a scratchpad and run EXPLAIN/QUERY PLAN to verify performance.
- Add a short note: what changed in your workflow?

## Relevance
🔴

## Source
https://dev.to/panditshivam/i-changed-the-rows-postgresqls-statistics-still-remembered-them-4k38

## Related notes
- [[2026-09-30-a-stored-procedure-can-compile-and-still-change-its-meaning]]
- [[2026-08-12-sql-ctes-how-to-build-a-query-in-steps-you-can-check]]
- [[2026-08-21-null-in-sql-why-null-finds-nothing-and-what-to-write-instead]]
- [[2026-10-30-count-accepted-jobs-not-successful-api-calls-when-comparing-ai-workflows]]
- [[2026-09-17-no-introspection-no-allowlist-reconstructing-whatnots-graphql-queries-from-a-compiled-ast]]
- [[2026-08-21-how-to-find-duplicate-rows-in-sql-and-decide-what-counts-as-one]]
