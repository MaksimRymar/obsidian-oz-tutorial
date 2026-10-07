---
title: 'Strands Decider 2B vs LLM as a judge: a keyword regex tied the 2B'
date: '2026-10-07'
source: https://dev.to/efraingaray/strands-decider-2b-vs-llm-as-a-judge-a-keyword-regex-tied-the-2b-i74
domain: AI-Tools
relevance: 🟡
tags:
- '#ai'
- '#feature'
related:
- '[[2026-08-11-code-interpreter-is-infrastructure-not-a-prompt]]'
- '[[2026-08-21-shipping-12-ios-apps-to-the-app-store-unattended-part-2-every-review-trap-beta-builds-rejected-pricing-name-collisions]]'
- '[[2026-09-21-how-to-build-a-creator-emails-pipeline-in-one-python-call]]'
- '[[2026-07-07-i-turned-a-claude-code-only-web-reader-into-a-normal-mcp-server]]'
- '[[2026-08-03-building-a-cost-aware-llm-router-with-deepseek-v4-flash-and-glm-5]]'
- '[[2026-09-21-i-ran-a-contract-check-against-the-swagger-petstore-here-is-what-came-back]]'
status: unread
---

> **TL;DR:** I wanted a cheap judge for my video pipeline: given a shot description, does it have a concrete subject, a visible action and an explicit camera decision, or is it generic? Strands Decider 2B is built for that kind of ye…

## What’s new and why it matters
I wanted a cheap judge for my video pipeline: given a shot description, does it have a concrete subject, a visible action and an explicit camera decision, or is it generic? Strands Decider 2B is built for that kind of yes/no call, so I measured it. 75 shot descriptions : 63 captured from my pipeline (22 from production, 41 from a weak model running the same step) and 12 adversarial, with the three features annotated before running any judge. With the choice primitive the 2B reaches AUC 0.91 in 34 ms per judgment. Claude Opus reaches 0.99 . A regex that only looks for framing words reaches 0.90…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Reproduce the example in a notebook; then refactor into a reusable function.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/efraingaray/strands-decider-2b-vs-llm-as-a-judge-a-keyword-regex-tied-the-2b-i74

## Related notes
- [[2026-08-11-code-interpreter-is-infrastructure-not-a-prompt]]
- [[2026-08-21-shipping-12-ios-apps-to-the-app-store-unattended-part-2-every-review-trap-beta-builds-rejected-pricing-name-collisions]]
- [[2026-09-21-how-to-build-a-creator-emails-pipeline-in-one-python-call]]
- [[2026-07-07-i-turned-a-claude-code-only-web-reader-into-a-normal-mcp-server]]
- [[2026-08-03-building-a-cost-aware-llm-router-with-deepseek-v4-flash-and-glm-5]]
- [[2026-09-21-i-ran-a-contract-check-against-the-swagger-petstore-here-is-what-came-back]]
