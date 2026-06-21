---
title: I built a VAD that beats Silero, Pyannote, and WebRTC on noisy audio — here's
  how
date: '2026-06-21'
source: https://dev.to/m_m_ce8454e07d6b8ffa6af4b/i-built-a-vad-that-beats-silero-pyannote-and-webrtc-on-noisy-audio-heres-how-4lmj
domain: AI-Tools
relevance: 🟡
tags:
- '#ai'
- '#feature'
- '#tool'
related:
- '[[2026-04-13-building-a-voice-controlled-ai-agent-with-groq-whisper-and-gradio]]'
- '[[2026-04-24-the-five-most-important-columns-to-add-to-every-database-table]]'
- '[[2026-04-15-how-to-see-inside-your-ai-model-in-3-lines-of-python]]'
- '[[2026-03-06-i-built-an-automated-call-to-tasks-pipeline-with-claude-code-whisper-and-caldav]]'
- '[[2026-05-20-how-i-built-a-free-carbon-credit-risk-model-using-nasa-satellite-data-dbt-and-streamlit]]'
- '[[2026-04-05-i-built-a-free-offline-all-in-one-file-converter-for-windows-documents-images-audio-video-no-uploads-no-account]]'
status: unread
---

> **TL;DR:** I built NOVA-VAD — a lightweight, explainable Voice Activity Detector that beats every major open source VAD on real-world noisy audio. GitHub:( https://github.com/monishmal3375/nova-vad ) Benchmark (100 held-out files,…

## What’s new and why it matters
I built NOVA-VAD — a lightweight, explainable Voice Activity Detector that beats every major open source VAD on real-world noisy audio. GitHub:( https://github.com/monishmal3375/nova-vad ) Benchmark (100 held-out files, never seen during training) Model Accuracy Lightweight Explainable WebRTC VAD 58.0% ✅ ❌ Pyannote VAD 62.0% ❌ ❌ Silero VAD 87.0% ❌ ❌ NOVA-VAD 93.0% ✅ ✅ What makes it different No PyTorch or GPU required — pure scikit-learn Explains every decision with confidence scores and feature importance Built-in denoiser pipeline Retrainable on your own data No existing VAD does all three s…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Reproduce the example in a notebook; then refactor into a reusable function.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/m_m_ce8454e07d6b8ffa6af4b/i-built-a-vad-that-beats-silero-pyannote-and-webrtc-on-noisy-audio-heres-how-4lmj

## Related notes
- [[2026-04-13-building-a-voice-controlled-ai-agent-with-groq-whisper-and-gradio]]
- [[2026-04-24-the-five-most-important-columns-to-add-to-every-database-table]]
- [[2026-04-15-how-to-see-inside-your-ai-model-in-3-lines-of-python]]
- [[2026-03-06-i-built-an-automated-call-to-tasks-pipeline-with-claude-code-whisper-and-caldav]]
- [[2026-05-20-how-i-built-a-free-carbon-credit-risk-model-using-nasa-satellite-data-dbt-and-streamlit]]
- [[2026-04-05-i-built-a-free-offline-all-in-one-file-converter-for-windows-documents-images-audio-video-no-uploads-no-account]]
