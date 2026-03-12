---
title: 'SQL Injection – Blind SQL injection with conditional errors | PortSwigger
  Lab Note #9'
date: '2026-03-12'
source: https://dev.to/kenny-cipher/sql-injection-blind-sql-injection-with-conditional-errors-portswigger-lab-note-9-528b
domain: SQL
relevance: 🔴
tags:
- '#sql'
- '#tool'
related:
- '[[2026-03-11-sql-injection-blind-sql-injection-with-conditional-responses-portswigger-lab-note-8]]'
- '[[2026-03-09-sql-injection-login-bypass-portswigger-lab-note-2]]'
- '[[2026-03-10-sql-injection-listing-the-database-contents-on-non-oracle-databases-portswigger-lab-note-7]]'
- '[[2026-03-10-sql-injection-union-attack-retrieving-multiple-values-in-a-single-column-portswigger-lab-note-5]]'
- '[[2026-03-09-sql-injection-union-attack-retrieving-data-from-other-tables-portswigger-lab-note-4]]'
- '[[2026-03-10-sql-injection-querying-the-database-type-and-version-portswigger-lab-note-6]]'
status: unread
---

> **TL;DR:** target： Lab URL: https://portswigger.net/web-security/learning-paths/sql-injection/sql-injection-error-based-sql-injection/sql-injection/blind/lab-conditional-errors# Tools Used: browser Burp suite Vulnerability Summary：…

## What’s new and why it matters
target： Lab URL: https://portswigger.net/web-security/learning-paths/sql-injection/sql-injection-error-based-sql-injection/sql-injection/blind/lab-conditional-errors# Tools Used: browser Burp suite Vulnerability Summary： Type: SQL Injection Description: The database contains a different table called users, with columns called username and password. You need to exploit the blind SQL injection vulnerability to find out the password of the administrator user. Steps to Exploit： 1.confirm that the server is interpreting the injection as a SQL query 2.try submitting an invalid query while still pres…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Write the query in a scratchpad and run EXPLAIN/QUERY PLAN to verify performance.
- Add a short note: what changed in your workflow?

## Relevance
🔴

## Source
https://dev.to/kenny-cipher/sql-injection-blind-sql-injection-with-conditional-errors-portswigger-lab-note-9-528b

## Related notes
- [[2026-03-11-sql-injection-blind-sql-injection-with-conditional-responses-portswigger-lab-note-8]]
- [[2026-03-09-sql-injection-login-bypass-portswigger-lab-note-2]]
- [[2026-03-10-sql-injection-listing-the-database-contents-on-non-oracle-databases-portswigger-lab-note-7]]
- [[2026-03-10-sql-injection-union-attack-retrieving-multiple-values-in-a-single-column-portswigger-lab-note-5]]
- [[2026-03-09-sql-injection-union-attack-retrieving-data-from-other-tables-portswigger-lab-note-4]]
- [[2026-03-10-sql-injection-querying-the-database-type-and-version-portswigger-lab-note-6]]
