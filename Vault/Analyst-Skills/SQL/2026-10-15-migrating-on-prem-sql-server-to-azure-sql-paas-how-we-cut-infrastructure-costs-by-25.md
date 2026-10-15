---
title: 'Migrating On-Prem SQL Server to Azure SQL PaaS: How We Cut Infrastructure
  Costs by 25%'
date: '2026-10-15'
source: https://dev.to/malavnaik_0381711024683d4/migrating-on-prem-sql-server-to-azure-sql-paas-how-we-cut-infrastructure-costs-by-25-2oo9
domain: SQL
relevance: 🟡
tags:
- '#feature'
- '#library'
- '#sql'
- '#tool'
related:
- '[[2026-08-21-how-to-find-duplicate-rows-in-sql-and-decide-what-counts-as-one]]'
- '[[2026-09-09-still-writing-slow-sql-queries-10-ways-to-improve-performance]]'
- '[[2026-07-24-how-i-cut-our-database-costs-by-40-with-one-config-change-connection-pooling-explained]]'
- '[[2026-05-31-i-didnt-have-a-pc-for-my-database-class-so-i-built-my-own-t-sql-sandbox-in-the-browser]]'
- '[[2026-04-15-how-to-build-a-strong-foundation-in-sql-and-databases-step-by-step]]'
- '[[2026-08-11-sql-aliases-how-to-read-a-query-out-loud]]'
status: unread
---

> **TL;DR:** At S&P Global Market Intelligence I helped migrate on-premise SQL Server databases to Azure SQL PaaS. Our team moved between 10 and 50 databases to Azure SQL Managed Instance. The headline result was a reduction in infra…

## What’s new and why it matters
At S&P Global Market Intelligence I helped migrate on-premise SQL Server databases to Azure SQL PaaS. Our team moved between 10 and 50 databases to Azure SQL Managed Instance. The headline result was a reduction in infrastructure costs of about 25%. The more important result was that the people using those databases barely noticed it happened. Here's what I learned about doing a migration like that well. 1. Inventory before you plan Before choosing a target, list everything that touches the database: ETL jobs, reports, linked servers, SQL Agent jobs, cross-database queries, CLR assemblies. Paa…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Write the query in a scratchpad and run EXPLAIN/QUERY PLAN to verify performance.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/malavnaik_0381711024683d4/migrating-on-prem-sql-server-to-azure-sql-paas-how-we-cut-infrastructure-costs-by-25-2oo9

## Related notes
- [[2026-08-21-how-to-find-duplicate-rows-in-sql-and-decide-what-counts-as-one]]
- [[2026-09-09-still-writing-slow-sql-queries-10-ways-to-improve-performance]]
- [[2026-07-24-how-i-cut-our-database-costs-by-40-with-one-config-change-connection-pooling-explained]]
- [[2026-05-31-i-didnt-have-a-pc-for-my-database-class-so-i-built-my-own-t-sql-sandbox-in-the-browser]]
- [[2026-04-15-how-to-build-a-strong-foundation-in-sql-and-databases-step-by-step]]
- [[2026-08-11-sql-aliases-how-to-read-a-query-out-loud]]
