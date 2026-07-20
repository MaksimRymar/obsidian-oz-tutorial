---
title: Additive column can 500 every login (Drizzle + Better Auth + preview deploys)
date: '2026-07-20'
source: https://dev.to/omar_bni_f6856a8bb0e021e9/additive-column-can-500-every-login-drizzle-better-auth-preview-deploys-3pg3
domain: SQL
relevance: 🟡
tags:
- '#ai'
- '#best-practice'
- '#feature'
- '#library'
- '#sql'
- '#tool'
- '#tutorial'
- '#zendesk'
related:
- '[[2026-05-03-claudemd-for-postgresql-13-rules-that-make-ai-write-safe-production-ready-sql]]'
- '[[2026-06-28-one-query-language-for-sql-mongo-and-the-browser-the-case-for-forge]]'
- '[[2026-07-06-your-postgres-already-knows-why-its-slow-you-just-have-to-ask-it]]'
- '[[2026-05-17-the-anatomy-of-an-apex-261-apexlang-file]]'
- '[[2026-04-12-every-ai-pitch-at-forbes-under-30-had-the-same-architecture-gap]]'
- '[[2026-05-02-uncovering-8-indexeddb-data-loss-after-browser-crashes-with-playwright]]'
status: unread
---

> **TL;DR:** Originally published on the Clanker Support blog . Migration 0017_user_role.sql in our repo is one line of SQL under eighteen lines of comment, and the comment is the interesting part: it explains why the column it adds…

## What’s new and why it matters
Originally published on the Clanker Support blog . Migration 0017_user_role.sql in our repo is one line of SQL under eighteen lines of comment, and the comment is the interesting part: it explains why the column it adds must never appear in our ORM schema. Declared the way every tutorial shows, that one additive column would have 500'd every authenticated request on any database that hadn't run the migration yet. "Additive nullable columns are always safe" is received wisdom, and on a modern stack it is false: ORMs like Drizzle and Prisma enumerate every mapped column on every SELECT, preview…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Write the query in a scratchpad and run EXPLAIN/QUERY PLAN to verify performance.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/omar_bni_f6856a8bb0e021e9/additive-column-can-500-every-login-drizzle-better-auth-preview-deploys-3pg3

## Related notes
- [[2026-05-03-claudemd-for-postgresql-13-rules-that-make-ai-write-safe-production-ready-sql]]
- [[2026-06-28-one-query-language-for-sql-mongo-and-the-browser-the-case-for-forge]]
- [[2026-07-06-your-postgres-already-knows-why-its-slow-you-just-have-to-ask-it]]
- [[2026-05-17-the-anatomy-of-an-apex-261-apexlang-file]]
- [[2026-04-12-every-ai-pitch-at-forbes-under-30-had-the-same-architecture-gap]]
- [[2026-05-02-uncovering-8-indexeddb-data-loss-after-browser-crashes-with-playwright]]
