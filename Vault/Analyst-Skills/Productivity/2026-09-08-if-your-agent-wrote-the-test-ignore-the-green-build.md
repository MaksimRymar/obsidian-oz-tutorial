---
title: If Your Agent Wrote the Test, Ignore the Green Build
date: '2026-09-08'
source: https://dev.to/airs_6907/if-your-agent-wrote-the-test-ignore-the-green-build-28ma
domain: Productivity
relevance: 🟡
tags:
- '#ai'
- '#best-practice'
- '#feature'
- '#productivity'
- '#python'
- '#sql'
- '#tool'
related:
- '[[2026-09-05-a-frozen-test-is-not-coverage-a-merge-gate-for-agent-patches]]'
- '[[2026-08-18-a-generated-sql-query-got-faster-by-returning-fewer-rows-test-that-before-you-merge-it]]'
- '[[2026-09-06-put-a-write-boundary-between-the-agent-patch-and-the-oracle]]'
- '[[2026-09-07-migration-diary-fail-closed-on-agent-json-before-you-leave-the-paid-model]]'
- '[[2026-09-08-ledger-one-entrypoint-before-you-touch-the-mess]]'
- '[[2026-04-22-your-pytest-retries-are-lying-to-you-the-hidden-cost-of---reruns-and-the-plugin-i-wrote-so-i-could-actually-see-what-my-]]'
status: unread
---

> **TL;DR:** A green test suite is not real evidence. It is often a closed argument loop. The same agent wrote both code and checks. Freeze an oracle before any agent run. Then let every patch fail in public. Cheap tokens do not weak…

## What’s new and why it matters
A green test suite is not real evidence. It is often a closed argument loop. The same agent wrote both code and checks. Freeze an oracle before any agent run. Then let every patch fail in public. Cheap tokens do not weaken this rule. Take a side Stop treating generated tests as quality control. A model that authors both sides grades itself. That process is narrative, not verification. Retry-heavy coding loops make the narrative cheaper. They also make the story smoother. Smooth output is the actual danger here. You need a human-owned expected result file. Put that file in git today. Deny the a…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/airs_6907/if-your-agent-wrote-the-test-ignore-the-green-build-28ma

## Related notes
- [[2026-09-05-a-frozen-test-is-not-coverage-a-merge-gate-for-agent-patches]]
- [[2026-08-18-a-generated-sql-query-got-faster-by-returning-fewer-rows-test-that-before-you-merge-it]]
- [[2026-09-06-put-a-write-boundary-between-the-agent-patch-and-the-oracle]]
- [[2026-09-07-migration-diary-fail-closed-on-agent-json-before-you-leave-the-paid-model]]
- [[2026-09-08-ledger-one-entrypoint-before-you-touch-the-mess]]
- [[2026-04-22-your-pytest-retries-are-lying-to-you-the-hidden-cost-of---reruns-and-the-plugin-i-wrote-so-i-could-actually-see-what-my-]]
