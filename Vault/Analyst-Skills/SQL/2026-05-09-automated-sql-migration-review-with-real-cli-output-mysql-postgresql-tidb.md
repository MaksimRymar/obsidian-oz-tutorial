---
title: Automated SQL Migration Review with Real CLI Output (MySQL, PostgreSQL, TiDB)
date: '2026-05-09'
source: https://dev.to/fanduzi/automated-sql-migration-review-with-real-cli-output-mysql-postgresql-tidb-17b5
domain: SQL
relevance: 🟡
tags:
- '#ai'
- '#best-practice'
- '#sql'
- '#tool'
- '#zendesk'
related:
- '[[2026-03-30-database-indexing-explained-whats-actually-happening-under-the-hood]]'
- '[[2026-05-03-claudemd-for-postgresql-13-rules-that-make-ai-write-safe-production-ready-sql]]'
- '[[2026-03-15-data-quality-testing-how-bruin-and-dbt-take-different-paths-to-the-same-goal]]'
- '[[2026-03-05-learning-sql-join-and-window-functions]]'
- '[[2026-03-26-alter-table]]'
- '[[2026-03-29-alter-tables]]'
status: unread
---

> **TL;DR:** Auditing MySQL ALTER TABLE Risks with a CLI (Real Output Included) Background I'm the author of DeltaScope , an open-source offline SQL audit tool that supports MySQL, TiDB, and PostgreSQL. This post skips the marketing…

## What’s new and why it matters
Auditing MySQL ALTER TABLE Risks with a CLI (Real Output Included) Background I'm the author of DeltaScope , an open-source offline SQL audit tool that supports MySQL, TiDB, and PostgreSQL. This post skips the marketing and shows real SQL inputs with real audit outputs — no fabrications. Scenario 1: An Innocent-Looking Migration File Consider a migration file migration.sql : -- Add columns and index to users table ALTER TABLE users ADD COLUMN phone VARCHAR ( 20 ); ALTER TABLE users ADD COLUMN age INT DEFAULT 0 ; ALTER TABLE users ADD INDEX idx_phone ( phone ); -- Clean up temp data DELETE FROM…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Write the query in a scratchpad and run EXPLAIN/QUERY PLAN to verify performance.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/fanduzi/automated-sql-migration-review-with-real-cli-output-mysql-postgresql-tidb-17b5

## Related notes
- [[2026-03-30-database-indexing-explained-whats-actually-happening-under-the-hood]]
- [[2026-05-03-claudemd-for-postgresql-13-rules-that-make-ai-write-safe-production-ready-sql]]
- [[2026-03-15-data-quality-testing-how-bruin-and-dbt-take-different-paths-to-the-same-goal]]
- [[2026-03-05-learning-sql-join-and-window-functions]]
- [[2026-03-26-alter-table]]
- [[2026-03-29-alter-tables]]
