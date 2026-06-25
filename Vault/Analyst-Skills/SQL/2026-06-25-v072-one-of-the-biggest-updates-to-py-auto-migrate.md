---
title: 'v0.7.2: One of the biggest updates to py-auto-migrate'
date: '2026-06-25'
source: https://dev.to/kasrakhaksar/v072-one-of-the-biggest-updates-to-py-auto-migrate-clo
domain: SQL
relevance: 🔴
tags:
- '#feature'
- '#library'
- '#sql'
related:
- '[[2026-06-24-semantic-search-with-postgresql-pragmatism-beats-hype---most-of-the-time]]'
- '[[2026-06-18-introducing-py-auto-migrate-database-migration-made-simple]]'
- '[[2026-03-05-learning-sql-join-and-window-functions]]'
- '[[2026-03-03-sql-joins-window-functions-the-skills-that-separate-analysts-from-beginners]]'
- '[[2026-04-17-essential-concepts-in-sql]]'
- '[[2026-06-15-how-to-choose-the-right-sql-database-for-your-project]]'
status: unread
---

> **TL;DR:** py-auto-migrate has added a new feature: --dep You can use the --dep option during migration to migrate tables that have foreign keys in the source table to the target database. Example : py-auto-migrate migrate \ --sour…

## What’s new and why it matters
py-auto-migrate has added a new feature: --dep You can use the --dep option during migration to migrate tables that have foreign keys in the source table to the target database. Example : py-auto-migrate migrate \ --source "postgresql://user:pass@localhost:5432/mydb" \ --target "mongodb://user:pass@localhost:27017/mydb" \ --table orders \ --dep This feature has been added to the py-auto-migrate package since version v0.7.2 and you can use it. In addition, the source database must be a relational database. Project links : GitHub PyPI

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Write the query in a scratchpad and run EXPLAIN/QUERY PLAN to verify performance.
- Add a short note: what changed in your workflow?

## Relevance
🔴

## Source
https://dev.to/kasrakhaksar/v072-one-of-the-biggest-updates-to-py-auto-migrate-clo

## Related notes
- [[2026-06-24-semantic-search-with-postgresql-pragmatism-beats-hype---most-of-the-time]]
- [[2026-06-18-introducing-py-auto-migrate-database-migration-made-simple]]
- [[2026-03-05-learning-sql-join-and-window-functions]]
- [[2026-03-03-sql-joins-window-functions-the-skills-that-separate-analysts-from-beginners]]
- [[2026-04-17-essential-concepts-in-sql]]
- [[2026-06-15-how-to-choose-the-right-sql-database-for-your-project]]
