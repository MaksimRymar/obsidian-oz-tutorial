---
title: Mechanisms, not agreements
date: '2026-08-17'
source: https://dev.to/serhovskyi/mechanisms-not-agreements-f9n
domain: SQL
relevance: 🟡
tags:
- '#ai'
- '#best-practice'
- '#feature'
- '#library'
- '#python'
- '#sql'
- '#support-analytics'
- '#tool'
- '#zendesk'
related:
- '[[2026-07-23-btree-height-after-delete-postgresql-fast-root]]'
- '[[2026-07-22-the-backfill-pattern-adding-required-columns-without-downtime]]'
- '[[2026-07-28-why-schema-drift-goes-undetected]]'
- '[[2026-04-22-your-pytest-retries-are-lying-to-you-the-hidden-cost-of---reruns-and-the-plugin-i-wrote-so-i-could-actually-see-what-my-]]'
- '[[2026-05-02-uncovering-8-indexeddb-data-loss-after-browser-crashes-with-playwright]]'
- '[[2026-06-28-how-to-generate-a-sql-schema-from-a-csv-file-without-hand-writing-every-column-type]]'
status: unread
---

> **TL;DR:** The type-check was green. All 263 tests were green. Every nutrient value on the screen read undefined . This was Pantensa, a household pantry and nutrition tracker — FastAPI and PostgreSQL on the backend, Vue on the fron…

## What’s new and why it matters
The type-check was green. All 263 tests were green. Every nutrient value on the screen read undefined . This was Pantensa, a household pantry and nutrition tracker — FastAPI and PostgreSQL on the backend, Vue on the front — midway through replacing eight hard-coded nutrient columns with a proper many-to-many catalog. The frontend carried a hand-written mirror of the backend's read schemas: a TypeScript interface for every Pydantic model, kept in sync by me remembering to keep it in sync. I had renamed fields on the backend. The mirror still described the old shape, the tests still asserted aga…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Write the query in a scratchpad and run EXPLAIN/QUERY PLAN to verify performance.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/serhovskyi/mechanisms-not-agreements-f9n

## Related notes
- [[2026-07-23-btree-height-after-delete-postgresql-fast-root]]
- [[2026-07-22-the-backfill-pattern-adding-required-columns-without-downtime]]
- [[2026-07-28-why-schema-drift-goes-undetected]]
- [[2026-04-22-your-pytest-retries-are-lying-to-you-the-hidden-cost-of---reruns-and-the-plugin-i-wrote-so-i-could-actually-see-what-my-]]
- [[2026-05-02-uncovering-8-indexeddb-data-loss-after-browser-crashes-with-playwright]]
- [[2026-06-28-how-to-generate-a-sql-schema-from-a-csv-file-without-hand-writing-every-column-type]]
