---
title: 'CodeClone b5: structural review that finally knows what your tests cover'
date: '2026-04-16'
source: https://dev.to/orenlab/codeclone-b5-structural-review-that-finally-knows-what-your-tests-cover-4l80
domain: AI-Tools
relevance: 🔴
tags:
- '#ai'
- '#feature'
- '#library'
- '#python'
- '#sql'
- '#tool'
related:
- '[[2026-02-24-stop-using-any-the-wrong-way-in-rails]]'
- '[[2026-04-01-i-turned-my-python-code-quality-tool-into-a-budget-aware-mcp-server-for-ai-agents]]'
- '[[2026-03-02-five-things-that-break-in-production-that-anthropics-free-curriculum-skips]]'
- '[[2026-03-15-why-i-as-someone-who-likes-mysql-now-want-to-recommend-postgresql]]'
- '[[2026-04-03-i-got-tired-of-watching-my-terminal-so-i-built-guga]]'
- '[[2026-04-02-how-to-stop-your-ai-agent-from-burning-400month-on-api-calls]]'
status: unread
---

> **TL;DR:** In earlier posts, I wrote about why I built CodeClone , why I exposed it through MCP for AI agents , and how b4 turned it into a real review surface for VS Code, Claude Desktop, and Codex. b5 is the release where structu…

## What’s new and why it matters
In earlier posts, I wrote about why I built CodeClone , why I exposed it through MCP for AI agents , and how b4 turned it into a real review surface for VS Code, Claude Desktop, and Codex. b5 is the release where structural review stops being a parallel universe to your test suite. Until now, CodeClone could tell you that a function is long, complex, duplicated, or coupled to everything — but it had no idea whether that function was covered by a single unit test. That mattered more than I wanted to admit. A complex function with a 0.98 coverage ratio is not the same risk as the identical funct…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Reproduce the example in a notebook; then refactor into a reusable function.
- Add a short note: what changed in your workflow?

## Relevance
🔴

## Source
https://dev.to/orenlab/codeclone-b5-structural-review-that-finally-knows-what-your-tests-cover-4l80

## Related notes
- [[2026-02-24-stop-using-any-the-wrong-way-in-rails]]
- [[2026-04-01-i-turned-my-python-code-quality-tool-into-a-budget-aware-mcp-server-for-ai-agents]]
- [[2026-03-02-five-things-that-break-in-production-that-anthropics-free-curriculum-skips]]
- [[2026-03-15-why-i-as-someone-who-likes-mysql-now-want-to-recommend-postgresql]]
- [[2026-04-03-i-got-tired-of-watching-my-terminal-so-i-built-guga]]
- [[2026-04-02-how-to-stop-your-ai-agent-from-burning-400month-on-api-calls]]
