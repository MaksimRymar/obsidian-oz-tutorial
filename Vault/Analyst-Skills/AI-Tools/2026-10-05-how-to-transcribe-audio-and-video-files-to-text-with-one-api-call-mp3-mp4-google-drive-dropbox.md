---
title: How to transcribe audio and video files to text with one API call (MP3, MP4,
  Google Drive, Dropbox)
date: '2026-10-05'
source: https://dev.to/clem616/how-to-transcribe-audio-and-video-files-to-text-with-one-api-call-mp3-mp4-google-drive-dropbox-4dml
domain: AI-Tools
relevance: 🟡
tags:
- '#ai'
- '#career'
- '#library'
- '#python'
- '#tool'
- '#tutorial'
related:
- '[[2026-07-17-how-to-use-the-google-flights-api-in-2026-python-mcp-and-a-no-code-shortcut]]'
- '[[2026-10-01-transcribe-tiktok-and-instagram-videos-to-text-with-python-whisper-no-api-key]]'
- '[[2026-09-04-i-built-an-offline-document-indexer-and-ollama-taught-me-two-things-i-did-not-expect]]'
- '[[2026-06-24-why-i-run-ai-locally-instead-of-using-chatgpt-for-client-work]]'
- '[[2026-09-01-i-raced-six-models-against-each-other-on-digitalocean-inference-the-cheapest-one-won]]'
- '[[2026-08-20-apify-store-scraper-market-intelligence-on-every-public-actor-in-2026]]'
status: unread
---

> **TL;DR:** Speech-to-text models are very good now. The annoying part is everything around them: recordings that are too big to upload, video files, and files that live behind a Google Drive or Dropbox share link. This post covers…

## What’s new and why it matters
Speech-to-text models are very good now. The annoying part is everything around them: recordings that are too big to upload, video files, and files that live behind a Google Drive or Dropbox share link. This post covers the do-it-yourself route first, then a one-call alternative I built for myself. The do-it-yourself route Short audio file If you have a short MP3 and Python, open-source Whisper is enough: pip install -U openai-whisper whisper interview.mp3 --model small --output_format txt Video file Whisper wants audio. Pull the audio track out with ffmpeg first, and shrink it while you are t…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Reproduce the example in a notebook; then refactor into a reusable function.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/clem616/how-to-transcribe-audio-and-video-files-to-text-with-one-api-call-mp3-mp4-google-drive-dropbox-4dml

## Related notes
- [[2026-07-17-how-to-use-the-google-flights-api-in-2026-python-mcp-and-a-no-code-shortcut]]
- [[2026-10-01-transcribe-tiktok-and-instagram-videos-to-text-with-python-whisper-no-api-key]]
- [[2026-09-04-i-built-an-offline-document-indexer-and-ollama-taught-me-two-things-i-did-not-expect]]
- [[2026-06-24-why-i-run-ai-locally-instead-of-using-chatgpt-for-client-work]]
- [[2026-09-01-i-raced-six-models-against-each-other-on-digitalocean-inference-the-cheapest-one-won]]
- [[2026-08-20-apify-store-scraper-market-intelligence-on-every-public-actor-in-2026]]
