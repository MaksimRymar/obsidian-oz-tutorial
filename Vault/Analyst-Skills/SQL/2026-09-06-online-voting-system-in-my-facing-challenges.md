---
title: Online Voting System in my facing challenges.....
date: '2026-09-06'
source: https://dev.to/abineshrajendiran/online-voting-system-in-my-facing-challenges-with-answer-pmh
domain: SQL
relevance: 🟡
tags:
- '#best-practice'
- '#sql'
- '#tool'
related:
- '[[2026-05-01-i-built-a-vs-code-extension-to-debug-mysql-queries-step-by-step]]'
- '[[2026-06-24-i-am-not-a-developer-i-built-a-database-audit-script-with-deepseek-here-is-where-it-went-wrong]]'
- '[[2026-04-08-how-building-a-streaming-sql-api-in-nodejs-changed-my-approach-to-real-time-data]]'
- '[[2026-04-23-i-built-a-browser-only-sql-practice-tool-because-installing-dbeaver-is-a-productivity-tax]]'
- '[[2026-08-14-from-messy-rows-to-a-boardroom-slide-building-safariconnect-in-sql-and-power-bi]]'
- '[[2026-07-30-i-wrote-integration-tests-for-my-mcp-failure-library-heres-the-pattern-that-caught-3-hidden-bugs]]'
status: unread
---

> **TL;DR:** 1. JDBC Connection & SQL Errors My first roadblock wasn't even logic — it was just getting connected. I kept hitting: com.mysql.cj.jdbc.exceptions.CommunicationsException: Communications link failure ** What was going wr…

## What’s new and why it matters
1. JDBC Connection & SQL Errors My first roadblock wasn't even logic — it was just getting connected. I kept hitting: com.mysql.cj.jdbc.exceptions.CommunicationsException: Communications link failure ** What was going wrong:** Wrong JDBC URL format (missing useSSL=false or timezone parameter caused issues on newer MySQL versions) MySQL service not running Driver JAR not added to the classpath correctly How I fixed it: java String url = "jdbc:mysql://localhost:3306/voting_db?useSSL=false&serverTimezone=UTC"; Connection con = DriverManager.getConnection(url, "root", "password"); I also wrapped e…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Write the query in a scratchpad and run EXPLAIN/QUERY PLAN to verify performance.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/abineshrajendiran/online-voting-system-in-my-facing-challenges-with-answer-pmh

## Related notes
- [[2026-05-01-i-built-a-vs-code-extension-to-debug-mysql-queries-step-by-step]]
- [[2026-06-24-i-am-not-a-developer-i-built-a-database-audit-script-with-deepseek-here-is-where-it-went-wrong]]
- [[2026-04-08-how-building-a-streaming-sql-api-in-nodejs-changed-my-approach-to-real-time-data]]
- [[2026-04-23-i-built-a-browser-only-sql-practice-tool-because-installing-dbeaver-is-a-productivity-tax]]
- [[2026-08-14-from-messy-rows-to-a-boardroom-slide-building-safariconnect-in-sql-and-power-bi]]
- [[2026-07-30-i-wrote-integration-tests-for-my-mcp-failure-library-heres-the-pattern-that-caught-3-hidden-bugs]]
