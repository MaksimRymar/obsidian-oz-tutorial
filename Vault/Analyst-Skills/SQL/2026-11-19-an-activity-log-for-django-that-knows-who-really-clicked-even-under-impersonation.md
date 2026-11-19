---
title: An activity log for Django that knows who really clicked, even under impersonation
date: '2026-11-19'
source: https://dev.to/ahmad_dogar_7d098f5e48f72/an-activity-log-for-django-that-knows-who-really-clicked-even-under-impersonation-1e9c
domain: SQL
relevance: 🟡
tags:
- '#ai'
- '#python'
- '#sql'
- '#tool'
- '#zendesk'
related:
- '[[2026-09-01-i-raced-six-models-against-each-other-on-digitalocean-inference-the-cheapest-one-won]]'
- '[[2026-10-26-48-hour-field-notes-my-free-box-looked-slow-until-i-logged-the-gap-between-requests]]'
- '[[2026-09-21-how-to-build-a-creator-emails-pipeline-in-one-python-call]]'
- '[[2026-10-11-your-chatgpt-api-bill-is-high-because-your-prompts-are-bloated-heres-a-free-checklist-to-fix-it]]'
- '[[2026-09-07-like-in-sql-explained-for-beginners]]'
- '[[2026-08-05-reconstructing-wallet-journeys-across-dex-frontends-one-chain-at-a-time]]'
status: unread
---

> **TL;DR:** Every B2B product reaches the day someone asks "who changed this quote?" and nobody can answer. In the Brava Roof Tile Pro Portal that question had a twist. Support staff can impersonate a contractor to help them, which…

## What’s new and why it matters
Every B2B product reaches the day someone asks "who changed this quote?" and nobody can answer. In the Brava Roof Tile Pro Portal that question had a twist. Support staff can impersonate a contractor to help them, which means the person logged in and the person who clicked are not the same. A log that stores request.user would blame the contractor for whatever support did. This post is about the activity log we built for the portal. It now spans 17 modules (quotes, leads, orders, pricebooks, proposals, chat, DocScan and more), and it is also where the analytics dashboard counts engagement. I w…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Write the query in a scratchpad and run EXPLAIN/QUERY PLAN to verify performance.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/ahmad_dogar_7d098f5e48f72/an-activity-log-for-django-that-knows-who-really-clicked-even-under-impersonation-1e9c

## Related notes
- [[2026-09-01-i-raced-six-models-against-each-other-on-digitalocean-inference-the-cheapest-one-won]]
- [[2026-10-26-48-hour-field-notes-my-free-box-looked-slow-until-i-logged-the-gap-between-requests]]
- [[2026-09-21-how-to-build-a-creator-emails-pipeline-in-one-python-call]]
- [[2026-10-11-your-chatgpt-api-bill-is-high-because-your-prompts-are-bloated-heres-a-free-checklist-to-fix-it]]
- [[2026-09-07-like-in-sql-explained-for-beginners]]
- [[2026-08-05-reconstructing-wallet-journeys-across-dex-frontends-one-chain-at-a-time]]
