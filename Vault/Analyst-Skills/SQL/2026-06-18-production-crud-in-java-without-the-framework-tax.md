---
title: Production CRUD in Java Without the Framework Tax
date: '2026-06-18'
source: https://dev.to/sqlfirst_dev/production-crud-in-java-without-the-framework-tax-2n82
domain: SQL
relevance: 🟡
tags:
- '#sql'
- '#tool'
related:
- '[[2026-05-03-claudemd-for-postgresql-13-rules-that-make-ai-write-safe-production-ready-sql]]'
- '[[2026-06-08-running-real-sql-on-dynamodb-how-it-actually-works]]'
- '[[2026-06-10-sql-for-data-analysis-the-10-query-patterns-that-matter]]'
- '[[2026-04-27-sql-group-by-having-the-beginners-guide-to-summarizing-data-like-a-pro]]'
- '[[2026-03-17-surrealdb-why-joins-are-so-2010-and-how-graphs-change-everything-part-3]]'
- '[[2026-06-13-top-12-sql-interview-problems-for-data-engineers-with-answers]]'
status: unread
---

> **TL;DR:** A practical walkthrough of SQL-First persistence: no XML, no Mapper interfaces, no generated queries. I maintain a Java backend that handles ~1M requests/day. For persistence, we used to run MyBatis. The XML was manageab…

## What’s new and why it matters
A practical walkthrough of SQL-First persistence: no XML, no Mapper interfaces, no generated queries. I maintain a Java backend that handles ~1M requests/day. For persistence, we used to run MyBatis. The XML was manageable at first, then it wasn't. Dynamic conditions became <if> tag soup. A simple join query needed three files and two languages. We switched to a simpler approach. Here's how it works for the most common case: single-table CRUD. What You Need Java 21+ Spring Boot (any 3.x) A database (H2 for the demo, MySQL/PostgreSQL for production) That's it. No XML parser, no code generator,…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Write the query in a scratchpad and run EXPLAIN/QUERY PLAN to verify performance.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/sqlfirst_dev/production-crud-in-java-without-the-framework-tax-2n82

## Related notes
- [[2026-05-03-claudemd-for-postgresql-13-rules-that-make-ai-write-safe-production-ready-sql]]
- [[2026-06-08-running-real-sql-on-dynamodb-how-it-actually-works]]
- [[2026-06-10-sql-for-data-analysis-the-10-query-patterns-that-matter]]
- [[2026-04-27-sql-group-by-having-the-beginners-guide-to-summarizing-data-like-a-pro]]
- [[2026-03-17-surrealdb-why-joins-are-so-2010-and-how-graphs-change-everything-part-3]]
- [[2026-06-13-top-12-sql-interview-problems-for-data-engineers-with-answers]]
