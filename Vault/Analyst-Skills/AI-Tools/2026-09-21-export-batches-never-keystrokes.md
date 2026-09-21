---
title: Export Batches, Never Keystrokes
date: '2026-09-21'
source: https://dev.to/gitjs_8094/export-batches-never-keystrokes-3a6
domain: AI-Tools
relevance: 🟡
tags:
- '#ai'
- '#python'
- '#sql'
- '#tool'
related:
- '[[2026-09-08-charge-wait-time-to-the-same-job]]'
- '[[2026-09-12-unclassified-tests-cannot-green-an-agent-patch]]'
- '[[2026-09-07-score-agent-hops-before-they-leave-disk]]'
- '[[2026-09-09-the-idle-gap-wore-a-model-badge]]'
- '[[2026-09-16-faq-five-myths-about-the-model-already-saw-the-repo]]'
- '[[2026-09-05-a-frozen-test-is-not-coverage-a-merge-gate-for-agent-patches]]'
status: unread
---

> **TL;DR:** Interactive completions belong inside the local editor process first. Remote compute should only accept scrubbed, offline-tolerant batches. The tab key is a reflex, not a shipping document. Reflexes die when they must cr…

## What’s new and why it matters
Interactive completions belong inside the local editor process first. Remote compute should only accept scrubbed, offline-tolerant batches. The tab key is a reflex, not a shipping document. Reflexes die when they must cross a building or an ocean. This article splits AI coding work into two job shapes. Completions stay in-process, while refactors may travel after measurement. The split is not ideology but a latency and secrecy budget. Blur the two shapes and the editor starts waiting on weather. Treat the next hour of editing as a closed control loop. Each keystroke expects an answer before at…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Reproduce the example in a notebook; then refactor into a reusable function.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/gitjs_8094/export-batches-never-keystrokes-3a6

## Related notes
- [[2026-09-08-charge-wait-time-to-the-same-job]]
- [[2026-09-12-unclassified-tests-cannot-green-an-agent-patch]]
- [[2026-09-07-score-agent-hops-before-they-leave-disk]]
- [[2026-09-09-the-idle-gap-wore-a-model-badge]]
- [[2026-09-16-faq-five-myths-about-the-model-already-saw-the-repo]]
- [[2026-09-05-a-frozen-test-is-not-coverage-a-merge-gate-for-agent-patches]]
