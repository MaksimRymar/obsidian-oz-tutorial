---
title: 'archery-cli: A psql-style CLI for Archery — Query Databases from Terminal
  or AI Agents'
date: '2026-04-27'
source: https://dev.to/rjchien728/archery-cli-connect-ai-tools-to-your-sql-audit-platform-4kdb
domain: AI-Tools
relevance: 🔴
tags:
- '#ai'
- '#feature'
- '#sql'
- '#tool'
related:
- '[[2026-04-04-i-tried-to-analyze-sql-lineage-across-15-databases-everything-broke-until-i-did-this]]'
- '[[2026-02-28-mastering-dcl-the-ultimate-guide-to-grant-and-revoke-in-sql]]'
- '[[2026-04-21-sql-window-functions-and-ctes]]'
- '[[2026-02-24-a-safe-way-to-let-coding-agents-interact-with-your-database-without-prod-write-access]]'
- '[[2026-04-02-ctes-vs-subqueries-in-sql-which-one-should-you-use]]'
- '[[2026-04-21-sql-nulls-demystified-what-they-are-and-how-to-handle-them]]'
status: unread
---

> **TL;DR:** If you've ever copy-pasted query results from a web UI just to paste them into ChatGPT, this might save you that step. At my company, we use Archery for SQL audit and read-only queries against our databases. Archery has…

## What’s new and why it matters
If you've ever copy-pasted query results from a web UI just to paste them into ChatGPT, this might save you that step. At my company, we use Archery for SQL audit and read-only queries against our databases. Archery has a nice web UI, but our AI tools (Claude Code, Cursor, Codex) cannot use a web UI. So I built archery-cli : a small psql -style command line client that wraps Archery's HTTP API. Both humans and AI agents can use it from the shell. Why a CLI? A CLI is the easiest way to bring AI tools into a workflow that already exists. AI agents already know how to run shell commands. A psql -…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Reproduce the example in a notebook; then refactor into a reusable function.
- Add a short note: what changed in your workflow?

## Relevance
🔴

## Source
https://dev.to/rjchien728/archery-cli-connect-ai-tools-to-your-sql-audit-platform-4kdb

## Related notes
- [[2026-04-04-i-tried-to-analyze-sql-lineage-across-15-databases-everything-broke-until-i-did-this]]
- [[2026-02-28-mastering-dcl-the-ultimate-guide-to-grant-and-revoke-in-sql]]
- [[2026-04-21-sql-window-functions-and-ctes]]
- [[2026-02-24-a-safe-way-to-let-coding-agents-interact-with-your-database-without-prod-write-access]]
- [[2026-04-02-ctes-vs-subqueries-in-sql-which-one-should-you-use]]
- [[2026-04-21-sql-nulls-demystified-what-they-are-and-how-to-handle-them]]
