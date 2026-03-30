---
title: SQL Assertions, ANSI join, and ORA-08697
date: '2026-03-29'
source: https://dev.to/franckpachot/sql-assertions-ansi-join-and-ora-08697-3bl9
domain: SQL
relevance: 🔴
tags:
- '#feature'
- '#sql'
related:
- '[[2026-03-10-joins-window-functions]]'
- '[[2026-03-09-sql-window-functions-dont-have-to-be-scary]]'
- '[[2026-03-11-sql-joins-window-functions]]'
- '[[2026-03-13-you-dont-need-a-framework-building-reliable-ai-agents-from-first-principles]]'
- '[[2026-02-24-stop-using-any-the-wrong-way-in-rails]]'
- '[[2026-03-11-i-thought-my-rails-query-was-fine-until-null-ate-my-data]]'
status: unread
---

> **TL;DR:** In the previous post on consistency boundaries, we saw that an updatable join view can hide a write-skew anomaly when the developer assumes the consistency boundary is a single row, even though there are actually two und…

## What’s new and why it matters
In the previous post on consistency boundaries, we saw that an updatable join view can hide a write-skew anomaly when the developer assumes the consistency boundary is a single row, even though there are actually two underlying rows and only one is locked. I wanted to see how the new SQL Assertions introduced in "Oracle AI Database 26ai Release 23.26.1.0.0" handle this, since they use a different locking mechanism. TL;DR: they handle it correctly, but without ANSI joins. Without assertions, for an employee with a salary of 1000 and a commission of 100, two concurrent users could each add 42 to…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Write the query in a scratchpad and run EXPLAIN/QUERY PLAN to verify performance.
- Add a short note: what changed in your workflow?

## Relevance
🔴

## Source
https://dev.to/franckpachot/sql-assertions-ansi-join-and-ora-08697-3bl9

## Related notes
- [[2026-03-10-joins-window-functions]]
- [[2026-03-09-sql-window-functions-dont-have-to-be-scary]]
- [[2026-03-11-sql-joins-window-functions]]
- [[2026-03-13-you-dont-need-a-framework-building-reliable-ai-agents-from-first-principles]]
- [[2026-02-24-stop-using-any-the-wrong-way-in-rails]]
- [[2026-03-11-i-thought-my-rails-query-was-fine-until-null-ate-my-data]]
