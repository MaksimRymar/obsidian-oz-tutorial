---
title: 'Log 02: The Sample Data Struggle & The "Wildcard" Trap'
date: '2026-03-21'
source: https://dev.to/codebasejournal/log-02-the-sample-data-struggle-the-wildcard-trap-5hp
domain: SQL
relevance: 🟡
tags:
- '#ai'
- '#sql'
- '#tool'
- '#zendesk'
related:
- '[[2026-03-15-sql-joins-and-window-functions-the-tools-that-changed-how-i-query-data]]'
- '[[2026-03-08-log-01-the-legacy-break-switching-to-docker-for-data-science]]'
- '[[2026-03-15-easy-query-the-most-powerful-orm-for-java]]'
- '[[2026-03-11-i-thought-my-rails-query-was-fine-until-null-ate-my-data]]'
- '[[2026-03-09-the-sql-query-that-ruined-my-weekend-and-what-i-built-to-prevent-it]]'
- '[[2026-03-16-my-journey-into-artificial-intelligence-why-i-chose-this-path]]'
status: unread
---

> **TL;DR:** With the Docker environment finally running, it was time to move from "configuring" to "doing." I went to the Microsoft SSMS source and pulled two classic sample files: instnwnd.sql (Northwind) and instpub.sql (Pubs). My…

## What’s new and why it matters
With the Docker environment finally running, it was time to move from "configuring" to "doing." I went to the Microsoft SSMS source and pulled two classic sample files: instnwnd.sql (Northwind) and instpub.sql (Pubs). My plan was simple: install them, run some queries, and sharpen my SQL skills. As is tradition in development, it wasn't that easy. The Ghost in the Container When I ran instnwnd.sql against my Docker-hosted SQL Express, the database simply didn't appear in the SSMS Object Explorer. I’m still not entirely sure why—it’s a task for another day. Instead of getting bogged down in ano…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Write the query in a scratchpad and run EXPLAIN/QUERY PLAN to verify performance.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/codebasejournal/log-02-the-sample-data-struggle-the-wildcard-trap-5hp

## Related notes
- [[2026-03-15-sql-joins-and-window-functions-the-tools-that-changed-how-i-query-data]]
- [[2026-03-08-log-01-the-legacy-break-switching-to-docker-for-data-science]]
- [[2026-03-15-easy-query-the-most-powerful-orm-for-java]]
- [[2026-03-11-i-thought-my-rails-query-was-fine-until-null-ate-my-data]]
- [[2026-03-09-the-sql-query-that-ruined-my-weekend-and-what-i-built-to-prevent-it]]
- [[2026-03-16-my-journey-into-artificial-intelligence-why-i-chose-this-path]]
