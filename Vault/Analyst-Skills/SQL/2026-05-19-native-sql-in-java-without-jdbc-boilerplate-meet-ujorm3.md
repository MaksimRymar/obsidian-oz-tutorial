---
title: Native SQL in Java without JDBC boilerplate — meet Ujorm3
date: '2026-05-19'
source: https://dev.to/pponec/native-sql-in-java-without-jdbc-boilerplate-meet-ujorm3-3ab2
domain: SQL
relevance: 🟡
tags:
- '#library'
- '#sql'
- '#tool'
- '#tutorial'
related:
- '[[2026-03-30-your-sql-client-is-a-relic-heres-what-a-duckdb-native-ide-looks-like]]'
- '[[2026-04-08-how-building-a-streaming-sql-api-in-nodejs-changed-my-approach-to-real-time-data]]'
- '[[2026-05-08-prisma-relationships-finally-explained-with-mysql-side-by-side]]'
- '[[2026-03-15-easy-query-the-most-powerful-orm-for-java]]'
- '[[2026-04-30-subqueries-vs-ctes-in-sql-master-nested-queries-and-write-cleaner-smarter-code]]'
- '[[2026-04-21-sql-window-functions-and-ctes]]'
status: unread
---

> **TL;DR:** If you've ever written raw JDBC, you know what's coming. Open a connection, create a PreparedStatement , set parameters by index (hope you counted right), iterate a ResultSet , close everything in a finally block, declar…

## What’s new and why it matters
If you've ever written raw JDBC, you know what's coming. Open a connection, create a PreparedStatement , set parameters by index (hope you counted right), iterate a ResultSet , close everything in a finally block, declare SQLException on every method signature… It's a lot of ceremony for "give me some rows." I've been experimenting with Ujorm3 , a new lightweight ORM library for Java 17+. Here's a realistic example — a JOIN query that maps results including a nested relation: static final ResultSetMapper < Employee > EMPLOYEE_MAPPER = ResultSetMapper . of ( Employee . class ); List < Employee…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Write the query in a scratchpad and run EXPLAIN/QUERY PLAN to verify performance.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/pponec/native-sql-in-java-without-jdbc-boilerplate-meet-ujorm3-3ab2

## Related notes
- [[2026-03-30-your-sql-client-is-a-relic-heres-what-a-duckdb-native-ide-looks-like]]
- [[2026-04-08-how-building-a-streaming-sql-api-in-nodejs-changed-my-approach-to-real-time-data]]
- [[2026-05-08-prisma-relationships-finally-explained-with-mysql-side-by-side]]
- [[2026-03-15-easy-query-the-most-powerful-orm-for-java]]
- [[2026-04-30-subqueries-vs-ctes-in-sql-master-nested-queries-and-write-cleaner-smarter-code]]
- [[2026-04-21-sql-window-functions-and-ctes]]
