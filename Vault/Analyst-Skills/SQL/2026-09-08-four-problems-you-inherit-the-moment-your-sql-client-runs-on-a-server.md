---
title: Four problems you inherit the moment your SQL client runs on a server
date: '2026-09-08'
source: https://dev.to/cevheri/four-problems-you-inherit-the-moment-your-sql-client-runs-on-a-server-424e
domain: SQL
relevance: 🟡
tags:
- '#ai'
- '#career'
- '#sql'
- '#tool'
related:
- '[[2026-08-27-i-gave-an-llm-the-keys-to-a-multi-tenant-database]]'
- '[[2026-08-21-how-to-find-duplicate-rows-in-sql-and-decide-what-counts-as-one]]'
- '[[2026-09-02-deriving-data-quality-rules-from-the-schema-what-the-metadata-already-knows]]'
- '[[2026-07-23-btree-height-after-delete-postgresql-fast-root]]'
- '[[2026-06-28-how-to-generate-a-sql-schema-from-a-csv-file-without-hand-writing-every-column-type]]'
- '[[2026-09-04-i-built-an-offline-document-indexer-and-ollama-taught-me-two-things-i-did-not-expect]]'
status: unread
---

> **TL;DR:** A desktop database client makes two demands nobody writes down: every laptop has to reach the production network, and every laptop has to hold a copy of every credential. Move the client onto a server next to the data an…

## What’s new and why it matters
A desktop database client makes two demands nobody writes down: every laptop has to reach the production network, and every laptop has to hold a copy of every credential. Move the client onto a server next to the data and both demands disappear. The credential lives in one place instead of sixty. The network path becomes a deployment topology instead of a VPN grant per person. That is the trade. This post is the invoice. Because the thing you just built is no longer a client. It is a multi-tenant network service holding every database connection your team owns, and it has four problems a deskt…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Write the query in a scratchpad and run EXPLAIN/QUERY PLAN to verify performance.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/cevheri/four-problems-you-inherit-the-moment-your-sql-client-runs-on-a-server-424e

## Related notes
- [[2026-08-27-i-gave-an-llm-the-keys-to-a-multi-tenant-database]]
- [[2026-08-21-how-to-find-duplicate-rows-in-sql-and-decide-what-counts-as-one]]
- [[2026-09-02-deriving-data-quality-rules-from-the-schema-what-the-metadata-already-knows]]
- [[2026-07-23-btree-height-after-delete-postgresql-fast-root]]
- [[2026-06-28-how-to-generate-a-sql-schema-from-a-csv-file-without-hand-writing-every-column-type]]
- [[2026-09-04-i-built-an-offline-document-indexer-and-ollama-taught-me-two-things-i-did-not-expect]]
