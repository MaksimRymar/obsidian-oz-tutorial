---
title: I tested 9 name-matching methods on the OFAC sanctions list. Here's what I
  found.
date: '2026-11-20'
source: https://dev.to/krunal_solanki_f19a805b67/how-fuzzy-name-matching-against-the-ofac-sanctions-list-actually-works-9fl
domain: AI-Tools
relevance: 🟡
tags:
- '#ai'
- '#library'
- '#python'
- '#sql'
- '#tool'
related:
- '[[2026-07-18-im-not-a-real-developer-so-i-built-my-app-the-simplest-way-possible]]'
- '[[2026-11-18-two-hallucination-tests-you-can-run-before-you-pay-for-a-judge-model]]'
- '[[2026-09-01-i-raced-six-models-against-each-other-on-digitalocean-inference-the-cheapest-one-won]]'
- '[[2026-08-11-sql-aliases-how-to-read-a-query-out-loud]]'
- '[[2026-08-20-a-benchmark-is-only-as-good-as-the-model-you-use-to-grade-it]]'
- '[[2026-11-18-how-to-find-out-what-1000-websites-are-built-with-and-what-you-cant-see-from-outside]]'
status: unread
---

> **TL;DR:** If you've ever built customer onboarding for a bank, a lender, a title company or a payments app, you've had to answer one question: is this person on the OFAC sanctions list? The list is public. The hard part is the nam…

## What’s new and why it matters
If you've ever built customer onboarding for a bank, a lender, a title company or a payments app, you've had to answer one question: is this person on the OFAC sanctions list? The list is public. The hard part is the name. Customers type "Aymen Zawahri"; the list says "AL ZAWAHIRI, Dr. Ayman". An exact match misses it. A loose fuzzy match flags half your customers named John. And when a compliance analyst asks why a name was flagged, "the library returned 0.87" is not an answer. I spent ten years building title and mortgage systems, including OFAC screening. This post walks through how I appro…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Reproduce the example in a notebook; then refactor into a reusable function.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/krunal_solanki_f19a805b67/how-fuzzy-name-matching-against-the-ofac-sanctions-list-actually-works-9fl

## Related notes
- [[2026-07-18-im-not-a-real-developer-so-i-built-my-app-the-simplest-way-possible]]
- [[2026-11-18-two-hallucination-tests-you-can-run-before-you-pay-for-a-judge-model]]
- [[2026-09-01-i-raced-six-models-against-each-other-on-digitalocean-inference-the-cheapest-one-won]]
- [[2026-08-11-sql-aliases-how-to-read-a-query-out-loud]]
- [[2026-08-20-a-benchmark-is-only-as-good-as-the-model-you-use-to-grade-it]]
- [[2026-11-18-how-to-find-out-what-1000-websites-are-built-with-and-what-you-cant-see-from-outside]]
