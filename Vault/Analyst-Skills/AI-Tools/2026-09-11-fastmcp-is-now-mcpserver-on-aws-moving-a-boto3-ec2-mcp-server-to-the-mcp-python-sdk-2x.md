---
title: 'FastMCP Is Now MCPServer on AWS: Moving a boto3 EC2 MCP Server to the MCP
  Python SDK 2.x'
date: '2026-09-11'
source: https://dev.to/aws-builders/fastmcp-is-now-mcpserver-on-aws-moving-a-boto3-ec2-mcp-server-to-the-mcp-python-sdk-2x-42gk
domain: AI-Tools
relevance: 🔴
tags:
- '#ai'
- '#feature'
- '#library'
- '#python'
- '#tool'
- '#tutorial'
related:
- '[[2026-08-06-building-an-mcp-tool-call-test-rig-with-the-python-sdk-in-2026]]'
- '[[2026-09-09-six-tables-out-of-260]]'
- '[[2026-07-15-build-your-first-mcp-server-in-python-give-claude-your-own-notes]]'
- '[[2026-08-10-i-installed-300-mcp-servers-from-pypi-about-43-dont-start]]'
- '[[2026-08-21-how-to-find-duplicate-rows-in-sql-and-decide-what-counts-as-one]]'
- '[[2026-06-02-claude-api-from-scratch-your-first-working-call-in-30-minutes-2026]]'
status: unread
---

> **TL;DR:** This article provides a step by step migration guide for an AWS MCP server from the MCP Python SDK 1.x ( FastMCP ) to 2.x ( MCPServer ). The server manages Gemma 4 E2B on an Amazon EC2 G5g instance, a Graviton2 host with…

## What’s new and why it matters
This article provides a step by step migration guide for an AWS MCP server from the MCP Python SDK 1.x ( FastMCP ) to 2.x ( MCPServer ). The server manages Gemma 4 E2B on an Amazon EC2 G5g instance, a Graviton2 host with an NVIDIA T4G GPU, and a suite of Python MCP tools built on boto3 simplifies management of the vLLM hosted deployment. https://github.com/xbill9/gemma4-dev/tree/main/gpu-vllm-g5g-2b What Broke? The rig's requirements.txt listed mcp with no version bound. Once the machine's Python moved to mcp 2.2.0, the server stopped importing: python3 -c "import server" ModuleNotFoundError:…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Reproduce the example in a notebook; then refactor into a reusable function.
- Add a short note: what changed in your workflow?

## Relevance
🔴

## Source
https://dev.to/aws-builders/fastmcp-is-now-mcpserver-on-aws-moving-a-boto3-ec2-mcp-server-to-the-mcp-python-sdk-2x-42gk

## Related notes
- [[2026-08-06-building-an-mcp-tool-call-test-rig-with-the-python-sdk-in-2026]]
- [[2026-09-09-six-tables-out-of-260]]
- [[2026-07-15-build-your-first-mcp-server-in-python-give-claude-your-own-notes]]
- [[2026-08-10-i-installed-300-mcp-servers-from-pypi-about-43-dont-start]]
- [[2026-08-21-how-to-find-duplicate-rows-in-sql-and-decide-what-counts-as-one]]
- [[2026-06-02-claude-api-from-scratch-your-first-working-call-in-30-minutes-2026]]
