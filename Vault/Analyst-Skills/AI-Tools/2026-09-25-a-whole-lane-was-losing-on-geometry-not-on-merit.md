---
title: A Whole Lane Was Losing on Geometry, Not on Merit
date: '2026-09-25'
source: https://dev.to/lexosi/a-whole-lane-was-losing-on-geometry-not-on-merit-da9
domain: AI-Tools
relevance: 🟡
tags:
- '#ai'
- '#python'
- '#tool'
- '#zendesk'
related:
- '[[2026-09-01-i-raced-six-models-against-each-other-on-digitalocean-inference-the-cheapest-one-won]]'
- '[[2026-09-04-i-built-an-offline-document-indexer-and-ollama-taught-me-two-things-i-did-not-expect]]'
- '[[2026-08-10-140-bugs-were-hiding-in-one-function-and-my-tests-couldnt-see-any-of-them]]'
- '[[2026-06-15-day-01-of-learning-data-engineering-step1-sql-joins-and-set-operators]]'
- '[[2026-08-31-running-total-in-sql-the-window-frame-that-decides-the-answer]]'
- '[[2026-08-21-how-to-find-duplicate-rows-in-sql-and-decide-what-counts-as-one]]'
status: unread
---

> **TL;DR:** I had three categories of document coming in, and a semantic classifier that scored every one against all three. It worked. Except one of the three never showed up near the top — not rarely, never. The obvious explanatio…

## What’s new and why it matters
I had three categories of document coming in, and a semantic classifier that scored every one against all three. It worked. Except one of the three never showed up near the top — not rarely, never. The obvious explanations were that there were fewer of them, or that they were simply worse matches. Both were wrong. They matched just as well. They were losing on geometry. How a whole lane can lose without being worse The setup is the ordinary one. Each category is described in a paragraph; that paragraph becomes a vector. Each document becomes another vector. Cosine against all three, keep the h…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Reproduce the example in a notebook; then refactor into a reusable function.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/lexosi/a-whole-lane-was-losing-on-geometry-not-on-merit-da9

## Related notes
- [[2026-09-01-i-raced-six-models-against-each-other-on-digitalocean-inference-the-cheapest-one-won]]
- [[2026-09-04-i-built-an-offline-document-indexer-and-ollama-taught-me-two-things-i-did-not-expect]]
- [[2026-08-10-140-bugs-were-hiding-in-one-function-and-my-tests-couldnt-see-any-of-them]]
- [[2026-06-15-day-01-of-learning-data-engineering-step1-sql-joins-and-set-operators]]
- [[2026-08-31-running-total-in-sql-the-window-frame-that-decides-the-answer]]
- [[2026-08-21-how-to-find-duplicate-rows-in-sql-and-decide-what-counts-as-one]]
