---
title: Tracking Codex Astra costs took more than updating a price table
date: '2026-09-06'
source: https://dev.to/shikiyusuke/tracking-codex-astra-costs-took-more-than-updating-a-price-table-3p3i
domain: AI-Tools
relevance: 🔴
tags:
- '#ai'
- '#feature'
- '#library'
- '#sql'
- '#tool'
related:
- '[[2026-08-21-how-to-find-duplicate-rows-in-sql-and-decide-what-counts-as-one]]'
- '[[2026-08-31-running-total-in-sql-the-window-frame-that-decides-the-answer]]'
- '[[2026-04-06-i-built-an-open-source-finops-layer-for-genai-apis-real-time-usd-cost-per-otel-span-multi-tenant-isolation-zero-prompt-l]]'
- '[[2026-08-31-how-to-reconcile-two-tables-in-sql-when-the-row-counts-match]]'
- '[[2026-08-31-i-left-an-ai-agent-running-unattended-for-a-day-here-is-everything-that-broke]]'
- '[[2026-06-24-i-am-not-a-developer-i-built-a-database-audit-script-with-deepseek-here-is-where-it-went-wrong]]'
status: unread
---

> **TL;DR:** I updated agent-cost , a CLI I maintain, to version 0.1.1 because I wanted to measure Codex's GPT-6 Astra usage too. It reads local Claude Code and Codex CLI logs and reports token usage and estimated costs, not actual b…

## What’s new and why it matters
I updated agent-cost , a CLI I maintain, to version 0.1.1 because I wanted to measure Codex's GPT-6 Astra usage too. It reads local Claude Code and Codex CLI logs and reports token usage and estimated costs, not actual billed amounts. Fast mode was where I ran into trouble. After adding Astra to the price table, I tested it with synthetic logs. Usage marked as Fast was still being priced at the Standard rate. The multiplier was in the catalog, but the log reader wasn't recognizing the setting. The fix involved both detecting the mode and deciding what to do when the logs didn't give me enough…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Reproduce the example in a notebook; then refactor into a reusable function.
- Add a short note: what changed in your workflow?

## Relevance
🔴

## Source
https://dev.to/shikiyusuke/tracking-codex-astra-costs-took-more-than-updating-a-price-table-3p3i

## Related notes
- [[2026-08-21-how-to-find-duplicate-rows-in-sql-and-decide-what-counts-as-one]]
- [[2026-08-31-running-total-in-sql-the-window-frame-that-decides-the-answer]]
- [[2026-04-06-i-built-an-open-source-finops-layer-for-genai-apis-real-time-usd-cost-per-otel-span-multi-tenant-isolation-zero-prompt-l]]
- [[2026-08-31-how-to-reconcile-two-tables-in-sql-when-the-row-counts-match]]
- [[2026-08-31-i-left-an-ai-agent-running-unattended-for-a-day-here-is-everything-that-broke]]
- [[2026-06-24-i-am-not-a-developer-i-built-a-database-audit-script-with-deepseek-here-is-where-it-went-wrong]]
