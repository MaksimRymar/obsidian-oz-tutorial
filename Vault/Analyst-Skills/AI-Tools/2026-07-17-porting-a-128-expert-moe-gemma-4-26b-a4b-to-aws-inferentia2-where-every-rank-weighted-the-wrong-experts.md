---
title: Porting a 128-expert MoE (Gemma-4 26B-A4B) to AWS Inferentia2 — where every
  rank weighted the wrong experts
date: '2026-07-17'
source: https://dev.to/xbill/porting-a-128-expert-moe-gemma-4-26b-a4b-to-aws-inferentia2-where-every-rank-weighted-the-wrong-2ege
domain: AI-Tools
relevance: 🟡
tags:
- '#ai'
- '#python'
- '#sql'
- '#tool'
related:
- '[[2026-07-17-my-inferentia-port-matched-its-reference-token-for-token-and-still-output-garbage]]'
- '[[2026-07-17-porting-gemma-4-12b-the-encoder-free-multimodal-one-to-aws-inferentia2]]'
- '[[2026-04-22-your-pytest-retries-are-lying-to-you-the-hidden-cost-of---reruns-and-the-plugin-i-wrote-so-i-could-actually-see-what-my-]]'
- '[[2026-05-29-part-14-window-functions-ninja-mode]]'
- '[[2026-07-02-dont-use-not-in]]'
- '[[2026-06-20-green-unit-tests-are-a-comfort-blanket]]'
status: unread
---

> **TL;DR:** Of the five Gemma-4 models I ported to AWS Inferentia2, the 26B-A4B was the one that was supposed to be impossible: a Mixture of Experts . It compiled on the first try — then produced nothing . The device output was empt…

## What’s new and why it matters
Of the five Gemma-4 models I ported to AWS Inferentia2, the 26B-A4B was the one that was supposed to be impossible: a Mixture of Experts . It compiled on the first try — then produced nothing . The device output was empty. The CPU reference was perfect. My unit tests all passed. The bug was in a place I'd have sworn couldn't have one. This is the MoE entry in the series. The dense models (E2B/E4B/12B/31B) are hard because of architecture; the 26B is hard because it's sparse — 128 experts, top-8 routing — and none of the AWS vendor stack has ever traced an MoE for Gemma-4. Model google/gemma-4-…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Reproduce the example in a notebook; then refactor into a reusable function.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/xbill/porting-a-128-expert-moe-gemma-4-26b-a4b-to-aws-inferentia2-where-every-rank-weighted-the-wrong-2ege

## Related notes
- [[2026-07-17-my-inferentia-port-matched-its-reference-token-for-token-and-still-output-garbage]]
- [[2026-07-17-porting-gemma-4-12b-the-encoder-free-multimodal-one-to-aws-inferentia2]]
- [[2026-04-22-your-pytest-retries-are-lying-to-you-the-hidden-cost-of---reruns-and-the-plugin-i-wrote-so-i-could-actually-see-what-my-]]
- [[2026-05-29-part-14-window-functions-ninja-mode]]
- [[2026-07-02-dont-use-not-in]]
- [[2026-06-20-green-unit-tests-are-a-comfort-blanket]]
