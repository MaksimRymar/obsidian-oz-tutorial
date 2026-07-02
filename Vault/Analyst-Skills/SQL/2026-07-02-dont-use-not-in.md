---
title: DON'T USE NOT IN
date: '2026-07-02'
source: https://dev.to/ryanabdaul/dont-use-not-in-3elk
domain: SQL
relevance: 🟡
tags:
- '#ai'
- '#python'
- '#sql'
- '#tool'
related:
- '[[2026-05-10-why-where-phone-null-returns-nothing-in-sql]]'
- '[[2026-06-15-day-01-of-learning-data-engineering-step1-sql-joins-and-set-operators]]'
- '[[2026-04-21-sql-window-functions-and-ctes]]'
- '[[2026-02-24-stop-using-any-the-wrong-way-in-rails]]'
- '[[2026-04-22-sql-set-operators-union-intersect-and-except-explained-simply]]'
- '[[2026-04-21-sql-nulls-demystified-what-they-are-and-how-to-handle-them]]'
status: unread
---

> **TL;DR:** Sometimes learning the inner details is not a waste of time, but actually, in some conditions, it can save you a lot! Look at this query: * SELECT s.name FROM students s WHERE s.name <> Null * What do you think the retur…

## What’s new and why it matters
Sometimes learning the inner details is not a waste of time, but actually, in some conditions, it can save you a lot! Look at this query: * SELECT s.name FROM students s WHERE s.name <> Null * What do you think the returned table? The returned table could be always an empty table ! Let me tell you why: If you have a programming background, we can say the following: NOT IN => != IN => == This happens because SQL can't compare values to NULL using = or <> any comparison with NULL returns UNKNOWN, not True or False. This same trap silently breaks NOT IN queries, and here's how. To understand why…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Write the query in a scratchpad and run EXPLAIN/QUERY PLAN to verify performance.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/ryanabdaul/dont-use-not-in-3elk

## Related notes
- [[2026-05-10-why-where-phone-null-returns-nothing-in-sql]]
- [[2026-06-15-day-01-of-learning-data-engineering-step1-sql-joins-and-set-operators]]
- [[2026-04-21-sql-window-functions-and-ctes]]
- [[2026-02-24-stop-using-any-the-wrong-way-in-rails]]
- [[2026-04-22-sql-set-operators-union-intersect-and-except-explained-simply]]
- [[2026-04-21-sql-nulls-demystified-what-they-are-and-how-to-handle-them]]
