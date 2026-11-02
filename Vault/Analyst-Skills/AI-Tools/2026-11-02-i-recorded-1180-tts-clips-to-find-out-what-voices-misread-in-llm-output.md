---
title: I recorded 1,180 TTS clips to find out what voices misread in LLM output
date: '2026-11-02'
source: https://dev.to/berkerbatur/i-recorded-1180-tts-clips-to-find-out-what-voices-misread-in-llm-output-1778
domain: AI-Tools
relevance: 🔴
tags:
- '#ai'
- '#feature'
- '#library'
- '#python'
- '#support-analytics'
- '#tool'
related:
- '[[2026-10-28-i-built-an-ai-phone-agent-the-voice-was-never-what-made-it-sound-fake]]'
- '[[2026-09-27-i-built-an-ai-agent-that-snapshots-every-edit-and-runs-your-tests-before-it-says-done]]'
- '[[2026-09-05-enforcing-data-invariants-in-odoo-model-constraints-migrations-and-tests-that-actually-cover-the-fix]]'
- '[[2026-10-05-how-to-get-a-transcript-of-any-spotify-podcast-episode-3-ways-with-and-without-code]]'
- '[[2026-10-17-check-that-a-package-exists-before-your-ai-agent-installs-it]]'
- '[[2026-09-08-cassandra-scylladb-wide-column-data-modeling-done-right]]'
status: unread
---

> **TL;DR:** Every voice agent has the same seam: a language model writes text for a reader, and a text-to-speech model reads it for a listener. The two were never designed for each other. The model writes **Step 1:** run `npm instal…

## What’s new and why it matters
Every voice agent has the same seam: a language model writes text for a reader, and a text-to-speech model reads it for a listener. The two were never designed for each other. The model writes **Step 1:** run `npm install` and the voice says "asterisk asterisk step one". It writes 1,250 units and some voices say "one two five zero". It writes a Turkish phone number as 0532 123 45 67 and the voice reads it as a single number with the wrong suffix. I kept patching these one at a time in prompts and regexes until I decided to do it properly. This post is about the result, and more about how I mea…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Reproduce the example in a notebook; then refactor into a reusable function.
- Add a short note: what changed in your workflow?

## Relevance
🔴

## Source
https://dev.to/berkerbatur/i-recorded-1180-tts-clips-to-find-out-what-voices-misread-in-llm-output-1778

## Related notes
- [[2026-10-28-i-built-an-ai-phone-agent-the-voice-was-never-what-made-it-sound-fake]]
- [[2026-09-27-i-built-an-ai-agent-that-snapshots-every-edit-and-runs-your-tests-before-it-says-done]]
- [[2026-09-05-enforcing-data-invariants-in-odoo-model-constraints-migrations-and-tests-that-actually-cover-the-fix]]
- [[2026-10-05-how-to-get-a-transcript-of-any-spotify-podcast-episode-3-ways-with-and-without-code]]
- [[2026-10-17-check-that-a-package-exists-before-your-ai-agent-installs-it]]
- [[2026-09-08-cassandra-scylladb-wide-column-data-modeling-done-right]]
