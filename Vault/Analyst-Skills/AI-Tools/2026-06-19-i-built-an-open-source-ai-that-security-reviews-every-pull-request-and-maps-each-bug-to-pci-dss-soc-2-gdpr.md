---
title: I built an open-source AI that security-reviews every pull request — and maps
  each bug to PCI-DSS, SOC 2 & GDPR
date: '2026-06-19'
source: https://dev.to/noobbatman/i-built-an-open-source-ai-that-security-reviews-every-pull-request-and-maps-each-bug-to-pci-dss-49ob
domain: AI-Tools
relevance: 🔴
tags:
- '#ai'
- '#best-practice'
- '#sql'
- '#tool'
- '#tutorial'
- '#zendesk'
related:
- '[[2026-06-07-what-a-policy-gate-catches-in-ai-generated-code-and-what-slips-through]]'
- '[[2026-03-10-pdf-ocr-extract-text-from-scanned-pdfs-with-an-api]]'
- '[[2026-03-16-stop-sending-your-code-to-the-cloud-to-find-bugs]]'
- '[[2026-03-09-5-prompt-engineering-patterns-that-actually-work-in-production]]'
- '[[2026-03-26-what-is-mutation-testing-a-practical-guide-for-qa-engineers]]'
- '[[2026-04-02-how-i-stopped-paying-openai-to-run-my-test-suite]]'
status: unread
---

> **TL;DR:** Code review is where most security bugs are supposed to get caught. In practice it's slow, inconsistent, and depends entirely on who happens to be looking that day. So I built GuardianCI — a CI check that reviews every p…

## What’s new and why it matters
Code review is where most security bugs are supposed to get caught. In practice it's slow, inconsistent, and depends entirely on who happens to be looking that day. So I built GuardianCI — a CI check that reviews every pull request for security issues automatically, comments inline at the exact line, and blocks the merge on anything CRITICAL. It's open source (MIT), works on GitHub and GitLab , and runs for free on Google Gemini's tier — or your own OpenAI, Anthropic, Groq, or local Ollama endpoint. Does it actually work? I planted vulnerabilities in a real project and opened a PR. Every one g…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Reproduce the example in a notebook; then refactor into a reusable function.
- Add a short note: what changed in your workflow?

## Relevance
🔴

## Source
https://dev.to/noobbatman/i-built-an-open-source-ai-that-security-reviews-every-pull-request-and-maps-each-bug-to-pci-dss-49ob

## Related notes
- [[2026-06-07-what-a-policy-gate-catches-in-ai-generated-code-and-what-slips-through]]
- [[2026-03-10-pdf-ocr-extract-text-from-scanned-pdfs-with-an-api]]
- [[2026-03-16-stop-sending-your-code-to-the-cloud-to-find-bugs]]
- [[2026-03-09-5-prompt-engineering-patterns-that-actually-work-in-production]]
- [[2026-03-26-what-is-mutation-testing-a-practical-guide-for-qa-engineers]]
- [[2026-04-02-how-i-stopped-paying-openai-to-run-my-test-suite]]
