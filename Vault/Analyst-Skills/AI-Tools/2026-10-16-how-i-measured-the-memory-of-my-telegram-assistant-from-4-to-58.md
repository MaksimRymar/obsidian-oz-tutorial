---
title: How I measured the memory of my Telegram assistant, from 4% to 58%
date: '2026-10-16'
source: https://dev.to/0xdevdav/how-i-measured-the-memory-of-my-telegram-assistant-from-4-to-58-2lao
domain: AI-Tools
relevance: 🟡
tags:
- '#ai'
- '#sql'
- '#tool'
- '#zendesk'
related:
- '[[2026-09-04-i-built-an-offline-document-indexer-and-ollama-taught-me-two-things-i-did-not-expect]]'
- '[[2026-09-28-set-based-vs-row-by-row-postgresql-refresh-from-114-to-12-seconds]]'
- '[[2026-10-15-see-every-google-ad-a-competitor-runs-from-just-their-domain-curl-python-n8n]]'
- '[[2026-07-14-i-got-tired-of-bad-fanfiction-recommendations-so-im-building-my-own-taste-engine]]'
- '[[2026-09-23-one-real-scan-counts-a-hundred-ranking-a-curation-queue-by-your-own-users]]'
- '[[2026-08-11-sql-aliases-how-to-read-a-query-out-loud]]'
status: unread
---

> **TL;DR:** Zoe is a personal assistant I talk to on Telegram. She runs on my own server on top of the Claude Code CLI: every message becomes a claude -p run, and a SQLite queue in front of it makes sure nothing is lost when a turn…

## What’s new and why it matters
Zoe is a personal assistant I talk to on Telegram. She runs on my own server on top of the Claude Code CLI: every message becomes a claude -p run, and a SQLite queue in front of it makes sure nothing is lost when a turn hangs or the service restarts. The code is MIT and on GitHub: https://github.com/0xDevDav/zoe This post is about the part that took the most work: her memory, and how I found out that my first version barely worked. Memory as neurons and synapses Every fact, preference, habit or correction Zoe learns is a neuron, a row in SQLite. Neurons learned in the same conversation are lin…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Reproduce the example in a notebook; then refactor into a reusable function.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/0xdevdav/how-i-measured-the-memory-of-my-telegram-assistant-from-4-to-58-2lao

## Related notes
- [[2026-09-04-i-built-an-offline-document-indexer-and-ollama-taught-me-two-things-i-did-not-expect]]
- [[2026-09-28-set-based-vs-row-by-row-postgresql-refresh-from-114-to-12-seconds]]
- [[2026-10-15-see-every-google-ad-a-competitor-runs-from-just-their-domain-curl-python-n8n]]
- [[2026-07-14-i-got-tired-of-bad-fanfiction-recommendations-so-im-building-my-own-taste-engine]]
- [[2026-09-23-one-real-scan-counts-a-hundred-ranking-a-curation-queue-by-your-own-users]]
- [[2026-08-11-sql-aliases-how-to-read-a-query-out-loud]]
