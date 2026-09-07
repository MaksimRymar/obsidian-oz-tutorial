---
title: Gate Agent Success on Closed Spans
date: '2026-09-07'
source: https://dev.to/codepro_3283/gate-agent-success-on-closed-spans-35je
domain: AI-Tools
relevance: 🟡
tags:
- '#ai'
- '#python'
- '#sql'
- '#tool'
related:
- '[[2026-09-05-a-frozen-test-is-not-coverage-a-merge-gate-for-agent-patches]]'
- '[[2026-09-01-i-raced-six-models-against-each-other-on-digitalocean-inference-the-cheapest-one-won]]'
- '[[2026-08-18-a-generated-sql-query-got-faster-by-returning-fewer-rows-test-that-before-you-merge-it]]'
- '[[2026-06-15-my-sigma-scanner-cant-count-so-i-wrote-that-down-instead-of-faking-it]]'
- '[[2026-09-01-seeding-fixtures-realistic-test-data-for-warehouse-integration-tests]]'
- '[[2026-08-21-how-to-find-duplicate-rows-in-sql-and-decide-what-counts-as-one]]'
status: unread
---

> **TL;DR:** The last assistant token is not a status code. If any tool span is still open, the run failed, even when the model wrote a confident wrap-up. Most agent UIs collapse that distinction. They paint a completed bubble as soo…

## What’s new and why it matters
The last assistant token is not a status code. If any tool span is still open, the run failed, even when the model wrote a confident wrap-up. Most agent UIs collapse that distinction. They paint a completed bubble as soon as the model stream ends. The trace underneath is often uglier: a read_file span that started, an apply_patch span that never returned, and a final sentence that assumes both finished. Treating the prose as success is how silent partial work lands on a branch. This is the same class of bug as an HTTP 200 from a checkout handler while the payment span is still in flight. The o…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Reproduce the example in a notebook; then refactor into a reusable function.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/codepro_3283/gate-agent-success-on-closed-spans-35je

## Related notes
- [[2026-09-05-a-frozen-test-is-not-coverage-a-merge-gate-for-agent-patches]]
- [[2026-09-01-i-raced-six-models-against-each-other-on-digitalocean-inference-the-cheapest-one-won]]
- [[2026-08-18-a-generated-sql-query-got-faster-by-returning-fewer-rows-test-that-before-you-merge-it]]
- [[2026-06-15-my-sigma-scanner-cant-count-so-i-wrote-that-down-instead-of-faking-it]]
- [[2026-09-01-seeding-fixtures-realistic-test-data-for-warehouse-integration-tests]]
- [[2026-08-21-how-to-find-duplicate-rows-in-sql-and-decide-what-counts-as-one]]
