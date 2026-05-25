---
title: 'Infinite recursion in Postgres RLS: a SECURITY DEFINER gotcha'
date: '2026-05-24'
source: https://dev.to/bairescodeai/infinite-recursion-in-postgres-rls-a-security-definer-gotcha-1916
domain: SQL
relevance: 🔴
tags:
- '#sql'
- '#tool'
- '#zendesk'
related:
- '[[2026-04-29-postgresql-subquery-and-cte-optimization]]'
- '[[2026-04-17-maybe-this-is-how-open-source-apps-are-born]]'
- '[[2026-03-11-i-thought-my-rails-query-was-fine-until-null-ate-my-data]]'
- '[[2026-02-22-what-mongodb-taught-me-about-postgres]]'
- '[[2026-05-18-top-orm-tools-practical-comparison]]'
- '[[2026-05-04-sql-subqueries-vs-ctes]]'
status: unread
---

> **TL;DR:** Spent a few hours yesterday on what looked like a haunted Postgres bug. Sharing the fix in case someone else hits it. The setup I had a multi-tenant app with a profiles table. I wanted "team admins can see all team profi…

## What’s new and why it matters
Spent a few hours yesterday on what looked like a haunted Postgres bug. Sharing the fix in case someone else hits it. The setup I had a multi-tenant app with a profiles table. I wanted "team admins can see all team profiles". Naive policy: sql CREATE POLICY "admin_sees_team" ON public.profiles FOR SELECT TO authenticated USING ( team_id IS NOT NULL AND EXISTS ( SELECT 1 FROM public.profiles me WHERE me.id = auth.uid() AND me.role = 'admin' ) ); Looks innocent, right? The bug Every query against profiles returned: ERROR: 42P17: infinite recursion detected in policy for relation "profiles" The p…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Write the query in a scratchpad and run EXPLAIN/QUERY PLAN to verify performance.
- Add a short note: what changed in your workflow?

## Relevance
🔴

## Source
https://dev.to/bairescodeai/infinite-recursion-in-postgres-rls-a-security-definer-gotcha-1916

## Related notes
- [[2026-04-29-postgresql-subquery-and-cte-optimization]]
- [[2026-04-17-maybe-this-is-how-open-source-apps-are-born]]
- [[2026-03-11-i-thought-my-rails-query-was-fine-until-null-ate-my-data]]
- [[2026-02-22-what-mongodb-taught-me-about-postgres]]
- [[2026-05-18-top-orm-tools-practical-comparison]]
- [[2026-05-04-sql-subqueries-vs-ctes]]
