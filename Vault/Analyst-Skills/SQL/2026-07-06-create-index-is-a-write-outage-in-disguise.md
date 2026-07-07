---
title: 🔒 CREATE INDEX Is a Write Outage in Disguise
date: '2026-07-06'
source: https://dev.to/code_with_kyryl/create-index-is-a-write-outage-in-disguise-4abo
domain: SQL
relevance: 🟡
tags:
- '#sql'
- '#tool'
related:
- '[[2026-03-30-database-indexing-explained-whats-actually-happening-under-the-hood]]'
- '[[2026-05-03-claudemd-for-postgresql-13-rules-that-make-ai-write-safe-production-ready-sql]]'
- '[[2026-06-05-your-postgres-is-failing-quietly-7-sql-checks-that-catch-it-before-grafana-does]]'
- '[[2026-06-28-how-to-generate-a-sql-schema-from-a-csv-file-without-hand-writing-every-column-type]]'
- '[[2026-06-05-i-got-tired-of-writing-the-same-history-table-boilerplate-so-i-built-a-postgres-extension]]'
- '[[2026-07-04-why-your-database-index-gets-ignored-and-how-to-design-one-that-isnt]]'
status: unread
---

> **TL;DR:** CREATE INDEX without CONCURRENTLY locks out writes for the entire build. On a large, live table that plain statement is not a migration. It is a multi-minute write outage for every endpoint touching that table. And the w…

## What’s new and why it matters
CREATE INDEX without CONCURRENTLY locks out writes for the entire build. On a large, live table that plain statement is not a migration. It is a multi-minute write outage for every endpoint touching that table. And the worst part is it sails through every test you have, because your test data is tiny and the build finishes before you can blink. The lock nobody reads about A plain CREATE INDEX acquires a SHARE lock on the table and holds it until the build completes. CREATE INDEX idx_orders_customer_id ON orders ( customer_id ); SHARE allows concurrent reads. It blocks anything that writes: INS…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Write the query in a scratchpad and run EXPLAIN/QUERY PLAN to verify performance.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/code_with_kyryl/create-index-is-a-write-outage-in-disguise-4abo

## Related notes
- [[2026-03-30-database-indexing-explained-whats-actually-happening-under-the-hood]]
- [[2026-05-03-claudemd-for-postgresql-13-rules-that-make-ai-write-safe-production-ready-sql]]
- [[2026-06-05-your-postgres-is-failing-quietly-7-sql-checks-that-catch-it-before-grafana-does]]
- [[2026-06-28-how-to-generate-a-sql-schema-from-a-csv-file-without-hand-writing-every-column-type]]
- [[2026-06-05-i-got-tired-of-writing-the-same-history-table-boilerplate-so-i-built-a-postgres-extension]]
- [[2026-07-04-why-your-database-index-gets-ignored-and-how-to-design-one-that-isnt]]
