---
title: 'Anthropic SDK max_retries Stacked on My Retries: 36 Calls per Job'
date: '2026-10-06'
source: https://dev.to/ji_ai/anthropic-sdk-maxretries-stacked-on-my-retries-36-calls-per-job-283l
domain: AI-Tools
relevance: 🟡
tags:
- '#ai'
- '#career'
- '#python'
- '#sql'
- '#support-analytics'
- '#tool'
- '#zendesk'
related:
- '[[2026-09-01-i-raced-six-models-against-each-other-on-digitalocean-inference-the-cheapest-one-won]]'
- '[[2026-04-02-how-to-stop-your-ai-agent-from-burning-400month-on-api-calls]]'
- '[[2026-04-03-i-got-tired-of-watching-my-terminal-so-i-built-guga]]'
- '[[2026-07-04-how-pythons-rglob-silently-loses-files-and-why-macos-makes-it-worse]]'
- '[[2026-08-01-my-mcp-servers-two-api-helpers-had-zero-except-blocks-every-bad-call-crashed-with-a-raw-urllib-traceback]]'
- '[[2026-09-24-what-a-server-knows-about-you-before-it-reads-a-single-header]]'
status: unread
---

> **TL;DR:** My application logs said the report worker called Claude 1,302 times in 22 minutes. An httpx hook I added the next morning said it was 3,904 HTTP requests. Both were right, which was the problem. That gap came from the A…

## What’s new and why it matters
My application logs said the report worker called Claude 1,302 times in 22 minutes. An httpx hook I added the next morning said it was 3,904 HTTP requests. Both were right, which was the problem. That gap came from the Anthropic SDK max_retries default sitting underneath two other retry layers I had written myself. Each layer looked reasonable on its own. Together they multiplied: 3 × 4 × 3 = 36 attempts for one failing call. During a short stretch of 529 overloaded_error responses, that multiplication turned a blip into a retry storm. When the API recovered, the storm hit my own rate limit an…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Reproduce the example in a notebook; then refactor into a reusable function.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/ji_ai/anthropic-sdk-maxretries-stacked-on-my-retries-36-calls-per-job-283l

## Related notes
- [[2026-09-01-i-raced-six-models-against-each-other-on-digitalocean-inference-the-cheapest-one-won]]
- [[2026-04-02-how-to-stop-your-ai-agent-from-burning-400month-on-api-calls]]
- [[2026-04-03-i-got-tired-of-watching-my-terminal-so-i-built-guga]]
- [[2026-07-04-how-pythons-rglob-silently-loses-files-and-why-macos-makes-it-worse]]
- [[2026-08-01-my-mcp-servers-two-api-helpers-had-zero-except-blocks-every-bad-call-crashed-with-a-raw-urllib-traceback]]
- [[2026-09-24-what-a-server-knows-about-you-before-it-reads-a-single-header]]
