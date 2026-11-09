---
title: My Solana buy bot doubled every buy amount. Here's the post-mortem.
date: '2026-11-09'
source: https://dev.to/opsnode_dev/my-solana-buy-bot-doubled-every-buy-amount-heres-the-post-mortem-2dea
domain: SQL
relevance: 🟡
tags:
- '#library'
- '#python'
- '#sql'
- '#tool'
- '#zendesk'
related:
- '[[2026-11-05-your-ai-says-fixed-would-a-test-notice-if-it-wasnt]]'
- '[[2026-04-03-i-got-tired-of-watching-my-terminal-so-i-built-guga]]'
- '[[2026-10-15-on-windows-four-processes-appending-to-one-file-lost-37-of-200-lines]]'
- '[[2026-09-27-i-built-an-ai-agent-that-snapshots-every-edit-and-runs-your-tests-before-it-says-done]]'
- '[[2026-10-09-dont-let-a-new-signal-engine-write-fake-trades-a-warm-up-flag-for-trading-alert-bots]]'
- '[[2026-07-21-my-gitignore-had-a-blanket-rule-one-file-broke-it-and-no-pattern-would-have-caught-that]]'
status: unread
---

> **TL;DR:** In October I audited the first version of the buy bot I was selling. I found 5 bugs. One of them doubled every buy amount . Another made the bot post zero alerts on the exact setup most buyers use: a Linux VPS. I stopped…

## What’s new and why it matters
In October I audited the first version of the buy bot I was selling. I found 5 bugs. One of them doubled every buy amount . Another made the bot post zero alerts on the exact setup most buyers use: a Linux VPS. I stopped selling v1 the same week and rewrote it from scratch. This is everything that went wrong, how I fixed it, and the code you need if you're building anything that reads Solana swaps. What v1 was A Python bot that watches a Solana token and posts buys to Telegram or Discord. It was aimed at traders. It worked on my machine, which, as you'll see, was the problem. The 5 bugs 1. Eve…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Write the query in a scratchpad and run EXPLAIN/QUERY PLAN to verify performance.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/opsnode_dev/my-solana-buy-bot-doubled-every-buy-amount-heres-the-post-mortem-2dea

## Related notes
- [[2026-11-05-your-ai-says-fixed-would-a-test-notice-if-it-wasnt]]
- [[2026-04-03-i-got-tired-of-watching-my-terminal-so-i-built-guga]]
- [[2026-10-15-on-windows-four-processes-appending-to-one-file-lost-37-of-200-lines]]
- [[2026-09-27-i-built-an-ai-agent-that-snapshots-every-edit-and-runs-your-tests-before-it-says-done]]
- [[2026-10-09-dont-let-a-new-signal-engine-write-fake-trades-a-warm-up-flag-for-trading-alert-bots]]
- [[2026-07-21-my-gitignore-had-a-blanket-rule-one-file-broke-it-and-no-pattern-would-have-caught-that]]
