---
title: 'Supabase Schema Diagram: Get an ERD You Can Keep, Not a Dashboard View'
date: '2026-08-01'
source: https://dev.to/tbson87/supabase-schema-diagram-get-an-erd-you-can-keep-not-a-dashboard-view-2hdd
domain: SQL
relevance: 🟡
tags:
- '#ai'
- '#feature'
- '#sql'
- '#tool'
- '#zendesk'
related:
- '[[2026-07-25-lucidchart-erd-alternative-a-desktop-erd-tool-that-connects-to-your-database]]'
- '[[2026-03-30-i-stopped-pasting-ddl-into-random-chatbots-heres-the-local-windows-db-client-i-use]]'
- '[[2026-06-28-how-to-generate-a-sql-schema-from-a-csv-file-without-hand-writing-every-column-type]]'
- '[[2026-07-18-the-data-dictionary-should-live-in-the-erd-not-in-a-spreadsheet]]'
- '[[2026-07-06-your-postgres-already-knows-why-its-slow-you-just-have-to-ask-it]]'
- '[[2026-07-23-comparing-staging-and-production-database-schemas-side-by-side]]'
status: unread
---

> **TL;DR:** Disclosure: I build Schemity , a desktop ERD tool - this post is from our blog and uses it for the examples. TL;DR: The Schema Visualizer built into Supabase Studio is a viewer, not a document - it renders one schema at…

## What’s new and why it matters
Disclosure: I build Schemity , a desktop ERD tool - this post is from our blog and uses it for the examples. TL;DR: The Schema Visualizer built into Supabase Studio is a viewer, not a document - it renders one schema at a time, saves your dragged layout only to that browser's localStorage, and exports at most a flat image. The durable way to get a Supabase schema diagram is to connect an ERD tool to the underlying Postgres over the session-mode connection string (port 5432) and reverse engineer it. Schemity treats Supabase as a first-class connection, pulls the schema with every foreign key an…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Write the query in a scratchpad and run EXPLAIN/QUERY PLAN to verify performance.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/tbson87/supabase-schema-diagram-get-an-erd-you-can-keep-not-a-dashboard-view-2hdd

## Related notes
- [[2026-07-25-lucidchart-erd-alternative-a-desktop-erd-tool-that-connects-to-your-database]]
- [[2026-03-30-i-stopped-pasting-ddl-into-random-chatbots-heres-the-local-windows-db-client-i-use]]
- [[2026-06-28-how-to-generate-a-sql-schema-from-a-csv-file-without-hand-writing-every-column-type]]
- [[2026-07-18-the-data-dictionary-should-live-in-the-erd-not-in-a-spreadsheet]]
- [[2026-07-06-your-postgres-already-knows-why-its-slow-you-just-have-to-ask-it]]
- [[2026-07-23-comparing-staging-and-production-database-schemas-side-by-side]]
