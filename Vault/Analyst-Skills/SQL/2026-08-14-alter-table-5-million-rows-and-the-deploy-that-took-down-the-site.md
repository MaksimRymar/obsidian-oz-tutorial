---
title: ALTER TABLE, 5 Million Rows, and the Deploy That Took Down the Site
date: '2026-08-14'
source: https://dev.to/mikh-shytsko/alter-table-5-million-rows-and-the-deploy-that-took-down-the-site-1fk5
domain: SQL
relevance: 🔴
tags:
- '#ai'
- '#best-practice'
- '#feature'
- '#sql'
- '#tool'
- '#tutorial'
related:
- '[[2026-03-30-database-indexing-explained-whats-actually-happening-under-the-hood]]'
- '[[2026-08-14-schema-linting-vs-migration-linting-which-database-problems-each-one-can-see]]'
- '[[2026-07-06-your-postgres-already-knows-why-its-slow-you-just-have-to-ask-it]]'
- '[[2026-05-03-claudemd-for-postgresql-13-rules-that-make-ai-write-safe-production-ready-sql]]'
- '[[2026-08-11-the-text-to-sql-demo-takes-an-afternoon-the-other-90-is-why-you-should-buy-it]]'
- '[[2026-07-22-the-backfill-pattern-adding-required-columns-without-downtime]]'
status: unread
---

> **TL;DR:** A migration that takes 50ms on your dev database can lock a production table for 20 minutes, and running it against production-scale volume first is how you catch that before your users do. The Thursday-afternoon deploy…

## What’s new and why it matters
A migration that takes 50ms on your dev database can lock a production table for 20 minutes, and running it against production-scale volume first is how you catch that before your users do. The Thursday-afternoon deploy looked harmless. Adding a NOT NULL column with a default value to the orders table had passed review and run fine on staging, and the pipeline showed green. Then production went quiet, the way an on-call channel goes quiet, because the orders table, all 8 million rows of it, sat locked while every API endpoint that touched orders queued and the load balancers began returning 50…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Write the query in a scratchpad and run EXPLAIN/QUERY PLAN to verify performance.
- Add a short note: what changed in your workflow?

## Relevance
🔴

## Source
https://dev.to/mikh-shytsko/alter-table-5-million-rows-and-the-deploy-that-took-down-the-site-1fk5

## Related notes
- [[2026-03-30-database-indexing-explained-whats-actually-happening-under-the-hood]]
- [[2026-08-14-schema-linting-vs-migration-linting-which-database-problems-each-one-can-see]]
- [[2026-07-06-your-postgres-already-knows-why-its-slow-you-just-have-to-ask-it]]
- [[2026-05-03-claudemd-for-postgresql-13-rules-that-make-ai-write-safe-production-ready-sql]]
- [[2026-08-11-the-text-to-sql-demo-takes-an-afternoon-the-other-90-is-why-you-should-buy-it]]
- [[2026-07-22-the-backfill-pattern-adding-required-columns-without-downtime]]
