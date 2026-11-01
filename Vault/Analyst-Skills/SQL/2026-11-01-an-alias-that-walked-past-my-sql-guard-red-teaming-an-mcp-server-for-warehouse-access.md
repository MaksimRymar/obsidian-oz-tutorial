---
title: 'An alias that walked past my SQL guard: red-teaming an MCP server for warehouse
  access'
date: '2026-11-01'
source: https://dev.to/tantn89/an-alias-that-walked-past-my-sql-guard-red-teaming-an-mcp-server-for-warehouse-access-1a52
domain: SQL
relevance: 🟡
tags:
- '#ai'
- '#best-practice'
- '#library'
- '#python'
- '#sql'
- '#tool'
related:
- '[[2026-08-21-how-to-find-duplicate-rows-in-sql-and-decide-what-counts-as-one]]'
- '[[2026-08-27-i-gave-an-llm-the-keys-to-a-multi-tenant-database]]'
- '[[2026-09-16-sql-joins-with-examples-of-each]]'
- '[[2026-09-04-i-built-an-offline-document-indexer-and-ollama-taught-me-two-things-i-did-not-expect]]'
- '[[2026-08-12-sql-ctes-how-to-build-a-query-in-steps-you-can-check]]'
- '[[2026-06-20-green-unit-tests-are-a-comfort-blanket]]'
status: unread
---

> **TL;DR:** I wrote an MCP server that lets an AI agent query a warehouse. A second model reviewed it and found a way past my SQL guard with a one-line alias. This post covers the design, the bug, the fix, and the other gaps a red t…

## What’s new and why it matters
I wrote an MCP server that lets an AI agent query a warehouse. A second model reviewed it and found a way past my SQL guard with a one-line alias. This post covers the design, the bug, the fix, and the other gaps a red team found. The repo is warehouse-mcp . It serves DuckDB, Postgres and BigQuery. The problem Agents are good at writing SQL and bad at knowing what they should not read. Giving one a warehouse connection raises three worries: It reads personal data it should not see. It writes, or reads files and system state, because a prompt told it to. It runs a query that scans terabytes and…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Write the query in a scratchpad and run EXPLAIN/QUERY PLAN to verify performance.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/tantn89/an-alias-that-walked-past-my-sql-guard-red-teaming-an-mcp-server-for-warehouse-access-1a52

## Related notes
- [[2026-08-21-how-to-find-duplicate-rows-in-sql-and-decide-what-counts-as-one]]
- [[2026-08-27-i-gave-an-llm-the-keys-to-a-multi-tenant-database]]
- [[2026-09-16-sql-joins-with-examples-of-each]]
- [[2026-09-04-i-built-an-offline-document-indexer-and-ollama-taught-me-two-things-i-did-not-expect]]
- [[2026-08-12-sql-ctes-how-to-build-a-query-in-steps-you-can-check]]
- [[2026-06-20-green-unit-tests-are-a-comfort-blanket]]
