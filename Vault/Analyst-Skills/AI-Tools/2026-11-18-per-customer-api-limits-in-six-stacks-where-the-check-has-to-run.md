---
title: 'Per-customer API limits in six stacks: where the check has to run'
date: '2026-11-18'
source: https://dev.to/jackmally/per-customer-api-limits-in-six-stacks-where-the-check-has-to-run-537i
domain: AI-Tools
relevance: 🟡
tags:
- '#ai'
- '#python'
- '#tool'
related:
- '[[2026-09-01-i-raced-six-models-against-each-other-on-digitalocean-inference-the-cheapest-one-won]]'
- '[[2026-11-03-small-guardrails-for-llm-calls-in-plain-python-injection-check-pii-masking-spend-cap-circuit-breaker-json-repair]]'
- '[[2026-05-26-meter-llm-usage-like-anthropic-tokens-models-weekly-and-monthly-caps]]'
- '[[2026-10-28-python-google-sheets-on-autopilot-why-your-script-dies-after-7-days-and-4-more-errors]]'
- '[[2026-11-01-per-customer-rate-limits-and-429s-in-express-and-fastapi]]'
- '[[2026-09-12-a-30-line-wrapper-that-tells-you-what-every-llm-call-actually-costs]]'
status: unread
---

> **TL;DR:** Every per-customer limit I've wired up comes down to the same five steps: work out which customer is calling, check their rate limit, reserve part of their quota, run the handler, then count what the request actually use…

## What’s new and why it matters
Every per-customer limit I've wired up comes down to the same five steps: work out which customer is calling, check their rate limit, reserve part of their quota, run the handler, then count what the request actually used. Those steps don't change between frameworks. What changes is where the framework lets you run code before and after a handler, what it tells you about the route that matched, and whether anything still runs once the response has gone out. This post skips the rate limiting algorithm itself and looks at where the check ends up in each framework and what caught us out. The exam…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Reproduce the example in a notebook; then refactor into a reusable function.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/jackmally/per-customer-api-limits-in-six-stacks-where-the-check-has-to-run-537i

## Related notes
- [[2026-09-01-i-raced-six-models-against-each-other-on-digitalocean-inference-the-cheapest-one-won]]
- [[2026-11-03-small-guardrails-for-llm-calls-in-plain-python-injection-check-pii-masking-spend-cap-circuit-breaker-json-repair]]
- [[2026-05-26-meter-llm-usage-like-anthropic-tokens-models-weekly-and-monthly-caps]]
- [[2026-10-28-python-google-sheets-on-autopilot-why-your-script-dies-after-7-days-and-4-more-errors]]
- [[2026-11-01-per-customer-rate-limits-and-429s-in-express-and-fastapi]]
- [[2026-09-12-a-30-line-wrapper-that-tells-you-what-every-llm-call-actually-costs]]
