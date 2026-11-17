---
title: 'Postgres RLS 42P17: infinite recursion in a policy, and the fix that keeps
  the policy'
date: '2026-11-17'
source: https://dev.to/rshday/postgres-rls-42p17-infinite-recursion-in-a-policy-and-the-fix-that-keeps-the-policy-26ln
domain: SQL
relevance: 🔴
tags:
- '#ai'
- '#sql'
- '#tool'
related:
- '[[2026-10-26-supabase-42501-permission-denied-is-a-grant-problem-not-rls]]'
- '[[2026-05-24-infinite-recursion-in-postgres-rls-a-security-definer-gotcha]]'
- '[[2026-09-30-a-stored-procedure-can-compile-and-still-change-its-meaning]]'
- '[[2026-10-16-an-ai-explained-sql-group-by-in-four-lines-one-of-them-is-wrong]]'
- '[[2026-08-18-a-generated-sql-query-got-faster-by-returning-fewer-rows-test-that-before-you-merge-it]]'
- '[[2026-10-15-sql-joins-explained-with-one-tiny-dataset-plus-5-interview-questions]]'
status: unread
---

> **TL;DR:** A shortened version of the full write-up: Postgres RLS 42P17: infinite recursion detected in policy . ERROR: 42P17: infinite recursion detected in policy for relation "members" — usually wrapped by Supabase as a 500 with…

## What’s new and why it matters
A shortened version of the full write-up: Postgres RLS 42P17: infinite recursion detected in policy . ERROR: 42P17: infinite recursion detected in policy for relation "members" — usually wrapped by Supabase as a 500 with code: "42P17" . The policy looks correct: it checks membership by querying the membership table. That is exactly the problem. Mistake Symptom Fix Policy on members reads members 42P17 on every select SECURITY DEFINER helper function UPDATE policy with no SELECT policy update ... returning * returns 0 rows add the SELECT policy Function without security definer still recurses c…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Write the query in a scratchpad and run EXPLAIN/QUERY PLAN to verify performance.
- Add a short note: what changed in your workflow?

## Relevance
🔴

## Source
https://dev.to/rshday/postgres-rls-42p17-infinite-recursion-in-a-policy-and-the-fix-that-keeps-the-policy-26ln

## Related notes
- [[2026-10-26-supabase-42501-permission-denied-is-a-grant-problem-not-rls]]
- [[2026-05-24-infinite-recursion-in-postgres-rls-a-security-definer-gotcha]]
- [[2026-09-30-a-stored-procedure-can-compile-and-still-change-its-meaning]]
- [[2026-10-16-an-ai-explained-sql-group-by-in-four-lines-one-of-them-is-wrong]]
- [[2026-08-18-a-generated-sql-query-got-faster-by-returning-fewer-rows-test-that-before-you-merge-it]]
- [[2026-10-15-sql-joins-explained-with-one-tiny-dataset-plus-5-interview-questions]]
