---
title: Building an Open-Source Text-to-30s-Cinematic-Reel Pipeline on a Single AMD
  MI300X
date: '2026-05-12'
source: https://dev.to/bladedevoff/building-an-open-source-text-to-30s-cinematic-reel-pipeline-on-a-single-amd-mi300x-5hhi
domain: AI-Tools
relevance: 🟡
tags:
- '#ai'
- '#sql'
- '#tool'
- '#zendesk'
related:
- '[[2026-04-13-pc-workman-v172-i-built-a-driver-booster-competitor-from-scratch-fixes-monday-grind-blueprint-3]]'
- '[[2026-02-22-a-beginners-guide-to-making-data-web-applications-using-python-with-streamlit]]'
- '[[2026-04-11-i-trusted-the-code-ai-wrote-for-me-my-data-was-silently-broken-the-whole-time]]'
- '[[2026-04-03-cathedral-gemma-4-persistent-agent-identity-no-cloud-required]]'
- '[[2026-04-06-i-built-an-open-source-benchmark-that-scores-ai-agents-not-models]]'
- '[[2026-03-16-wan-27-the-open-source-ai-video-generator-that-rivals-closed-source-models]]'
status: unread
---

> **TL;DR:** Built this for the AMD x lablab hackathon. One English sentence becomes a 30-second cinematic reel with characters, story, music, and per-shot voice-over. ~45 minutes end-to-end on a single AMD Instinct MI300X. Every mod…

## What’s new and why it matters
Built this for the AMD x lablab hackathon. One English sentence becomes a 30-second cinematic reel with characters, story, music, and per-shot voice-over. ~45 minutes end-to-end on a single AMD Instinct MI300X. Every model is Apache 2.0 or MIT. Code: github.com/bladedevoff/studiomi300 Architecture The Director also doubles as the Vision Critic — same Qwen3.5-35B checkpoint reloaded with a different system prompt, two roles. Saves 70 GB of VRAM. Why a single MI300X 192 GB HBM3 lets four very different architectures share one card sequentially: 35B MoE director, 4B diffusion, 14B I2V MoE, 3.5B m…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Reproduce the example in a notebook; then refactor into a reusable function.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/bladedevoff/building-an-open-source-text-to-30s-cinematic-reel-pipeline-on-a-single-amd-mi300x-5hhi

## Related notes
- [[2026-04-13-pc-workman-v172-i-built-a-driver-booster-competitor-from-scratch-fixes-monday-grind-blueprint-3]]
- [[2026-02-22-a-beginners-guide-to-making-data-web-applications-using-python-with-streamlit]]
- [[2026-04-11-i-trusted-the-code-ai-wrote-for-me-my-data-was-silently-broken-the-whole-time]]
- [[2026-04-03-cathedral-gemma-4-persistent-agent-identity-no-cloud-required]]
- [[2026-04-06-i-built-an-open-source-benchmark-that-scores-ai-agents-not-models]]
- [[2026-03-16-wan-27-the-open-source-ai-video-generator-that-rivals-closed-source-models]]
