---
title: 'psyctl: Steer LLM Personality Without Fine-Tuning'
date: '2026-03-15'
source: https://dev.to/ho4040/psyctl-steer-llm-personality-without-fine-tuning-4i0a
domain: AI-Tools
relevance: 🟡
tags:
- '#ai'
- '#tool'
related:
- '[[2026-03-10-building-an-ai-tool-that-generates-sql-queries-from-natural-language]]'
- '[[2026-02-22-building-a-fully-local-offline-trading-research-memory-agent-with-zvec]]'
- '[[2026-03-01-stop-manually-entering-medical-data-how-to-automate-pdf-lab-reports-with-layoutparser-ocr]]'
- '[[2026-02-26-5-free-ai-apis-every-developer-should-know-in-2025]]'
- '[[2026-02-27-how-to-build-a-competitive-intelligence-tool-that-reveals-any-companys-tech-stack]]'
- '[[2026-03-08-building-autonomous-ai-agents-that-actually-do-work]]'
status: unread
---

> **TL;DR:** What if you could make an LLM more extroverted — without any training? That's the idea behind psyctl , a CLI tool I'm building at Modulabs Persona Lab . It lets you extract personality vectors from a model's internal act…

## What’s new and why it matters
What if you could make an LLM more extroverted — without any training? That's the idea behind psyctl , a CLI tool I'm building at Modulabs Persona Lab . It lets you extract personality vectors from a model's internal activations and inject them during inference to shift behavior. No fine-tuning, no LoRA, no RLHF — just vector addition. How It Works The technique is called Contrastive Activation Addition (CAA) . Here's the pipeline: Generate a contrastive dataset — pairs of responses that differ only in personality (e.g., extroverted vs. neutral) Extract a steering vector — compute the mean act…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Reproduce the example in a notebook; then refactor into a reusable function.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/ho4040/psyctl-steer-llm-personality-without-fine-tuning-4i0a

## Related notes
- [[2026-03-10-building-an-ai-tool-that-generates-sql-queries-from-natural-language]]
- [[2026-02-22-building-a-fully-local-offline-trading-research-memory-agent-with-zvec]]
- [[2026-03-01-stop-manually-entering-medical-data-how-to-automate-pdf-lab-reports-with-layoutparser-ocr]]
- [[2026-02-26-5-free-ai-apis-every-developer-should-know-in-2025]]
- [[2026-02-27-how-to-build-a-competitive-intelligence-tool-that-reveals-any-companys-tech-stack]]
- [[2026-03-08-building-autonomous-ai-agents-that-actually-do-work]]
