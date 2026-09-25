---
title: 'Zero updated rows do not fail a D1 batch: testing the rollback boundary'
date: '2026-09-25'
source: https://dev.to/hirodeath/zero-updated-rows-do-not-fail-a-d1-batch-testing-the-rollback-boundary-3odn
domain: SQL
relevance: 🟡
tags:
- '#ai'
- '#library'
- '#sql'
- '#tool'
related:
- '[[2026-08-21-how-to-find-duplicate-rows-in-sql-and-decide-what-counts-as-one]]'
- '[[2026-07-28-why-schema-drift-goes-undetected]]'
- '[[2026-08-26-the-postgres-insert-that-fails-right-after-a-successful-load]]'
- '[[2026-09-01-seeding-fixtures-realistic-test-data-for-warehouse-integration-tests]]'
- '[[2026-03-26-atomicity---design-a-reliable-wallet-transfer-system-with-acid-guarantees]]'
- '[[2026-05-24-day-4-creating-tables-data-types-null-and-default-constraints]]'
status: unread
---

> **TL;DR:** Suppose a D1 batch() reduces stock and then saves an order. If the UPDATE affects zero rows when stock is insufficient, will the order also remain unsaved? In a local D1 binding experiment, the INSERT succeeded even when…

## What’s new and why it matters
Suppose a D1 batch() reduces stock and then saves an order. If the UPDATE affects zero rows when stock is insufficient, will the order also remain unsaved? In a local D1 binding experiment, the INSERT succeeded even when the UPDATE affected zero rows. Throwing a JavaScript exception after batch() returned did not remove the saved order. SQL failure and an unfulfilled business operation need separate treatment. batch() provides atomicity when SQL fails. It does not automatically turn the application's conclusion that stock was unavailable into a SQL error. Start with a SQL statement that fails…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Write the query in a scratchpad and run EXPLAIN/QUERY PLAN to verify performance.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/hirodeath/zero-updated-rows-do-not-fail-a-d1-batch-testing-the-rollback-boundary-3odn

## Related notes
- [[2026-08-21-how-to-find-duplicate-rows-in-sql-and-decide-what-counts-as-one]]
- [[2026-07-28-why-schema-drift-goes-undetected]]
- [[2026-08-26-the-postgres-insert-that-fails-right-after-a-successful-load]]
- [[2026-09-01-seeding-fixtures-realistic-test-data-for-warehouse-integration-tests]]
- [[2026-03-26-atomicity---design-a-reliable-wallet-transfer-system-with-acid-guarantees]]
- [[2026-05-24-day-4-creating-tables-data-types-null-and-default-constraints]]
