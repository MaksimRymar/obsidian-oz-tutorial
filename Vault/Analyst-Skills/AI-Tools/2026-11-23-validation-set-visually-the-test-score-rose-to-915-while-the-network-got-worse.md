---
title: 'Validation set, visually: the test score rose to 91.5% while the network got
  worse'
date: '2026-11-23'
source: https://dev.to/logitsolutionsai/validation-set-visually-the-test-score-rose-to-915-while-the-network-got-worse-58lb
domain: AI-Tools
relevance: 🟡
tags:
- '#ai'
- '#best-practice'
- '#python'
- '#tool'
related:
- '[[2026-09-01-i-raced-six-models-against-each-other-on-digitalocean-inference-the-cheapest-one-won]]'
- '[[2026-10-17-i-added-a-fourth-shard-in-python-and-75-of-the-keys-moved]]'
- '[[2026-06-12-build-a-rag-chatbot-from-scratch-in-about-40-lines-of-python]]'
- '[[2026-11-18-google-maps-rank-tracker-check-your-google-maps-ranking-from-every-street-around-you]]'
- '[[2026-08-04-you-cant-unit-test-an-llm-heres-what-i-built-instead]]'
- '[[2026-11-11-setting-up-postgresql-with-docker-psql-and-pgadmin]]'
status: unread
---

> **TL;DR:** Deep Learning, Visually #22 Watch the Short: youtube.com/watch?v=qxIv68yQA0A A test set is supposed to tell you how good your network really is. It can only do that if you never use it to choose anything. In this article…

## What’s new and why it matters
Deep Learning, Visually #22 Watch the Short: youtube.com/watch?v=qxIv68yQA0A A test set is supposed to tell you how good your network really is. It can only do that if you never use it to choose anything. In this article we break that rule on purpose, in a real experiment, and measure what it costs. An honest score We train a small digit network on 1,000 images: 26,432 weights, Adam, the same setup as the runs in this series. We stop at epoch 14, where its loss on new images is lowest. We keep 200 more images as a test set. The network never trains on them, so its score there should be honest.…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Reproduce the example in a notebook; then refactor into a reusable function.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/logitsolutionsai/validation-set-visually-the-test-score-rose-to-915-while-the-network-got-worse-58lb

## Related notes
- [[2026-09-01-i-raced-six-models-against-each-other-on-digitalocean-inference-the-cheapest-one-won]]
- [[2026-10-17-i-added-a-fourth-shard-in-python-and-75-of-the-keys-moved]]
- [[2026-06-12-build-a-rag-chatbot-from-scratch-in-about-40-lines-of-python]]
- [[2026-11-18-google-maps-rank-tracker-check-your-google-maps-ranking-from-every-street-around-you]]
- [[2026-08-04-you-cant-unit-test-an-llm-heres-what-i-built-instead]]
- [[2026-11-11-setting-up-postgresql-with-docker-psql-and-pgadmin]]
