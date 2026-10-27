---
title: infinite recursion detected in policy for relation (42P17)
date: '2026-10-27'
source: https://dev.to/builtsafely-org/infinite-recursion-detected-in-policy-for-relation-42p17-2c6f
domain: SQL
relevance: 🔴
tags:
- '#ai'
- '#best-practice'
- '#sql'
- '#tool'
- '#tutorial'
related:
- '[[2026-05-24-infinite-recursion-in-postgres-rls-a-security-definer-gotcha]]'
- '[[2026-08-11-the-text-to-sql-demo-takes-an-afternoon-the-other-90-is-why-you-should-buy-it]]'
- '[[2026-09-07-your-text-to-sql-agent-picks-tables-before-security-runs-heres-the-fix]]'
- '[[2026-08-20-read-only-by-design-letting-ai-explore-your-database-without-the-risk-of-writes]]'
- '[[2026-10-02-your-rls-policy-returns-zero-rows-the-view-next-to-it-returns-two]]'
- '[[2026-08-21-how-to-find-duplicate-rows-in-sql-and-decide-what-counts-as-one]]'
status: unread
---

> **TL;DR:** If your Supabase queries suddenly fail with "infinite recursion detected in policy for relation", the cause is almost always a row-level security policy that ends up checking itself. The tempting shortcut is to switch RL…

## What’s new and why it matters
If your Supabase queries suddenly fail with "infinite recursion detected in policy for relation", the cause is almost always a row-level security policy that ends up checking itself. The tempting shortcut is to switch RLS off, which removes the error by removing your access rules. Below is the fix we tested instead: move the lookup into a small private helper function and keep RLS on. AI disclosure: This article was written with AI. An AI agent adapted it from our original guide, and every claim links to the official source it came from. Steps marked Verified were run by us in a throwaway test…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Write the query in a scratchpad and run EXPLAIN/QUERY PLAN to verify performance.
- Add a short note: what changed in your workflow?

## Relevance
🔴

## Source
https://dev.to/builtsafely-org/infinite-recursion-detected-in-policy-for-relation-42p17-2c6f

## Related notes
- [[2026-05-24-infinite-recursion-in-postgres-rls-a-security-definer-gotcha]]
- [[2026-08-11-the-text-to-sql-demo-takes-an-afternoon-the-other-90-is-why-you-should-buy-it]]
- [[2026-09-07-your-text-to-sql-agent-picks-tables-before-security-runs-heres-the-fix]]
- [[2026-08-20-read-only-by-design-letting-ai-explore-your-database-without-the-risk-of-writes]]
- [[2026-10-02-your-rls-policy-returns-zero-rows-the-view-next-to-it-returns-two]]
- [[2026-08-21-how-to-find-duplicate-rows-in-sql-and-decide-what-counts-as-one]]
