---
title: My .gitignore Had a Blanket Rule. One File Broke It, and No Pattern Would Have
  Caught That.
date: '2026-07-21'
source: https://dev.to/enjoy_kumawat/my-gitignore-had-a-blanket-rule-one-file-broke-it-and-no-pattern-would-have-caught-that-5bmo
domain: AI-Tools
relevance: 🟡
tags:
- '#ai'
- '#best-practice'
- '#python'
- '#sql'
- '#tool'
related:
- '[[2026-07-19-my-comment-reply-bot-hit-a-wall-the-docs-never-mentioned-that-wall-turned-out-to-be-a-security-feature]]'
- '[[2026-07-20-df-said-my-sandbox-had-no-disk-left-it-wasnt-wrong-it-just-wasnt-answering-the-question-i-asked]]'
- '[[2026-06-15-my-sigma-scanner-cant-count-so-i-wrote-that-down-instead-of-faking-it]]'
- '[[2026-05-25-i-added-mcp-support-to-my-saas-in-an-afternoon-heres-the-whole-thing]]'
- '[[2026-06-02-claude-api-from-scratch-your-first-working-call-in-30-minutes-2026]]'
- '[[2026-06-04-i-built-a-cache-engine-from-scratch-in-python-and-o1-lfu-eviction-is-sneakier-than-lru]]'
status: unread
---

> **TL;DR:** A few weeks ago I found out this repo's .gitignore had been silently eating every draft article I ever wrote, since the very first commit. The fix at the time was straightforward: drafts/ was meant to hold ephemeral scra…

## What’s new and why it matters
A few weeks ago I found out this repo's .gitignore had been silently eating every draft article I ever wrote, since the very first commit. The fix at the time was straightforward: drafts/ was meant to hold ephemeral scratch files, so I made that exclusion deliberate instead of accidental and moved on. What I didn't write up then is the part that came right after — the same folder turned out to contain one file that categorically wasn't ephemeral, and the pattern that correctly ignored ninety-nine other files was flatly wrong about this one. I only found that out because I went looking, not bec…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Reproduce the example in a notebook; then refactor into a reusable function.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/enjoy_kumawat/my-gitignore-had-a-blanket-rule-one-file-broke-it-and-no-pattern-would-have-caught-that-5bmo

## Related notes
- [[2026-07-19-my-comment-reply-bot-hit-a-wall-the-docs-never-mentioned-that-wall-turned-out-to-be-a-security-feature]]
- [[2026-07-20-df-said-my-sandbox-had-no-disk-left-it-wasnt-wrong-it-just-wasnt-answering-the-question-i-asked]]
- [[2026-06-15-my-sigma-scanner-cant-count-so-i-wrote-that-down-instead-of-faking-it]]
- [[2026-05-25-i-added-mcp-support-to-my-saas-in-an-afternoon-heres-the-whole-thing]]
- [[2026-06-02-claude-api-from-scratch-your-first-working-call-in-30-minutes-2026]]
- [[2026-06-04-i-built-a-cache-engine-from-scratch-in-python-and-o1-lfu-eviction-is-sneakier-than-lru]]
