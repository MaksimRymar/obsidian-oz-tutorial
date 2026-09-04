---
title: I pulled Roblox's public API every day for a week to watch one game go vertical
date: '2026-09-04'
source: https://dev.to/jackzhouqd/i-pulled-robloxs-public-api-every-day-for-a-week-to-watch-one-game-go-vertical-1m7h
domain: AI-Tools
relevance: 🟡
tags:
- '#ai'
- '#python'
- '#tool'
- '#tutorial'
related:
- '[[2026-08-21-how-to-find-duplicate-rows-in-sql-and-decide-what-counts-as-one]]'
- '[[2026-04-17-maybe-this-is-how-open-source-apps-are-born]]'
- '[[2026-08-12-im-building-an-algorithmic-trading-system-in-python]]'
- '[[2026-06-19-the-hard-part-of-national-id-ocr-isnt-the-ocr]]'
- '[[2026-08-17-try-minimax-h3-without-hardcoding-it-into-your-free-server]]'
- '[[2026-04-02-how-to-stop-your-ai-agent-from-burning-400month-on-api-calls]]'
status: unread
---

> **TL;DR:** Late August I kept seeing the name Dungeon Lootr in places it hadn't been before. I wanted to know whether the game was actually growing or whether I was just noticing it more. Turns out Roblox exposes enough public data…

## What’s new and why it matters
Late August I kept seeing the name Dungeon Lootr in places it hadn't been before. I wanted to know whether the game was actually growing or whether I was just noticing it more. Turns out Roblox exposes enough public data to answer that without an API key, so I started pulling it every day. The endpoint is boring in the best way: curl "https://games.roblox.com/v1/games?universeIds=9656201728" You get back visits , playing , favoritedCount , updated and a few other fields. A second call to /v1/games/votes?universeIds=... gives you up and down votes. No auth, no rate-limit drama at once-a-day vol…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Reproduce the example in a notebook; then refactor into a reusable function.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/jackzhouqd/i-pulled-robloxs-public-api-every-day-for-a-week-to-watch-one-game-go-vertical-1m7h

## Related notes
- [[2026-08-21-how-to-find-duplicate-rows-in-sql-and-decide-what-counts-as-one]]
- [[2026-04-17-maybe-this-is-how-open-source-apps-are-born]]
- [[2026-08-12-im-building-an-algorithmic-trading-system-in-python]]
- [[2026-06-19-the-hard-part-of-national-id-ocr-isnt-the-ocr]]
- [[2026-08-17-try-minimax-h3-without-hardcoding-it-into-your-free-server]]
- [[2026-04-02-how-to-stop-your-ai-agent-from-burning-400month-on-api-calls]]
