---
title: The Wasteful JOIN I Was Afraid to Write? GORM Wrote It for Me.
date: '2026-11-16'
source: https://dev.to/danny0728/the-wasteful-join-i-was-afraid-to-write-gorm-wrote-it-for-me-16ea
domain: SQL
relevance: 🟡
tags:
- '#ai'
- '#feature'
- '#sql'
- '#tool'
related:
- '[[2026-11-14-i-wrote-a-wasteful-join-on-purpose-it-ran-faster-until-it-didnt]]'
- '[[2026-09-29-sql-joins-how-to-combine-tables-the-right-way]]'
- '[[2026-10-26-sql-joins-explained-inner-left-right-and-full-with-examples]]'
- '[[2026-09-16-sql-joins-with-examples-of-each]]'
- '[[2026-08-11-sql-joins-how-to-join-two-tables-without-losing-or-doubling-rows]]'
- '[[2026-08-21-how-to-find-duplicate-rows-in-sql-and-decide-what-counts-as-one]]'
status: unread
---

> **TL;DR:** In my last article I wrote an unnecessary JOIN by hand to see what it cost. That test came from a worry: after a long time of letting GORM write my SQL, I didn't trust myself to write it efficiently. I ended that article…

## What’s new and why it matters
In my last article I wrote an unnecessary JOIN by hand to see what it cost. That test came from a worry: after a long time of letting GORM write my SQL, I didn't trust myself to write it efficiently. I ended that article with a promise to check the other half of the worry, which was my assumption that GORM's own SQL is efficient. So I took the same task and wrote it three ways in GORM. The version I would have reached for at work, GORM's association joins, generated the same wasteful join I had been afraid of writing myself. It also finished first in every run with default settings, which make…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Write the query in a scratchpad and run EXPLAIN/QUERY PLAN to verify performance.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/danny0728/the-wasteful-join-i-was-afraid-to-write-gorm-wrote-it-for-me-16ea

## Related notes
- [[2026-11-14-i-wrote-a-wasteful-join-on-purpose-it-ran-faster-until-it-didnt]]
- [[2026-09-29-sql-joins-how-to-combine-tables-the-right-way]]
- [[2026-10-26-sql-joins-explained-inner-left-right-and-full-with-examples]]
- [[2026-09-16-sql-joins-with-examples-of-each]]
- [[2026-08-11-sql-joins-how-to-join-two-tables-without-losing-or-doubling-rows]]
- [[2026-08-21-how-to-find-duplicate-rows-in-sql-and-decide-what-counts-as-one]]
