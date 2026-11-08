---
title: Connect .NET to Azure SQL with Managed Identity (No Passwords)
date: '2026-11-08'
source: https://dev.to/lingamsuyambu/connect-net-to-azure-sql-with-managed-identity-no-passwords-34oh
domain: SQL
relevance: 🟡
tags:
- '#library'
- '#sql'
- '#tool'
- '#tutorial'
related:
- '[[2026-11-08-azure-sql-database-vs-sql-server-on-azure-vm-cost-comparison-2026]]'
- '[[2026-08-26-redb-371-props-search-up-to-100x-faster-an-alternative-to-ef-core-or-a-companion-to-it]]'
- '[[2026-08-21-which-sql-database-should-you-install]]'
- '[[2026-10-29-isolation-levels-how-the-last-item-in-stock-gets-sold-twice]]'
- '[[2026-09-27-how-to-optimize-a-database-one-step-at-a-time]]'
- '[[2026-10-22-how-to-auto-update-an-updatedat-column-mysql-on-update-vs-a-database-trigger-vs-the-orm]]'
status: unread
---

> **TL;DR:** Originally published at SQL & Cloud Lab . This post was drafted with AI assistance. Connection strings with a SQL username and password end up in config files, pipelines and sometimes source control. With a managed ident…

## What’s new and why it matters
Originally published at SQL & Cloud Lab . This post was drafted with AI assistance. Connection strings with a SQL username and password end up in config files, pipelines and sometimes source control. With a managed identity , your Azure-hosted .NET app signs in to Azure SQL using Microsoft Entra ID (formerly Azure AD) and gets tokens automatically. There is no secret to store, rotate or leak. How it works Azure gives your App Service, Function App, container or VM an identity in Microsoft Entra ID. Your code asks for a token for that identity, and SQL Server accepts the token instead of a pass…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Write the query in a scratchpad and run EXPLAIN/QUERY PLAN to verify performance.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/lingamsuyambu/connect-net-to-azure-sql-with-managed-identity-no-passwords-34oh

## Related notes
- [[2026-11-08-azure-sql-database-vs-sql-server-on-azure-vm-cost-comparison-2026]]
- [[2026-08-26-redb-371-props-search-up-to-100x-faster-an-alternative-to-ef-core-or-a-companion-to-it]]
- [[2026-08-21-which-sql-database-should-you-install]]
- [[2026-10-29-isolation-levels-how-the-last-item-in-stock-gets-sold-twice]]
- [[2026-09-27-how-to-optimize-a-database-one-step-at-a-time]]
- [[2026-10-22-how-to-auto-update-an-updatedat-column-mysql-on-update-vs-a-database-trigger-vs-the-orm]]
