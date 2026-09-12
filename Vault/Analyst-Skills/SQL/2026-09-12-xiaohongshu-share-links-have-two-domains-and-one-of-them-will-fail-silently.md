---
title: Xiaohongshu share links have two domains, and one of them will fail silently
date: '2026-09-12'
source: https://dev.to/programming_withjackche/xiaohongshu-share-links-have-two-domains-and-one-of-them-will-fail-silently-hpd
domain: SQL
relevance: 🟡
tags:
- '#ai'
- '#python'
- '#sql'
- '#tool'
related:
- '[[2026-09-12-what-it-actually-takes-to-read-a-xiaohongshu-post-from-a-server]]'
- '[[2026-09-04-i-built-an-offline-document-indexer-and-ollama-taught-me-two-things-i-did-not-expect]]'
- '[[2026-04-22-your-pytest-retries-are-lying-to-you-the-hidden-cost-of---reruns-and-the-plugin-i-wrote-so-i-could-actually-see-what-my-]]'
- '[[2026-09-09-six-tables-out-of-260]]'
- '[[2026-08-27-a-longmemeval-s-number-you-can-reproduce]]'
- '[[2026-08-31-i-left-an-ai-agent-running-unattended-for-a-day-here-is-everything-that-broke]]'
status: unread
---

> **TL;DR:** Originally published at linkdigest.dev , where I build this. Every number here came from a live link on 2026-09-08 and 2026-09-10. The failure described is one this service shipped to a real user. If you have a host tabl…

## What’s new and why it matters
Originally published at linkdigest.dev , where I build this. Every number here came from a live link on 2026-09-08 and 2026-09-10. The failure described is one this service shipped to a real user. If you have a host table that maps domains to platforms, and Xiaohongshu is in it, check what you wrote. There is a good chance it says xhslink.com and nothing else. That was true here, and it cost us the first person who ever signed up. Two domains, same platform Share a note from the Xiaohongshu iOS app today and the clipboard gets something like: https://xhslink.cn/o/AxnRePgIokn Older shares, and…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Write the query in a scratchpad and run EXPLAIN/QUERY PLAN to verify performance.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/programming_withjackche/xiaohongshu-share-links-have-two-domains-and-one-of-them-will-fail-silently-hpd

## Related notes
- [[2026-09-12-what-it-actually-takes-to-read-a-xiaohongshu-post-from-a-server]]
- [[2026-09-04-i-built-an-offline-document-indexer-and-ollama-taught-me-two-things-i-did-not-expect]]
- [[2026-04-22-your-pytest-retries-are-lying-to-you-the-hidden-cost-of---reruns-and-the-plugin-i-wrote-so-i-could-actually-see-what-my-]]
- [[2026-09-09-six-tables-out-of-260]]
- [[2026-08-27-a-longmemeval-s-number-you-can-reproduce]]
- [[2026-08-31-i-left-an-ai-agent-running-unattended-for-a-day-here-is-everything-that-broke]]
