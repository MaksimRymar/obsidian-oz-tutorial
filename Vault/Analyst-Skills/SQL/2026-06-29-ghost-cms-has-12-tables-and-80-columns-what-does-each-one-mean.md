---
title: Ghost CMS has 12 tables and 80+ columns. What does each one mean?
date: '2026-06-29'
source: https://dev.to/kekekuki/ghost-cms-has-12-tables-and-80-columns-what-does-each-one-mean-m2m
domain: SQL
relevance: 🔴
tags:
- '#feature'
- '#library'
- '#sql'
- '#support-analytics'
- '#tool'
related:
- '[[2026-03-14-schema-risk]]'
- '[[2026-06-10-sql-for-data-analysis-the-10-query-patterns-that-matter]]'
- '[[2026-05-19-in-some-scenarios-relying-on-llms-to-generate-sql-is-neither-rigorous-nor-reliableright-way-to-teach-llms-to-generate-sq]]'
- '[[2026-04-23-i-built-a-browser-only-sql-practice-tool-because-installing-dbeaver-is-a-productivity-tax]]'
- '[[2026-02-28-ai-data-analysis-tools-i-actually-use-daily]]'
- '[[2026-05-03-claudemd-for-postgresql-13-rules-that-make-ai-write-safe-production-ready-sql]]'
status: unread
---

> **TL;DR:** Ghost is one of the most popular open-source blogging platforms — 30K+ GitHub stars, powering millions of blogs. Its database has evolved over 10 years. From posts and users in 2015 to v6.0's big cleanup in 2025: 8 migra…

## What’s new and why it matters
Ghost is one of the most popular open-source blogging platforms — 30K+ GitHub stars, powering millions of blogs. Its database has evolved over 10 years. From posts and users in 2015 to v6.0's big cleanup in 2025: 8 migrations, 12 tables, 80+ columns, plus Stripe payments, email tracking, and a membership system. The SQL migration files are all there in migrations/ . But not a single comment explains what any field actually means. Can you answer these questions? Here's a migration from Ghost's codebase: ALTER TABLE posts DROP COLUMN created_by ; ALTER TABLE posts DROP COLUMN updated_by ; ALTER…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Write the query in a scratchpad and run EXPLAIN/QUERY PLAN to verify performance.
- Add a short note: what changed in your workflow?

## Relevance
🔴

## Source
https://dev.to/kekekuki/ghost-cms-has-12-tables-and-80-columns-what-does-each-one-mean-m2m

## Related notes
- [[2026-03-14-schema-risk]]
- [[2026-06-10-sql-for-data-analysis-the-10-query-patterns-that-matter]]
- [[2026-05-19-in-some-scenarios-relying-on-llms-to-generate-sql-is-neither-rigorous-nor-reliableright-way-to-teach-llms-to-generate-sq]]
- [[2026-04-23-i-built-a-browser-only-sql-practice-tool-because-installing-dbeaver-is-a-productivity-tax]]
- [[2026-02-28-ai-data-analysis-tools-i-actually-use-daily]]
- [[2026-05-03-claudemd-for-postgresql-13-rules-that-make-ai-write-safe-production-ready-sql]]
