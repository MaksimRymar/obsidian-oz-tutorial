---
title: Sixteen JAX devices on a CPU, and one gradient bug worth finding
date: '2026-10-26'
source: https://dev.to/panditshivam/sixteen-jax-devices-on-a-cpu-and-one-gradient-bug-worth-finding-25f6
domain: AI-Tools
relevance: 🔴
tags:
- '#ai'
- '#feature'
- '#library'
- '#python'
- '#tool'
- '#tutorial'
- '#zendesk'
related:
- '[[2026-09-25-marimo-the-reactive-python-notebook-for-reproducible-data-work]]'
- '[[2026-08-17-test-the-ai-generated-test-in-a-throwaway-two-version-server]]'
- '[[2026-10-11-your-first-sql-query-can-work-before-you-understand-it]]'
- '[[2026-07-01-how-to-write-a-python-script-that-finds-cannibalized-queries-in-a-search-console-export]]'
- '[[2026-07-18-im-not-a-real-developer-so-i-built-my-app-the-simplest-way-possible]]'
- '[[2026-09-14-test-the-next-effect-not-just-the-first-tool-call]]'
status: unread
---

> **TL;DR:** My favorite use for a pretend cluster is a real correctness failure. Here, replacing an average with a sum makes the gradient 16 times larger , even though every shard computes a perfectly sensible local loss. 🐛 Rishiraj…

## What’s new and why it matters
My favorite use for a pretend cluster is a real correctness failure. Here, replacing an average with a sum makes the gradient 16 times larger , even though every shard computes a perfectly sensible local loss. 🐛 Rishiraj Acharya's new Jaxotron walkthrough shows how to expose logical CPU devices to JAX and explore distributed layouts without renting accelerators. I took a smaller route: one linear model, one batch and a deliberately wrong reduction. The whole check fits in a single script. [1] Original explanatory diagram, with values from the executed JAX example. Logical CPU devices share one…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Reproduce the example in a notebook; then refactor into a reusable function.
- Add a short note: what changed in your workflow?

## Relevance
🔴

## Source
https://dev.to/panditshivam/sixteen-jax-devices-on-a-cpu-and-one-gradient-bug-worth-finding-25f6

## Related notes
- [[2026-09-25-marimo-the-reactive-python-notebook-for-reproducible-data-work]]
- [[2026-08-17-test-the-ai-generated-test-in-a-throwaway-two-version-server]]
- [[2026-10-11-your-first-sql-query-can-work-before-you-understand-it]]
- [[2026-07-01-how-to-write-a-python-script-that-finds-cannibalized-queries-in-a-search-console-export]]
- [[2026-07-18-im-not-a-real-developer-so-i-built-my-app-the-simplest-way-possible]]
- [[2026-09-14-test-the-next-effect-not-just-the-first-tool-call]]
