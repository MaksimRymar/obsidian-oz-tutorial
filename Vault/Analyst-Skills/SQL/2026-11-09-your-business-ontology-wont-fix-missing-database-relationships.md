---
title: Your Business Ontology Won't Fix Missing Database Relationships
date: '2026-11-09'
source: https://dev.to/arisyndata/your-business-ontology-wont-fix-missing-database-relationships-54gp
domain: SQL
relevance: 🟡
tags:
- '#ai'
- '#best-practice'
- '#career'
- '#sql'
- '#tool'
related:
- '[[2026-06-11-why-text-to-sql-needs-table-relationship-discovery-before-sql-generation]]'
- '[[2026-06-15-why-text-to-sql-needs-join-path-context-not-just-schema]]'
- '[[2026-09-07-the-semantic-cold-start-problem-in-enterprise-data-agents]]'
- '[[2026-06-08-designing-relationship-context-for-text-to-sql-systems]]'
- '[[2026-10-06-i-scanned-1152-dbt-models-for-joins-that-inflate-sum-here-is-what-i-found]]'
- '[[2026-09-15-sql-joins-explained]]'
status: unread
---

> **TL;DR:** An ontology can describe what a customer, contract, or payment means. It cannot, by itself, prove which columns should be joined. Business ontology is getting a lot of attention in enterprise AI. That is a welcome develo…

## What’s new and why it matters
An ontology can describe what a customer, contract, or payment means. It cannot, by itself, prove which columns should be joined. Business ontology is getting a lot of attention in enterprise AI. That is a welcome development. Models need more than table names: they need definitions of customers, contracts, revenue, and the rules behind those terms. But there is a problem that tends to appear one layer below the ontology. You can define every business entity correctly and still generate the wrong SQL. The reason is surprisingly mundane: the database does not always tell you how its tables conn…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Write the query in a scratchpad and run EXPLAIN/QUERY PLAN to verify performance.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/arisyndata/your-business-ontology-wont-fix-missing-database-relationships-54gp

## Related notes
- [[2026-06-11-why-text-to-sql-needs-table-relationship-discovery-before-sql-generation]]
- [[2026-06-15-why-text-to-sql-needs-join-path-context-not-just-schema]]
- [[2026-09-07-the-semantic-cold-start-problem-in-enterprise-data-agents]]
- [[2026-06-08-designing-relationship-context-for-text-to-sql-systems]]
- [[2026-10-06-i-scanned-1152-dbt-models-for-joins-that-inflate-sum-here-is-what-i-found]]
- [[2026-09-15-sql-joins-explained]]
