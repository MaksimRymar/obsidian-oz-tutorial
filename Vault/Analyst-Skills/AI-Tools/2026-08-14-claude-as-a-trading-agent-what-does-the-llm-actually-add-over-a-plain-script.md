---
title: 'Claude as a trading agent: what does the LLM actually add over a plain script?'
date: '2026-08-14'
source: https://dev.to/shenao_yu_e15c14815264a44/claude-as-a-trading-agent-what-does-the-llm-actually-add-over-a-plain-script-21l2
domain: AI-Tools
relevance: 🟡
tags:
- '#ai'
- '#python'
- '#sql'
- '#tool'
related:
- '[[2026-02-22-i-built-an-ai-system-that-generates-trading-signals-across-4-stock-markets-heres-how]]'
- '[[2026-04-21-what-happens-to-your-mutual-fund-between-9-am-and-9-pm]]'
- '[[2026-04-21-i-build-custom-trading-bots-for-deriv-and-mt4mt5-heres-what-that-actually-looks-like]]'
- '[[2026-08-02-how-i-built-relay-an-ast-based-latency-auditor-for-python-ai-agents]]'
- '[[2026-03-08-building-autonomous-ai-agents-that-actually-do-work]]'
- '[[2026-06-21-product-analytics-with-sql-tracking-what-actually-matters]]'
status: unread
---

> **TL;DR:** This came up in Chinese AI developer communities this week, and the numbers are almost beside the point. A physics researcher (no CS background, no finance training) connected Claude to a US brokerage account via API, wr…

## What’s new and why it matters
This came up in Chinese AI developer communities this week, and the numbers are almost beside the point. A physics researcher (no CS background, no finance training) connected Claude to a US brokerage account via API, wrote a simple automated trading strategy, and ran a live experiment for one week with $500. The rules were deliberately conservative: long equities only, no margin, no futures, no shorting, no HFT. "You can't earn beyond your own understanding," the author wrote, "so I only do things I can understand." After seven trading days: $510.65, up 2.20%. VOO returned 1.88% that week. QQ…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Reproduce the example in a notebook; then refactor into a reusable function.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/shenao_yu_e15c14815264a44/claude-as-a-trading-agent-what-does-the-llm-actually-add-over-a-plain-script-21l2

## Related notes
- [[2026-02-22-i-built-an-ai-system-that-generates-trading-signals-across-4-stock-markets-heres-how]]
- [[2026-04-21-what-happens-to-your-mutual-fund-between-9-am-and-9-pm]]
- [[2026-04-21-i-build-custom-trading-bots-for-deriv-and-mt4mt5-heres-what-that-actually-looks-like]]
- [[2026-08-02-how-i-built-relay-an-ast-based-latency-auditor-for-python-ai-agents]]
- [[2026-03-08-building-autonomous-ai-agents-that-actually-do-work]]
- [[2026-06-21-product-analytics-with-sql-tracking-what-actually-matters]]
