---
title: 'Dev log #26 Deep in the libp2p weeds: Fixing DHT prefixes and Yamux resets'
date: '2026-10-20'
source: https://dev.to/yashksaini/dev-log-26-deep-in-the-libp2p-weeds-fixing-dht-prefixes-and-yamux-resets-315n
domain: Tableau
relevance: 🔴
tags:
- '#feature'
- '#library'
- '#python'
- '#tableau'
- '#tool'
related:
- '[[2026-09-28-i-kept-hitting-supabase-errors-so-i-built-a-scanner-for-the-legacy-api-key-deprecation-published-false]]'
- '[[2026-04-17-maybe-this-is-how-open-source-apps-are-born]]'
- '[[2026-05-26-from-screen-recording-to-test-cases-in-seconds-meet-clipcase]]'
- '[[2026-06-24-i-got-tired-of-cryptic-python-error-messages-so-i-built-a-vs-code-extension-that-fixes-them-automatically]]'
- '[[2026-06-15-day-01-of-learning-data-engineering-step1-sql-joins-and-set-operators]]'
- '[[2026-05-31-i-didnt-have-a-pc-for-my-database-class-so-i-built-my-own-t-sql-sandbox-in-the-browser]]'
status: unread
---

> **TL;DR:** Hi, glad you found your way here. I'm Yash, a developer who contributes to open source, mostly p2p networking and AI tooling. Each week I write up what I shipped, what broke, and what fixing it taught me. GitHub · X · Li…

## What’s new and why it matters
Hi, glad you found your way here. I'm Yash, a developer who contributes to open source, mostly p2p networking and AI tooling. Each week I write up what I shipped, what broke, and what fixing it taught me. GitHub · X · LinkedIn · Portfolio TL;DR I spent the week chasing ghosts in the networking stack, specifically focusing on the Python libp2p implementation. It was one of those weeks where you don't necessarily ship a brand-new feature, but you find the cracks in the foundation and start patching them up. I opened two significant PRs to fix protocol-level bugs in Kademlia and Yamux, and flagge…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Add a short note: what changed in your workflow?

## Relevance
🔴

## Source
https://dev.to/yashksaini/dev-log-26-deep-in-the-libp2p-weeds-fixing-dht-prefixes-and-yamux-resets-315n

## Related notes
- [[2026-09-28-i-kept-hitting-supabase-errors-so-i-built-a-scanner-for-the-legacy-api-key-deprecation-published-false]]
- [[2026-04-17-maybe-this-is-how-open-source-apps-are-born]]
- [[2026-05-26-from-screen-recording-to-test-cases-in-seconds-meet-clipcase]]
- [[2026-06-24-i-got-tired-of-cryptic-python-error-messages-so-i-built-a-vs-code-extension-that-fixes-them-automatically]]
- [[2026-06-15-day-01-of-learning-data-engineering-step1-sql-joins-and-set-operators]]
- [[2026-05-31-i-didnt-have-a-pc-for-my-database-class-so-i-built-my-own-t-sql-sandbox-in-the-browser]]
