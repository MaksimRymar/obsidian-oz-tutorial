---
title: REDB inside, part 1 — the 13 tables the whole engine runs on (with the actual
  SQL, and why it's not EAV)
date: '2026-06-04'
source: https://dev.to/rinat_kozin_d0a2ef43e7824/redb-inside-part-1-the-13-tables-the-whole-engine-runs-on-with-the-actual-sql-and-why-its-not-18mf
domain: SQL
relevance: 🟡
tags:
- '#ai'
- '#best-practice'
- '#sql'
- '#tool'
- '#zendesk'
related:
- '[[2026-04-21-sql-joins-and-window-functions-a-practical-guide]]'
- '[[2026-04-22-sql-set-operators-union-intersect-and-except-explained-simply]]'
- '[[2026-03-30-database-indexing-explained-whats-actually-happening-under-the-hood]]'
- '[[2026-04-19-build-your-own-types-classes-explained-simply]]'
- '[[2026-04-19-level-up-your-sql-subqueries-ctes-in-the-real-world]]'
- '[[2026-05-20-learning-sql-as-if-you-built-it-yourself]]'
status: unread
---

> **TL;DR:** A couple of weeks ago I published the redb.Core intro post — what RedBase is at the API level, why I wrote it, what production looks like, the LINQ surface, what generated SQL looks like for nested dictionary lookups. If…

## What’s new and why it matters
A couple of weeks ago I published the redb.Core intro post — what RedBase is at the API level, why I wrote it, what production looks like, the LINQ surface, what generated SQL looks like for nested dictionary lookups. If you haven't read it, start there — it's the wide-angle shot. This post starts a new series — "REDB inside" — that drills down into the engine. One article per layer: Part 1 (this post) — the database schema. 13 tables, what each one does, why the design is what it is, and the SQL you'd run to dump any object flat. Part 2 — code-first schemes. How SyncSchemeAsync<T> walks a C#…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Write the query in a scratchpad and run EXPLAIN/QUERY PLAN to verify performance.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/rinat_kozin_d0a2ef43e7824/redb-inside-part-1-the-13-tables-the-whole-engine-runs-on-with-the-actual-sql-and-why-its-not-18mf

## Related notes
- [[2026-04-21-sql-joins-and-window-functions-a-practical-guide]]
- [[2026-04-22-sql-set-operators-union-intersect-and-except-explained-simply]]
- [[2026-03-30-database-indexing-explained-whats-actually-happening-under-the-hood]]
- [[2026-04-19-build-your-own-types-classes-explained-simply]]
- [[2026-04-19-level-up-your-sql-subqueries-ctes-in-the-real-world]]
- [[2026-05-20-learning-sql-as-if-you-built-it-yourself]]
