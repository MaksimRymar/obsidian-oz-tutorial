---
title: Score Agent Hops Before They Leave Disk
date: '2026-09-07'
source: https://dev.to/gitjs_8094/score-agent-hops-before-they-leave-disk-1lja
domain: SQL
relevance: 🟡
tags:
- '#best-practice'
- '#library'
- '#python'
- '#sql'
- '#tool'
related:
- '[[2026-08-21-how-to-find-duplicate-rows-in-sql-and-decide-what-counts-as-one]]'
- '[[2026-08-18-a-generated-sql-query-got-faster-by-returning-fewer-rows-test-that-before-you-merge-it]]'
- '[[2026-09-05-a-frozen-test-is-not-coverage-a-merge-gate-for-agent-patches]]'
- '[[2026-08-18-a-free-model-vs-30-security-advisory-records-an-accuracy-test-you-can-rerun]]'
- '[[2026-09-01-i-raced-six-models-against-each-other-on-digitalocean-inference-the-cheapest-one-won]]'
- '[[2026-09-04-i-built-an-offline-document-indexer-and-ollama-taught-me-two-things-i-did-not-expect]]'
status: unread
---

> **TL;DR:** Agent loops fail at the first unplanned hop. The failure is architectural, not model quality. Default remote calls treat every thought as cargo. That default burns latency on work that never left disk. It also ships secr…

## What’s new and why it matters
Agent loops fail at the first unplanned hop. The failure is architectural, not model quality. Default remote calls treat every thought as cargo. That default burns latency on work that never left disk. It also ships secret-shaped text that needed no network. A hop score reverses the order before any client opens a socket. Think of each agent step as a package at a loading dock. Some packages never leave the building. Some wait for a clean truck and a clear road. The dock does not ship first and audit later. Three signals decide the dock on every step. Latency budget is the first signal. Secret…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Write the query in a scratchpad and run EXPLAIN/QUERY PLAN to verify performance.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/gitjs_8094/score-agent-hops-before-they-leave-disk-1lja

## Related notes
- [[2026-08-21-how-to-find-duplicate-rows-in-sql-and-decide-what-counts-as-one]]
- [[2026-08-18-a-generated-sql-query-got-faster-by-returning-fewer-rows-test-that-before-you-merge-it]]
- [[2026-09-05-a-frozen-test-is-not-coverage-a-merge-gate-for-agent-patches]]
- [[2026-08-18-a-free-model-vs-30-security-advisory-records-an-accuracy-test-you-can-rerun]]
- [[2026-09-01-i-raced-six-models-against-each-other-on-digitalocean-inference-the-cheapest-one-won]]
- [[2026-09-04-i-built-an-offline-document-indexer-and-ollama-taught-me-two-things-i-did-not-expect]]
