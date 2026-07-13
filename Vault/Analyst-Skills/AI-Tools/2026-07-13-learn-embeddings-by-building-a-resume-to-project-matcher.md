---
title: Learn Embeddings by Building a Resume-to-Project Matcher
date: '2026-07-13'
source: https://dev.to/magickong/learn-embeddings-by-building-a-resume-to-project-matcher-nc7
domain: AI-Tools
relevance: 🟡
tags:
- '#ai'
- '#career'
- '#feature'
- '#python'
- '#sql'
- '#tool'
- '#tutorial'
related:
- '[[2026-06-24-semantic-search-with-postgresql-pragmatism-beats-hype---most-of-the-time]]'
- '[[2026-03-14-the-ai-engineering-stack-in-2026-what-to-learn-first]]'
- '[[2026-04-04-build-your-first-ai-agent-with-langgraph-step-by-step-python-tutorial-2026]]'
- '[[2026-04-05-ai-memory-is-broken-we-built-one-that-forgets]]'
- '[[2026-07-09-create-a-serp-diff-table-for-titles-urls-and-positions]]'
- '[[2026-06-29-hybrid-search-full-text-and-vector-similarity-in-horizondb]]'
status: unread
---

> **TL;DR:** Embedding demos often jump from text to a magical list of “similar” results. A tiny matcher makes the missing steps visible: normalize vectors, compute scores, rank candidates, and inspect failure cases. This example use…

## What’s new and why it matters
Embedding demos often jump from text to a magical list of “similar” results. A tiny matcher makes the missing steps visible: normalize vectors, compute scores, rank candidates, and inspect failure cases. This example uses fixed vectors so it runs without an API key. import numpy as np resume = np . array ([ 0.8 , 0.6 , 0.1 , 0.0 ]) projects = { " accessible React dashboard " : np . array ([ 0.7 , 0.7 , 0.1 , 0.0 ]), " Kubernetes cost monitor " : np . array ([ 0.1 , 0.2 , 0.8 , 0.6 ]), " Python retrieval tutorial " : np . array ([ 0.4 , 0.4 , 0.5 , 0.1 ]), } def unit ( vector ): length = np . l…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Reproduce the example in a notebook; then refactor into a reusable function.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/magickong/learn-embeddings-by-building-a-resume-to-project-matcher-nc7

## Related notes
- [[2026-06-24-semantic-search-with-postgresql-pragmatism-beats-hype---most-of-the-time]]
- [[2026-03-14-the-ai-engineering-stack-in-2026-what-to-learn-first]]
- [[2026-04-04-build-your-first-ai-agent-with-langgraph-step-by-step-python-tutorial-2026]]
- [[2026-04-05-ai-memory-is-broken-we-built-one-that-forgets]]
- [[2026-07-09-create-a-serp-diff-table-for-titles-urls-and-positions]]
- [[2026-06-29-hybrid-search-full-text-and-vector-similarity-in-horizondb]]
