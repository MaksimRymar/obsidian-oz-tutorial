---
title: Built an AI Incident Response Agent That Remembers What Worked
date: '2026-09-29'
source: https://dev.to/kawsik_m/built-an-ai-incident-response-agent-that-remembers-what-worked-23b8
domain: AI-Tools
relevance: 🟡
tags:
- '#ai'
- '#best-practice'
- '#python'
- '#sql'
- '#tool'
related:
- '[[2026-09-01-i-raced-six-models-against-each-other-on-digitalocean-inference-the-cheapest-one-won]]'
- '[[2026-08-04-you-cant-unit-test-an-llm-heres-what-i-built-instead]]'
- '[[2026-09-07-bloom-filters-for-data-engineers-cheap-membership-tests]]'
- '[[2026-07-06-i-got-tired-of-my-portfolio-looking-like-a-list-of-links-so-i-built-an-mcp-server-for-it]]'
- '[[2026-04-05-ai-memory-is-broken-we-built-one-that-forgets]]'
- '[[2026-09-11-every-tennis-match-with-15-bookmakers-form-and-head-to-head-in-one-json-row]]'
status: unread
---

> **TL;DR:** How do you know an agent's memory is helping? "The answers feel better" is the usual evidence, and it's terrible. I wanted something I could point at, so I built the evaluation into the product: one endpoint that answers…

## What’s new and why it matters
How do you know an agent's memory is helping? "The answers feel better" is the usual evidence, and it's terrible. I wanted something I could point at, so I built the evaluation into the product: one endpoint that answers the same incident twice, once with memory and once without. It ended up being the most useful debugging tool in the whole system. The system OnCall Memory is an incident co-pilot. An engineer submits an incident (title, service, description, symptoms, logs). The backend recalls similar past incidents from a long-term memory bank, grades their relevance to the service in questi…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Reproduce the example in a notebook; then refactor into a reusable function.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/kawsik_m/built-an-ai-incident-response-agent-that-remembers-what-worked-23b8

## Related notes
- [[2026-09-01-i-raced-six-models-against-each-other-on-digitalocean-inference-the-cheapest-one-won]]
- [[2026-08-04-you-cant-unit-test-an-llm-heres-what-i-built-instead]]
- [[2026-09-07-bloom-filters-for-data-engineers-cheap-membership-tests]]
- [[2026-07-06-i-got-tired-of-my-portfolio-looking-like-a-list-of-links-so-i-built-an-mcp-server-for-it]]
- [[2026-04-05-ai-memory-is-broken-we-built-one-that-forgets]]
- [[2026-09-11-every-tennis-match-with-15-bookmakers-form-and-head-to-head-in-one-json-row]]
