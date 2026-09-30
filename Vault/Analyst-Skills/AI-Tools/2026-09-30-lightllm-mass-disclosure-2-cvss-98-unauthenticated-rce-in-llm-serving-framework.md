---
title: LightLLM Mass Disclosure — 2 CVSS 9.8 Unauthenticated RCE in LLM Serving Framework
date: '2026-09-30'
source: https://dev.to/threataft_dev/lightllm-mass-disclosure-2-x-cvss-98-unauthenticated-rce-in-llm-serving-framework-4ob0
domain: AI-Tools
relevance: 🟡
tags:
- '#ai'
- '#best-practice'
- '#python'
- '#sql'
- '#tool'
related:
- '[[2026-04-02-how-to-stop-your-ai-agent-from-burning-400month-on-api-calls]]'
- '[[2026-04-28-why-i-run-every-code-snippet-through-two-validation-gates-before-publishing]]'
- '[[2026-07-02-beyond-tryexcept-advanced-exception-handling-patterns-every-ai-engineer-should-know]]'
- '[[2026-04-21-how-to-safely-run-ai-generated-code-with-smolvm-open-source-microvm-sandbox]]'
- '[[2026-06-02-claude-api-from-scratch-your-first-working-call-in-30-minutes-2026]]'
- '[[2026-02-26-choosing-an-agent-framework-in-2026-a-data-driven-decision-guide]]'
status: unread
---

> **TL;DR:** Two unauthenticated CVSS 9.8 RCEs in LightLLM — the LLM serving framework used with LLaMA, Mistral, and Qwen deployments. No patch confirmed. All versions through 1.2.0 are affected. The CVEs CVE CVSS Type Vector CVE-202…

## What’s new and why it matters
Two unauthenticated CVSS 9.8 RCEs in LightLLM — the LLM serving framework used with LLaMA, Mistral, and Qwen deployments. No patch confirmed. All versions through 1.2.0 are affected. The CVEs CVE CVSS Type Vector CVE-2026-103040 9.8 Pickle deserialization RCE Router profiler RPyC service CVE-2026-103041 9.8 Pickle deserialization RCE Embed cache RPyC service CVE-2026-103042 7.5 Memory exhaustion DoS NCCL control channel What happened Both RCE flaws share the same root cause: unauthenticated RPyC services passing untrusted input directly to pickle.loads() . Python's pickle module executes arbit…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Reproduce the example in a notebook; then refactor into a reusable function.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/threataft_dev/lightllm-mass-disclosure-2-x-cvss-98-unauthenticated-rce-in-llm-serving-framework-4ob0

## Related notes
- [[2026-04-02-how-to-stop-your-ai-agent-from-burning-400month-on-api-calls]]
- [[2026-04-28-why-i-run-every-code-snippet-through-two-validation-gates-before-publishing]]
- [[2026-07-02-beyond-tryexcept-advanced-exception-handling-patterns-every-ai-engineer-should-know]]
- [[2026-04-21-how-to-safely-run-ai-generated-code-with-smolvm-open-source-microvm-sandbox]]
- [[2026-06-02-claude-api-from-scratch-your-first-working-call-in-30-minutes-2026]]
- [[2026-02-26-choosing-an-agent-framework-in-2026-a-data-driven-decision-guide]]
