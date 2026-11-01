---
title: Reading Complex XML in SQL Server — Shredding a Thousand Attributes Generically
  Instead of Looping for Hours
date: '2026-10-31'
source: https://dev.to/marcus1968/reading-complex-xml-in-sql-server-shredding-a-thousand-attributes-generically-instead-of-looping-5be0
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
- '#tutorial'
- '#zendesk'
related:
- '[[2026-09-28-set-based-vs-row-by-row-postgresql-refresh-from-114-to-12-seconds]]'
- '[[2026-07-23-btree-height-after-delete-postgresql-fast-root]]'
- '[[2026-08-26-redb-371-props-search-up-to-100x-faster-an-alternative-to-ef-core-or-a-companion-to-it]]'
- '[[2026-09-09-still-writing-slow-sql-queries-10-ways-to-improve-performance]]'
- '[[2026-08-31-running-total-in-sql-the-window-frame-that-decides-the-answer]]'
- '[[2026-09-04-i-built-an-offline-document-indexer-and-ollama-taught-me-two-things-i-did-not-expect]]'
status: unread
---

> **TL;DR:** A catalog of around 3000 product configurations arrives as XML. Depending on the equipment, a configuration carries different and additional attributes, around a thousand across all variants. In an earlier project, the e…

## What’s new and why it matters
A catalog of around 3000 product configurations arrives as XML. Depending on the equipment, a configuration carries different and additional attributes, around a thousand across all variants. In an earlier project, the evaluation of such a catalog ran in application code: a loop over the object types, inside it a loop over the attributes, plus lists in memory that grew with every iteration. The program took several hours. Where exactly the time went can no longer be said in hindsight. What is certain is what the design demanded: code per type, a separate lookup per attribute, and a schema that…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Write the query in a scratchpad and run EXPLAIN/QUERY PLAN to verify performance.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/marcus1968/reading-complex-xml-in-sql-server-shredding-a-thousand-attributes-generically-instead-of-looping-5be0

## Related notes
- [[2026-09-28-set-based-vs-row-by-row-postgresql-refresh-from-114-to-12-seconds]]
- [[2026-07-23-btree-height-after-delete-postgresql-fast-root]]
- [[2026-08-26-redb-371-props-search-up-to-100x-faster-an-alternative-to-ef-core-or-a-companion-to-it]]
- [[2026-09-09-still-writing-slow-sql-queries-10-ways-to-improve-performance]]
- [[2026-08-31-running-total-in-sql-the-window-frame-that-decides-the-answer]]
- [[2026-09-04-i-built-an-offline-document-indexer-and-ollama-taught-me-two-things-i-did-not-expect]]
