---
title: How I built a SaaS in 2 hours
date: '2026-07-27'
source: https://dev.to/supermiojo/how-i-built-a-saas-in-2-hours-20k1
domain: SQL
relevance: 🟡
tags:
- '#ai'
- '#feature'
- '#library'
- '#sql'
- '#tool'
related:
- '[[2026-03-17-from-0-to-production-ai-agent-in-30-minutes-full-stack-template-with-5-ai-frameworks]]'
- '[[2026-03-29-drizzle-orm-has-a-free-api-that-makes-sql-type-safe-without-the-magic]]'
- '[[2026-03-16-why-alembic-is-basically-git-for-your-database-and-why-you-need-it]]'
- '[[2026-05-13-design-review-live-sql-queries-on-postgresql]]'
- '[[2026-07-24-long-running-sql-queries-a-sample-exploration]]'
- '[[2026-03-24-stop-tuning-blind-query-observability-as-the-foundation-for-database-optimization]]'
status: unread
---

> **TL;DR:** So, I've built a few SaaS products over the last year, and the part that always takes the longest isn't the product, it's the plumbing. Auth, billing, database, dashboard, the stuff every SaaS needs before you write a si…

## What’s new and why it matters
So, I've built a few SaaS products over the last year, and the part that always takes the longest isn't the product, it's the plumbing. Auth, billing, database, dashboard, the stuff every SaaS needs before you write a single line of business logic. For anyone who cares; I stripped my production stack down to the essentials and turned it into a repeatable setup. Here's exactly what it looks like and how long each piece takes. The stack Next.js 14 with App Router + TypeScript NextAuth v4 , email/password + Google OAuth Stripe , subscription checkout + customer portal Prisma , type-safe ORM with…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Write the query in a scratchpad and run EXPLAIN/QUERY PLAN to verify performance.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/supermiojo/how-i-built-a-saas-in-2-hours-20k1

## Related notes
- [[2026-03-17-from-0-to-production-ai-agent-in-30-minutes-full-stack-template-with-5-ai-frameworks]]
- [[2026-03-29-drizzle-orm-has-a-free-api-that-makes-sql-type-safe-without-the-magic]]
- [[2026-03-16-why-alembic-is-basically-git-for-your-database-and-why-you-need-it]]
- [[2026-05-13-design-review-live-sql-queries-on-postgresql]]
- [[2026-07-24-long-running-sql-queries-a-sample-exploration]]
- [[2026-03-24-stop-tuning-blind-query-observability-as-the-foundation-for-database-optimization]]
