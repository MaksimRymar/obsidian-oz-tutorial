---
title: Build an MCP Server in Python in 15 Minutes
date: '2026-05-05'
source: https://dev.to/thedailyagent/build-an-mcp-server-in-python-in-15-minutes-43c6
domain: AI-Tools
relevance: 🟡
tags:
- '#ai'
- '#library'
- '#python'
- '#sql'
- '#support-analytics'
- '#tool'
related:
- '[[2026-02-25-i-built-a-free-alternative-to-langsmith-one-decorator-local-sqlite-zero-infrastructure]]'
- '[[2026-03-26-sqlite-is-enough-for-your-side-project-full-text-search-json-and-wal-mode-included]]'
- '[[2026-03-02-python-automation-12-scripts-that-save-hours-every-week]]'
- '[[2026-03-23-build-your-first-ai-agent-with-python-and-langchain-in-2026]]'
- '[[2026-03-24-sqlite-as-a-graph-database-recursive-ctes-semantic-search-and-why-we-ditched-neo4j]]'
- '[[2026-03-28-prefect-has-a-free-api-the-python-workflow-orchestration-platform-that-replaces-airflow-without-the-configuration-pain]]'
status: unread
---

> **TL;DR:** Drop this into a file and run it: from mcp.server.fastmcp import FastMCP import httpx mcp = FastMCP ( " mini-tools " ) @mcp.tool () def read_file ( path : str ) -> str : """ Read the contents of a file. """ with open ( p…

## What’s new and why it matters
Drop this into a file and run it: from mcp.server.fastmcp import FastMCP import httpx mcp = FastMCP ( " mini-tools " ) @mcp.tool () def read_file ( path : str ) -> str : """ Read the contents of a file. """ with open ( path ) as f : return f . read () @mcp.tool () async def fetch_url ( url : str ) -> str : """ Fetch a URL and return the response text. """ async with httpx . AsyncClient () as client : resp = await client . get ( url ) return resp . text if __name__ == " __main__ " : mcp . run () Save as server.py , install the one dependency, and start it: pip install mcp httpx python server.py…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Reproduce the example in a notebook; then refactor into a reusable function.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/thedailyagent/build-an-mcp-server-in-python-in-15-minutes-43c6

## Related notes
- [[2026-02-25-i-built-a-free-alternative-to-langsmith-one-decorator-local-sqlite-zero-infrastructure]]
- [[2026-03-26-sqlite-is-enough-for-your-side-project-full-text-search-json-and-wal-mode-included]]
- [[2026-03-02-python-automation-12-scripts-that-save-hours-every-week]]
- [[2026-03-23-build-your-first-ai-agent-with-python-and-langchain-in-2026]]
- [[2026-03-24-sqlite-as-a-graph-database-recursive-ctes-semantic-search-and-why-we-ditched-neo4j]]
- [[2026-03-28-prefect-has-a-free-api-the-python-workflow-orchestration-platform-that-replaces-airflow-without-the-configuration-pain]]
