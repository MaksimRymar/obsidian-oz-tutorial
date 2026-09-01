---
title: I raced six models against each other on DigitalOcean Inference. The cheapest
  one won.
date: '2026-09-01'
source: https://dev.to/remdore/i-raced-six-models-against-each-other-on-digitalocean-inference-the-cheapest-one-won-4lga
domain: AI-Tools
relevance: 🟡
tags:
- '#ai'
- '#feature'
- '#python'
- '#sql'
- '#tool'
related:
- '[[2026-08-11-sql-aliases-how-to-read-a-query-out-loud]]'
- '[[2026-07-24-ai-generated-sql-has-a-silent-failure-problem-heres-a-way-to-catch-it]]'
- '[[2026-04-17-maybe-this-is-how-open-source-apps-are-born]]'
- '[[2026-06-09-how-i-messed-up-ai-streaming-and-how-you-can-avoid-it]]'
- '[[2026-08-21-how-to-find-duplicate-rows-in-sql-and-decide-what-counts-as-one]]'
- '[[2026-04-03-i-got-tired-of-watching-my-terminal-so-i-built-guga]]'
status: unread
---

> **TL;DR:** Every time I put a model behind an endpoint I make the same lazy decision. I pick whatever I used last time, or whatever I read about most recently, and I tell myself I'll benchmark it properly later, and later never arr…

## What’s new and why it matters
Every time I put a model behind an endpoint I make the same lazy decision. I pick whatever I used last time, or whatever I read about most recently, and I tell myself I'll benchmark it properly later, and later never arrives because there is always something with an actual deadline on it and comparing model latencies feels like procrastination even when it isn't. I never do it. Not once. So I built the thing that would make me do it. One prompt, fired at six models at once, streaming side by side in columns, with time to first token and cost per run underneath each one. About 390 lines of Pyth…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Reproduce the example in a notebook; then refactor into a reusable function.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/remdore/i-raced-six-models-against-each-other-on-digitalocean-inference-the-cheapest-one-won-4lga

## Related notes
- [[2026-08-11-sql-aliases-how-to-read-a-query-out-loud]]
- [[2026-07-24-ai-generated-sql-has-a-silent-failure-problem-heres-a-way-to-catch-it]]
- [[2026-04-17-maybe-this-is-how-open-source-apps-are-born]]
- [[2026-06-09-how-i-messed-up-ai-streaming-and-how-you-can-avoid-it]]
- [[2026-08-21-how-to-find-duplicate-rows-in-sql-and-decide-what-counts-as-one]]
- [[2026-04-03-i-got-tired-of-watching-my-terminal-so-i-built-guga]]
