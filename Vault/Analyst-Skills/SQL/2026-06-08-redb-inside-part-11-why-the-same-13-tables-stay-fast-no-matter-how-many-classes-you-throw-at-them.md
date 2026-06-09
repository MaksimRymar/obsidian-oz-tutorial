---
title: REDB inside, part 1.1 — why the same 13 tables stay fast no matter how many
  classes you throw at them
date: '2026-06-08'
source: https://dev.to/rinat_kozin_d0a2ef43e7824/redb-inside-part-11-why-the-same-13-tables-stay-fast-no-matter-how-many-classes-you-throw-at-1gg5
domain: SQL
relevance: 🔴
tags:
- '#ai'
- '#best-practice'
- '#feature'
- '#library'
- '#sql'
- '#support-analytics'
- '#tool'
related:
- '[[2026-06-04-redb-inside-part-1-the-13-tables-the-whole-engine-runs-on-with-the-actual-sql-and-why-its-not-eav]]'
- '[[2026-03-30-database-indexing-explained-whats-actually-happening-under-the-hood]]'
- '[[2026-06-08-running-real-sql-on-dynamodb-how-it-actually-works]]'
- '[[2026-05-20-learning-sql-as-if-you-built-it-yourself]]'
- '[[2026-04-27-sql-group-by-having-the-beginners-guide-to-summarizing-data-like-a-pro]]'
- '[[2026-02-24-stop-using-any-the-wrong-way-in-rails]]'
status: unread
---

> **TL;DR:** A couple of weeks ago I published REDB inside, part 1 — the 13 tables the whole engine runs on . It walked through _objects , _values , _structures , why this isn't classical EAV, and what the _scheme_metadata_cache does…

## What’s new and why it matters
A couple of weeks ago I published REDB inside, part 1 — the 13 tables the whole engine runs on . It walked through _objects , _values , _structures , why this isn't classical EAV, and what the _scheme_metadata_cache does. If you haven't read it, start there — the rest of this post assumes you know the layout. This is part 1.1 , not part 2. Same physical-storage conversation, different angle. Part 2 is going to be about code-first schemes ( SyncSchemeAsync<T> ), and the deep C# dive — LINQ translator, CRUD internals, trees — that's parts 3 through 5 of the series . This post stays in the databa…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Write the query in a scratchpad and run EXPLAIN/QUERY PLAN to verify performance.
- Add a short note: what changed in your workflow?

## Relevance
🔴

## Source
https://dev.to/rinat_kozin_d0a2ef43e7824/redb-inside-part-11-why-the-same-13-tables-stay-fast-no-matter-how-many-classes-you-throw-at-1gg5

## Related notes
- [[2026-06-04-redb-inside-part-1-the-13-tables-the-whole-engine-runs-on-with-the-actual-sql-and-why-its-not-eav]]
- [[2026-03-30-database-indexing-explained-whats-actually-happening-under-the-hood]]
- [[2026-06-08-running-real-sql-on-dynamodb-how-it-actually-works]]
- [[2026-05-20-learning-sql-as-if-you-built-it-yourself]]
- [[2026-04-27-sql-group-by-having-the-beginners-guide-to-summarizing-data-like-a-pro]]
- [[2026-02-24-stop-using-any-the-wrong-way-in-rails]]
