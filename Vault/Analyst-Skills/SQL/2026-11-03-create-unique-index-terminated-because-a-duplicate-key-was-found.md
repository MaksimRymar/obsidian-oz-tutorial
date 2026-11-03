---
title: CREATE UNIQUE INDEX terminated because a duplicate key was found
date: '2026-11-03'
source: https://dev.to/woodfiresam/create-unique-index-terminated-because-a-duplicate-key-was-found-4fc7
domain: SQL
relevance: 🟡
tags:
- '#sql'
- '#tool'
related:
- '[[2026-10-13-how-to-change-a-primary-key-that-foreign-keys-already-point-at]]'
- '[[2026-08-21-how-to-find-duplicate-rows-in-sql-and-decide-what-counts-as-one]]'
- '[[2026-10-23-sql-server-msg-1934-set-options-have-incorrect-settings-quotedidentifier---why-it-happens-and-how-to-fix-it]]'
- '[[2026-09-27-how-to-optimize-a-database-one-step-at-a-time]]'
- '[[2026-10-26-sql-joins-explained-inner-left-right-and-full-with-examples]]'
- '[[2026-10-01-how-i-close-a-monthly-dataset-and-the-month-i-found-out-mine-had-been-lying]]'
status: unread
---

> **TL;DR:** You make a column unique on a table that has been in use for a while: CREATE UNIQUE INDEX UX_Account_Email ON dbo . Account ( Email ); Msg 1505, Level 16, State 1, Line 1 The CREATE UNIQUE INDEX statement terminated beca…

## What’s new and why it matters
You make a column unique on a table that has been in use for a while: CREATE UNIQUE INDEX UX_Account_Email ON dbo . Account ( Email ); Msg 1505, Level 16, State 1, Line 1 The CREATE UNIQUE INDEX statement terminated because a duplicate key was found for the object name 'dbo.Account' and the index name 'UX_Account_Email'. The duplicate key value is (a@x.com). The message names exactly one value. It is the first collision found, not a report — there may be one more or four hundred, and fixing the named one just gets you the next message. A unique constraint fails the same way, with an extra line…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Write the query in a scratchpad and run EXPLAIN/QUERY PLAN to verify performance.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/woodfiresam/create-unique-index-terminated-because-a-duplicate-key-was-found-4fc7

## Related notes
- [[2026-10-13-how-to-change-a-primary-key-that-foreign-keys-already-point-at]]
- [[2026-08-21-how-to-find-duplicate-rows-in-sql-and-decide-what-counts-as-one]]
- [[2026-10-23-sql-server-msg-1934-set-options-have-incorrect-settings-quotedidentifier---why-it-happens-and-how-to-fix-it]]
- [[2026-09-27-how-to-optimize-a-database-one-step-at-a-time]]
- [[2026-10-26-sql-joins-explained-inner-left-right-and-full-with-examples]]
- [[2026-10-01-how-i-close-a-monthly-dataset-and-the-month-i-found-out-mine-had-been-lying]]
