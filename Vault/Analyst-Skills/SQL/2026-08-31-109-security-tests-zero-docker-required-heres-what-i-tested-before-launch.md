---
title: 109 Security Tests, Zero Docker Required. Here's What I Tested Before Launch.
date: '2026-08-31'
source: https://dev.to/eu_ti_f127c5b5d7535b7174f/109-security-tests-zero-docker-required-heres-what-i-tested-before-launch-3abg
domain: SQL
relevance: 🔴
tags:
- '#ai'
- '#best-practice'
- '#feature'
- '#python'
- '#sql'
- '#support-analytics'
- '#tool'
- '#tutorial'
related:
- '[[2026-05-03-i-built-a-sast-scanner-from-scratch-heres-every-design-decision-i-made]]'
- '[[2026-05-20-learning-sql-as-if-you-built-it-yourself]]'
- '[[2026-08-21-how-to-find-duplicate-rows-in-sql-and-decide-what-counts-as-one]]'
- '[[2026-06-08-running-real-sql-on-dynamodb-how-it-actually-works]]'
- '[[2026-03-26-sqlite-is-enough-for-your-side-project-full-text-search-json-and-wal-mode-included]]'
- '[[2026-04-23-i-built-a-browser-only-sql-practice-tool-because-installing-dbeaver-is-a-productivity-tax]]'
status: unread
---

> **TL;DR:** Before deploying Datanika to production, I wrote 109 security tests across 10 test files. They all run in the existing SQLite test suite — no Docker, no external services, no security-specific infrastructure. What I Test…

## What’s new and why it matters
Before deploying Datanika to production, I wrote 109 security tests across 10 test files. They all run in the existing SQLite test suite — no Docker, no external services, no security-specific infrastructure. What I Tested I organized the tests by threat category, roughly following OWASP's top 10 but focused on the attack surface that actually matters for a data platform handling credentials: Category Tests What it covers SQL injection 11 Malicious names, config values, dbt model names — every user-supplied string that touches a query Path traversal 8 Escaping dbt project directories, upload d…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Write the query in a scratchpad and run EXPLAIN/QUERY PLAN to verify performance.
- Add a short note: what changed in your workflow?

## Relevance
🔴

## Source
https://dev.to/eu_ti_f127c5b5d7535b7174f/109-security-tests-zero-docker-required-heres-what-i-tested-before-launch-3abg

## Related notes
- [[2026-05-03-i-built-a-sast-scanner-from-scratch-heres-every-design-decision-i-made]]
- [[2026-05-20-learning-sql-as-if-you-built-it-yourself]]
- [[2026-08-21-how-to-find-duplicate-rows-in-sql-and-decide-what-counts-as-one]]
- [[2026-06-08-running-real-sql-on-dynamodb-how-it-actually-works]]
- [[2026-03-26-sqlite-is-enough-for-your-side-project-full-text-search-json-and-wal-mode-included]]
- [[2026-04-23-i-built-a-browser-only-sql-practice-tool-because-installing-dbeaver-is-a-productivity-tax]]
