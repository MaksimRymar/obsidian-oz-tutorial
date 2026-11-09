---
title: Adding a live FPS counter to a tiny USB PC screen (and the update bug that
  came with it)
date: '2026-11-09'
source: https://dev.to/emirmrkaljevic/adding-a-live-fps-counter-to-a-tiny-usb-pc-screen-and-the-update-bug-that-came-with-it-55a7
domain: Productivity
relevance: 🔴
tags:
- '#feature'
- '#productivity'
- '#sql'
- '#tool'
related:
- '[[2026-09-04-i-built-an-offline-document-indexer-and-ollama-taught-me-two-things-i-did-not-expect]]'
- '[[2026-10-05-how-to-get-a-transcript-of-any-spotify-podcast-episode-3-ways-with-and-without-code]]'
- '[[2026-10-17-check-that-a-package-exists-before-your-ai-agent-installs-it]]'
- '[[2026-08-12-my-comment-reply-pipeline-picks-one-winner-per-thread-two-commenters-broke-that]]'
- '[[2026-04-17-maybe-this-is-how-open-source-apps-are-born]]'
- '[[2026-06-15-my-sigma-scanner-cant-count-so-i-wrote-that-down-instead-of-faking-it]]'
status: unread
---

> **TL;DR:** The small 3.5 inch USB screen in my PC case runs a tray app I wrote called PanelOS. It shows CPU and GPU temps, watts, RAM and VRAM, a fan, and the song that is playing in the Spotify desktop app with its cover. The most…

## What’s new and why it matters
The small 3.5 inch USB screen in my PC case runs a tray app I wrote called PanelOS. It shows CPU and GPU temps, watts, RAM and VRAM, a fan, and the song that is playing in the Spotify desktop app with its cover. The most requested thing was simple: show the FPS of the game I am playing. Where the number comes from I did not want an overlay or to inject anything into games. Windows already reports every frame a program presents through ETW (Event Tracing for Windows). PanelOS listens to those present events, keeps only the ones from the app in the foreground, and counts them per second. No hook…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Add a short note: what changed in your workflow?

## Relevance
🔴

## Source
https://dev.to/emirmrkaljevic/adding-a-live-fps-counter-to-a-tiny-usb-pc-screen-and-the-update-bug-that-came-with-it-55a7

## Related notes
- [[2026-09-04-i-built-an-offline-document-indexer-and-ollama-taught-me-two-things-i-did-not-expect]]
- [[2026-10-05-how-to-get-a-transcript-of-any-spotify-podcast-episode-3-ways-with-and-without-code]]
- [[2026-10-17-check-that-a-package-exists-before-your-ai-agent-installs-it]]
- [[2026-08-12-my-comment-reply-pipeline-picks-one-winner-per-thread-two-commenters-broke-that]]
- [[2026-04-17-maybe-this-is-how-open-source-apps-are-born]]
- [[2026-06-15-my-sigma-scanner-cant-count-so-i-wrote-that-down-instead-of-faking-it]]
