---
title: 'Choosing a Primary Key: A Tour of the IDs Real Systems Actually Use'
date: '2026-09-14'
source: https://dev.to/yasir323/choosing-a-primary-key-a-tour-of-the-ids-real-systems-actually-use-9hg
domain: SQL
relevance: 🟡
tags:
- '#ai'
- '#python'
- '#sql'
- '#tool'
related:
- '[[2026-05-29-the-hard-truth-about-choosing-a-database-and-why-most-projects-get-it-wrong]]'
- '[[2026-09-14-keeping-strands-agents-honest-in-a-household-money-app]]'
- '[[2026-08-11-sql-aliases-how-to-read-a-query-out-loud]]'
- '[[2026-08-28-stop-writing-raw-sql-in-your-migrations-most-of-the-time]]'
- '[[2026-07-06-your-postgres-already-knows-why-its-slow-you-just-have-to-ask-it]]'
- '[[2026-08-21-how-to-find-duplicate-rows-in-sql-and-decide-what-counts-as-one]]'
status: unread
---

> **TL;DR:** The last article in this series was all about picking the right UUID version. This one pulls back a bit further, because UUIDs are just one item on a much longer menu, and depending on what you're building, they might no…

## What’s new and why it matters
The last article in this series was all about picking the right UUID version. This one pulls back a bit further, because UUIDs are just one item on a much longer menu, and depending on what you're building, they might not even be the right pick. Auto-increment integers, short UUIDs, Snowflake-style IDs, ULIDs, KSUIDs, NanoIDs, CUID2s: every one of these exists because somebody hit a real wall with the others and built something to get past it. I've used some of these at some point in production, usually because whatever I'd picked earlier stopped scaling the way I expected it to. So think of t…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Write the query in a scratchpad and run EXPLAIN/QUERY PLAN to verify performance.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/yasir323/choosing-a-primary-key-a-tour-of-the-ids-real-systems-actually-use-9hg

## Related notes
- [[2026-05-29-the-hard-truth-about-choosing-a-database-and-why-most-projects-get-it-wrong]]
- [[2026-09-14-keeping-strands-agents-honest-in-a-household-money-app]]
- [[2026-08-11-sql-aliases-how-to-read-a-query-out-loud]]
- [[2026-08-28-stop-writing-raw-sql-in-your-migrations-most-of-the-time]]
- [[2026-07-06-your-postgres-already-knows-why-its-slow-you-just-have-to-ask-it]]
- [[2026-08-21-how-to-find-duplicate-rows-in-sql-and-decide-what-counts-as-one]]
