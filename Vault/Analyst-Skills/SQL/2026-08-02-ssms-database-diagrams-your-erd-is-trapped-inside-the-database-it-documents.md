---
title: 'SSMS Database Diagrams: Your ERD Is Trapped Inside the Database It Documents'
date: '2026-08-02'
source: https://dev.to/tbson87/ssms-database-diagrams-your-erd-is-trapped-inside-the-database-it-documents-49i1
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
- '[[2026-08-01-supabase-schema-diagram-get-an-erd-you-can-keep-not-a-dashboard-view]]'
- '[[2026-07-18-the-data-dictionary-should-live-in-the-erd-not-in-a-spreadsheet]]'
- '[[2026-07-22-many-to-many-in-an-erd-shouldnt-mean-hand-building-the-junction-table]]'
- '[[2026-07-23-comparing-staging-and-production-database-schemas-side-by-side]]'
- '[[2026-03-30-i-stopped-pasting-ddl-into-random-chatbots-heres-the-local-windows-db-client-i-use]]'
status: unread
---

> **TL;DR:** Disclosure: I build Schemity , a desktop ERD tool - this post is from our blog and uses it for the examples. TL;DR: SSMS keeps every database diagram as a binary blob in the sysdiagrams system table of the database it de…

## What’s new and why it matters
Disclosure: I build Schemity , a desktop ERD tool - this post is from our blog and uses it for the examples. TL;DR: SSMS keeps every database diagram as a binary blob in the sysdiagrams system table of the database it describes, so it cannot be saved to a file, versioned in Git, or opened without a server connection - and the feature itself was removed in SSMS 18.0 and restored in 18.1 only after user outcry. Schemity, a desktop ERD tool with SQL Server support, reverse engineers the same schema into a plain local JSON file that diffs in pull requests, exports to SVG and Mermaid, and re-syncs…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Write the query in a scratchpad and run EXPLAIN/QUERY PLAN to verify performance.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/tbson87/ssms-database-diagrams-your-erd-is-trapped-inside-the-database-it-documents-49i1

## Related notes
- [[2026-07-25-lucidchart-erd-alternative-a-desktop-erd-tool-that-connects-to-your-database]]
- [[2026-08-01-supabase-schema-diagram-get-an-erd-you-can-keep-not-a-dashboard-view]]
- [[2026-07-18-the-data-dictionary-should-live-in-the-erd-not-in-a-spreadsheet]]
- [[2026-07-22-many-to-many-in-an-erd-shouldnt-mean-hand-building-the-junction-table]]
- [[2026-07-23-comparing-staging-and-production-database-schemas-side-by-side]]
- [[2026-03-30-i-stopped-pasting-ddl-into-random-chatbots-heres-the-local-windows-db-client-i-use]]
