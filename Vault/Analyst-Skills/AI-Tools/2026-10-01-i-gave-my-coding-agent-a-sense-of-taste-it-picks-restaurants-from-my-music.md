---
title: I gave my coding agent a sense of taste. It picks restaurants from my music.
date: '2026-10-01'
source: https://dev.to/haoli/i-gave-my-coding-agent-a-sense-of-taste-it-picks-restaurants-from-my-music-4o1
domain: AI-Tools
relevance: 🔴
tags:
- '#ai'
- '#python'
- '#tool'
related:
- '[[2026-03-23-build-your-first-ai-agent-with-python-and-langchain-in-2026]]'
- '[[2026-09-28-how-i-connected-an-ai-agent-to-github-with-nango-and-mcp-without-touching-a-single-oauth-token-published-false-tags-ai-m]]'
- '[[2026-09-21-a-1145-star-cli-promised-nothing-leaves-your-machine-it-executes-a-hidden-payload-at-import-time]]'
- '[[2026-06-30-how-i-built-an-mcp-server-that-combines-hunterio-and-apollo-for-b2b-lead-enrichment]]'
- '[[2026-08-31-i-left-an-ai-agent-running-unattended-for-a-day-here-is-everything-that-broke]]'
- '[[2026-04-13-how-i-learned-sql-by-creating-a-simple-school-database]]'
status: unread
---

> **TL;DR:** My coding agent can refactor a thousand lines without breaking a sweat, but ask it "where should I take a date Friday night" and it's useless. It knows my code. It knows nothing about my taste. Qloo's Taste API sits on 2…

## What’s new and why it matters
My coding agent can refactor a thousand lines without breaking a sweat, but ask it "where should I take a date Friday night" and it's useless. It knows my code. It knows nothing about my taste. Qloo's Taste API sits on 250M+ cultural entities — music, movies, restaurants, brands, destinations — with a graph of how tastes connect. So I built qloo-taste-mcp : an MCP server that hands all of that to any agent as four tools. Tool What it does qloo_search Search the taste graph ("Taylor Swift", "ramen") → entity IDs qloo_recommend Recommendations seeded by entity IDs — movies, restaurants, brands q…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Reproduce the example in a notebook; then refactor into a reusable function.
- Add a short note: what changed in your workflow?

## Relevance
🔴

## Source
https://dev.to/haoli/i-gave-my-coding-agent-a-sense-of-taste-it-picks-restaurants-from-my-music-4o1

## Related notes
- [[2026-03-23-build-your-first-ai-agent-with-python-and-langchain-in-2026]]
- [[2026-09-28-how-i-connected-an-ai-agent-to-github-with-nango-and-mcp-without-touching-a-single-oauth-token-published-false-tags-ai-m]]
- [[2026-09-21-a-1145-star-cli-promised-nothing-leaves-your-machine-it-executes-a-hidden-payload-at-import-time]]
- [[2026-06-30-how-i-built-an-mcp-server-that-combines-hunterio-and-apollo-for-b2b-lead-enrichment]]
- [[2026-08-31-i-left-an-ai-agent-running-unattended-for-a-day-here-is-everything-that-broke]]
- [[2026-04-13-how-i-learned-sql-by-creating-a-simple-school-database]]
