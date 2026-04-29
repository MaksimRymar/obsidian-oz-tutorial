---
title: 'AI Governance in Practice: FastAPI on EKS with Model Cards, Audit Logging,
  and Helm'
date: '2026-04-29'
source: https://dev.to/tsekatm/ai-governance-in-practice-fastapi-on-eks-with-model-cards-audit-logging-and-helm-37p5
domain: SQL
relevance: 🟡
tags:
- '#ai'
- '#feature'
- '#library'
- '#python'
- '#sql'
- '#tool'
related:
- '[[2026-04-20-try-asqav-in-30-seconds]]'
- '[[2026-02-24-your-ai-agents-have-5-months-to-comply-with-the-eu-ai-act-heres-what-youre-missing]]'
- '[[2026-03-10-pdf-ocr-extract-text-from-scanned-pdfs-with-an-api]]'
- '[[2026-04-03-cathedral-gemma-4-persistent-agent-identity-no-cloud-required]]'
- '[[2026-03-13-test-your-ai-agent-like-a-senior-engineer-4-patterns-that-work]]'
- '[[2026-03-05-i-built-a-python-library-to-make-tcp-networking-as-simple-as-fastapi]]'
status: unread
---

> **TL;DR:** AI governance is increasingly a business requirement, not an afterthought. Whether it's the EU AI Act, NIST AI RMF, or an internal risk committee, the question is the same: can you prove your model is behaving as intende…

## What’s new and why it matters
AI governance is increasingly a business requirement, not an afterthought. Whether it's the EU AI Act, NIST AI RMF, or an internal risk committee, the question is the same: can you prove your model is behaving as intended, on every request, with a documented audit trail? This post walks through an AI governance platform I built on AWS EKS: a FastAPI service that runs churn inference, records every prediction to an audit log, exposes a machine-readable model card, and packages everything into a Helm chart with horizontal pod autoscaling. Source code : github.com/tsekatm/eks-ai-governance Archit…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Write the query in a scratchpad and run EXPLAIN/QUERY PLAN to verify performance.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/tsekatm/ai-governance-in-practice-fastapi-on-eks-with-model-cards-audit-logging-and-helm-37p5

## Related notes
- [[2026-04-20-try-asqav-in-30-seconds]]
- [[2026-02-24-your-ai-agents-have-5-months-to-comply-with-the-eu-ai-act-heres-what-youre-missing]]
- [[2026-03-10-pdf-ocr-extract-text-from-scanned-pdfs-with-an-api]]
- [[2026-04-03-cathedral-gemma-4-persistent-agent-identity-no-cloud-required]]
- [[2026-03-13-test-your-ai-agent-like-a-senior-engineer-4-patterns-that-work]]
- [[2026-03-05-i-built-a-python-library-to-make-tcp-networking-as-simple-as-fastapi]]
