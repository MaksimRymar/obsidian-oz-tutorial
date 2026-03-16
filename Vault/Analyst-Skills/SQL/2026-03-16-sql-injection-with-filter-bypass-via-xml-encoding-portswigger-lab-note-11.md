---
title: 'SQL Injection – with filter bypass via XML encoding | PortSwigger Lab Note
  #11'
date: '2026-03-16'
source: https://dev.to/kenny-cipher/sql-injection-with-filter-bypass-via-xml-encoding-portswigger-lab-note-11-2khh
domain: SQL
relevance: 🔴
tags:
- '#sql'
- '#tool'
related:
- '[[2026-03-12-sql-injection-blind-sql-injection-with-conditional-errors-portswigger-lab-note-9]]'
- '[[2026-03-09-sql-injection-union-attack-retrieving-data-from-other-tables-portswigger-lab-note-4]]'
- '[[2026-03-10-sql-injection-union-attack-retrieving-multiple-values-in-a-single-column-portswigger-lab-note-5]]'
- '[[2026-03-11-sql-injection-blind-sql-injection-with-conditional-responses-portswigger-lab-note-8]]'
- '[[2026-03-10-sql-injection-querying-the-database-type-and-version-portswigger-lab-note-6]]'
- '[[2026-03-09-sql-injection-login-bypass-portswigger-lab-note-2]]'
status: unread
---

> **TL;DR:** target： Lab URL: https://portswigger.net/web-security/learning-paths/sql-injection/sql-injection-in-different-contexts/sql-injection/lab-sql-injection-with-filter-bypass-via-xml-encoding# Tools Used: browser Burp suite V…

## What’s new and why it matters
target： Lab URL: https://portswigger.net/web-security/learning-paths/sql-injection/sql-injection-in-different-contexts/sql-injection/lab-sql-injection-with-filter-bypass-via-xml-encoding# Tools Used: browser Burp suite Vulnerability Summary： Type: SQL Injection Description: This lab demonstrates a SQL injection vulnerability inside XML input. The application performs a database query using user-supplied XML data without proper sanitization. However, a weak WAF (Web Application Firewall) attempts to block common SQL injection payloads. The goal is to bypass the filter using XML encoding, extrac…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Write the query in a scratchpad and run EXPLAIN/QUERY PLAN to verify performance.
- Add a short note: what changed in your workflow?

## Relevance
🔴

## Source
https://dev.to/kenny-cipher/sql-injection-with-filter-bypass-via-xml-encoding-portswigger-lab-note-11-2khh

## Related notes
- [[2026-03-12-sql-injection-blind-sql-injection-with-conditional-errors-portswigger-lab-note-9]]
- [[2026-03-09-sql-injection-union-attack-retrieving-data-from-other-tables-portswigger-lab-note-4]]
- [[2026-03-10-sql-injection-union-attack-retrieving-multiple-values-in-a-single-column-portswigger-lab-note-5]]
- [[2026-03-11-sql-injection-blind-sql-injection-with-conditional-responses-portswigger-lab-note-8]]
- [[2026-03-10-sql-injection-querying-the-database-type-and-version-portswigger-lab-note-6]]
- [[2026-03-09-sql-injection-login-bypass-portswigger-lab-note-2]]
