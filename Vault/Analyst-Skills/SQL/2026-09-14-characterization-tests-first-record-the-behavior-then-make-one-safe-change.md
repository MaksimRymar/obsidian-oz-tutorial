---
title: 'Characterization Tests First: Record the Behavior, Then Make One Safe Change'
date: '2026-09-14'
source: https://dev.to/hackrs_6393/characterization-tests-first-record-the-behavior-then-make-one-safe-change-4joe
domain: SQL
relevance: 🟡
tags:
- '#ai'
- '#feature'
- '#python'
- '#sql'
- '#tool'
related:
- '[[2026-08-31-i-left-an-ai-agent-running-unattended-for-a-day-here-is-everything-that-broke]]'
- '[[2026-08-29-the-golden-file-refactor-loop-record-verify-move-commit]]'
- '[[2026-09-04-i-built-an-offline-document-indexer-and-ollama-taught-me-two-things-i-did-not-expect]]'
- '[[2026-09-14-characterization-tests-first-the-smallest-safe-refactor-in-a-scary-repo]]'
- '[[2026-09-08-give-the-model-one-json-job-run-everything-else-yourself]]'
- '[[2026-09-05-hash-the-entrypoint-before-you-extract-one-module]]'
status: unread
---

> **TL;DR:** Characterization tests record what the code does today, bugs included. They are a baseline, not a specification. So the order matters: record, freeze the noise, then change one thing. This is the workflow I use on repos…

## What’s new and why it matters
Characterization tests record what the code does today, bugs included. They are a baseline, not a specification. So the order matters: record, freeze the noise, then change one thing. This is the workflow I use on repos where nobody remembers the original intent. It works on a 4,000-line module as well as a 200-line one. The only requirement is a reproducible entry point. Why messy-repo refactors fail without a baseline Most refactors start with a reading of the code, not a recording of it. Reading tells you what you think the code does. A transcript tells you what it actually printed, wrote,…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Write the query in a scratchpad and run EXPLAIN/QUERY PLAN to verify performance.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/hackrs_6393/characterization-tests-first-record-the-behavior-then-make-one-safe-change-4joe

## Related notes
- [[2026-08-31-i-left-an-ai-agent-running-unattended-for-a-day-here-is-everything-that-broke]]
- [[2026-08-29-the-golden-file-refactor-loop-record-verify-move-commit]]
- [[2026-09-04-i-built-an-offline-document-indexer-and-ollama-taught-me-two-things-i-did-not-expect]]
- [[2026-09-14-characterization-tests-first-the-smallest-safe-refactor-in-a-scary-repo]]
- [[2026-09-08-give-the-model-one-json-job-run-everything-else-yourself]]
- [[2026-09-05-hash-the-entrypoint-before-you-extract-one-module]]
