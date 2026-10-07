---
title: 'Custom Fresh v2.1.0: Take Control of Laravel Database Resets'
date: '2026-10-07'
source: https://dev.to/mmramadan496/custom-fresh-v210-take-control-of-laravel-database-resets-59n4
domain: AI-Tools
relevance: 🟡
tags:
- '#ai'
- '#library'
- '#tool'
related:
- '[[2026-08-22-bringing-relational-sql-databases-to-the-p2p-world]]'
- '[[2026-09-09-six-tables-out-of-260]]'
- '[[2026-07-28-why-schema-drift-goes-undetected]]'
- '[[2026-08-17-oracle-ora-02297-error-causes-and-solutions-complete-guide]]'
- '[[2026-08-29-jooq-codegen-from-flyway-migrations-with-no-database]]'
- '[[2026-06-08-running-real-sql-on-dynamodb-how-it-actually-works]]'
status: unread
---

> **TL;DR:** 🚀 Custom Fresh v2.1.0 is here! Laravel database resets are easy until your project has tables you need to keep. Reference data, imported records, configuration tables, and other data not managed by migrations can be lost…

## What’s new and why it matters
🚀 Custom Fresh v2.1.0 is here! Laravel database resets are easy until your project has tables you need to keep. Reference data, imported records, configuration tables, and other data not managed by migrations can be lost when using migrate:fresh . Custom Fresh gives you more control over what gets reset and what stays. Keep specific tables during database resets: php artisan db:fresh --keep = users ,settings Keep raw data without relying on migrations: php artisan db:fresh --keep-raw = locations Reset the data without rebuilding the schema: php artisan db:fresh --freeze-schema What’s new in v2…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Reproduce the example in a notebook; then refactor into a reusable function.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/mmramadan496/custom-fresh-v210-take-control-of-laravel-database-resets-59n4

## Related notes
- [[2026-08-22-bringing-relational-sql-databases-to-the-p2p-world]]
- [[2026-09-09-six-tables-out-of-260]]
- [[2026-07-28-why-schema-drift-goes-undetected]]
- [[2026-08-17-oracle-ora-02297-error-causes-and-solutions-complete-guide]]
- [[2026-08-29-jooq-codegen-from-flyway-migrations-with-no-database]]
- [[2026-06-08-running-real-sql-on-dynamodb-how-it-actually-works]]
