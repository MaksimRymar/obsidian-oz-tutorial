---
title: Your text-to-SQL accuracy is measured on schemas your users will never build
date: '2026-08-06'
source: https://dev.to/omer_hochman/your-text-to-sql-accuracy-is-measured-on-schemas-your-users-will-never-build-32b2
domain: AI-Tools
relevance: 🟡
tags:
- '#ai'
- '#feature'
- '#sql'
- '#tool'
- '#zendesk'
related:
- '[[2026-06-28-how-to-generate-a-sql-schema-from-a-csv-file-without-hand-writing-every-column-type]]'
- '[[2026-04-30-the-database-is-where-ai-agents-in-production-get-weird]]'
- '[[2026-05-08-prisma-relationships-finally-explained-with-mysql-side-by-side]]'
- '[[2026-04-04-i-tried-to-analyze-sql-lineage-across-15-databases-everything-broke-until-i-did-this]]'
- '[[2026-07-06-your-postgres-already-knows-why-its-slow-you-just-have-to-ask-it]]'
- '[[2026-07-24-ai-generated-sql-has-a-silent-failure-problem-heres-a-way-to-catch-it]]'
status: unread
---

> **TL;DR:** Originally published at nlqdb.com/blog Every text-to-SQL engine publishes the same two numbers: BIRD and Spider. Ours are not flattering — the strict-$0 free-model chain behind nlqdb currently scores 0.52 on BIRD Mini-De…

## What’s new and why it matters
Originally published at nlqdb.com/blog Every text-to-SQL engine publishes the same two numbers: BIRD and Spider. Ours are not flattering — the strict-$0 free-model chain behind nlqdb currently scores 0.52 on BIRD Mini-Dev and 0.19 on the Spider 2.0-lite SQLite subset. We track both weekly, against a pinned baseline, with a paired significance test, because those benchmarks are the honesty instrument of this field: hard, public, and comparable to every research paper. But look at what they actually measure. BIRD's databases are real-world dumps — dozens of tables, cryptic column names, dirty va…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Reproduce the example in a notebook; then refactor into a reusable function.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/omer_hochman/your-text-to-sql-accuracy-is-measured-on-schemas-your-users-will-never-build-32b2

## Related notes
- [[2026-06-28-how-to-generate-a-sql-schema-from-a-csv-file-without-hand-writing-every-column-type]]
- [[2026-04-30-the-database-is-where-ai-agents-in-production-get-weird]]
- [[2026-05-08-prisma-relationships-finally-explained-with-mysql-side-by-side]]
- [[2026-04-04-i-tried-to-analyze-sql-lineage-across-15-databases-everything-broke-until-i-did-this]]
- [[2026-07-06-your-postgres-already-knows-why-its-slow-you-just-have-to-ask-it]]
- [[2026-07-24-ai-generated-sql-has-a-silent-failure-problem-heres-a-way-to-catch-it]]
