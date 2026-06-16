---
title: Clearbit died. Here's a pay-per-call company enrichment API for AI agents ($0.03/lookup)
date: '2026-06-16'
source: https://dev.to/tufti/clearbit-died-heres-a-pay-per-call-company-enrichment-api-for-ai-agents-003lookup-52p2
domain: AI-Tools
relevance: 🟡
tags:
- '#ai'
- '#library'
- '#python'
- '#tool'
related:
- '[[2026-04-20-i-built-a-pay-per-call-trading-signal-api-for-ai-agents]]'
- '[[2026-04-27-i-built-a-pay-per-call-trading-signal-api-for-ai-agents]]'
- '[[2026-04-10-free-kokoro-tts-api-open-source-voice-synthesis-with-no-monthly-fee]]'
- '[[2026-03-25-nasa-has-20-free-apis-asteroids-mars-photos-exoplanets-and-more-no-signup]]'
- '[[2026-04-03-i-built-a-pii-detection-api-with-zero-ai-cost-pure-regex]]'
- '[[2026-05-09-i-built-a-simple-ai-text-summarizer-in-python]]'
status: unread
---

> **TL;DR:** Clearbit's free API shut down April 30, 2025. The replacement (HubSpot Breeze Intelligence) requires an enterprise contract that starts around $20K/year. If you're building AI agents that need company context from a doma…

## What’s new and why it matters
Clearbit's free API shut down April 30, 2025. The replacement (HubSpot Breeze Intelligence) requires an enterprise contract that starts around $20K/year. If you're building AI agents that need company context from a domain name, you've probably felt this gap. I built a pay-per-call alternative: POST a domain, get back structured JSON. No subscription. No contract. $0.03 per lookup. How it works import requests resp = requests . post ( ' https://api.ideafactorylab.org/company-info ' , json = { ' domain ' : ' stripe.com ' } ) print ( resp . json ()) Returns: { "domain" : "stripe.com" , "name" :…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Reproduce the example in a notebook; then refactor into a reusable function.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/tufti/clearbit-died-heres-a-pay-per-call-company-enrichment-api-for-ai-agents-003lookup-52p2

## Related notes
- [[2026-04-20-i-built-a-pay-per-call-trading-signal-api-for-ai-agents]]
- [[2026-04-27-i-built-a-pay-per-call-trading-signal-api-for-ai-agents]]
- [[2026-04-10-free-kokoro-tts-api-open-source-voice-synthesis-with-no-monthly-fee]]
- [[2026-03-25-nasa-has-20-free-apis-asteroids-mars-photos-exoplanets-and-more-no-signup]]
- [[2026-04-03-i-built-a-pii-detection-api-with-zero-ai-cost-pure-regex]]
- [[2026-05-09-i-built-a-simple-ai-text-summarizer-in-python]]
