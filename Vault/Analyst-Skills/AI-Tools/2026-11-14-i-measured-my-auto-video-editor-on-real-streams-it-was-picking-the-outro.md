---
title: I measured my auto video editor on real streams. It was picking the outro.
date: '2026-11-14'
source: https://dev.to/thekillsquad007/i-measured-my-auto-video-editor-on-real-streams-it-was-picking-the-outro-77d
domain: AI-Tools
relevance: 🟡
tags:
- '#ai'
- '#feature'
- '#sql'
- '#support-analytics'
- '#tool'
- '#tutorial'
related:
- '[[2026-06-12-how-i-built-an-open-source-ai-video-editor-you-control-by-chatting]]'
- '[[2026-11-05-your-ai-says-fixed-would-a-test-notice-if-it-wasnt]]'
- '[[2026-10-26-48-hour-field-notes-my-free-box-looked-slow-until-i-logged-the-gap-between-requests]]'
- '[[2026-04-17-maybe-this-is-how-open-source-apps-are-born]]'
- '[[2026-09-04-i-built-an-offline-document-indexer-and-ollama-taught-me-two-things-i-did-not-expect]]'
- '[[2026-04-03-i-got-tired-of-watching-my-terminal-so-i-built-guga]]'
status: unread
---

> **TL;DR:** I build Phoenix Editor , a desktop app that takes a long stream or Let's Play recording, cuts the dead air and filler words, and turns the best moments into captioned vertical Shorts. It runs on your own GPU: faster-whis…

## What’s new and why it matters
I build Phoenix Editor , a desktop app that takes a long stream or Let's Play recording, cuts the dead air and filler words, and turns the best moments into captioned vertical Shorts. It runs on your own GPU: faster-whisper on NVIDIA, whisper.cpp over Vulkan on AMD and Intel, and the encoder your card has. For months the test suite ran it against generated fixtures, and everything passed. Then someone called it "vibecoded slop" in public, and I realised I had no evidence they were wrong. Nothing in the repo showed the edits were actually good on real footage. So I built a harness, ran it on re…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Reproduce the example in a notebook; then refactor into a reusable function.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/thekillsquad007/i-measured-my-auto-video-editor-on-real-streams-it-was-picking-the-outro-77d

## Related notes
- [[2026-06-12-how-i-built-an-open-source-ai-video-editor-you-control-by-chatting]]
- [[2026-11-05-your-ai-says-fixed-would-a-test-notice-if-it-wasnt]]
- [[2026-10-26-48-hour-field-notes-my-free-box-looked-slow-until-i-logged-the-gap-between-requests]]
- [[2026-04-17-maybe-this-is-how-open-source-apps-are-born]]
- [[2026-09-04-i-built-an-offline-document-indexer-and-ollama-taught-me-two-things-i-did-not-expect]]
- [[2026-04-03-i-got-tired-of-watching-my-terminal-so-i-built-guga]]
