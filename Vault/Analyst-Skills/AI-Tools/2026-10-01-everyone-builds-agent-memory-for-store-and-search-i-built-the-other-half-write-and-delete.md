---
title: 'Everyone builds agent memory for store-and-search. I built the other half:
  write and delete.'
date: '2026-10-01'
source: https://dev.to/haoli/everyone-builds-agent-memory-for-store-and-search-i-built-the-other-half-write-and-delete-ab5
domain: AI-Tools
relevance: 🟡
tags:
- '#ai'
- '#python'
- '#sql'
- '#tool'
related:
- '[[2026-09-24-should-you-pay-rs-50000-to-1-lakh-for-a-sql-course-when-free-is-available]]'
- '[[2026-04-20-the-latest-bug-that-silently-duplicated-transaction-ids-in-production]]'
- '[[2026-04-22-i-kept-forgetting-to-delete-my-venvs-so-i-built-a-gui-for-it]]'
- '[[2026-07-23-the-devops-team-that-never-sleeps]]'
- '[[2026-03-13-you-dont-need-a-framework-building-reliable-ai-agents-from-first-principles]]'
- '[[2026-07-31-lao-the-calibration-layer-that-stops-llms-from-forgetting-and-lying-3-line-demo]]'
status: unread
---

> **TL;DR:** The agent-memory space is crowded on the store-and-search side: embeddings, retrieval, ranking. But I kept hitting the neglected half — write and delete : When should a memory fade ? A fact from 6 months ago shouldn't ou…

## What’s new and why it matters
The agent-memory space is crowded on the store-and-search side: embeddings, retrieval, ranking. But I kept hitting the neglected half — write and delete : When should a memory fade ? A fact from 6 months ago shouldn't outrank yesterday's correction. When two memories disagree , who wins? Silent overwrite is how agents end up confidently wrong. When you delete , can you undo it — and can you explain why it was deleted? memgovern treats these as first-class operations. Zero dependencies, SQLite under the hood: Decay: memories carry importance + TTL; queries rank by exponential-decay score, not r…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Reproduce the example in a notebook; then refactor into a reusable function.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/haoli/everyone-builds-agent-memory-for-store-and-search-i-built-the-other-half-write-and-delete-ab5

## Related notes
- [[2026-09-24-should-you-pay-rs-50000-to-1-lakh-for-a-sql-course-when-free-is-available]]
- [[2026-04-20-the-latest-bug-that-silently-duplicated-transaction-ids-in-production]]
- [[2026-04-22-i-kept-forgetting-to-delete-my-venvs-so-i-built-a-gui-for-it]]
- [[2026-07-23-the-devops-team-that-never-sleeps]]
- [[2026-03-13-you-dont-need-a-framework-building-reliable-ai-agents-from-first-principles]]
- [[2026-07-31-lao-the-calibration-layer-that-stops-llms-from-forgetting-and-lying-3-line-demo]]
