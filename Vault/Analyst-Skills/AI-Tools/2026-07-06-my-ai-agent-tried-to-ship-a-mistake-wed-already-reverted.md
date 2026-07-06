---
title: My AI agent tried to ship a mistake we'd already reverted
date: '2026-07-06'
source: https://dev.to/masondelan/my-ai-agent-tried-to-ship-a-mistake-wed-already-reverted-4737
domain: AI-Tools
relevance: 🟡
tags:
- '#ai'
- '#sql'
- '#support-analytics'
- '#tool'
related:
- '[[2026-05-04-why-we-chose-self-hosted-ai-over-cloud-for-business-data-posted-by-the-ragleap-team-building-ragleap-a-private-server-ai]]'
- '[[2026-04-16-whats-eating-your-claude-code-context-window-i-wrote-a-500-line-python-script-to-find-out]]'
- '[[2026-03-23-i-was-so-tired-of-my-ai-agent-starting-from-zero-every-single-session]]'
- '[[2026-04-13-your-claude-code-and-cursor-agents-have-amnesia-heres-the-fix]]'
- '[[2026-04-10-i-built-a-local-ai-coding-system-that-actually-understands-your-codebase-heres-what-i-learned]]'
- '[[2026-05-31-i-didnt-have-a-pc-for-my-database-class-so-i-built-my-own-t-sql-sandbox-in-the-browser]]'
status: unread
---

> **TL;DR:** A month ago we added a card_token column to the users table so a background job could retry failed Pro charges. It lasted about two days. Storing card data in your own database drops you into PCI-DSS (the compliance stan…

## What’s new and why it matters
A month ago we added a card_token column to the users table so a background job could retry failed Pro charges. It lasted about two days. Storing card data in your own database drops you into PCI-DSS (the compliance standard that kicks in the moment card data touches your systems), so we pulled it and moved to Stripe-managed payment methods. Last week the charges started failing again. New Claude Code session, no memory of any of that. Its plan? Add a card_token column to users and retry. I don't really blame the agent. It had the context the first time and it was right. The problem is that co…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Reproduce the example in a notebook; then refactor into a reusable function.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/masondelan/my-ai-agent-tried-to-ship-a-mistake-wed-already-reverted-4737

## Related notes
- [[2026-05-04-why-we-chose-self-hosted-ai-over-cloud-for-business-data-posted-by-the-ragleap-team-building-ragleap-a-private-server-ai]]
- [[2026-04-16-whats-eating-your-claude-code-context-window-i-wrote-a-500-line-python-script-to-find-out]]
- [[2026-03-23-i-was-so-tired-of-my-ai-agent-starting-from-zero-every-single-session]]
- [[2026-04-13-your-claude-code-and-cursor-agents-have-amnesia-heres-the-fix]]
- [[2026-04-10-i-built-a-local-ai-coding-system-that-actually-understands-your-codebase-heres-what-i-learned]]
- [[2026-05-31-i-didnt-have-a-pc-for-my-database-class-so-i-built-my-own-t-sql-sandbox-in-the-browser]]
