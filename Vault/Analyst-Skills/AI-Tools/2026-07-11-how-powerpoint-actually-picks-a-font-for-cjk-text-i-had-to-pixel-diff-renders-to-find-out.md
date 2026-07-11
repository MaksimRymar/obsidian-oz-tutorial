---
title: How PowerPoint actually picks a font for CJK text (I had to pixel-diff renders
  to find out)
date: '2026-07-11'
source: https://dev.to/loveash/how-powerpoint-actually-picks-a-font-for-cjk-text-i-had-to-pixel-diff-renders-to-find-out-3ajj
domain: AI-Tools
relevance: 🟡
tags:
- '#ai'
- '#presentations'
- '#python'
- '#sql'
- '#tool'
related:
- '[[2026-06-04-i-built-a-cache-engine-from-scratch-in-python-and-o1-lfu-eviction-is-sneakier-than-lru]]'
- '[[2026-07-04-how-pythons-rglob-silently-loses-files-and-why-macos-makes-it-worse]]'
- '[[2026-03-23-i-was-so-tired-of-my-ai-agent-starting-from-zero-every-single-session]]'
- '[[2026-02-24-stop-using-any-the-wrong-way-in-rails]]'
- '[[2026-04-30-the-database-is-where-ai-agents-in-production-get-weird]]'
- '[[2026-06-15-my-sigma-scanner-cant-count-so-i-wrote-that-down-instead-of-faking-it]]'
status: unread
---

> **TL;DR:** I build a lot of .pptx files with LLM agents and python-pptx. The most damaging defect I kept shipping was invisible in code review: CJK text silently rendering in the wrong font. No error, no warning. The file opens fin…

## What’s new and why it matters
I build a lot of .pptx files with LLM agents and python-pptx. The most damaging defect I kept shipping was invisible in code review: CJK text silently rendering in the wrong font. No error, no warning. The file opens fine. The text is just... not in the font anyone chose. This post is about the day I stopped guessing how PowerPoint resolves fonts and measured it instead, and about the open-source linter that came out of it. The question that has no documented answer OOXML (ECMA-376) gives every text run three font slots: a:latin , a:ea (East Asian), and a:cs (complex script). On top of that si…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Reproduce the example in a notebook; then refactor into a reusable function.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/loveash/how-powerpoint-actually-picks-a-font-for-cjk-text-i-had-to-pixel-diff-renders-to-find-out-3ajj

## Related notes
- [[2026-06-04-i-built-a-cache-engine-from-scratch-in-python-and-o1-lfu-eviction-is-sneakier-than-lru]]
- [[2026-07-04-how-pythons-rglob-silently-loses-files-and-why-macos-makes-it-worse]]
- [[2026-03-23-i-was-so-tired-of-my-ai-agent-starting-from-zero-every-single-session]]
- [[2026-02-24-stop-using-any-the-wrong-way-in-rails]]
- [[2026-04-30-the-database-is-where-ai-agents-in-production-get-weird]]
- [[2026-06-15-my-sigma-scanner-cant-count-so-i-wrote-that-down-instead-of-faking-it]]
