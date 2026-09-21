---
title: 'When AI Agents Hammer tools/list: Building a Caching-Aware MCP Server (SEP-2549)'
date: '2026-09-21'
source: https://dev.to/sindhuja_sudhakar/when-ai-agents-hammer-toolslist-building-a-caching-aware-mcp-server-sep-2549-38k6
domain: AI-Tools
relevance: 🟡
tags:
- '#ai'
- '#feature'
- '#python'
- '#sql'
- '#tool'
related:
- '[[2026-04-02-how-to-stop-your-ai-agent-from-burning-400month-on-api-calls]]'
- '[[2026-09-01-i-raced-six-models-against-each-other-on-digitalocean-inference-the-cheapest-one-won]]'
- '[[2026-04-21-how-to-safely-run-ai-generated-code-with-smolvm-open-source-microvm-sandbox]]'
- '[[2026-08-11-stop-doing-it-manually-7-ai-automation-workflows-worth-building-this-weekend]]'
- '[[2026-07-15-i-built-with-both-apis-as-a-bootcamp-grad-heres-what-actually-matters]]'
- '[[2026-06-24-i-am-not-a-developer-i-built-a-database-audit-script-with-deepseek-here-is-where-it-went-wrong]]'
status: unread
---

> **TL;DR:** Part 2 of 2. Part 1 covered statelessness; here I tackle caching. Part 1 was about statelessness, now shipped in the 2026-07-28 spec. This time it's another feature from that same spec: caching (SEP-2549, "TTL for List R…

## What’s new and why it matters
Part 2 of 2. Part 1 covered statelessness; here I tackle caching. Part 1 was about statelessness, now shipped in the 2026-07-28 spec. This time it's another feature from that same spec: caching (SEP-2549, "TTL for List Results") . It adds two tiny fields — ttlMs and cacheScope — to cacheable results, giving clients a way to avoid re-fetching the same discovery data. So I built a server that emits them, pointed real AI clients at it, and watched what actually happened. The result surprised me. The problem: repeated discovery AI agents plan in loops. A human calls a tool because they decided to;…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Reproduce the example in a notebook; then refactor into a reusable function.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/sindhuja_sudhakar/when-ai-agents-hammer-toolslist-building-a-caching-aware-mcp-server-sep-2549-38k6

## Related notes
- [[2026-04-02-how-to-stop-your-ai-agent-from-burning-400month-on-api-calls]]
- [[2026-09-01-i-raced-six-models-against-each-other-on-digitalocean-inference-the-cheapest-one-won]]
- [[2026-04-21-how-to-safely-run-ai-generated-code-with-smolvm-open-source-microvm-sandbox]]
- [[2026-08-11-stop-doing-it-manually-7-ai-automation-workflows-worth-building-this-weekend]]
- [[2026-07-15-i-built-with-both-apis-as-a-bootcamp-grad-heres-what-actually-matters]]
- [[2026-06-24-i-am-not-a-developer-i-built-a-database-audit-script-with-deepseek-here-is-where-it-went-wrong]]
