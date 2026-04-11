---
title: I built a local screen reader that reads your screen aloud — no cloud, no API
  keys
date: '2026-04-11'
source: https://dev.to/paradisecy/i-built-a-local-screen-reader-that-reads-your-screen-aloud-no-cloud-no-api-keys-m9
domain: Productivity
relevance: 🟡
tags:
- '#feature'
- '#productivity'
- '#python'
- '#tool'
related:
- '[[2026-02-22-building-a-fully-local-offline-trading-research-memory-agent-with-zvec]]'
- '[[2026-02-28-prompt-run-run-prompt-files-against-any-llm-from-your-terminal]]'
- '[[2026-03-18-i-built-a-free-accessibility-auditor-that-actually-passes-its-own-audit]]'
- '[[2026-02-26-i-gave-an-open-source-ai-full-access-to-my-linux-terminal-and-lived-to-tell-the-tale]]'
- '[[2026-03-19-restore-old-photos-with-ai-colorize-enhance-faces-via-api]]'
- '[[2026-04-03-cathedral-gemma-4-persistent-agent-identity-no-cloud-required]]'
status: unread
---

> **TL;DR:** I got tired of switching between reading and listening, so I built sttts — a local pipeline that watches any region of your screen, OCRs it, and speaks it aloud in real time. Everything runs on your own machine. Demo Wha…

## What’s new and why it matters
I got tired of switching between reading and listening, so I built sttts — a local pipeline that watches any region of your screen, OCRs it, and speaks it aloud in real time. Everything runs on your own machine. Demo What it does 🖱️ You draw a rectangle on any part of your screen 📸 It snapshots that region every N seconds 🔍 Pixel diff check — skips frames where nothing changed 🧠 LightOnOCR-2-1B reads the text (runs on AMD GPU via ROCm) 🗣️ Kokoro-82M speaks it through your speakers (runs on CPU) 🖥️ screen → 🔍 diff → 🧠 OCR → ✨ clean text → 🗣️ TTS → 🔊 speaker The killer feature — auto page-turn Y…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/paradisecy/i-built-a-local-screen-reader-that-reads-your-screen-aloud-no-cloud-no-api-keys-m9

## Related notes
- [[2026-02-22-building-a-fully-local-offline-trading-research-memory-agent-with-zvec]]
- [[2026-02-28-prompt-run-run-prompt-files-against-any-llm-from-your-terminal]]
- [[2026-03-18-i-built-a-free-accessibility-auditor-that-actually-passes-its-own-audit]]
- [[2026-02-26-i-gave-an-open-source-ai-full-access-to-my-linux-terminal-and-lived-to-tell-the-tale]]
- [[2026-03-19-restore-old-photos-with-ai-colorize-enhance-faces-via-api]]
- [[2026-04-03-cathedral-gemma-4-persistent-agent-identity-no-cloud-required]]
