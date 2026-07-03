---
title: Modbus Writes Through the Cache Proxy in Home Assistant
date: '2026-07-03'
source: https://dev.to/cloudapp_dev/modbus-writes-through-the-cache-proxy-in-home-assistant-1ioe
domain: Productivity
relevance: 🔴
tags:
- '#best-practice'
- '#productivity'
- '#python'
- '#support-analytics'
- '#tool'
- '#zendesk'
related:
- '[[2026-06-16-sql-or-python-the-line-is-sharper-than-you-think-with-code]]'
- '[[2026-04-22-your-pytest-retries-are-lying-to-you-the-hidden-cost-of---reruns-and-the-plugin-i-wrote-so-i-could-actually-see-what-my-]]'
- '[[2026-04-21-i-spent-6-months-obsessing-over-mt5-bot-logic-heres-what-finally-clicked]]'
- '[[2026-04-17-maybe-this-is-how-open-source-apps-are-born]]'
- '[[2026-06-20-green-unit-tests-are-a-comfort-blanket]]'
- '[[2026-03-13-you-dont-need-a-framework-building-reliable-ai-agents-from-first-principles]]'
status: unread
---

> **TL;DR:** My Huawei SDongle allows exactly one Modbus connection at a time. That's why I run a small caching proxy in front of it that holds the connection exclusively and answers all reads from cache — I described it in detail in…

## What’s new and why it matters
My Huawei SDongle allows exactly one Modbus connection at a time. That's why I run a small caching proxy in front of it that holds the connection exclusively and answers all reads from cache — I described it in detail in the caching proxy post . It works beautifully as long as you only read. Then Tibber came into the picture, I wanted to force-charge the battery on negative electricity prices and set the export limit dynamically — and suddenly I needed writes. Here's the non-obvious catch: a cache only solves reads. A write has no business sitting in a cache — it has to actually reach the inve…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Add a short note: what changed in your workflow?

## Relevance
🔴

## Source
https://dev.to/cloudapp_dev/modbus-writes-through-the-cache-proxy-in-home-assistant-1ioe

## Related notes
- [[2026-06-16-sql-or-python-the-line-is-sharper-than-you-think-with-code]]
- [[2026-04-22-your-pytest-retries-are-lying-to-you-the-hidden-cost-of---reruns-and-the-plugin-i-wrote-so-i-could-actually-see-what-my-]]
- [[2026-04-21-i-spent-6-months-obsessing-over-mt5-bot-logic-heres-what-finally-clicked]]
- [[2026-04-17-maybe-this-is-how-open-source-apps-are-born]]
- [[2026-06-20-green-unit-tests-are-a-comfort-blanket]]
- [[2026-03-13-you-dont-need-a-framework-building-reliable-ai-agents-from-first-principles]]
