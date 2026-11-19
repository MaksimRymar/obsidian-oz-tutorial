---
title: 'How we tested an AI classifier on marketplace data: two error rates, not one
  accuracy number'
date: '2026-11-19'
source: https://dev.to/sam_compsapi/how-we-tested-an-ai-classifier-on-marketplace-data-two-error-rates-not-one-accuracy-number-3aji
domain: AI-Tools
relevance: 🟡
tags:
- '#ai'
- '#python'
- '#tool'
related:
- '[[2026-08-21-how-to-find-duplicate-rows-in-sql-and-decide-what-counts-as-one]]'
- '[[2026-11-11-your-unique-constraint-in-postgresql-lets-duplicates-through-here-is-how-to-find-every-one]]'
- '[[2026-11-18-how-to-find-out-what-1000-websites-are-built-with-and-what-you-cant-see-from-outside]]'
- '[[2026-11-08-48-hour-field-notes-my-slow-free-endpoint-was-three-different-clocks-in-one-request]]'
- '[[2026-11-18-two-hallucination-tests-you-can-run-before-you-pay-for-a-judge-model]]'
- '[[2026-11-01-getting-only-the-new-dois-from-the-crossref-api-every-day-dates-cursors-and-rate-limits]]'
status: unread
---

> **TL;DR:** Disclosure: we build CompsAPI, the sold-price API whose filter is measured in this post. It was drafted with AI assistance, and every figure below comes from CompsAPI's published test notes. The labels in the test were m…

## What’s new and why it matters
Disclosure: we build CompsAPI, the sold-price API whose filter is measured in this post. It was drafted with AI assistance, and every figure below comes from CompsAPI's published test notes. The labels in the test were made by us, which is a limit I come back to at the end. "The model is 92% accurate" is a sentence that sounds like a result and tells you almost nothing. This post takes one real example, a classifier that labels marketplace sales as "a normal item" or "junk", and shows what the published test numbers say once you split the one percentage into the parts it hides. The task Sold-p…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Reproduce the example in a notebook; then refactor into a reusable function.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/sam_compsapi/how-we-tested-an-ai-classifier-on-marketplace-data-two-error-rates-not-one-accuracy-number-3aji

## Related notes
- [[2026-08-21-how-to-find-duplicate-rows-in-sql-and-decide-what-counts-as-one]]
- [[2026-11-11-your-unique-constraint-in-postgresql-lets-duplicates-through-here-is-how-to-find-every-one]]
- [[2026-11-18-how-to-find-out-what-1000-websites-are-built-with-and-what-you-cant-see-from-outside]]
- [[2026-11-08-48-hour-field-notes-my-slow-free-endpoint-was-three-different-clocks-in-one-request]]
- [[2026-11-18-two-hallucination-tests-you-can-run-before-you-pay-for-a-judge-model]]
- [[2026-11-01-getting-only-the-new-dois-from-the-crossref-api-every-day-dates-cursors-and-rate-limits]]
