---
title: Why WHERE phone = NULL Returns Nothing in SQL
date: '2026-05-10'
source: https://dev.to/dechive/why-where-phone-null-returns-nothing-in-sql-m1j
domain: SQL
relevance: 🟡
tags:
- '#ai'
- '#sql'
- '#tool'
related:
- '[[2026-03-03-sql-joins-window-functions-the-skills-that-separate-analysts-from-beginners]]'
- '[[2026-04-21-sql-window-functions-and-ctes]]'
- '[[2026-04-21-sql-joins-and-window-functions-a-practical-guide]]'
- '[[2026-04-23-i-built-a-browser-only-sql-practice-tool-because-installing-dbeaver-is-a-productivity-tax]]'
- '[[2026-03-08-understanding-group-by-in-sql]]'
- '[[2026-03-09-sql-window-functions-dont-have-to-be-scary]]'
status: unread
---

> **TL;DR:** If you are new to SQL, this query can look perfectly reasonable at first: SELECT name FROM users WHERE phone = NULL ; You have a users table. Some users did not enter their phone number. The phone column looks empty. So…

## What’s new and why it matters
If you are new to SQL, this query can look perfectly reasonable at first: SELECT name FROM users WHERE phone = NULL ; You have a users table. Some users did not enter their phone number. The phone column looks empty. So you try to find those rows with phone = NULL . But the result comes back empty. The table is not necessarily wrong. The column name may be correct. The query may even look logical. The problem is that NULL is not a normal value. To understand why this query returns nothing, we need to understand what NULL really means. NULL is not an empty value At first, NULL looks like an emp…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Write the query in a scratchpad and run EXPLAIN/QUERY PLAN to verify performance.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/dechive/why-where-phone-null-returns-nothing-in-sql-m1j

## Related notes
- [[2026-03-03-sql-joins-window-functions-the-skills-that-separate-analysts-from-beginners]]
- [[2026-04-21-sql-window-functions-and-ctes]]
- [[2026-04-21-sql-joins-and-window-functions-a-practical-guide]]
- [[2026-04-23-i-built-a-browser-only-sql-practice-tool-because-installing-dbeaver-is-a-productivity-tax]]
- [[2026-03-08-understanding-group-by-in-sql]]
- [[2026-03-09-sql-window-functions-dont-have-to-be-scary]]
