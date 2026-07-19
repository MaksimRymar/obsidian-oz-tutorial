---
title: Your LLM can't actually watch video. Here's the smallest fix (MIT)
date: '2026-07-19'
source: https://dev.to/huangchihhungleo/your-llm-cant-actually-watch-video-heres-the-smallest-fix-mit-2igp
domain: AI-Tools
relevance: 🟡
tags:
- '#ai'
- '#tool'
related:
- '[[2026-04-03-stop-switching-between-chatgpt-claude-and-gemini-i-automated-it]]'
- '[[2026-07-18-im-not-a-real-developer-so-i-built-my-app-the-simplest-way-possible]]'
- '[[2026-06-19-i-built-an-open-source-ai-that-security-reviews-every-pull-request-and-maps-each-bug-to-pci-dss-soc-2-gdpr]]'
- '[[2026-06-15-my-sigma-scanner-cant-count-so-i-wrote-that-down-instead-of-faking-it]]'
- '[[2026-04-26-i-built-a-multi-agent-system-without-governance-heres-the-3-layer-stack-i-wish-id-had]]'
- '[[2026-04-02-how-to-stop-your-ai-agent-from-burning-400month-on-api-calls]]'
status: unread
---

> **TL;DR:** Every model card says "multimodal". Then you hand the model a real video file and discover what that means in practice: ChatGPT reads the subtitle track, Claude doesn't accept video files at all. The model narrates a vid…

## What’s new and why it matters
Every model card says "multimodal". Then you hand the model a real video file and discover what that means in practice: ChatGPT reads the subtitle track, Claude doesn't accept video files at all. The model narrates a video it mostly never saw. I unpack viral videos daily for my own content work, so I couldn't route around this. I built a small tool instead. The mechanism claude-real-video converts a video into three things an LLM can genuinely read: Scene-aware sampled frames — ffmpeg scene scores decide where to sample, so you get a frame when the picture changes, not every N seconds. An --ad…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Reproduce the example in a notebook; then refactor into a reusable function.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/huangchihhungleo/your-llm-cant-actually-watch-video-heres-the-smallest-fix-mit-2igp

## Related notes
- [[2026-04-03-stop-switching-between-chatgpt-claude-and-gemini-i-automated-it]]
- [[2026-07-18-im-not-a-real-developer-so-i-built-my-app-the-simplest-way-possible]]
- [[2026-06-19-i-built-an-open-source-ai-that-security-reviews-every-pull-request-and-maps-each-bug-to-pci-dss-soc-2-gdpr]]
- [[2026-06-15-my-sigma-scanner-cant-count-so-i-wrote-that-down-instead-of-faking-it]]
- [[2026-04-26-i-built-a-multi-agent-system-without-governance-heres-the-3-layer-stack-i-wish-id-had]]
- [[2026-04-02-how-to-stop-your-ai-agent-from-burning-400month-on-api-calls]]
