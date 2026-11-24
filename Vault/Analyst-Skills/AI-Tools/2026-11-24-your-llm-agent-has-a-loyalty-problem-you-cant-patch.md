---
title: Your LLM Agent Has a Loyalty Problem You Can't Patch
date: '2026-11-24'
source: https://dev.to/robust_true_try/your-llm-agent-has-a-loyalty-problem-you-cant-patch-p9g
domain: AI-Tools
relevance: 🟡
tags:
- '#ai'
- '#best-practice'
- '#python'
- '#sql'
- '#tool'
related:
- '[[2026-08-11-the-text-to-sql-demo-takes-an-afternoon-the-other-90-is-why-you-should-buy-it]]'
- '[[2026-10-06-mcp-vs-custom-rest-tooling-security-and-the-latest-mcp-architecture]]'
- '[[2026-08-21-how-to-find-duplicate-rows-in-sql-and-decide-what-counts-as-one]]'
- '[[2026-11-11-five-security-tests-for-mcp-servers-and-agents-in-173-lines-of-python]]'
- '[[2026-09-21-how-to-build-a-creator-emails-pipeline-in-one-python-call]]'
- '[[2026-05-15-stop-passing-entire-chat-histories-to-ai-agents]]'
status: unread
---

> **TL;DR:** Your agent refuses a task, and the refusal has nothing to do with your prompt. A developer asked Claude Code to find a Bandcamp page for an artist from an Instagram reel so he could buy the song. The model declined to wo…

## What’s new and why it matters
Your agent refuses a task, and the refusal has nothing to do with your prompt. A developer asked Claude Code to find a Bandcamp page for an artist from an Instagram reel so he could buy the song. The model declined to work around Bandcamp's search challenge -- but happily offered to download the same track from YouTube, which pays the artist nothing. Same user, same session, opposite outcomes. That is not a bug you can fix with better prompting. The provider's policy is baked into the model weights and system plumbing, and it overrides your intent. By the end of this piece you will know how to…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Reproduce the example in a notebook; then refactor into a reusable function.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/robust_true_try/your-llm-agent-has-a-loyalty-problem-you-cant-patch-p9g

## Related notes
- [[2026-08-11-the-text-to-sql-demo-takes-an-afternoon-the-other-90-is-why-you-should-buy-it]]
- [[2026-10-06-mcp-vs-custom-rest-tooling-security-and-the-latest-mcp-architecture]]
- [[2026-08-21-how-to-find-duplicate-rows-in-sql-and-decide-what-counts-as-one]]
- [[2026-11-11-five-security-tests-for-mcp-servers-and-agents-in-173-lines-of-python]]
- [[2026-09-21-how-to-build-a-creator-emails-pipeline-in-one-python-call]]
- [[2026-05-15-stop-passing-entire-chat-histories-to-ai-agents]]
