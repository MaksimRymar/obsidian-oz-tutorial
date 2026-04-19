---
title: Your WAF thinks in ATT&CK. Your LLM app needs ATLAS. Here's the bridge.
date: '2026-04-19'
source: https://dev.to/uzy1bit/your-waf-thinks-in-attck-your-llm-app-needs-atlas-heres-the-bridge-39ld
domain: AI-Tools
relevance: 🔴
tags:
- '#ai'
- '#best-practice'
- '#feature'
- '#presentations'
- '#python'
- '#sql'
- '#tool'
- '#tutorial'
related:
- '[[2026-03-26-i-built-an-ai-that-reads-your-pets-mood-heres-the-python-behind-it]]'
- '[[2026-03-21-write-better-ai-agent-tools-5-python-patterns-llms-actually-understand]]'
- '[[2026-04-19-ai-agents-explained-simply-the-biggest-tech-shift-of-2026]]'
- '[[2026-03-13-you-dont-need-a-framework-building-reliable-ai-agents-from-first-principles]]'
- '[[2026-02-22-stop-wiring-dependencies-by-hand---meet-injectq-python-di-done-right]]'
- '[[2026-04-02-how-to-stop-your-ai-agent-from-burning-400month-on-api-calls]]'
status: unread
---

> **TL;DR:** If you're shipping a web app in 2026, your security story has shape. You know what SQL injection is. You know what XSS is. You've got a WAF in front of the thing, and that WAF thinks in MITRE ATT&CK — the industry-standa…

## What’s new and why it matters
If you're shipping a web app in 2026, your security story has shape. You know what SQL injection is. You know what XSS is. You've got a WAF in front of the thing, and that WAF thinks in MITRE ATT&CK — the industry-standard taxonomy for adversary tactics and techniques. Everyone from your SOC to your Grafana dashboards to your Jira tickets speaks that language. Now your company wants to ship an LLM feature. A chatbot, an internal assistant, a RAG pipeline, whatever. And suddenly all of that taxonomy goes sideways. Prompt injection isn't in ATT&CK. Jailbreaks aren't in ATT&CK. Data leakage via a…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Reproduce the example in a notebook; then refactor into a reusable function.
- Add a short note: what changed in your workflow?

## Relevance
🔴

## Source
https://dev.to/uzy1bit/your-waf-thinks-in-attck-your-llm-app-needs-atlas-heres-the-bridge-39ld

## Related notes
- [[2026-03-26-i-built-an-ai-that-reads-your-pets-mood-heres-the-python-behind-it]]
- [[2026-03-21-write-better-ai-agent-tools-5-python-patterns-llms-actually-understand]]
- [[2026-04-19-ai-agents-explained-simply-the-biggest-tech-shift-of-2026]]
- [[2026-03-13-you-dont-need-a-framework-building-reliable-ai-agents-from-first-principles]]
- [[2026-02-22-stop-wiring-dependencies-by-hand---meet-injectq-python-di-done-right]]
- [[2026-04-02-how-to-stop-your-ai-agent-from-burning-400month-on-api-calls]]
