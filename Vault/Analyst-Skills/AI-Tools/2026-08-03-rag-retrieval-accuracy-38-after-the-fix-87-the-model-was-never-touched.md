---
title: 'RAG Retrieval Accuracy: 38%. After the Fix: 87%. The Model Was Never Touched.'
date: '2026-08-03'
source: https://dev.to/fagundesv/rag-retrieval-accuracy-38-after-the-fix-87-the-model-was-never-touched-22ci
domain: AI-Tools
relevance: 🟡
tags:
- '#ai'
- '#best-practice'
- '#python'
- '#sql'
- '#tool'
related:
- '[[2026-02-24-rag-from-scratch-build-a-system-that-answers-questions-from-your-docs]]'
- '[[2026-06-19-how-to-embed-a-sql-dashboard-into-your-saas-app-without-building-everything-from-scratch]]'
- '[[2026-07-24-ai-generated-sql-has-a-silent-failure-problem-heres-a-way-to-catch-it]]'
- '[[2026-08-01-staff-principal-data-engineer-interviews-scope-impact-cross-team-architecture-loops]]'
- '[[2026-06-16-sql-or-python-the-line-is-sharper-than-you-think-with-code]]'
- '[[2026-07-03-stop-optimizing-your-data-platform-for-dashboards]]'
status: unread
---

> **TL;DR:** That's a rebuild I shipped. The system: a RAG assistant for fraud analysts — ask it "how do we handle card testing followed by a successful auth?" and it should answer from the team's own SOPs and case history. The compl…

## What’s new and why it matters
That's a rebuild I shipped. The system: a RAG assistant for fraud analysts — ask it "how do we handle card testing followed by a successful auth?" and it should answer from the team's own SOPs and case history. The complaint: the answers were wrong, therefore the model must be dumb, therefore procurement should buy a bigger model. The model was fine. It was answering perfectly — from garbage context. Walk the forensic trail with me, because every step is checkable on your own system this week. Exhibit A: the chunking was destroying meaning before anything was embedded The ingestion split SOP d…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Reproduce the example in a notebook; then refactor into a reusable function.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/fagundesv/rag-retrieval-accuracy-38-after-the-fix-87-the-model-was-never-touched-22ci

## Related notes
- [[2026-02-24-rag-from-scratch-build-a-system-that-answers-questions-from-your-docs]]
- [[2026-06-19-how-to-embed-a-sql-dashboard-into-your-saas-app-without-building-everything-from-scratch]]
- [[2026-07-24-ai-generated-sql-has-a-silent-failure-problem-heres-a-way-to-catch-it]]
- [[2026-08-01-staff-principal-data-engineer-interviews-scope-impact-cross-team-architecture-loops]]
- [[2026-06-16-sql-or-python-the-line-is-sharper-than-you-think-with-code]]
- [[2026-07-03-stop-optimizing-your-data-platform-for-dashboards]]
