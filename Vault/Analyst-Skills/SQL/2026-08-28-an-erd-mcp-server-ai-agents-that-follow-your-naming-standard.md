---
title: 'An ERD MCP Server: AI Agents That Follow Your Naming Standard'
date: '2026-08-28'
source: https://dev.to/sqemo/an-erd-mcp-server-ai-agents-that-follow-your-naming-standard-5dee
domain: SQL
relevance: 🟡
tags:
- '#ai'
- '#feature'
- '#library'
- '#sql'
- '#tool'
related:
- '[[2026-08-21-which-sql-database-should-you-install]]'
- '[[2026-03-30-i-stopped-pasting-ddl-into-random-chatbots-heres-the-local-windows-db-client-i-use]]'
- '[[2026-08-14-schema-linting-vs-migration-linting-which-database-problems-each-one-can-see]]'
- '[[2026-08-21-mariadb-106-to-130-for-wordpress-only-one-upgrade-actually-does-anything-benchmark]]'
- '[[2026-05-08-prisma-relationships-finally-explained-with-mysql-side-by-side]]'
- '[[2026-08-04-you-cant-unit-test-an-llm-heres-what-i-built-instead]]'
status: unread
---

> **TL;DR:** AI agents already write database schemas. Ask Claude or Cursor for a feature and the migration file comes back with tables, columns, and foreign keys — named however the model's training data leans that day. user_id here…

## What’s new and why it matters
AI agents already write database schemas. Ask Claude or Cursor for a feature and the migration file comes back with tables, columns, and foreign keys — named however the model's training data leans that day. user_id here, userId there, usr_no when it read one too many legacy dumps. The agent isn't wrong; it just has no idea your team writes cust_no , because your naming convention lives in a wiki the model has never seen. That's the actual problem an ERD MCP server solves. Not "AI can draw diagrams now" — but that schema work done by agents can follow the same standard as schema work done by p…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Write the query in a scratchpad and run EXPLAIN/QUERY PLAN to verify performance.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/sqemo/an-erd-mcp-server-ai-agents-that-follow-your-naming-standard-5dee

## Related notes
- [[2026-08-21-which-sql-database-should-you-install]]
- [[2026-03-30-i-stopped-pasting-ddl-into-random-chatbots-heres-the-local-windows-db-client-i-use]]
- [[2026-08-14-schema-linting-vs-migration-linting-which-database-problems-each-one-can-see]]
- [[2026-08-21-mariadb-106-to-130-for-wordpress-only-one-upgrade-actually-does-anything-benchmark]]
- [[2026-05-08-prisma-relationships-finally-explained-with-mysql-side-by-side]]
- [[2026-08-04-you-cant-unit-test-an-llm-heres-what-i-built-instead]]
