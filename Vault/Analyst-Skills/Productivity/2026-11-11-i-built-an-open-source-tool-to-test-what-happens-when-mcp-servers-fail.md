---
title: I Built an Open-Source Tool to Test What Happens When MCP Servers Fail
date: '2026-11-11'
source: https://dev.to/kuruash/i-built-an-open-source-tool-to-test-what-happens-when-mcp-servers-fail-g1g
domain: Productivity
relevance: 🔴
tags:
- '#feature'
- '#library'
- '#productivity'
- '#python'
- '#sql'
- '#tool'
related:
- '[[2026-10-06-mcp-vs-custom-rest-tooling-security-and-the-latest-mcp-architecture]]'
- '[[2026-03-08-building-autonomous-ai-agents-that-actually-do-work]]'
- '[[2026-10-29-keelyard-making-ai-coding-agents-prove-their-work]]'
- '[[2026-07-24-ai-generated-sql-has-a-silent-failure-problem-heres-a-way-to-catch-it]]'
- '[[2026-05-03-i-built-a-sast-scanner-from-scratch-heres-every-design-decision-i-made]]'
- '[[2026-07-30-i-wrote-integration-tests-for-my-mcp-failure-library-heres-the-pattern-that-caught-3-hidden-bugs]]'
status: unread
---

> **TL;DR:** I've been spending a lot of time exploring MCP servers and AI agents lately. One thing that caught my attention: we spend a lot of time testing whether tools work, but what about when they don't? What happens when an MCP…

## What’s new and why it matters
I've been spending a lot of time exploring MCP servers and AI agents lately. One thing that caught my attention: we spend a lot of time testing whether tools work, but what about when they don't? What happens when an MCP tool crashes? When it receives invalid arguments? When a protected endpoint receives an unauthorized request? And more importantly, does the server actually report those failures correctly? That's what led me to build MCP Verdict . The problem Imagine an MCP tool fails internally but returns something like this: { "isError" : false , "content" : [ { "type" : "text" , "text" :…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Add a short note: what changed in your workflow?

## Relevance
🔴

## Source
https://dev.to/kuruash/i-built-an-open-source-tool-to-test-what-happens-when-mcp-servers-fail-g1g

## Related notes
- [[2026-10-06-mcp-vs-custom-rest-tooling-security-and-the-latest-mcp-architecture]]
- [[2026-03-08-building-autonomous-ai-agents-that-actually-do-work]]
- [[2026-10-29-keelyard-making-ai-coding-agents-prove-their-work]]
- [[2026-07-24-ai-generated-sql-has-a-silent-failure-problem-heres-a-way-to-catch-it]]
- [[2026-05-03-i-built-a-sast-scanner-from-scratch-heres-every-design-decision-i-made]]
- [[2026-07-30-i-wrote-integration-tests-for-my-mcp-failure-library-heres-the-pattern-that-caught-3-hidden-bugs]]
