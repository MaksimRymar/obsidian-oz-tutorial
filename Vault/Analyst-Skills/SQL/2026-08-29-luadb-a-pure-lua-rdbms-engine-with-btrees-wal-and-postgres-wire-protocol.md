---
title: LuaDB – A pure Lua RDBMS engine with B+Trees, WAL, and Postgres wire protocol
date: '2026-08-29'
source: https://dev.to/cold_war/luadb-a-pure-lua-rdbms-engine-with-btrees-wal-and-postgres-wire-protocol-2mn6
domain: SQL
relevance: 🟡
tags:
- '#ai'
- '#feature'
- '#sql'
related:
- '[[2026-03-28-duckdb-has-a-free-analytical-database-run-sql-on-csv-parquet-and-json-without-a-server]]'
- '[[2026-04-26-postgres-database-data-types-in-postgres-and-the-write-penalty-2026]]'
- '[[2026-03-26-sqlite-is-enough-for-your-side-project-full-text-search-json-and-wal-mode-included]]'
- '[[2026-03-28-surrealdb-has-a-free-multi-model-database-sql-graph-document-in-one-database]]'
- '[[2026-08-25-postgresql-23001-error-causes-and-solutions-complete-guide]]'
- '[[2026-08-14-how-to-seed-a-neon-database-psql-prisma-drizzle]]'
status: unread
---

> **TL;DR:** I built LuaDB – an embeddable relational database written 100% from scratch in pure Lua (no C extensions or external dependencies). Key features: Slotted 4KB binary pages with B+Tree primary/secondary indexing ACID trans…

## What’s new and why it matters
I built LuaDB – an embeddable relational database written 100% from scratch in pure Lua (no C extensions or external dependencies). Key features: Slotted 4KB binary pages with B+Tree primary/secondary indexing ACID transactions via Write-Ahead Logging (WAL) Built-in PostgreSQL Wire Protocol server (connect via psql or DBeaver) Pluggable VFS storage (Local disk, RAM, and Amazon S3 with AWS SigV4) Native JSON/JSONB extractions (-> / ->>), Foreign Keys with ON DELETE CASCADE, and WITH CTEs. Runs anywhere Lua runs (Lua 5.1+, 5.4, 5.5, LuaJIT). Feedback and technical questions welcome! https://gith…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Write the query in a scratchpad and run EXPLAIN/QUERY PLAN to verify performance.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/cold_war/luadb-a-pure-lua-rdbms-engine-with-btrees-wal-and-postgres-wire-protocol-2mn6

## Related notes
- [[2026-03-28-duckdb-has-a-free-analytical-database-run-sql-on-csv-parquet-and-json-without-a-server]]
- [[2026-04-26-postgres-database-data-types-in-postgres-and-the-write-penalty-2026]]
- [[2026-03-26-sqlite-is-enough-for-your-side-project-full-text-search-json-and-wal-mode-included]]
- [[2026-03-28-surrealdb-has-a-free-multi-model-database-sql-graph-document-in-one-database]]
- [[2026-08-25-postgresql-23001-error-causes-and-solutions-complete-guide]]
- [[2026-08-14-how-to-seed-a-neon-database-psql-prisma-drizzle]]
