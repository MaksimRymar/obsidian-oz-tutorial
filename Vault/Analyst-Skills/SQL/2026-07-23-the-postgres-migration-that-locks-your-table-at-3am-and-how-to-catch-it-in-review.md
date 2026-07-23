---
title: The Postgres migration that locks your table at 3am, and how to catch it in
  review
date: '2026-07-23'
source: https://dev.to/technical_turtle/the-postgres-migration-that-locks-your-table-at-3am-and-how-to-catch-it-in-review-17pa
domain: SQL
relevance: 🟡
tags:
- '#ai'
- '#best-practice'
- '#python'
- '#sql'
- '#tool'
- '#tutorial'
related:
- '[[2026-07-22-the-backfill-pattern-adding-required-columns-without-downtime]]'
- '[[2026-03-30-database-indexing-explained-whats-actually-happening-under-the-hood]]'
- '[[2026-05-03-claudemd-for-postgresql-13-rules-that-make-ai-write-safe-production-ready-sql]]'
- '[[2026-07-06-create-index-is-a-write-outage-in-disguise]]'
- '[[2026-05-25-i-added-mcp-support-to-my-saas-in-an-afternoon-heres-the-whole-thing]]'
- '[[2026-06-10-your-database-is-fast-your-queries-are-slow]]'
status: unread
---

> **TL;DR:** -- looks fine in review, locks your busiest table in prod: ALTER TABLE users ALTER COLUMN email SET NOT NULL ; -- same result, no outage: ALTER TABLE users ADD CONSTRAINT users_email_nn CHECK ( email IS NOT NULL ) NOT VA…

## What’s new and why it matters
-- looks fine in review, locks your busiest table in prod: ALTER TABLE users ALTER COLUMN email SET NOT NULL ; -- same result, no outage: ALTER TABLE users ADD CONSTRAINT users_email_nn CHECK ( email IS NOT NULL ) NOT VALID ; ALTER TABLE users VALIDATE CONSTRAINT users_email_nn ; ALTER TABLE users ALTER COLUMN email SET NOT NULL ; The top one scans every row under an ACCESS EXCLUSIVE lock, so every read and write to the table blocks until it finishes. On a big table that is a four-minute outage. The bottom one gets to the same place without ever holding that lock during a scan. A generalist re…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Write the query in a scratchpad and run EXPLAIN/QUERY PLAN to verify performance.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/technical_turtle/the-postgres-migration-that-locks-your-table-at-3am-and-how-to-catch-it-in-review-17pa

## Related notes
- [[2026-07-22-the-backfill-pattern-adding-required-columns-without-downtime]]
- [[2026-03-30-database-indexing-explained-whats-actually-happening-under-the-hood]]
- [[2026-05-03-claudemd-for-postgresql-13-rules-that-make-ai-write-safe-production-ready-sql]]
- [[2026-07-06-create-index-is-a-write-outage-in-disguise]]
- [[2026-05-25-i-added-mcp-support-to-my-saas-in-an-afternoon-heres-the-whole-thing]]
- [[2026-06-10-your-database-is-fast-your-queries-are-slow]]
