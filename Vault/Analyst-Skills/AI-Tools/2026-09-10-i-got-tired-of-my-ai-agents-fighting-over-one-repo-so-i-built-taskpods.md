---
title: I got tired of my AI agents fighting over one repo, so I built taskpods
date: '2026-09-10'
source: https://dev.to/yanairon/i-got-tired-of-my-ai-agents-fighting-over-one-repo-so-i-built-taskpods-nk0
domain: AI-Tools
relevance: 🟡
tags:
- '#ai'
- '#library'
- '#python'
- '#tool'
related:
- '[[2026-04-22-i-kept-forgetting-to-delete-my-venvs-so-i-built-a-gui-for-it]]'
- '[[2026-07-20-df-said-my-sandbox-had-no-disk-left-it-wasnt-wrong-it-just-wasnt-answering-the-question-i-asked]]'
- '[[2026-08-11-stop-doing-it-manually-7-ai-automation-workflows-worth-building-this-weekend]]'
- '[[2026-03-02-five-things-that-break-in-production-that-anthropics-free-curriculum-skips]]'
- '[[2026-08-02-how-i-built-relay-an-ast-based-latency-auditor-for-python-ai-agents]]'
- '[[2026-05-15-stop-passing-entire-chat-histories-to-ai-agents]]'
status: unread
---

> **TL;DR:** A few months ago I started running AI coding agents in parallel: one fixing a bug, one updating docs, one trying a refactor. The agents were fine. My repo was not. Every agent CLI works in your working tree. Two agents o…

## What’s new and why it matters
A few months ago I started running AI coding agents in parallel: one fixing a bug, one updating docs, one trying a refactor. The agents were fine. My repo was not. Every agent CLI works in your working tree. Two agents on the same repo means they edit the same files, stage each other's changes, and occasionally commit on top of one another. The "solution" I kept seeing was manual git worktrees: create one per agent, remember the branch names, remember where you put them, clean them up later. It works, but it's fiddly enough that I kept not doing it. So I wrote the thing I wanted: taskpods , a…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Reproduce the example in a notebook; then refactor into a reusable function.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/yanairon/i-got-tired-of-my-ai-agents-fighting-over-one-repo-so-i-built-taskpods-nk0

## Related notes
- [[2026-04-22-i-kept-forgetting-to-delete-my-venvs-so-i-built-a-gui-for-it]]
- [[2026-07-20-df-said-my-sandbox-had-no-disk-left-it-wasnt-wrong-it-just-wasnt-answering-the-question-i-asked]]
- [[2026-08-11-stop-doing-it-manually-7-ai-automation-workflows-worth-building-this-weekend]]
- [[2026-03-02-five-things-that-break-in-production-that-anthropics-free-curriculum-skips]]
- [[2026-08-02-how-i-built-relay-an-ast-based-latency-auditor-for-python-ai-agents]]
- [[2026-05-15-stop-passing-entire-chat-histories-to-ai-agents]]
