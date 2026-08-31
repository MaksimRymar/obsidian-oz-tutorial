---
title: 'SQLite FTS5 vs Whoosh: when to reach for a pure-Python search library'
date: '2026-08-31'
source: https://dev.to/priyasundaram/sqlite-fts5-vs-whoosh-when-to-reach-for-a-pure-python-search-library-555l
domain: SQL
relevance: 🟡
tags:
- '#ai'
- '#best-practice'
- '#library'
- '#python'
- '#sql'
- '#tool'
- '#tutorial'
related:
- '[[2026-08-29-add-real-search-to-your-python-web-app-no-elasticsearch-no-separate-service]]'
- '[[2026-08-08-how-full-text-search-works-in-pure-python-a-tour-with-whoosh]]'
- '[[2026-08-10-sqlite-fts5-is-faster-than-whoosh-so-why-would-you-ever-use-a-pure-python-search-engine]]'
- '[[2026-03-26-sqlite-can-do-more-than-you-think-full-text-search-json-window-functions-and-281tb-databases]]'
- '[[2026-08-28-stop-writing-raw-sql-in-your-migrations-most-of-the-time]]'
- '[[2026-08-08-how-to-set-up-a-sql-database-for-beginners]]'
status: unread
---

> **TL;DR:** If you need full-text search inside a Python app, two options come up again and again: SQLite's built-in FTS5 extension, and Whoosh , a pure-Python search library. I maintain the current Whoosh fork, so treat this as a b…

## What’s new and why it matters
If you need full-text search inside a Python app, two options come up again and again: SQLite's built-in FTS5 extension, and Whoosh , a pure-Python search library. I maintain the current Whoosh fork, so treat this as a biased-but-honest field guide rather than a sales pitch — for a lot of apps, FTS5 is the right answer, and I'll say so. The 30-second version FTS5 ships with SQLite, is written in C, and is blisteringly fast on large corpora. If you already have a SQLite database and your search needs are "match these words, rank by relevance," reach for it first. Whoosh is pure Python — no C ex…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Write the query in a scratchpad and run EXPLAIN/QUERY PLAN to verify performance.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/priyasundaram/sqlite-fts5-vs-whoosh-when-to-reach-for-a-pure-python-search-library-555l

## Related notes
- [[2026-08-29-add-real-search-to-your-python-web-app-no-elasticsearch-no-separate-service]]
- [[2026-08-08-how-full-text-search-works-in-pure-python-a-tour-with-whoosh]]
- [[2026-08-10-sqlite-fts5-is-faster-than-whoosh-so-why-would-you-ever-use-a-pure-python-search-engine]]
- [[2026-03-26-sqlite-can-do-more-than-you-think-full-text-search-json-window-functions-and-281tb-databases]]
- [[2026-08-28-stop-writing-raw-sql-in-your-migrations-most-of-the-time]]
- [[2026-08-08-how-to-set-up-a-sql-database-for-beginners]]
