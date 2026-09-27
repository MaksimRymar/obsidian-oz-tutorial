---
title: Two hotfixes in one day
date: '2026-09-27'
source: https://dev.to/natuworkguy/two-hotfixes-in-one-day-kpf
domain: AI-Tools
relevance: 🔴
tags:
- '#ai'
- '#feature'
- '#sql'
- '#tool'
related:
- '[[2026-09-02-the-48-hour-verdict-sort-your-ai-failures-before-you-fix-them]]'
- '[[2026-06-13-soft-delete-vs-archive-table-the-choice-that-haunts-your-queries]]'
- '[[2026-05-29-when-web-scraping-breaks-using-ai-to-extract-messy-data]]'
- '[[2026-04-02-how-to-stop-your-ai-agent-from-burning-400month-on-api-calls]]'
- '[[2026-06-20-i-built-a-machine-verifiable-contract-system-for-python-code-heres-how-it-works]]'
- '[[2026-08-09-my-mcp-servers-two-credential-checks-were-flagged-missing-five-days-ago-nobody-fixed-them]]'
status: unread
---

> **TL;DR:** This morning I shipped Flash 0.5.6. A hotfix. By the evening I shipped 0.5.7. Also a hotfix. What broke Flash kept forgetting what it said two messages ago. The model was fine. The math wasn't. Flash reserved room for th…

## What’s new and why it matters
This morning I shipped Flash 0.5.6. A hotfix. By the evening I shipped 0.5.7. Also a hotfix. What broke Flash kept forgetting what it said two messages ago. The model was fine. The math wasn't. Flash reserved room for the model's reply, and on my setup that reservation was the entire context window. The conversation got whatever was left: about two messages. The fix The reply gets a quarter of the window, max. Your last three exchanges always stay word for word. Old tool output shrinks before anything else is dropped. Summarizing is now off by default. The history budget on my machine went fro…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Reproduce the example in a notebook; then refactor into a reusable function.
- Add a short note: what changed in your workflow?

## Relevance
🔴

## Source
https://dev.to/natuworkguy/two-hotfixes-in-one-day-kpf

## Related notes
- [[2026-09-02-the-48-hour-verdict-sort-your-ai-failures-before-you-fix-them]]
- [[2026-06-13-soft-delete-vs-archive-table-the-choice-that-haunts-your-queries]]
- [[2026-05-29-when-web-scraping-breaks-using-ai-to-extract-messy-data]]
- [[2026-04-02-how-to-stop-your-ai-agent-from-burning-400month-on-api-calls]]
- [[2026-06-20-i-built-a-machine-verifiable-contract-system-for-python-code-heres-how-it-works]]
- [[2026-08-09-my-mcp-servers-two-credential-checks-were-flagged-missing-five-days-ago-nobody-fixed-them]]
