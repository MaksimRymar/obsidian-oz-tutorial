---
title: 'SQL Injection – UNION attack, retrieving multiple values in a single column
  | PortSwigger Lab Note #5'
date: '2026-03-10'
source: https://dev.to/kenny-cipher/sql-injection-union-attack-retrieving-multiple-values-in-a-single-column-portswigger-lab-note-2mm
domain: SQL
relevance: 🔴
tags:
- '#sql'
- '#tool'
related:
- '[[2026-03-09-sql-injection-union-attack-portswigger-lab-note-3]]'
- '[[2026-03-09-sql-injection-login-bypass-portswigger-lab-note-2]]'
- '[[2026-03-10-sql-injection-querying-the-database-type-and-version-portswigger-lab-note-6]]'
- '[[2026-03-07-where-clause-allowing-retrieval-of-hidden-data-sql-injection-vulnerability]]'
- '[[2026-03-01-joins-and-windows-functions-in-sql]]'
- '[[2026-03-02-master-sql-navigating-joins-and-windows-functions]]'
status: unread
---

> **TL;DR:** target： Lab URL: https://portswigger.net/web-security/learning-paths/sql-injection/sql-injection-retrieving-multiple-values-within-a-single-column/sql-injection/union-attacks/lab-retrieve-multiple-values-in-single-column…

## What’s new and why it matters
target： Lab URL: https://portswigger.net/web-security/learning-paths/sql-injection/sql-injection-retrieving-multiple-values-within-a-single-column/sql-injection/union-attacks/lab-retrieve-multiple-values-in-single-column Tools Used: browser Burp suite Vulnerability Summary： Type: SQL Injection Description: To solve the lab, perform a SQL injection UNION attack that retrieves all usernames and passwords, and use the information to log in as the administrator user Steps to Exploit： 1.Determine the number of columns and which columns contain string data. '+UNION+SELECT+NULL,username||'~'||passwor…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Write the query in a scratchpad and run EXPLAIN/QUERY PLAN to verify performance.
- Add a short note: what changed in your workflow?

## Relevance
🔴

## Source
https://dev.to/kenny-cipher/sql-injection-union-attack-retrieving-multiple-values-in-a-single-column-portswigger-lab-note-2mm

## Related notes
- [[2026-03-09-sql-injection-union-attack-portswigger-lab-note-3]]
- [[2026-03-09-sql-injection-login-bypass-portswigger-lab-note-2]]
- [[2026-03-10-sql-injection-querying-the-database-type-and-version-portswigger-lab-note-6]]
- [[2026-03-07-where-clause-allowing-retrieval-of-hidden-data-sql-injection-vulnerability]]
- [[2026-03-01-joins-and-windows-functions-in-sql]]
- [[2026-03-02-master-sql-navigating-joins-and-windows-functions]]
