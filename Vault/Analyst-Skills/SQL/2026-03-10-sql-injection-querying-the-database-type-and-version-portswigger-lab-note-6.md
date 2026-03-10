---
title: 'SQL Injection – querying the database type and version | PortSwigger Lab Note
  #6'
date: '2026-03-10'
source: https://dev.to/kenny-cipher/sql-injection-querying-the-database-type-and-version-portswigger-lab-note-6-1fji
domain: SQL
relevance: 🔴
tags:
- '#sql'
- '#tool'
related:
- '[[2026-03-09-sql-injection-union-attack-portswigger-lab-note-3]]'
- '[[2026-03-09-sql-injection-login-bypass-portswigger-lab-note-2]]'
- '[[2026-03-07-where-clause-allowing-retrieval-of-hidden-data-sql-injection-vulnerability]]'
- '[[2026-03-02-dbeaver-postgres-aiven-and-other-sql-shenanigans]]'
- '[[2026-03-06-sql-joins-and-window-functions-a-practical-guide]]'
- '[[2026-02-26-beginner-friendly-guide---leetcode-problem-1404-c-python-javascript]]'
status: unread
---

> **TL;DR:** target： Lab URL: https://portswigger.net/web-security/learning-paths/sql-injection/sql-injection-examining-the-database-in-sql-injection-attacks/sql-injection/examining-the-database/lab-querying-database-version-mysql-mi…

## What’s new and why it matters
target： Lab URL: https://portswigger.net/web-security/learning-paths/sql-injection/sql-injection-examining-the-database-in-sql-injection-attacks/sql-injection/examining-the-database/lab-querying-database-version-mysql-microsoft Tools Used: browser Burp suite Vulnerability Summary： Type: SQL Injection Description: Steps to Exploit： 1.Determine the number of columns and which columns contain string data. 2.If the error-based payload fails, try changing the comment format. 3.According to the cheat sheet, determine that the database version is MySQL, and note the space after the double dash. 4.Sol…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Write the query in a scratchpad and run EXPLAIN/QUERY PLAN to verify performance.
- Add a short note: what changed in your workflow?

## Relevance
🔴

## Source
https://dev.to/kenny-cipher/sql-injection-querying-the-database-type-and-version-portswigger-lab-note-6-1fji

## Related notes
- [[2026-03-09-sql-injection-union-attack-portswigger-lab-note-3]]
- [[2026-03-09-sql-injection-login-bypass-portswigger-lab-note-2]]
- [[2026-03-07-where-clause-allowing-retrieval-of-hidden-data-sql-injection-vulnerability]]
- [[2026-03-02-dbeaver-postgres-aiven-and-other-sql-shenanigans]]
- [[2026-03-06-sql-joins-and-window-functions-a-practical-guide]]
- [[2026-02-26-beginner-friendly-guide---leetcode-problem-1404-c-python-javascript]]
