---
title: How I Shaved 10 MB Off My Portfolio in One Command
date: '2026-06-03'
source: https://dev.to/highcenburg/how-i-shaved-10-mb-off-my-portfolio-in-one-command-2697
domain: AI-Tools
relevance: 🟡
tags:
- '#ai'
- '#python'
- '#support-analytics'
- '#tool'
related:
- '[[2026-04-23-i-built-a-browser-only-sql-practice-tool-because-installing-dbeaver-is-a-productivity-tax]]'
- '[[2026-04-17-maybe-this-is-how-open-source-apps-are-born]]'
- '[[2026-05-02-uncovering-8-indexeddb-data-loss-after-browser-crashes-with-playwright]]'
- '[[2026-05-15-built-a-tool-that-transforms-your-linux-audio-in-one-command]]'
- '[[2026-04-02-how-to-stop-your-ai-agent-from-burning-400month-on-api-calls]]'
- '[[2026-03-13-you-dont-need-a-framework-building-reliable-ai-agents-from-first-principles]]'
status: unread
---

> **TL;DR:** PageSpeed Insights had been staring at me for weeks. Desktop was holding at 91. Mobile was stuck at 63. I'd already fixed the obvious stuff — non-blocking fonts, preconnects, fetchpriority on the hero image. But there it…

## What’s new and why it matters
PageSpeed Insights had been staring at me for weeks. Desktop was holding at 91. Mobile was stuck at 63. I'd already fixed the obvious stuff — non-blocking fonts, preconnects, fetchpriority on the hero image. But there it was, every single run: Improve image delivery — Est savings of 985 KiB Nearly a megabyte of wasted transfer, just from six project screenshots. And that was just the images visible above the fold. The full list across all projects was worse. The culprit: every image I'd ever uploaded through the Django admin was a PNG. Some of them were over 1 MB. WebP would have cut most of t…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Reproduce the example in a notebook; then refactor into a reusable function.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/highcenburg/how-i-shaved-10-mb-off-my-portfolio-in-one-command-2697

## Related notes
- [[2026-04-23-i-built-a-browser-only-sql-practice-tool-because-installing-dbeaver-is-a-productivity-tax]]
- [[2026-04-17-maybe-this-is-how-open-source-apps-are-born]]
- [[2026-05-02-uncovering-8-indexeddb-data-loss-after-browser-crashes-with-playwright]]
- [[2026-05-15-built-a-tool-that-transforms-your-linux-audio-in-one-command]]
- [[2026-04-02-how-to-stop-your-ai-agent-from-burning-400month-on-api-calls]]
- [[2026-03-13-you-dont-need-a-framework-building-reliable-ai-agents-from-first-principles]]
