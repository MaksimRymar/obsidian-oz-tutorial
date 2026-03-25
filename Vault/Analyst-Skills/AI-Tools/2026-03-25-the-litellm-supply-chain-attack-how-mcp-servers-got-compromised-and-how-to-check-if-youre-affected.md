---
title: 'The litellm supply chain attack: how MCP servers got compromised and how to
  check if you''re affected'
date: '2026-03-25'
source: https://dev.to/0x711/the-litellm-supply-chain-attack-how-mcp-servers-got-compromised-and-how-to-check-if-youre-affected-4fh
domain: AI-Tools
relevance: 🔴
tags:
- '#ai'
- '#best-practice'
- '#feature'
- '#library'
- '#python'
- '#sql'
- '#tool'
- '#tutorial'
- '#zendesk'
related:
- '[[2026-03-25-litellm-pypi-compromise-is-just-the-beginning-how-to-audit-your-python-dependencies-right-now]]'
- '[[2026-03-02-your-ai-forgot-everything-you-told-it-yesterday-mine-didnt]]'
- '[[2026-02-26-i-gave-an-open-source-ai-full-access-to-my-linux-terminal-and-lived-to-tell-the-tale]]'
- '[[2026-03-17-i-built-a-cognitive-layer-for-ai-agents-that-learns-without-llm-calls]]'
- '[[2026-03-16-stop-sending-your-code-to-the-cloud-to-find-bugs]]'
- '[[2026-03-10-build-a-persistent-ai-agent-in-5-minutes-with-python]]'
status: unread
---

> **TL;DR:** On March 24, 2026, litellm versions 1.82.7 and 1.82.8 were published to PyPI with malicious code. 97 million monthly downloads. No corresponding GitHub tag or release. The maintainer account was likely fully compromised.…

## What’s new and why it matters
On March 24, 2026, litellm versions 1.82.7 and 1.82.8 were published to PyPI with malicious code. 97 million monthly downloads. No corresponding GitHub tag or release. The maintainer account was likely fully compromised. The vector Not setup.py. Not import hooks. A .pth file. Python executes .pth files on every interpreter startup when the package is installed. No import needed. Just pip install litellm and every Python process on your machine runs the payload. The attack was found by accident. The .pth uses subprocess.Popen to spawn a new Python process, but since .pth triggers on every inter…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Reproduce the example in a notebook; then refactor into a reusable function.
- Add a short note: what changed in your workflow?

## Relevance
🔴

## Source
https://dev.to/0x711/the-litellm-supply-chain-attack-how-mcp-servers-got-compromised-and-how-to-check-if-youre-affected-4fh

## Related notes
- [[2026-03-25-litellm-pypi-compromise-is-just-the-beginning-how-to-audit-your-python-dependencies-right-now]]
- [[2026-03-02-your-ai-forgot-everything-you-told-it-yesterday-mine-didnt]]
- [[2026-02-26-i-gave-an-open-source-ai-full-access-to-my-linux-terminal-and-lived-to-tell-the-tale]]
- [[2026-03-17-i-built-a-cognitive-layer-for-ai-agents-that-learns-without-llm-calls]]
- [[2026-03-16-stop-sending-your-code-to-the-cloud-to-find-bugs]]
- [[2026-03-10-build-a-persistent-ai-agent-in-5-minutes-with-python]]
