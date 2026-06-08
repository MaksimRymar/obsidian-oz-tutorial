---
title: 'Running Real SQL on DynamoDB: How It Actually Works'
date: '2026-06-08'
source: https://dev.to/camma_smith_1/running-real-sql-on-dynamodb-how-it-actually-works-32lg
domain: SQL
relevance: 🟡
tags:
- '#best-practice'
- '#sql'
- '#tool'
related:
- '[[2026-02-24-stop-using-any-the-wrong-way-in-rails]]'
- '[[2026-03-30-database-indexing-explained-whats-actually-happening-under-the-hood]]'
- '[[2026-05-04-sql-subqueries-vs-ctes]]'
- '[[2026-04-22-sql-set-operators-union-intersect-and-except-explained-simply]]'
- '[[2026-04-17-i-tested-postgresql-on-5-million-rows-heres-what-actually-makes-queries-fast]]'
- '[[2026-05-20-learning-sql-as-if-you-built-it-yourself]]'
status: unread
---

> **TL;DR:** DynamoDB is good at what it was designed for: fast, predictable reads and writes against known access patterns. It is not designed for ad-hoc queries. If you need to join two tables, aggregate by a column, or ask a quest…

## What’s new and why it matters
DynamoDB is good at what it was designed for: fast, predictable reads and writes against known access patterns. It is not designed for ad-hoc queries. If you need to join two tables, aggregate by a column, or ask a question your schema didn't anticipate, the answer is application code: SDK calls, manual pagination, in-memory joins. A simple question might take 50 lines. A complex one takes more, and the logic ends up scattered across your codebase. As you can imagine, that gets frustrating very quickly. That's where DynamoSQL comes in. DynamoSQL is a read-only SQL engine built on top of Dynamo…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Write the query in a scratchpad and run EXPLAIN/QUERY PLAN to verify performance.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/camma_smith_1/running-real-sql-on-dynamodb-how-it-actually-works-32lg

## Related notes
- [[2026-02-24-stop-using-any-the-wrong-way-in-rails]]
- [[2026-03-30-database-indexing-explained-whats-actually-happening-under-the-hood]]
- [[2026-05-04-sql-subqueries-vs-ctes]]
- [[2026-04-22-sql-set-operators-union-intersect-and-except-explained-simply]]
- [[2026-04-17-i-tested-postgresql-on-5-million-rows-heres-what-actually-makes-queries-fast]]
- [[2026-05-20-learning-sql-as-if-you-built-it-yourself]]
