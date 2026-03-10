---
title: 'SQL Injection – UNION attack, retrieving data from other tables | PortSwigger
  Lab Note #4'
date: '2026-03-09'
source: https://dev.to/kenny-cipher/sql-injection-union-attack-retrieving-data-from-other-tables-portswigger-lab-note-4-580c
domain: SQL
relevance: 🔴
tags:
- '#sql'
- '#tool'
related:
- '[[2026-03-10-sql-injection-union-attack-retrieving-multiple-values-in-a-single-column-portswigger-lab-note-5]]'
- '[[2026-03-09-sql-injection-login-bypass-portswigger-lab-note-2]]'
- '[[2026-03-09-sql-injection-union-attack-portswigger-lab-note-3]]'
- '[[2026-03-10-sql-injection-querying-the-database-type-and-version-portswigger-lab-note-6]]'
- '[[2026-03-07-where-clause-allowing-retrieval-of-hidden-data-sql-injection-vulnerability]]'
- '[[2026-03-01-sql-joins]]'
status: unread
---

> **TL;DR:** target： Lab URL: https://portswigger.net/web-security/learning-paths/sql-injection/sql-injection-using-a-sql-injection-union-attack-to-retrieve-interesting-data/sql-injection/union-attacks/lab-retrieve-data-from-other-ta…

## What’s new and why it matters
target： Lab URL: https://portswigger.net/web-security/learning-paths/sql-injection/sql-injection-using-a-sql-injection-union-attack-to-retrieve-interesting-data/sql-injection/union-attacks/lab-retrieve-data-from-other-tables Tools Used: browser Burp suite Vulnerability Summary： Type: SQL Injection Description: To solve the lab, perform a SQL injection UNION attack that retrieves all usernames and passwords, and use the information to log in as the administrator user. Steps to Exploit： 1.Using the technique mentioned in the last note, we can determine the number of columns returned by the query…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Write the query in a scratchpad and run EXPLAIN/QUERY PLAN to verify performance.
- Add a short note: what changed in your workflow?

## Relevance
🔴

## Source
https://dev.to/kenny-cipher/sql-injection-union-attack-retrieving-data-from-other-tables-portswigger-lab-note-4-580c

## Related notes
- [[2026-03-10-sql-injection-union-attack-retrieving-multiple-values-in-a-single-column-portswigger-lab-note-5]]
- [[2026-03-09-sql-injection-login-bypass-portswigger-lab-note-2]]
- [[2026-03-09-sql-injection-union-attack-portswigger-lab-note-3]]
- [[2026-03-10-sql-injection-querying-the-database-type-and-version-portswigger-lab-note-6]]
- [[2026-03-07-where-clause-allowing-retrieval-of-hidden-data-sql-injection-vulnerability]]
- [[2026-03-01-sql-joins]]
