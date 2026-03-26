---
title: Version 2 of the Audit Script for SQL Server
date: '2026-03-26'
source: https://dev.to/greenmtnsun/version-2-of-the-audit-script-for-sql-server-1e7k
domain: SQL
relevance: 🟡
tags:
- '#ai'
- '#feature'
- '#sql'
- '#tool'
- '#zendesk'
related:
- '[[2026-03-15-sql-for-generating-test-data-in-mysql]]'
- '[[2026-03-26-sqlite-is-enough-for-your-side-project-full-text-search-json-and-wal-mode-included]]'
- '[[2026-03-25-the-only-sql-cheatsheet-youll-ever-need-with-real-examples]]'
- '[[2026-02-21-sql-masterclass]]'
- '[[2026-03-10-duckdb-150-released-new-features-and-tools-enhance-performance-and-functionality]]'
- '[[2026-02-24-countcolumn-vs-count-in-sql-with-inner-left-right-full-join-explained]]'
status: unread
---

> **TL;DR:** <# ways to call it. .\Invoke-SqlServerNewInstallAudit_dbatools_v3.ps1 -SqlInstance "MyServer\SQL2022" -OutputPath "C:\Temp\SqlAudit.html" $cred = Get-Credential .\Invoke-SqlServerNewInstallAudit_dbatools_v3.ps1 -SqlInsta…

## What’s new and why it matters
<# ways to call it. .\Invoke-SqlServerNewInstallAudit_dbatools_v3.ps1 -SqlInstance "MyServer\SQL2022" -OutputPath "C:\Temp\SqlAudit.html" $cred = Get-Credential .\Invoke-SqlServerNewInstallAudit_dbatools_v3.ps1 -SqlInstance "MyServer\SQL2022" -SqlCredential $cred ` -OutputPath "C:\Temp\SqlAudit.html" $cred = Get-Credential .\Invoke-SqlServerNewInstallAudit_dbatools_v3.ps1 -SqlInstance "MyServer\SQL2022" -SqlCredential $cred ` -OutputPath "C:\Temp\SqlAudit.html" > [CmdletBinding()] param( [Parameter(Mandatory)] [string]$SqlInstance, [PSCredential]$SqlCredential, [string]$OutputPath = ".\SqlServ…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Write the query in a scratchpad and run EXPLAIN/QUERY PLAN to verify performance.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/greenmtnsun/version-2-of-the-audit-script-for-sql-server-1e7k

## Related notes
- [[2026-03-15-sql-for-generating-test-data-in-mysql]]
- [[2026-03-26-sqlite-is-enough-for-your-side-project-full-text-search-json-and-wal-mode-included]]
- [[2026-03-25-the-only-sql-cheatsheet-youll-ever-need-with-real-examples]]
- [[2026-02-21-sql-masterclass]]
- [[2026-03-10-duckdb-150-released-new-features-and-tools-enhance-performance-and-functionality]]
- [[2026-02-24-countcolumn-vs-count-in-sql-with-inner-left-right-full-join-explained]]
