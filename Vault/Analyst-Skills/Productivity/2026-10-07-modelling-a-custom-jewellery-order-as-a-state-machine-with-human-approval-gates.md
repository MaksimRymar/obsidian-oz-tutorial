---
title: Modelling a Custom Jewellery Order as a State Machine (with Human Approval
  Gates)
date: '2026-10-07'
source: https://dev.to/ujjwal_dubey_9/modelling-a-custom-jewellery-order-as-a-state-machine-with-human-approval-gates-3a6c
domain: Productivity
relevance: 🟡
tags:
- '#best-practice'
- '#library'
- '#productivity'
- '#python'
- '#tool'
related:
- '[[2026-06-28-the-python-interview-roadmap-what-to-learn-in-what-order-before-someone-asks-you-about-the-gil]]'
- '[[2026-07-30-langchain-for-absolute-beginners---part-6-debugging-observing-agents-with-langsmith]]'
- '[[2026-03-03-sql-joins-window-functions-the-skills-that-separate-analysts-from-beginners]]'
- '[[2026-05-04-why-we-chose-self-hosted-ai-over-cloud-for-business-data-posted-by-the-ragleap-team-building-ragleap-a-private-server-ai]]'
- '[[2026-04-04-build-your-first-ai-agent-with-langgraph-step-by-step-python-tutorial-2026]]'
- '[[2026-08-20-apify-store-scraper-market-intelligence-on-every-public-actor-in-2026]]'
status: unread
---

> **TL;DR:** Custom jewellery orders are a nice, small example of why "add a chatbot" is the wrong first move for retail automation. The real problem is state: the customer wants to know where their order is, and the answer lives in…

## What’s new and why it matters
Custom jewellery orders are a nice, small example of why "add a chatbot" is the wrong first move for retail automation. The real problem is state: the customer wants to know where their order is, and the answer lives in someone's head or a paper order book. This post shows a tiny state machine for a custom order, with approval gates on the steps that touch money or promises. It is the pattern we use when we build AI automation for custom jewellery orders for Indian stores, stripped down to the standard library. The states ENQUIRY -> DESIGN_SHARED -> DESIGN_APPROVED -> ADVANCE_RECEIVED -> IN_MA…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/ujjwal_dubey_9/modelling-a-custom-jewellery-order-as-a-state-machine-with-human-approval-gates-3a6c

## Related notes
- [[2026-06-28-the-python-interview-roadmap-what-to-learn-in-what-order-before-someone-asks-you-about-the-gil]]
- [[2026-07-30-langchain-for-absolute-beginners---part-6-debugging-observing-agents-with-langsmith]]
- [[2026-03-03-sql-joins-window-functions-the-skills-that-separate-analysts-from-beginners]]
- [[2026-05-04-why-we-chose-self-hosted-ai-over-cloud-for-business-data-posted-by-the-ragleap-team-building-ragleap-a-private-server-ai]]
- [[2026-04-04-build-your-first-ai-agent-with-langgraph-step-by-step-python-tutorial-2026]]
- [[2026-08-20-apify-store-scraper-market-intelligence-on-every-public-actor-in-2026]]
