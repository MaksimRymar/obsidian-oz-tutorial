---
title: The Unicode Layer Your Validator Can't See
date: '2026-05-28'
source: https://dev.to/jeremy_longshore/the-unicode-layer-your-validator-cant-see-35m1
domain: AI-Tools
relevance: 🟡
tags:
- '#ai'
- '#best-practice'
- '#library'
- '#python'
- '#sql'
- '#tool'
related:
- '[[2026-04-22-your-pytest-retries-are-lying-to-you-the-hidden-cost-of---reruns-and-the-plugin-i-wrote-so-i-could-actually-see-what-my-]]'
- '[[2026-04-02-how-i-stopped-paying-openai-to-run-my-test-suite]]'
- '[[2026-03-13-you-dont-need-a-framework-building-reliable-ai-agents-from-first-principles]]'
- '[[2026-03-30-database-indexing-explained-whats-actually-happening-under-the-hood]]'
- '[[2026-03-09-sql-window-functions-dont-have-to-be-scary]]'
- '[[2026-03-25-sql-notebooks-in-vs-code-like-jupyter-but-for-databases]]'
status: unread
---

> **TL;DR:** A schema validator reads parsed structure. It never sees the bytes. That gap is where a whole class of supply-chain attack lives. The claude-code-plugins marketplace already ran a schema validator over every skill, agent…

## What’s new and why it matters
A schema validator reads parsed structure. It never sees the bytes. That gap is where a whole class of supply-chain attack lives. The claude-code-plugins marketplace already ran a schema validator over every skill, agent, command, and catalog file — confirming required fields, enum values, shapes. All of it operating on the parsed document. None of it looking at the raw codepoints underneath. An attacker can hide an instruction in characters that are invisible to a human reviewer and invisible to a structural validator, yet fully meaningful to an LLM that parses the file as text — or to a shel…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Reproduce the example in a notebook; then refactor into a reusable function.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/jeremy_longshore/the-unicode-layer-your-validator-cant-see-35m1

## Related notes
- [[2026-04-22-your-pytest-retries-are-lying-to-you-the-hidden-cost-of---reruns-and-the-plugin-i-wrote-so-i-could-actually-see-what-my-]]
- [[2026-04-02-how-i-stopped-paying-openai-to-run-my-test-suite]]
- [[2026-03-13-you-dont-need-a-framework-building-reliable-ai-agents-from-first-principles]]
- [[2026-03-30-database-indexing-explained-whats-actually-happening-under-the-hood]]
- [[2026-03-09-sql-window-functions-dont-have-to-be-scary]]
- [[2026-03-25-sql-notebooks-in-vs-code-like-jupyter-but-for-databases]]
