---
title: 'SQL Injection – time delays and information retrieval| PortSwigger Lab Note
  #10'
date: '2026-03-13'
source: https://dev.to/kenny-cipher/sql-injection-time-delays-and-information-retrieval-portswigger-lab-note-10-2ima
domain: SQL
relevance: 🔴
tags:
- '#sql'
- '#tool'
related:
- '[[2026-03-12-sql-injection-blind-sql-injection-with-conditional-errors-portswigger-lab-note-9]]'
- '[[2026-03-11-sql-injection-blind-sql-injection-with-conditional-responses-portswigger-lab-note-8]]'
- '[[2026-03-10-sql-injection-union-attack-retrieving-multiple-values-in-a-single-column-portswigger-lab-note-5]]'
- '[[2026-03-09-sql-injection-union-attack-retrieving-data-from-other-tables-portswigger-lab-note-4]]'
- '[[2026-03-09-sql-injection-login-bypass-portswigger-lab-note-2]]'
- '[[2026-03-09-sql-injection-union-attack-portswigger-lab-note-3]]'
status: unread
---

> **TL;DR:** target： Lab URL: https://portswigger.net/web-security/learning-paths/sql-injection/sql-injection-exploiting-blind-sql-injection-by-triggering-time-delays/sql-injection/blind/lab-time-delays-info-retrieval Tools Used: bro…

## What’s new and why it matters
target： Lab URL: https://portswigger.net/web-security/learning-paths/sql-injection/sql-injection-exploiting-blind-sql-injection-by-triggering-time-delays/sql-injection/blind/lab-time-delays-info-retrieval Tools Used: browser Burp suite Vulnerability Summary： Type: Blind SQL Injection Description: The results of the SQL query are not returned, and the application does not respond any differently based on whether the query returns any rows or causes an error. However, since the query is executed synchronously, it is possible to trigger conditional time delays to infer information. Steps to Explo…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Write the query in a scratchpad and run EXPLAIN/QUERY PLAN to verify performance.
- Add a short note: what changed in your workflow?

## Relevance
🔴

## Source
https://dev.to/kenny-cipher/sql-injection-time-delays-and-information-retrieval-portswigger-lab-note-10-2ima

## Related notes
- [[2026-03-12-sql-injection-blind-sql-injection-with-conditional-errors-portswigger-lab-note-9]]
- [[2026-03-11-sql-injection-blind-sql-injection-with-conditional-responses-portswigger-lab-note-8]]
- [[2026-03-10-sql-injection-union-attack-retrieving-multiple-values-in-a-single-column-portswigger-lab-note-5]]
- [[2026-03-09-sql-injection-union-attack-retrieving-data-from-other-tables-portswigger-lab-note-4]]
- [[2026-03-09-sql-injection-login-bypass-portswigger-lab-note-2]]
- [[2026-03-09-sql-injection-union-attack-portswigger-lab-note-3]]
