---
title: 'SQL Injection – UNION attack | PortSwigger Lab Note #3'
date: '2026-03-09'
source: https://dev.to/kenny-cipher/sql-injection-union-attack-portswigger-lab-note-3-2d5
domain: SQL
relevance: 🔴
tags:
- '#sql'
- '#tool'
related:
- '[[2026-03-09-sql-injection-login-bypass-portswigger-lab-note-2]]'
- '[[2026-03-07-where-clause-allowing-retrieval-of-hidden-data-sql-injection-vulnerability]]'
- '[[2026-03-02-master-sql-navigating-joins-and-windows-functions]]'
- '[[2026-03-06-a-guide-to-sql-joins-and-window-functions]]'
- '[[2026-03-02-dbeaver-postgres-aiven-and-other-sql-shenanigans]]'
- '[[2026-02-10-real-world-business-use-cases-of-ai-in-market-research]]'
status: unread
---

> **TL;DR:** target： Lab URL: https://portswigger.net/web-security/learning-paths/sql-injection/sql-injection-determining-the-number-of-columns-required/sql-injection/union-attacks/lab-determine-number-of-columns Tools Used: browser…

## What’s new and why it matters
target： Lab URL: https://portswigger.net/web-security/learning-paths/sql-injection/sql-injection-determining-the-number-of-columns-required/sql-injection/union-attacks/lab-determine-number-of-columns Tools Used: browser Burp suite Vulnerability Summary： Type: SQL Injection Description: To solve the lab, determine the number of columns returned by the query by performing a SQL injection UNION attack Steps to Exploit： 1.Click any category to send a request to the server and check the query. 2.Modify the parameter multiple times, then try to determine the number of columns returned by the query.…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Write the query in a scratchpad and run EXPLAIN/QUERY PLAN to verify performance.
- Add a short note: what changed in your workflow?

## Relevance
🔴

## Source
https://dev.to/kenny-cipher/sql-injection-union-attack-portswigger-lab-note-3-2d5

## Related notes
- [[2026-03-09-sql-injection-login-bypass-portswigger-lab-note-2]]
- [[2026-03-07-where-clause-allowing-retrieval-of-hidden-data-sql-injection-vulnerability]]
- [[2026-03-02-master-sql-navigating-joins-and-windows-functions]]
- [[2026-03-06-a-guide-to-sql-joins-and-window-functions]]
- [[2026-03-02-dbeaver-postgres-aiven-and-other-sql-shenanigans]]
- [[2026-02-10-real-world-business-use-cases-of-ai-in-market-research]]
