---
title: Discovering PII Inside InterSystems IRIS
date: '2026-06-16'
source: https://dev.to/intersystems/discovering-pii-inside-intersystems-iris-1i2l
domain: SQL
relevance: 🔴
tags:
- '#ai'
- '#best-practice'
- '#library'
- '#python'
- '#sql'
- '#tool'
- '#zendesk'
related:
- '[[2026-04-03-i-built-a-pii-detection-api-with-zero-ai-cost-pure-regex]]'
- '[[2026-06-08-running-real-sql-on-dynamodb-how-it-actually-works]]'
- '[[2026-04-15-how-to-build-a-strong-foundation-in-sql-and-databases-step-by-step]]'
- '[[2026-03-30-database-indexing-explained-whats-actually-happening-under-the-hood]]'
- '[[2026-05-17-the-anatomy-of-an-apex-261-apexlang-file]]'
- '[[2026-04-22-sql-set-operators-union-intersect-and-except-explained-simply]]'
status: unread
---

> **TL;DR:** Data privacy regulations such as GDPR, LGPD, and HIPAA demand that organizations know exactly where Personally Identifiable Information (PII) lives inside their databases. Yet in practice, most teams rely on manual inven…

## What’s new and why it matters
Data privacy regulations such as GDPR, LGPD, and HIPAA demand that organizations know exactly where Personally Identifiable Information (PII) lives inside their databases. Yet in practice, most teams rely on manual inventories, tribal knowledge, or external scanning tools that require data to leave the database engine — a process that itself creates privacy and security risks. This article presents an MVP that takes a different approach: it runs PII detection inside InterSystems IRIS using Embedded Python, analyzing data where it lives and never exporting it to an external process. The result…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Write the query in a scratchpad and run EXPLAIN/QUERY PLAN to verify performance.
- Add a short note: what changed in your workflow?

## Relevance
🔴

## Source
https://dev.to/intersystems/discovering-pii-inside-intersystems-iris-1i2l

## Related notes
- [[2026-04-03-i-built-a-pii-detection-api-with-zero-ai-cost-pure-regex]]
- [[2026-06-08-running-real-sql-on-dynamodb-how-it-actually-works]]
- [[2026-04-15-how-to-build-a-strong-foundation-in-sql-and-databases-step-by-step]]
- [[2026-03-30-database-indexing-explained-whats-actually-happening-under-the-hood]]
- [[2026-05-17-the-anatomy-of-an-apex-261-apexlang-file]]
- [[2026-04-22-sql-set-operators-union-intersect-and-except-explained-simply]]
