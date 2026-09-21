---
title: A Determinism Check Has to Leave the Process
date: '2026-09-21'
source: https://dev.to/megapixel99/a-determinism-check-has-to-leave-the-process-3ink
domain: Presentations
relevance: 🔴
tags:
- '#ai'
- '#feature'
- '#library'
- '#presentations'
- '#python'
- '#tool'
related:
- '[[2026-09-04-i-built-an-offline-document-indexer-and-ollama-taught-me-two-things-i-did-not-expect]]'
- '[[2026-08-07-i-paged-a-table-with-no-order-by-and-lost-2797-rows]]'
- '[[2026-08-31-a-passing-check-is-a-claim-about-what-ran-not-whats-true]]'
- '[[2026-06-15-my-sigma-scanner-cant-count-so-i-wrote-that-down-instead-of-faking-it]]'
- '[[2026-08-21-how-to-find-duplicate-rows-in-sql-and-decide-what-counts-as-one]]'
- '[[2026-08-13-my-doc-drift-checker-has-two-different-ideas-of-documented-and-only-uses-the-wrong-one]]'
status: unread
---

> **TL;DR:** Code: Megapixel99/nondet The obvious way to check whether a Python function is deterministic is to call it twice and compare. I wrote that check, and it is blind to the commonest source of nondeterminism in the language.…

## What’s new and why it matters
Code: Megapixel99/nondet The obvious way to check whether a Python function is deterministic is to call it twice and compare. I wrote that check, and it is blind to the commonest source of nondeterminism in the language. String hashing is randomised per interpreter, so set and dict iteration order is stable within a process and different in every new one. A function returning list({'alpha', 'beta', 'gamma'}) answers identically twenty times out of twenty inside one interpreter. In the transcript the README records, three fresh python3 -c invocations gave three different orderings (six ordering…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Add a short note: what changed in your workflow?

## Relevance
🔴

## Source
https://dev.to/megapixel99/a-determinism-check-has-to-leave-the-process-3ink

## Related notes
- [[2026-09-04-i-built-an-offline-document-indexer-and-ollama-taught-me-two-things-i-did-not-expect]]
- [[2026-08-07-i-paged-a-table-with-no-order-by-and-lost-2797-rows]]
- [[2026-08-31-a-passing-check-is-a-claim-about-what-ran-not-whats-true]]
- [[2026-06-15-my-sigma-scanner-cant-count-so-i-wrote-that-down-instead-of-faking-it]]
- [[2026-08-21-how-to-find-duplicate-rows-in-sql-and-decide-what-counts-as-one]]
- [[2026-08-13-my-doc-drift-checker-has-two-different-ideas-of-documented-and-only-uses-the-wrong-one]]
