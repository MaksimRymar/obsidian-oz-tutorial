---
title: I Built an AI Agent Security Scanner. Semgrep and CodeQL Detect 0 Percent of
  These Attacks
date: '2026-07-05'
source: https://dev.to/dockfixlabs/i-built-an-ai-agent-security-scanner-semgrep-and-codeql-detect-0-percent-of-these-attacks-nj4
domain: AI-Tools
relevance: 🔴
tags:
- '#ai'
- '#tool'
related:
- '[[2026-04-30-7-best-python-frameworks-for-building-ai-agents-in-2026]]'
- '[[2026-03-19-five-things-that-go-wrong-when-ai-agents-hold-api-keys]]'
- '[[2026-02-24-your-ai-agents-have-5-months-to-comply-with-the-eu-ai-act-heres-what-youre-missing]]'
- '[[2026-03-31-i-tested-9-ai-agent-frameworks-for-basic-security-none-of-them-passed]]'
- '[[2026-05-01-building-an-open-source-snyk-alternative-secret-detection-sast-and-sbom-in-one-tool]]'
- '[[2026-06-07-what-a-policy-gate-catches-in-ai-generated-code-and-what-slips-through]]'
status: unread
---

> **TL;DR:** I have spent the last 6 hours building what I believe is the most comprehensive AI agent security scanner in existence. The Numbers Metric Value Detection rules 18 (10 OWASP ASI + 5 novel) Benchmark 50 samples (100% dete…

## What’s new and why it matters
I have spent the last 6 hours building what I believe is the most comprehensive AI agent security scanner in existence. The Numbers Metric Value Detection rules 18 (10 OWASP ASI + 5 novel) Benchmark 50 samples (100% detection, 0 FP) Tests 96 passing Frameworks scanned LlamaIndex 252C, AutoGen 80C Semgrep 0% on same benchmark CodeQL 0% on same benchmark 5 Novel Vectors Memory Poisoning - corrupting vector stores Tool Output Trust - blind trust in tool results Action Chain Amplification - single trigger mass destruction Multi-Agent Collusion - agents conspiring through shared state Prompt Templa…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Reproduce the example in a notebook; then refactor into a reusable function.
- Add a short note: what changed in your workflow?

## Relevance
🔴

## Source
https://dev.to/dockfixlabs/i-built-an-ai-agent-security-scanner-semgrep-and-codeql-detect-0-percent-of-these-attacks-nj4

## Related notes
- [[2026-04-30-7-best-python-frameworks-for-building-ai-agents-in-2026]]
- [[2026-03-19-five-things-that-go-wrong-when-ai-agents-hold-api-keys]]
- [[2026-02-24-your-ai-agents-have-5-months-to-comply-with-the-eu-ai-act-heres-what-youre-missing]]
- [[2026-03-31-i-tested-9-ai-agent-frameworks-for-basic-security-none-of-them-passed]]
- [[2026-05-01-building-an-open-source-snyk-alternative-secret-detection-sast-and-sbom-in-one-tool]]
- [[2026-06-07-what-a-policy-gate-catches-in-ai-generated-code-and-what-slips-through]]
