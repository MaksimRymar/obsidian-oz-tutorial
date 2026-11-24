---
title: Designing PostgreSQL RLS with permissive and restrictive policies
date: '2026-11-24'
source: https://dev.to/chriserodriguez/designing-postgresql-rls-with-permissive-and-restrictive-policies-3me3
domain: SQL
relevance: 🔴
tags:
- '#sql'
- '#tool'
- '#zendesk'
related:
- '[[2026-10-29-use-insert-with-check-and-update-using-to-allow-owner-on-create-but-block-owner-transfers]]'
- '[[2026-03-08-understanding-group-by-in-sql]]'
- '[[2026-08-27-i-gave-an-llm-the-keys-to-a-multi-tenant-database]]'
- '[[2026-09-12-unclassified-tests-cannot-green-an-agent-patch]]'
- '[[2026-09-01-i-raced-six-models-against-each-other-on-digitalocean-inference-the-cheapest-one-won]]'
- '[[2026-11-18-query-a-csv-file-with-sql-without-setting-up-a-database]]'
status: unread
---

> **TL;DR:** PostgreSQL RLS policies do not compete for precedence. For each command and role, PostgreSQL gathers the applicable policies and combines them by policy mode: permissive policies form an OR group, while restrictive polic…

## What’s new and why it matters
PostgreSQL RLS policies do not compete for precedence. For each command and role, PostgreSQL gathers the applicable policies and combines them by policy mode: permissive policies form an OR group, while restrictive policies form an AND group. The effective decision is therefore “at least one permissive rule passes, and every restrictive rule passes.” A small tenant-records design makes the distinction concrete. Put tenant ownership in a permissive policy: it establishes the rows the current caller may consider. Put the active-record requirement in a restrictive policy: it narrows those candida…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Write the query in a scratchpad and run EXPLAIN/QUERY PLAN to verify performance.
- Add a short note: what changed in your workflow?

## Relevance
🔴

## Source
https://dev.to/chriserodriguez/designing-postgresql-rls-with-permissive-and-restrictive-policies-3me3

## Related notes
- [[2026-10-29-use-insert-with-check-and-update-using-to-allow-owner-on-create-but-block-owner-transfers]]
- [[2026-03-08-understanding-group-by-in-sql]]
- [[2026-08-27-i-gave-an-llm-the-keys-to-a-multi-tenant-database]]
- [[2026-09-12-unclassified-tests-cannot-green-an-agent-patch]]
- [[2026-09-01-i-raced-six-models-against-each-other-on-digitalocean-inference-the-cheapest-one-won]]
- [[2026-11-18-query-a-csv-file-with-sql-without-setting-up-a-database]]
