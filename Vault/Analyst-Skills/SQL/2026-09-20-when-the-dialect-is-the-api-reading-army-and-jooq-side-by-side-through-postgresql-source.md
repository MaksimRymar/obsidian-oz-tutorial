---
title: 'When the Dialect IS the API: Reading Army and jOOQ Side by Side, Through PostgreSQL
  Source'
date: '2026-09-20'
source: https://dev.to/zoro7/when-the-dialect-is-the-api-reading-army-and-jooq-side-by-side-through-postgresql-source-14h8
domain: SQL
relevance: 🔴
tags:
- '#ai'
- '#feature'
- '#library'
- '#python'
- '#sql'
- '#support-analytics'
- '#tool'
- '#zendesk'
related:
- '[[2026-03-15-easy-query-the-most-powerful-orm-for-java]]'
- '[[2026-07-23-btree-height-after-delete-postgresql-fast-root]]'
- '[[2026-08-19-final-weeks-of-gsoc]]'
- '[[2026-04-19-sql-deep-dive-subqueries-vs-ctes-which-one-should-you-use]]'
- '[[2026-05-22-i-built-a-type-safe-sql-library-for-bun-no-orm-no-codegen-just-sql-using-claude-code]]'
- '[[2026-08-31-subquery-vs-cte-in-sql-same-logic-one-you-can-check]]'
status: unread
---

> **TL;DR:** Army (the subject of this article) : https://github.com/PillArmy/army jOOQ (the comparison target) : https://github.com/jOOQ/jOOQ Versions & methodology : Army at 0.6.8-SNAPSHOT (Java 25); jOOQ from a local source checko…

## What’s new and why it matters
Army (the subject of this article) : https://github.com/PillArmy/army jOOQ (the comparison target) : https://github.com/jOOQ/jOOQ Versions & methodology : Army at 0.6.8-SNAPSHOT (Java 25); jOOQ from a local source checkout at 3.22.0-SNAPSHOT (commit 41e84edc85 , 2026-06-25, git describe = version-3.21.0.RC1-140-g41e84edc85 , root pom <java.version>25</java.version> ). Every Army code block below is a verbatim excerpt (file path + line numbers given). The jOOQ open-source checkout contains no tests and no example modules (see §7.3), so jOOQ code appears in two flavors: verbatim quotes of source…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Write the query in a scratchpad and run EXPLAIN/QUERY PLAN to verify performance.
- Add a short note: what changed in your workflow?

## Relevance
🔴

## Source
https://dev.to/zoro7/when-the-dialect-is-the-api-reading-army-and-jooq-side-by-side-through-postgresql-source-14h8

## Related notes
- [[2026-03-15-easy-query-the-most-powerful-orm-for-java]]
- [[2026-07-23-btree-height-after-delete-postgresql-fast-root]]
- [[2026-08-19-final-weeks-of-gsoc]]
- [[2026-04-19-sql-deep-dive-subqueries-vs-ctes-which-one-should-you-use]]
- [[2026-05-22-i-built-a-type-safe-sql-library-for-bun-no-orm-no-codegen-just-sql-using-claude-code]]
- [[2026-08-31-subquery-vs-cte-in-sql-same-logic-one-you-can-check]]
