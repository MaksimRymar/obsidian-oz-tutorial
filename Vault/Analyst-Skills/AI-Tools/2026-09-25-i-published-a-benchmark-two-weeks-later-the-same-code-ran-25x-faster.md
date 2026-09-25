---
title: I published a benchmark. Two weeks later the same code ran 2.5x faster.
date: '2026-09-25'
source: https://dev.to/frankchu/i-published-a-benchmark-two-weeks-later-the-same-code-ran-25x-faster-1fa5
domain: AI-Tools
relevance: 🟡
tags:
- '#ai'
- '#python'
- '#tool'
related:
- '[[2026-09-01-i-raced-six-models-against-each-other-on-digitalocean-inference-the-cheapest-one-won]]'
- '[[2026-05-25-i-added-mcp-support-to-my-saas-in-an-afternoon-heres-the-whole-thing]]'
- '[[2026-03-09-i-got-frustrated-my-ai-kept-forgetting-me-so-i-spent-6-months-building-a-fix]]'
- '[[2026-07-01-one-big-table-vs-the-star-schema-i-think-everyones-arguing-about-the-wrong-thing]]'
- '[[2026-08-11-code-interpreter-is-infrastructure-not-a-prompt]]'
- '[[2026-09-21-a-1145-star-cli-promised-nothing-leaves-your-machine-it-executes-a-hidden-payload-at-import-time]]'
status: unread
---

> **TL;DR:** Two weeks ago I published a timing measurement and called it a fixed cost. Five runs, 2.24 to 2.36 seconds each, variance of 0.12 seconds. I wrote that the tightness was "the signature of a fixed cost rather than work th…

## What’s new and why it matters
Two weeks ago I published a timing measurement and called it a fixed cost. Five runs, 2.24 to 2.36 seconds each, variance of 0.12 seconds. I wrote that the tightness was "the signature of a fixed cost rather than work that scales with the input," and I built a whole argument on it. Today, same machine, same script, same Chrome flags: 12 sequential runs: min 0.78s max 1.28s mean 0.93s stdev 0.164s first run 1.28s vs rest mean 0.90s (cold-start effect: +0.37s) 0.93 seconds. Two and a half times faster than the number I published, from code I have not touched. What actually differed Not the code.…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Reproduce the example in a notebook; then refactor into a reusable function.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/frankchu/i-published-a-benchmark-two-weeks-later-the-same-code-ran-25x-faster-1fa5

## Related notes
- [[2026-09-01-i-raced-six-models-against-each-other-on-digitalocean-inference-the-cheapest-one-won]]
- [[2026-05-25-i-added-mcp-support-to-my-saas-in-an-afternoon-heres-the-whole-thing]]
- [[2026-03-09-i-got-frustrated-my-ai-kept-forgetting-me-so-i-spent-6-months-building-a-fix]]
- [[2026-07-01-one-big-table-vs-the-star-schema-i-think-everyones-arguing-about-the-wrong-thing]]
- [[2026-08-11-code-interpreter-is-infrastructure-not-a-prompt]]
- [[2026-09-21-a-1145-star-cli-promised-nothing-leaves-your-machine-it-executes-a-hidden-payload-at-import-time]]
