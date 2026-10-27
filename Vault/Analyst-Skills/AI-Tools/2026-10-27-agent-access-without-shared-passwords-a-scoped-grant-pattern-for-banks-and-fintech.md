---
title: 'Agent Access Without Shared Passwords: A Scoped Grant Pattern for Banks and
  Fintech'
date: '2026-10-27'
source: https://dev.to/chinmay_garg/agent-access-without-shared-passwords-a-scoped-grant-pattern-for-banks-and-fintech-930
domain: AI-Tools
relevance: 🟡
tags:
- '#ai'
- '#best-practice'
- '#python'
- '#sql'
- '#tool'
related:
- '[[2026-09-17-i-fact-checked-5-viral-my-ai-bot-made-money-posts-against-primary-data-none-survived]]'
- '[[2026-03-13-you-dont-need-a-framework-building-reliable-ai-agents-from-first-principles]]'
- '[[2026-09-01-i-raced-six-models-against-each-other-on-digitalocean-inference-the-cheapest-one-won]]'
- '[[2026-10-14-43-days-17040-ai-signals-four-things-the-data-says-that-trend-lists-wont-tell-you]]'
- '[[2026-08-25-your-ai-agent-has-bash-access-whos-watching-the-logs]]'
- '[[2026-08-27-a-longmemeval-s-number-you-can-reproduce]]'
status: unread
---

> **TL;DR:** On October 22, Reuters and Axios reported that major US banks are restricting outside AI agents from customer accounts. As reported, customers share a username and password with an AI tool, the agent logs in, and the ban…

## What’s new and why it matters
On October 22, Reuters and Axios reported that major US banks are restricting outside AI agents from customer accounts. As reported, customers share a username and password with an AI tool, the agent logs in, and the bank sees only the customer. Some agents tried actions the customer had not asked for. Most banks are moving towards read-only access for agents as a middle ground. Read-only is a sensible stopgap. It is not a design. The underlying problem is that the bank cannot tell the agent from the person. This post sketches a small pattern that fixes that, with code I ran before writing thi…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Reproduce the example in a notebook; then refactor into a reusable function.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/chinmay_garg/agent-access-without-shared-passwords-a-scoped-grant-pattern-for-banks-and-fintech-930

## Related notes
- [[2026-09-17-i-fact-checked-5-viral-my-ai-bot-made-money-posts-against-primary-data-none-survived]]
- [[2026-03-13-you-dont-need-a-framework-building-reliable-ai-agents-from-first-principles]]
- [[2026-09-01-i-raced-six-models-against-each-other-on-digitalocean-inference-the-cheapest-one-won]]
- [[2026-10-14-43-days-17040-ai-signals-four-things-the-data-says-that-trend-lists-wont-tell-you]]
- [[2026-08-25-your-ai-agent-has-bash-access-whos-watching-the-logs]]
- [[2026-08-27-a-longmemeval-s-number-you-can-reproduce]]
