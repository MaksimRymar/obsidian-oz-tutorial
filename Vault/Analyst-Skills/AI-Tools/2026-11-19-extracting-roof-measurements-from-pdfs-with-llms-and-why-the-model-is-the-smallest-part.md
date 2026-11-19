---
title: Extracting roof measurements from PDFs with LLMs, and why the model is the
  smallest part
date: '2026-11-19'
source: https://dev.to/ahmad_dogar_7d098f5e48f72/extracting-roof-measurements-from-pdfs-with-llms-and-why-the-model-is-the-smallest-part-41cb
domain: AI-Tools
relevance: 🟡
tags:
- '#ai'
- '#python'
- '#sql'
- '#tool'
related:
- '[[2026-08-21-how-to-find-duplicate-rows-in-sql-and-decide-what-counts-as-one]]'
- '[[2026-10-15-free-draft-volume-or-paid-first-passes-a-debate-for-agent-sql-budgets]]'
- '[[2026-08-11-sql-joins-how-to-join-two-tables-without-losing-or-doubling-rows]]'
- '[[2026-08-31-running-total-in-sql-the-window-frame-that-decides-the-answer]]'
- '[[2026-11-18-two-hallucination-tests-you-can-run-before-you-pay-for-a-judge-model]]'
- '[[2026-11-12-ai-brand-tracking-a-practical-check-you-can-run-today-by-yourself]]'
status: unread
---

> **TL;DR:** A roofing distributor cannot price a tile roof without numbers: total area, the area at each pitch, and the lengths of every ridge, hip, rake, eave and valley. Those numbers already exist. They sit inside PDF reports fro…

## What’s new and why it matters
A roofing distributor cannot price a tile roof without numbers: total area, the area at each pitch, and the lengths of every ridge, hip, rake, eave and valley. Those numbers already exist. They sit inside PDF reports from EagleView, RoofScope, Hover, Roofr and a few others, each with its own layout, units and quirks. Before we built DocScan for the Brava Roof Tile Pro Portal, someone re-typed them into a quote form by hand. It sounds like a weekend job: send the PDF to a model, ask for JSON, fill in the form. It is not. Below is why that version breaks on real uploads and what we shipped inste…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Reproduce the example in a notebook; then refactor into a reusable function.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/ahmad_dogar_7d098f5e48f72/extracting-roof-measurements-from-pdfs-with-llms-and-why-the-model-is-the-smallest-part-41cb

## Related notes
- [[2026-08-21-how-to-find-duplicate-rows-in-sql-and-decide-what-counts-as-one]]
- [[2026-10-15-free-draft-volume-or-paid-first-passes-a-debate-for-agent-sql-budgets]]
- [[2026-08-11-sql-joins-how-to-join-two-tables-without-losing-or-doubling-rows]]
- [[2026-08-31-running-total-in-sql-the-window-frame-that-decides-the-answer]]
- [[2026-11-18-two-hallucination-tests-you-can-run-before-you-pay-for-a-judge-model]]
- [[2026-11-12-ai-brand-tracking-a-practical-check-you-can-run-today-by-yourself]]
