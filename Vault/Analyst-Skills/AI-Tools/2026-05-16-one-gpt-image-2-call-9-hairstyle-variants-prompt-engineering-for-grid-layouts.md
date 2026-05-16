---
title: 'One gpt-image-2 call, 9 hairstyle variants: prompt engineering for grid layouts'
date: '2026-05-16'
source: https://dev.to/xspring1982/one-gpt-image-2-call-9-hairstyle-variants-prompt-engineering-for-grid-layouts-23ke
domain: AI-Tools
relevance: 🟡
tags:
- '#ai'
- '#best-practice'
- '#feature'
- '#python'
- '#tool'
- '#zendesk'
related:
- '[[2026-04-17-maybe-this-is-how-open-source-apps-are-born]]'
- '[[2026-03-15-why-i-as-someone-who-likes-mysql-now-want-to-recommend-postgresql]]'
- '[[2026-04-02-how-to-stop-your-ai-agent-from-burning-400month-on-api-calls]]'
- '[[2026-03-14-how-to-swap-faces-in-images-with-an-ai-api]]'
- '[[2026-02-22-a-beginners-guide-to-making-data-web-applications-using-python-with-streamlit]]'
- '[[2026-03-09-i-got-frustrated-my-ai-kept-forgetting-me-so-i-spent-6-months-building-a-fix]]'
status: unread
---

> **TL;DR:** The first version of our hairstyle preview tool made 8 separate gpt-image-2 API calls — one per hairstyle. It worked. It was also $0.32 per preview, took 40 seconds, and the faces drifted between calls (each generation r…

## What’s new and why it matters
The first version of our hairstyle preview tool made 8 separate gpt-image-2 API calls — one per hairstyle. It worked. It was also $0.32 per preview, took 40 seconds, and the faces drifted between calls (each generation re-derived the face from the prompt + uploaded image). This post is about how we cut that to a single API call producing a 9-grid (1 reference + 8 variants) — same face, lower cost, faster, and weirdly easier to prompt. The 8-call problem Naive architecture: for hairstyle in [ ' crew cut ' , ' mid fade ' , ...]: img = gpt_image_2 . generate ( prompt = f " User ' s face with { ha…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Reproduce the example in a notebook; then refactor into a reusable function.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/xspring1982/one-gpt-image-2-call-9-hairstyle-variants-prompt-engineering-for-grid-layouts-23ke

## Related notes
- [[2026-04-17-maybe-this-is-how-open-source-apps-are-born]]
- [[2026-03-15-why-i-as-someone-who-likes-mysql-now-want-to-recommend-postgresql]]
- [[2026-04-02-how-to-stop-your-ai-agent-from-burning-400month-on-api-calls]]
- [[2026-03-14-how-to-swap-faces-in-images-with-an-ai-api]]
- [[2026-02-22-a-beginners-guide-to-making-data-web-applications-using-python-with-streamlit]]
- [[2026-03-09-i-got-frustrated-my-ai-kept-forgetting-me-so-i-spent-6-months-building-a-fix]]
