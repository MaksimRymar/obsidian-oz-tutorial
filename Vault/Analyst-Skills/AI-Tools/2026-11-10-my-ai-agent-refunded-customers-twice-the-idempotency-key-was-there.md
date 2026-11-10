---
title: My AI agent refunded customers twice. The idempotency key was there
date: '2026-11-10'
source: https://dev.to/rakesh_kumar_04012c337851/my-ai-agent-refunded-customers-twice-the-idempotency-key-was-there-12le
domain: AI-Tools
relevance: 🟡
tags:
- '#ai'
- '#feature'
- '#python'
- '#sql'
- '#tool'
related:
- '[[2026-09-01-i-raced-six-models-against-each-other-on-digitalocean-inference-the-cheapest-one-won]]'
- '[[2026-10-12-your-ai-agent-needs-a-brake-pedal-stopping-loops-and-runaway-cost-at-runtime]]'
- '[[2026-09-22-we-have-no-marketing-state-table-only-five-sql-windows-over-timestamps-we-already-had]]'
- '[[2026-08-11-sql-aliases-how-to-read-a-query-out-loud]]'
- '[[2026-08-21-how-to-find-duplicate-rows-in-sql-and-decide-what-counts-as-one]]'
- '[[2026-11-04-let-an-ai-agent-drive-your-mac-for-a-fiftieth-of-a-cent-per-step-with-typesafe-computer-use]]'
status: unread
---

> **TL;DR:** Part 2 of **Shipping AI Agents to Production . Part 1 was about the second check: the eval gate judges the version, the smoke eval judges the environment. I promised bundles, canaries and rollback for this part. Then som…

## What’s new and why it matters
Part 2 of **Shipping AI Agents to Production . Part 1 was about the second check: the eval gate judges the version, the smoke eval judges the environment. I promised bundles, canaries and rollback for this part. Then something happened that no canary could have caught, so those move to Part 3. A refund call timed out on a Friday evening. No deploy, no prompt change. The customer asked, "Did my refund go through?" So our support agent called the refund tool again. 9 customers were refunded twice in 14 minutes. We already had an idempotency key on every refund. We built it from the tool call ID.…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Reproduce the example in a notebook; then refactor into a reusable function.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/rakesh_kumar_04012c337851/my-ai-agent-refunded-customers-twice-the-idempotency-key-was-there-12le

## Related notes
- [[2026-09-01-i-raced-six-models-against-each-other-on-digitalocean-inference-the-cheapest-one-won]]
- [[2026-10-12-your-ai-agent-needs-a-brake-pedal-stopping-loops-and-runaway-cost-at-runtime]]
- [[2026-09-22-we-have-no-marketing-state-table-only-five-sql-windows-over-timestamps-we-already-had]]
- [[2026-08-11-sql-aliases-how-to-read-a-query-out-loud]]
- [[2026-08-21-how-to-find-duplicate-rows-in-sql-and-decide-what-counts-as-one]]
- [[2026-11-04-let-an-ai-agent-drive-your-mac-for-a-fiftieth-of-a-cent-per-step-with-typesafe-computer-use]]
