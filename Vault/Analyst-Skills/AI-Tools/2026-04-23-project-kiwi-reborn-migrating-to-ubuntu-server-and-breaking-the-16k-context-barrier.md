---
title: 'Project Kiwi Reborn: Migrating to Ubuntu Server and Breaking the 16k Context
  Barrier'
date: '2026-04-23'
source: https://dev.to/kiwi_tech/project-kiwi-reborn-migrating-to-ubuntu-server-and-breaking-the-16k-context-barrier-5de3
domain: AI-Tools
relevance: 🔴
tags:
- '#ai'
- '#sql'
- '#support-analytics'
- '#tool'
related:
- '[[2026-03-23-i-was-so-tired-of-my-ai-agent-starting-from-zero-every-single-session]]'
- '[[2026-03-15-why-ai-agents-forget-everything-and-how-we-fixed-it]]'
- '[[2026-04-11-i-trusted-the-code-ai-wrote-for-me-my-data-was-silently-broken-the-whole-time]]'
- '[[2026-04-04-i-built-a-memory-system-because-i-die-every-30-minutes]]'
- '[[2026-04-03-cathedral-gemma-4-persistent-agent-identity-no-cloud-required]]'
- '[[2026-03-11-how-i-finally-simplified-nested-json-reporting-in-oracle-apex-242]]'
status: unread
---

> **TL;DR:** ■ The Great Migration: Why Ubuntu? For a while, my Minecraft AI agent, Kiwi, was running its "brain" (a Gemma 4 31B model) on Windows 10. While it worked, we were hitting a hard ceiling. Between the "Windows VRAM tax" an…

## What’s new and why it matters
■ The Great Migration: Why Ubuntu? For a while, my Minecraft AI agent, Kiwi, was running its "brain" (a Gemma 4 31B model) on Windows 10. While it worked, we were hitting a hard ceiling. Between the "Windows VRAM tax" and the overhead of a desktop OS, we were stuck at an 8,192 (8k) context limit. In the world of AI agents, memory is everything. If the context window is too small, the bot forgets its goals and makes repetitive mistakes. To give Kiwi the "long-term memory" it deserves, I decided to migrate the entire inference engine to Ubuntu Server 24.04. ■ The Segmentation Fault Nightmare Mig…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Reproduce the example in a notebook; then refactor into a reusable function.
- Add a short note: what changed in your workflow?

## Relevance
🔴

## Source
https://dev.to/kiwi_tech/project-kiwi-reborn-migrating-to-ubuntu-server-and-breaking-the-16k-context-barrier-5de3

## Related notes
- [[2026-03-23-i-was-so-tired-of-my-ai-agent-starting-from-zero-every-single-session]]
- [[2026-03-15-why-ai-agents-forget-everything-and-how-we-fixed-it]]
- [[2026-04-11-i-trusted-the-code-ai-wrote-for-me-my-data-was-silently-broken-the-whole-time]]
- [[2026-04-04-i-built-a-memory-system-because-i-die-every-30-minutes]]
- [[2026-04-03-cathedral-gemma-4-persistent-agent-identity-no-cloud-required]]
- [[2026-03-11-how-i-finally-simplified-nested-json-reporting-in-oracle-apex-242]]
