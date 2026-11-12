---
title: 'GDPR is a Storage Problem: Implementing Hard Deletes in Apache Iceberg'
date: '2026-11-11'
source: https://dev.to/aniketsoni/gdpr-is-a-storage-problem-implementing-hard-deletes-in-apache-iceberg-468a
domain: SQL
relevance: 🟡
tags:
- '#ai'
- '#best-practice'
- '#sql'
- '#support-analytics'
- '#tool'
- '#tutorial'
related:
- '[[2026-08-26-sql-taught-me-that-there-is-always-an-easier-way-to-do-things]]'
- '[[2026-05-10-why-where-phone-null-returns-nothing-in-sql]]'
- '[[2026-11-09-database-indexing-101-how-to-stop-slow-sql-queries-before-they-kill-your-app]]'
- '[[2026-10-21-your-bi-quote-is-really-a-data-quote]]'
- '[[2026-08-12-sql-ctes-how-to-build-a-query-in-steps-you-can-check]]'
- '[[2026-09-08-postgres-autovacuum-isnt-keeping-up-diagnosing-bloat-long-transactions-and-wraparound-warnings]]'
status: unread
---

> **TL;DR:** Data deletion in a lakehouse is a lie if you only run a DELETE statement. In regulated environments, "erasure" isn't a logical filter; it is a physical guarantee that sensitive information no longer exists within your st…

## What’s new and why it matters
Data deletion in a lakehouse is a lie if you only run a DELETE statement. In regulated environments, "erasure" isn't a logical filter; it is a physical guarantee that sensitive information no longer exists within your storage layer. Most engineers assume that once a record is removed from the current view of a table, they have met their compliance obligations. They are wrong. Why this matters: Regulations like GDPR and CCPA require the permanent removal of personal data upon request. In modern table formats like Apache Iceberg, data is versioned; a simple delete command leaves the sensitive in…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Write the query in a scratchpad and run EXPLAIN/QUERY PLAN to verify performance.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/aniketsoni/gdpr-is-a-storage-problem-implementing-hard-deletes-in-apache-iceberg-468a

## Related notes
- [[2026-08-26-sql-taught-me-that-there-is-always-an-easier-way-to-do-things]]
- [[2026-05-10-why-where-phone-null-returns-nothing-in-sql]]
- [[2026-11-09-database-indexing-101-how-to-stop-slow-sql-queries-before-they-kill-your-app]]
- [[2026-10-21-your-bi-quote-is-really-a-data-quote]]
- [[2026-08-12-sql-ctes-how-to-build-a-query-in-steps-you-can-check]]
- [[2026-09-08-postgres-autovacuum-isnt-keeping-up-diagnosing-bloat-long-transactions-and-wraparound-warnings]]
