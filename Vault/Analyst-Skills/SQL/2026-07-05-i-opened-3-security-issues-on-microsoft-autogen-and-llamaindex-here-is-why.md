---
title: I Opened 3 Security Issues on Microsoft AutoGen and LlamaIndex. Here Is Why
date: '2026-07-05'
source: https://dev.to/dockfixlabs/i-opened-3-security-issues-on-microsoft-autogen-and-llamaindex-here-is-why-48dg
domain: SQL
relevance: 🔴
tags:
- '#ai'
- '#best-practice'
- '#sql'
- '#tool'
- '#zendesk'
related:
- '[[2026-07-05-i-built-an-ai-agent-security-scanner-semgrep-and-codeql-detect-0-percent-of-these-attacks]]'
- '[[2026-07-05-agentguard-vs-semgrep-vs-codeql-100-percent-vs-0-percent-on-ai-agent-security]]'
- '[[2026-06-18-two-ai-agents-just-had-a-child-and-the-birth-certificate-is-cryptographically-verifiable]]'
- '[[2026-07-02-the-ultimate-collection-of-18k-ai-agent-skills-across-14-frameworks]]'
- '[[2026-04-19-ai-agents-explained-simply-the-biggest-tech-shift-of-2026]]'
- '[[2026-02-24-your-ai-agents-have-5-months-to-comply-with-the-eu-ai-act-heres-what-youre-missing]]'
status: unread
---

> **TL;DR:** I just opened 3 security issues on two of the most popular AI agent frameworks on GitHub (combined 110K+ stars). The Issues microsoft/autogen#7917 : Docker code executor mounts host filesystem into sandboxed containers w…

## What’s new and why it matters
I just opened 3 security issues on two of the most popular AI agent frameworks on GitHub (combined 110K+ stars). The Issues microsoft/autogen#7917 : Docker code executor mounts host filesystem into sandboxed containers without trust boundary validation — container escape vector. microsoft/autogen#7918 : Agent self-modification patterns in Canvas memory module — agents can alter their own operating constraints during execution. run-llama/llama_index#22245 : 441 instances of unbounded recursive agent execution across 2,951 files — systemic resource exhaustion risk. All found with AgentGuard v0.6…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Write the query in a scratchpad and run EXPLAIN/QUERY PLAN to verify performance.
- Add a short note: what changed in your workflow?

## Relevance
🔴

## Source
https://dev.to/dockfixlabs/i-opened-3-security-issues-on-microsoft-autogen-and-llamaindex-here-is-why-48dg

## Related notes
- [[2026-07-05-i-built-an-ai-agent-security-scanner-semgrep-and-codeql-detect-0-percent-of-these-attacks]]
- [[2026-07-05-agentguard-vs-semgrep-vs-codeql-100-percent-vs-0-percent-on-ai-agent-security]]
- [[2026-06-18-two-ai-agents-just-had-a-child-and-the-birth-certificate-is-cryptographically-verifiable]]
- [[2026-07-02-the-ultimate-collection-of-18k-ai-agent-skills-across-14-frameworks]]
- [[2026-04-19-ai-agents-explained-simply-the-biggest-tech-shift-of-2026]]
- [[2026-02-24-your-ai-agents-have-5-months-to-comply-with-the-eu-ai-act-heres-what-youre-missing]]
