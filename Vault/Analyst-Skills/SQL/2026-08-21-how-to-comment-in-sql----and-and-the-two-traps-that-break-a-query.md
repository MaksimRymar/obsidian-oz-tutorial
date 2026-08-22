---
title: 'How to Comment in SQL: -- and /* */, and the Two Traps That Break a Query'
date: '2026-08-21'
source: https://dev.to/michaelnocito/how-to-comment-in-sql-and-and-the-two-traps-that-break-a-query-3bc
domain: SQL
relevance: 🟡
tags:
- '#ai'
- '#feature'
- '#python'
- '#sql'
- '#support-analytics'
- '#tableau'
- '#tool'
- '#tutorial'
related:
- '[[2026-08-21-comment-on-table-how-to-store-a-table-description-in-the-database-itself]]'
- '[[2026-08-11-sql-aliases-how-to-read-a-query-out-loud]]'
- '[[2026-08-22-where-to-get-a-sample-database-to-practice-sql-and-how-to-check-it-loaded]]'
- '[[2026-08-21-how-to-find-duplicate-rows-in-sql-and-decide-what-counts-as-one]]'
- '[[2026-08-21-sql-comment-syntax-by-database-mysql-postgresql-sql-server-sqlite-oracle]]'
- '[[2026-08-21-which-sql-database-should-you-install]]'
status: unread
---

> **TL;DR:** By Michael Nocito , data analyst · Updated August 11, 2026 SQL has two comment syntaxes and you will use both today. -- hides the rest of one line. /* opens a block that stays hidden until */ closes it, however many line…

## What’s new and why it matters
By Michael Nocito , data analyst · Updated August 11, 2026 SQL has two comment syntaxes and you will use both today. -- hides the rest of one line. /* opens a block that stays hidden until */ closes it, however many lines that takes. Nothing inside a comment runs. The part nobody warns you about is what happens when you comment out a line that was holding the query together. There are exactly two shapes that break, and one small habit prevents both. That habit is the reason to read past the first screen. The short version. -- for one line, /* */ for a block. Write your column lists with the co…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Write the query in a scratchpad and run EXPLAIN/QUERY PLAN to verify performance.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/michaelnocito/how-to-comment-in-sql-and-and-the-two-traps-that-break-a-query-3bc

## Related notes
- [[2026-08-21-comment-on-table-how-to-store-a-table-description-in-the-database-itself]]
- [[2026-08-11-sql-aliases-how-to-read-a-query-out-loud]]
- [[2026-08-22-where-to-get-a-sample-database-to-practice-sql-and-how-to-check-it-loaded]]
- [[2026-08-21-how-to-find-duplicate-rows-in-sql-and-decide-what-counts-as-one]]
- [[2026-08-21-sql-comment-syntax-by-database-mysql-postgresql-sql-server-sqlite-oracle]]
- [[2026-08-21-which-sql-database-should-you-install]]
