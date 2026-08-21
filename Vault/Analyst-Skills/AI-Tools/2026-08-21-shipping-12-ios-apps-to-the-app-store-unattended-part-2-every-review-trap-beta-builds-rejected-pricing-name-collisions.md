---
title: Shipping 12 iOS Apps to the App Store Unattended, Part 2 — Every Review Trap
  (Beta Builds Rejected, Pricing, Name Collisions)
date: '2026-08-21'
source: https://dev.to/bokuwalily/shipping-12-ios-apps-to-the-app-store-unattended-part-2-every-review-trap-beta-builds-rejected-2jim
domain: AI-Tools
relevance: 🟡
tags:
- '#ai'
- '#best-practice'
- '#feature'
- '#library'
- '#python'
- '#sql'
- '#support-analytics'
- '#tool'
- '#zendesk'
related:
- '[[2026-08-07-my-mcp-tools-docstring-promised-limit-1-100-passing--1-returned-almost-everything-not-nothing]]'
- '[[2026-08-01-my-mcp-servers-two-api-helpers-had-zero-except-blocks-every-bad-call-crashed-with-a-raw-urllib-traceback]]'
- '[[2026-08-11-stop-doing-it-manually-7-ai-automation-workflows-worth-building-this-weekend]]'
- '[[2026-04-03-i-got-tired-of-watching-my-terminal-so-i-built-guga]]'
- '[[2026-08-13-3-testing-habits-that-caught-bugs-before-my-users-did]]'
- '[[2026-08-02-how-i-built-relay-an-ast-based-latency-auditor-for-python-ai-agents]]'
status: unread
---

> **TL;DR:** I got laid off with ¥0 in the bank. Six months later, rebuilt around Claude Code running as an autonomous environment, I'm clearing ¥1.2M a month — and one of the load-bearing pieces is a pipeline that submits apps to th…

## What’s new and why it matters
I got laid off with ¥0 in the bank. Six months later, rebuilt around Claude Code running as an autonomous environment, I'm clearing ¥1.2M a month — and one of the load-bearing pieces is a pipeline that submits apps to the App Store without me touching it. Part 1 covered how to wire up JWT authentication and the skeleton of asc.py . This time I'm collecting the three "review rejection traps" that only showed up once the thing went into real production use: how the true cause of ITMS-90111 turned out to be BuildMachineOSBuild , the correct request shape for appPriceSchedules , and how to dodge t…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Reproduce the example in a notebook; then refactor into a reusable function.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/bokuwalily/shipping-12-ios-apps-to-the-app-store-unattended-part-2-every-review-trap-beta-builds-rejected-2jim

## Related notes
- [[2026-08-07-my-mcp-tools-docstring-promised-limit-1-100-passing--1-returned-almost-everything-not-nothing]]
- [[2026-08-01-my-mcp-servers-two-api-helpers-had-zero-except-blocks-every-bad-call-crashed-with-a-raw-urllib-traceback]]
- [[2026-08-11-stop-doing-it-manually-7-ai-automation-workflows-worth-building-this-weekend]]
- [[2026-04-03-i-got-tired-of-watching-my-terminal-so-i-built-guga]]
- [[2026-08-13-3-testing-habits-that-caught-bugs-before-my-users-did]]
- [[2026-08-02-how-i-built-relay-an-ast-based-latency-auditor-for-python-ai-agents]]
