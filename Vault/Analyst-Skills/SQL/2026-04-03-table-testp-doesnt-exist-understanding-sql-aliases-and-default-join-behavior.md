---
title: '"Table ''test.p'' doesn''t exist" — Understanding SQL Aliases and Default
  JOIN Behavior'
date: '2026-04-03'
source: https://dev.to/dean_lee/table-testp-doesnt-exist-understanding-sql-aliases-and-default-join-behavior-1ndc
domain: SQL
relevance: 🟡
tags:
- '#sql'
- '#tool'
related:
- '[[2026-03-01-sql-joins]]'
- '[[2026-03-01-a-simple-guide-to-joins-and-window-functions]]'
- '[[2026-03-01-joins-and-windows-functions-in-sql]]'
- '[[2026-03-05-joins-and-window-functions-in-sql]]'
- '[[2026-03-02-joins-and-window-functions-in-sql]]'
- '[[2026-03-10-joins-window-functions]]'
status: unread
---

> **TL;DR:** While solving the LeetCode #175 (Combine Two Tables) problem, I encountered a couple of unexpected errors. What seemed like a simple query taught me a valuable lesson about SQL syntax and the fundamental behavior of JOIN…

## What’s new and why it matters
While solving the LeetCode #175 (Combine Two Tables) problem, I encountered a couple of unexpected errors. What seemed like a simple query taught me a valuable lesson about SQL syntax and the fundamental behavior of JOINs. Here’s a breakdown of the "traps" I fell into and how I fixed them. 1. The Problem I initially wrote the following MySQL query to fetch person details along with their addresses: SELECT firstName , lastName , city , state FROM P Person JOIN Address A ON P . personId = A . personId However, I hit a Runtime Error: Table 'test.p' doesn't exist. Even after fixing the syntax, I r…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Write the query in a scratchpad and run EXPLAIN/QUERY PLAN to verify performance.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/dean_lee/table-testp-doesnt-exist-understanding-sql-aliases-and-default-join-behavior-1ndc

## Related notes
- [[2026-03-01-sql-joins]]
- [[2026-03-01-a-simple-guide-to-joins-and-window-functions]]
- [[2026-03-01-joins-and-windows-functions-in-sql]]
- [[2026-03-05-joins-and-window-functions-in-sql]]
- [[2026-03-02-joins-and-window-functions-in-sql]]
- [[2026-03-10-joins-window-functions]]
