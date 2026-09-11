---
title: My "Last Hour" Query Returned 1,252 Rows. The Real Answer Was 68.
date: '2026-09-11'
source: https://dev.to/ai_changewatch/my-last-hour-query-returned-1252-rows-the-real-answer-was-68-5fgh
domain: SQL
relevance: 🔴
tags:
- '#ai'
- '#feature'
- '#sql'
- '#tool'
related:
- '[[2026-09-04-i-built-an-offline-document-indexer-and-ollama-taught-me-two-things-i-did-not-expect]]'
- '[[2026-04-21-sql-window-functions-and-ctes]]'
- '[[2026-08-31-running-total-in-sql-the-window-frame-that-decides-the-answer]]'
- '[[2026-08-21-how-to-find-duplicate-rows-in-sql-and-decide-what-counts-as-one]]'
- '[[2026-08-21-null-in-sql-why-null-finds-nothing-and-what-to-write-instead]]'
- '[[2026-08-11-sql-aliases-how-to-read-a-query-out-loud]]'
status: unread
---

> **TL;DR:** I run AI Change Watch , a small independent project that crawls what 15 AI vendors publish about their own models — deprecation tables, lifecycle pages, pricing and SDK releases — and records every time one of them chang…

## What’s new and why it matters
I run AI Change Watch , a small independent project that crawls what 15 AI vendors publish about their own models — deprecation tables, lifecycle pages, pricing and SDK releases — and records every time one of them changes. Every so often I check whether the crawler is still alive by counting recent runs. The query is the obvious one: SELECT COUNT ( * ) FROM crawl_runs WHERE started_at > datetime ( 'now' , '-1 hour' ); It returned 1,252 . The true number of runs in that hour was 68 . No error. No warning. A plausible-looking integer, roughly eighteen times too large, from a query that reads co…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Write the query in a scratchpad and run EXPLAIN/QUERY PLAN to verify performance.
- Add a short note: what changed in your workflow?

## Relevance
🔴

## Source
https://dev.to/ai_changewatch/my-last-hour-query-returned-1252-rows-the-real-answer-was-68-5fgh

## Related notes
- [[2026-09-04-i-built-an-offline-document-indexer-and-ollama-taught-me-two-things-i-did-not-expect]]
- [[2026-04-21-sql-window-functions-and-ctes]]
- [[2026-08-31-running-total-in-sql-the-window-frame-that-decides-the-answer]]
- [[2026-08-21-how-to-find-duplicate-rows-in-sql-and-decide-what-counts-as-one]]
- [[2026-08-21-null-in-sql-why-null-finds-nothing-and-what-to-write-instead]]
- [[2026-08-11-sql-aliases-how-to-read-a-query-out-loud]]
