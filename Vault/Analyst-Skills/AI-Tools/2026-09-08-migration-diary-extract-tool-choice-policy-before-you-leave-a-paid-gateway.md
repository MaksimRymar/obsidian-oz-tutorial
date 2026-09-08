---
title: 'Migration Diary: Extract Tool-Choice Policy Before You Leave a Paid Gateway'
date: '2026-09-08'
source: https://dev.to/techpy_768/migration-diary-extract-tool-choice-policy-before-you-leave-a-paid-gateway-47c9
domain: AI-Tools
relevance: 🟡
tags:
- '#ai'
- '#python'
- '#sql'
- '#tool'
related:
- '[[2026-09-07-migration-diary-fail-closed-on-agent-json-before-you-leave-the-paid-model]]'
- '[[2026-08-21-how-to-find-duplicate-rows-in-sql-and-decide-what-counts-as-one]]'
- '[[2026-09-07-score-the-trace-not-the-final-payload]]'
- '[[2026-09-07-migration-diary-freeze-tool-dispatch-until-every-paid-runtime-lease-drains]]'
- '[[2026-08-18-a-generated-sql-query-got-faster-by-returning-fewer-rows-test-that-before-you-merge-it]]'
- '[[2026-08-12-sql-ctes-how-to-build-a-query-in-steps-you-can-check]]'
status: unread
---

> **TL;DR:** The paid gateway is still choosing your tools even after you think last week's cutover finished. You should pull tool-choice policy into your own process before production traffic leaves that vendor SDK. A free runtime t…

## What’s new and why it matters
The paid gateway is still choosing your tools even after you think last week's cutover finished. You should pull tool-choice policy into your own process before production traffic leaves that vendor SDK. A free runtime then looks cheaper while it skips required tools, invents parallel calls, or ignores your deny list. This diary covers a local policy plane, a shadow comparison harness, and leftovers that remain after you move DNS. The real failure is a missing policy plane Paid agent SDKs usually hide three important decisions behind a single enum that looks deceptively portable. Those decisio…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Reproduce the example in a notebook; then refactor into a reusable function.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/techpy_768/migration-diary-extract-tool-choice-policy-before-you-leave-a-paid-gateway-47c9

## Related notes
- [[2026-09-07-migration-diary-fail-closed-on-agent-json-before-you-leave-the-paid-model]]
- [[2026-08-21-how-to-find-duplicate-rows-in-sql-and-decide-what-counts-as-one]]
- [[2026-09-07-score-the-trace-not-the-final-payload]]
- [[2026-09-07-migration-diary-freeze-tool-dispatch-until-every-paid-runtime-lease-drains]]
- [[2026-08-18-a-generated-sql-query-got-faster-by-returning-fewer-rows-test-that-before-you-merge-it]]
- [[2026-08-12-sql-ctes-how-to-build-a-query-in-steps-you-can-check]]
