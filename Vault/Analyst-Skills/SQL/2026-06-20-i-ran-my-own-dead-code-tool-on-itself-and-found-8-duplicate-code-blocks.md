---
title: I ran my own dead-code tool on itself and found 8 duplicate code blocks
date: '2026-06-20'
source: https://dev.to/prathik_arun_a1b1871bbbd3/i-ran-my-own-dead-code-tool-on-itself-and-found-8-duplicate-code-blocks-3e8p
domain: SQL
relevance: 🟡
tags:
- '#python'
- '#sql'
- '#tool'
related:
- '[[2026-05-03-shipping-python-and-node-sdks-for-html2dochub]]'
- '[[2026-03-13-you-dont-need-a-framework-building-reliable-ai-agents-from-first-principles]]'
- '[[2026-06-05-i-tried-ai-powered-web-scraping-so-my-selectors-could-finally-rest]]'
- '[[2026-04-22-i-kept-forgetting-to-delete-my-venvs-so-i-built-a-gui-for-it]]'
- '[[2026-03-13-i-built-and-launched-a-mobile-app-in-3-months-as-a-solo-engineer-heres-exactly-what-happened]]'
- '[[2026-05-31-i-built-a-release-intelligence-agent-in-4-days-with-coral-groq-and-claude-code-heres-the-exact-route]]'
status: unread
---

> **TL;DR:** A few weeks ago I shipped Archaeologist, a codebase intelligence toolkit. This week I finally pointed it at its own source code. It found 8 duplicate groups in scanner.py — the file responsible for parsing 9 different la…

## What’s new and why it matters
A few weeks ago I shipped Archaeologist, a codebase intelligence toolkit. This week I finally pointed it at its own source code. It found 8 duplicate groups in scanner.py — the file responsible for parsing 9 different languages. Three of them were 84-89% identical: walk() in the JS scanner — 89% similar to walk() in the Go scanner walk() in the Rust scanner — 87% similar walk() in the Java scanner — 86% similar Turns out every one of my 9 language scanners (Python, JS, Ruby, Go, Java, Rust, Kotlin, Swift) had copy-pasted the same ~40 line walk/ recurse/build-FunctionDef boilerplate, with only…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Write the query in a scratchpad and run EXPLAIN/QUERY PLAN to verify performance.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/prathik_arun_a1b1871bbbd3/i-ran-my-own-dead-code-tool-on-itself-and-found-8-duplicate-code-blocks-3e8p

## Related notes
- [[2026-05-03-shipping-python-and-node-sdks-for-html2dochub]]
- [[2026-03-13-you-dont-need-a-framework-building-reliable-ai-agents-from-first-principles]]
- [[2026-06-05-i-tried-ai-powered-web-scraping-so-my-selectors-could-finally-rest]]
- [[2026-04-22-i-kept-forgetting-to-delete-my-venvs-so-i-built-a-gui-for-it]]
- [[2026-03-13-i-built-and-launched-a-mobile-app-in-3-months-as-a-solo-engineer-heres-exactly-what-happened]]
- [[2026-05-31-i-built-a-release-intelligence-agent-in-4-days-with-coral-groq-and-claude-code-heres-the-exact-route]]
