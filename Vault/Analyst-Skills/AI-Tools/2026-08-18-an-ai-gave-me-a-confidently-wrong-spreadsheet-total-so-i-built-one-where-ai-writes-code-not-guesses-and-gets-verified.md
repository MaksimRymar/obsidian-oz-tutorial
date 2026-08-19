---
title: An AI gave me a confidently wrong spreadsheet total — so I built one where
  AI writes code, not guesses, and gets verified.
date: '2026-08-18'
source: https://dev.to/durlabh_kumar_a839a974273/an-ai-gave-me-a-confidently-wrong-spreadsheet-total-so-i-built-one-where-ai-writes-code-not-1nf3
domain: AI-Tools
relevance: 🟡
tags:
- '#ai'
- '#best-practice'
- '#tool'
related:
- '[[2026-07-20-ada-an-open-source-ai-data-analyst-that-shows-its-math]]'
- '[[2026-08-07-i-paged-a-table-with-no-order-by-and-lost-2797-rows]]'
- '[[2026-06-22-i-built-an-open-source-tool-that-cleans-a-decade-old-mailbox-with-local-first-ai]]'
- '[[2026-08-18-my-ai-api-cost-spreadsheet-184-models-real-production-numbers]]'
- '[[2026-05-25-i-added-mcp-support-to-my-saas-in-an-afternoon-heres-the-whole-thing]]'
- '[[2026-05-26-i-did-the-math-your-serpapi-bill-is-10x-what-it-should-be]]'
status: unread
---

> **TL;DR:** How I Stopped an AI From Lying to Me About Spreadsheet Totals A few months ago I asked an AI tool to total up a sales spreadsheet. It gave me a clean, confident number. It was wrong. Not "rounding error" wrong — it had q…

## What’s new and why it matters
How I Stopped an AI From Lying to Me About Spreadsheet Totals A few months ago I asked an AI tool to total up a sales spreadsheet. It gave me a clean, confident number. It was wrong. Not "rounding error" wrong — it had quietly skipped rows and produced a total that just looked plausible. Nothing flagged it. Nothing hedged. It just said the number, like it was fact. That's the actual problem with LLMs on tabular data: they don't calculate, they estimate. Ask a model to sum a column and, under the hood, it's doing next-token prediction over a serialized chunk of your spreadsheet — not arithmetic…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Reproduce the example in a notebook; then refactor into a reusable function.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/durlabh_kumar_a839a974273/an-ai-gave-me-a-confidently-wrong-spreadsheet-total-so-i-built-one-where-ai-writes-code-not-1nf3

## Related notes
- [[2026-07-20-ada-an-open-source-ai-data-analyst-that-shows-its-math]]
- [[2026-08-07-i-paged-a-table-with-no-order-by-and-lost-2797-rows]]
- [[2026-06-22-i-built-an-open-source-tool-that-cleans-a-decade-old-mailbox-with-local-first-ai]]
- [[2026-08-18-my-ai-api-cost-spreadsheet-184-models-real-production-numbers]]
- [[2026-05-25-i-added-mcp-support-to-my-saas-in-an-afternoon-heres-the-whole-thing]]
- [[2026-05-26-i-did-the-math-your-serpapi-bill-is-10x-what-it-should-be]]
