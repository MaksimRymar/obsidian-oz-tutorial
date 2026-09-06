---
title: What actually happens in a database index (and why half of them do nothing)
date: '2026-09-05'
source: https://dev.to/vladut02/what-actually-happens-in-a-database-index-and-why-half-of-them-do-nothing-3mh6
domain: SQL
relevance: 🟡
tags:
- '#sql'
- '#tool'
related:
- '[[2026-03-30-database-indexing-explained-whats-actually-happening-under-the-hood]]'
- '[[2026-06-29-how-database-indexes-actually-work-and-when-they-backfire]]'
- '[[2026-07-04-why-your-database-index-gets-ignored-and-how-to-design-one-that-isnt]]'
- '[[2026-05-02-why-standard-indexes-fail-the-architecture-of-the-covering-index]]'
- '[[2026-05-20-learning-sql-as-if-you-built-it-yourself]]'
- '[[2026-08-11-sql-joins-how-to-join-two-tables-without-losing-or-doubling-rows]]'
status: unread
---

> **TL;DR:** Same query. Same table. Same million rows. One day it takes 4 seconds . The next day, 4 milliseconds . Nothing changed in the data. The only thing that changed was one line — you added an index . Four seconds to four mil…

## What’s new and why it matters
Same query. Same table. Same million rows. One day it takes 4 seconds . The next day, 4 milliseconds . Nothing changed in the data. The only thing that changed was one line — you added an index . Four seconds to four milliseconds is a thousand times faster, from one line of SQL. But here's the part nobody tells you: half the indexes people add do nothing. The query stays slow, the writes get slower, and they can't figure out why. By the end of this you'll know what an index actually is — and the one rule that decides whether yours even gets used. Prefer to watch? Full walkthrough with the B-tr…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Write the query in a scratchpad and run EXPLAIN/QUERY PLAN to verify performance.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/vladut02/what-actually-happens-in-a-database-index-and-why-half-of-them-do-nothing-3mh6

## Related notes
- [[2026-03-30-database-indexing-explained-whats-actually-happening-under-the-hood]]
- [[2026-06-29-how-database-indexes-actually-work-and-when-they-backfire]]
- [[2026-07-04-why-your-database-index-gets-ignored-and-how-to-design-one-that-isnt]]
- [[2026-05-02-why-standard-indexes-fail-the-architecture-of-the-covering-index]]
- [[2026-05-20-learning-sql-as-if-you-built-it-yourself]]
- [[2026-08-11-sql-joins-how-to-join-two-tables-without-losing-or-doubling-rows]]
