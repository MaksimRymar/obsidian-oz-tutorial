---
title: 'Share the Schema, Not the Password: How Schema-Aware AI Stops Inventing Columns'
date: '2026-09-06'
source: https://dev.to/vivekdraxlr/share-the-schema-not-the-password-how-schema-aware-ai-stops-inventing-columns-5ei7
domain: AI-Tools
relevance: 🟡
tags:
- '#ai'
- '#best-practice'
- '#presentations'
- '#sql'
- '#tool'
related:
- '[[2026-07-06-stop-pasting-your-database-schema-into-every-ai-prompt]]'
- '[[2026-08-17-what-is-mcp-and-why-should-anyone-working-with-a-database-care]]'
- '[[2026-08-24-how-to-connect-an-ai-assistant-to-your-sql-database-safely]]'
- '[[2026-08-28-an-erd-mcp-server-ai-agents-that-follow-your-naming-standard]]'
- '[[2026-07-31-why-ai-keeps-inventing-columns-that-dont-exist-and-how-to-stop-it]]'
- '[[2026-05-04-why-we-chose-self-hosted-ai-over-cloud-for-business-data-posted-by-the-ragleap-team-building-ragleap-a-private-server-ai]]'
status: unread
---

> **TL;DR:** You ask an AI assistant, "How many active subscriptions did we add last month?" It confidently returns a query: SELECT COUNT ( * ) FROM subscriptions WHERE status = 'active' AND signup_date >= '2026-08-01' ; Clean, reada…

## What’s new and why it matters
You ask an AI assistant, "How many active subscriptions did we add last month?" It confidently returns a query: SELECT COUNT ( * ) FROM subscriptions WHERE status = 'active' AND signup_date >= '2026-08-01' ; Clean, readable, and completely wrong for your database. Your table calls the column created_at , not signup_date . There is no status column — you track state in canceled_at IS NULL . The query either fails loudly with column "signup_date" does not exist , or worse, it runs against a lookalike column and hands you a confident, incorrect number that nobody catches until it's in a board dec…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Reproduce the example in a notebook; then refactor into a reusable function.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/vivekdraxlr/share-the-schema-not-the-password-how-schema-aware-ai-stops-inventing-columns-5ei7

## Related notes
- [[2026-07-06-stop-pasting-your-database-schema-into-every-ai-prompt]]
- [[2026-08-17-what-is-mcp-and-why-should-anyone-working-with-a-database-care]]
- [[2026-08-24-how-to-connect-an-ai-assistant-to-your-sql-database-safely]]
- [[2026-08-28-an-erd-mcp-server-ai-agents-that-follow-your-naming-standard]]
- [[2026-07-31-why-ai-keeps-inventing-columns-that-dont-exist-and-how-to-stop-it]]
- [[2026-05-04-why-we-chose-self-hosted-ai-over-cloud-for-business-data-posted-by-the-ragleap-team-building-ragleap-a-private-server-ai]]
