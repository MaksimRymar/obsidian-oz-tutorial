---
title: 'Database Views in Your ERD: Read-Only Entities, Not Fake Tables'
date: '2026-08-02'
source: https://dev.to/tbson87/database-views-in-your-erd-read-only-entities-not-fake-tables-27l3
domain: SQL
relevance: 🔴
tags:
- '#ai'
- '#feature'
- '#sql'
- '#tool'
- '#zendesk'
related:
- '[[2026-07-18-the-data-dictionary-should-live-in-the-erd-not-in-a-spreadsheet]]'
- '[[2026-07-25-lucidchart-erd-alternative-a-desktop-erd-tool-that-connects-to-your-database]]'
- '[[2026-07-30-on-delete-cascade-is-invisible-in-your-erd-and-in-your-database-logs]]'
- '[[2026-08-01-supabase-schema-diagram-get-an-erd-you-can-keep-not-a-dashboard-view]]'
- '[[2026-07-04-why-your-database-index-gets-ignored-and-how-to-design-one-that-isnt]]'
- '[[2026-04-10-dapple-terminal-graphics-composed]]'
status: unread
---

> **TL;DR:** Disclosure: I build Schemity , a desktop ERD tool - this post is from our blog and uses it for the examples. TL;DR: Database views carry real responsibilities - reporting layers, security boundaries, API surfaces - but E…

## What’s new and why it matters
Disclosure: I build Schemity , a desktop ERD tool - this post is from our blog and uses it for the examples. TL;DR: Database views carry real responsibilities - reporting layers, security boundaries, API surfaces - but ERD tools either leave them out entirely (DBML has no view support despite requests since 2022) or draw them as if they were ordinary tables. Schemity displays views and materialized views as read-only entities with italic names and a bold view or mview token in the entity footer, so derived relations are distinguishable from base tables at a glance, and they can be imported int…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Write the query in a scratchpad and run EXPLAIN/QUERY PLAN to verify performance.
- Add a short note: what changed in your workflow?

## Relevance
🔴

## Source
https://dev.to/tbson87/database-views-in-your-erd-read-only-entities-not-fake-tables-27l3

## Related notes
- [[2026-07-18-the-data-dictionary-should-live-in-the-erd-not-in-a-spreadsheet]]
- [[2026-07-25-lucidchart-erd-alternative-a-desktop-erd-tool-that-connects-to-your-database]]
- [[2026-07-30-on-delete-cascade-is-invisible-in-your-erd-and-in-your-database-logs]]
- [[2026-08-01-supabase-schema-diagram-get-an-erd-you-can-keep-not-a-dashboard-view]]
- [[2026-07-04-why-your-database-index-gets-ignored-and-how-to-design-one-that-isnt]]
- [[2026-04-10-dapple-terminal-graphics-composed]]
