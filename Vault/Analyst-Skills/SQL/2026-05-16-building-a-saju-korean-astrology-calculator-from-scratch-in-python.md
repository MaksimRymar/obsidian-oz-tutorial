---
title: Building a Saju (Korean Astrology) Calculator from Scratch in Python
date: '2026-05-16'
source: https://dev.to/tarofortune/building-a-saju-korean-astrology-calculator-from-scratch-in-python-3cpc
domain: SQL
relevance: 🟡
tags:
- '#python'
- '#sql'
- '#tool'
related:
- '[[2026-05-06-i-built-an-ai-powered-chinese-bazi-fortune-teller-heres-what-deepseek-revealed-about-destiny]]'
- '[[2026-04-11-i-trusted-the-code-ai-wrote-for-me-my-data-was-silently-broken-the-whole-time]]'
- '[[2026-04-22-i-priced-18-million-spy-put-spreads-across-8-years-every-bucket-was--ev-every-year-made-money]]'
- '[[2026-03-15-i-was-tired-of-writing-fix-as-my-commit-message-so-i-built-this-in-one-afternoon]]'
- '[[2026-03-25-i-built-a-job-alert-bot-that-texts-me-new-remote-jobs-every-hour-python-telegram]]'
- '[[2026-05-06-testing-sigma-rules-against-local-logs-without-a-siem]]'
status: unread
---

> **TL;DR:** I built a free Korean astrology (Saju) calculator and wanted to share what makes the math interesting. What's Saju? Saju is the Korean tradition of Chinese 4-pillar astrology (BaZi). Your birth year, month, day, and hour…

## What’s new and why it matters
I built a free Korean astrology (Saju) calculator and wanted to share what makes the math interesting. What's Saju? Saju is the Korean tradition of Chinese 4-pillar astrology (BaZi). Your birth year, month, day, and hour each get encoded as a Heavenly Stem + Earthly Branch pair, giving you 8 characters that describe your "energetic signature." The interesting parts 1. Solar terms via Meeus algorithm The year boundary isn't January 1 — it's the solar term Ipchun (立春, ~Feb 4) , the moment the sun reaches 315° ecliptic longitude. To compute this precisely, I implemented the Meeus astronomical alg…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Write the query in a scratchpad and run EXPLAIN/QUERY PLAN to verify performance.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/tarofortune/building-a-saju-korean-astrology-calculator-from-scratch-in-python-3cpc

## Related notes
- [[2026-05-06-i-built-an-ai-powered-chinese-bazi-fortune-teller-heres-what-deepseek-revealed-about-destiny]]
- [[2026-04-11-i-trusted-the-code-ai-wrote-for-me-my-data-was-silently-broken-the-whole-time]]
- [[2026-04-22-i-priced-18-million-spy-put-spreads-across-8-years-every-bucket-was--ev-every-year-made-money]]
- [[2026-03-15-i-was-tired-of-writing-fix-as-my-commit-message-so-i-built-this-in-one-afternoon]]
- [[2026-03-25-i-built-a-job-alert-bot-that-texts-me-new-remote-jobs-every-hour-python-telegram]]
- [[2026-05-06-testing-sigma-rules-against-local-logs-without-a-siem]]
