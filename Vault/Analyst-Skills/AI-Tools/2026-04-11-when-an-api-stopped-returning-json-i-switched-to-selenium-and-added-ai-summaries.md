---
title: When an API stopped returning JSON, I switched to Selenium and added AI summaries
date: '2026-04-11'
source: https://dev.to/dmitriy_dmitriy_d50839940/when-an-api-stopped-returning-json-i-switched-to-selenium-and-added-ai-summaries-1kfl
domain: AI-Tools
relevance: 🟡
tags:
- '#ai'
- '#tool'
related:
- '[[2026-03-23-i-ran-56-experiments-to-find-the-best-way-to-make-ai-watch-videos]]'
- '[[2026-04-08-i-built-a-bot-that-answers-github-discussions-using-free-ai-models-heres-what-i-learned]]'
- '[[2026-03-19-i-used-ai-to-build-my-project-but-then-i-had-to-actually-understand-it]]'
- '[[2026-03-07-why-i-rebuilt-my-first-api-from-scratch]]'
- '[[2026-03-11-how-i-built-a-self-hosted-paper-digest-that-uses-llm-scoring-to-filter-research-papers]]'
- '[[2026-04-03-i-built-a-pii-detection-api-with-zero-ai-cost-pure-regex]]'
status: unread
---

> **TL;DR:** I built a parser around the DNB Business Directory API. At first, everything worked fine — simple requests, JSON responses, clean and fast. Then it suddenly stopped working. My script started getting empty or unusable re…

## What’s new and why it matters
I built a parser around the DNB Business Directory API. At first, everything worked fine — simple requests, JSON responses, clean and fast. Then it suddenly stopped working. My script started getting empty or unusable responses, even though the same requests still worked perfectly in the browser. Status codes were often 200, but the data was missing or incomplete. After trying different headers, sessions, retries, and delays, it became clear that this wasn’t a normal API issue. Most likely, anti-bot filtering. What I changed Instead of trying to bypass it at the HTTP level, I switched to Selen…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Reproduce the example in a notebook; then refactor into a reusable function.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/dmitriy_dmitriy_d50839940/when-an-api-stopped-returning-json-i-switched-to-selenium-and-added-ai-summaries-1kfl

## Related notes
- [[2026-03-23-i-ran-56-experiments-to-find-the-best-way-to-make-ai-watch-videos]]
- [[2026-04-08-i-built-a-bot-that-answers-github-discussions-using-free-ai-models-heres-what-i-learned]]
- [[2026-03-19-i-used-ai-to-build-my-project-but-then-i-had-to-actually-understand-it]]
- [[2026-03-07-why-i-rebuilt-my-first-api-from-scratch]]
- [[2026-03-11-how-i-built-a-self-hosted-paper-digest-that-uses-llm-scoring-to-filter-research-papers]]
- [[2026-04-03-i-built-a-pii-detection-api-with-zero-ai-cost-pure-regex]]
