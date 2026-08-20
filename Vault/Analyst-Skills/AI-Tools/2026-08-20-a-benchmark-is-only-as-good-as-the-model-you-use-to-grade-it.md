---
title: A benchmark is only as good as the model you use to grade it
date: '2026-08-20'
source: https://dev.to/sara_bezjak/a-benchmark-is-only-as-good-as-the-model-you-use-to-grade-it-4h01
domain: AI-Tools
relevance: 🟡
tags:
- '#ai'
- '#sql'
- '#tool'
related:
- '[[2026-04-17-maybe-this-is-how-open-source-apps-are-born]]'
- '[[2026-04-22-your-pytest-retries-are-lying-to-you-the-hidden-cost-of---reruns-and-the-plugin-i-wrote-so-i-could-actually-see-what-my-]]'
- '[[2026-05-13-the-silent-failure-i-never-saw-coming-what-vaultpay-taught-me-about-consistency-under-failure]]'
- '[[2026-07-22-when-to-trust-ai-generated-sql-and-when-not-to]]'
- '[[2026-06-02-deepseek-vs-qwen-vs-kimi-vs-glm-which-chinese-ai-model-actually-wins-in-2026]]'
- '[[2026-06-29-i-wish-id-known-about-ai-api-speed-sooner-heres-my-honest-breakdown]]'
status: unread
---

> **TL;DR:** I built a pytest harness that runs the same set of questions through five language models at once - a free local Llama, plus GPT, DeepSeek, and two Claude models - and compares them on the three things a team pays for: c…

## What’s new and why it matters
I built a pytest harness that runs the same set of questions through five language models at once - a free local Llama, plus GPT, DeepSeek, and two Claude models - and compares them on the three things a team pays for: cost per query, speed, and answer quality. The plan was simple. Run the grid, read the scoreboard, say which model to use. The scoreboard came back clean and easy to read. This is the story of why I didn't trust it, and what I found when I checked. The thing I stopped trusting wasn't any of the models. It was the tool I was using to score them. It's also the first project in thi…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Reproduce the example in a notebook; then refactor into a reusable function.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/sara_bezjak/a-benchmark-is-only-as-good-as-the-model-you-use-to-grade-it-4h01

## Related notes
- [[2026-04-17-maybe-this-is-how-open-source-apps-are-born]]
- [[2026-04-22-your-pytest-retries-are-lying-to-you-the-hidden-cost-of---reruns-and-the-plugin-i-wrote-so-i-could-actually-see-what-my-]]
- [[2026-05-13-the-silent-failure-i-never-saw-coming-what-vaultpay-taught-me-about-consistency-under-failure]]
- [[2026-07-22-when-to-trust-ai-generated-sql-and-when-not-to]]
- [[2026-06-02-deepseek-vs-qwen-vs-kimi-vs-glm-which-chinese-ai-model-actually-wins-in-2026]]
- [[2026-06-29-i-wish-id-known-about-ai-api-speed-sooner-heres-my-honest-breakdown]]
