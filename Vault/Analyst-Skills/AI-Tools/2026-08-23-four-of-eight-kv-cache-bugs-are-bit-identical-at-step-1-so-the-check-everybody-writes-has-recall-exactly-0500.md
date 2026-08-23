---
title: Four of Eight KV-Cache Bugs Are Bit-Identical at Step 1, So the Check Everybody
  Writes Has Recall Exactly 0.500
date: '2026-08-23'
source: https://dev.to/dev48v/four-of-eight-kv-cache-bugs-are-bit-identical-at-step-1-so-the-check-everybody-writes-has-recall-5gkn
domain: AI-Tools
relevance: 🟡
tags:
- '#ai'
- '#sql'
- '#tool'
related:
- '[[2026-07-23-btree-height-after-delete-postgresql-fast-root]]'
- '[[2026-08-19-the-arabic-pdf-bug-was-never-in-my-code-it-was-the-library-version]]'
- '[[2026-08-04-you-cant-unit-test-an-llm-heres-what-i-built-instead]]'
- '[[2026-08-21-how-to-find-duplicate-rows-in-sql-and-decide-what-counts-as-one]]'
- '[[2026-08-13-my-doc-drift-checker-has-two-different-ideas-of-documented-and-only-uses-the-wrong-one]]'
- '[[2026-08-19-final-weeks-of-gsoc]]'
status: unread
---

> **TL;DR:** A KV cache is not an approximation. Under causal attention, appending a token cannot move an earlier position's residual stream, keys or values - measured at exactly 0 per layer - so a cached decode and a full recompute…

## What’s new and why it matters
A KV cache is not an approximation. Under causal attention, appending a token cannot move an earlier position's residual stream, keys or values - measured at exactly 0 per layer - so a cached decode and a full recompute are the same function. Turn the mask off and the cache is still exact at layer 1 and wrong from layer 2, which is the depth at which information can flow backwards. So any deviation is a bug, and the test everyone writes compares the two paths at one step: forward ( M , tokens , { cache }) // all T positions, layer-major, fills the cache decodeStep ( M , cache , tok , pos ) //…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Reproduce the example in a notebook; then refactor into a reusable function.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/dev48v/four-of-eight-kv-cache-bugs-are-bit-identical-at-step-1-so-the-check-everybody-writes-has-recall-5gkn

## Related notes
- [[2026-07-23-btree-height-after-delete-postgresql-fast-root]]
- [[2026-08-19-the-arabic-pdf-bug-was-never-in-my-code-it-was-the-library-version]]
- [[2026-08-04-you-cant-unit-test-an-llm-heres-what-i-built-instead]]
- [[2026-08-21-how-to-find-duplicate-rows-in-sql-and-decide-what-counts-as-one]]
- [[2026-08-13-my-doc-drift-checker-has-two-different-ideas-of-documented-and-only-uses-the-wrong-one]]
- [[2026-08-19-final-weeks-of-gsoc]]
