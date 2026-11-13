---
title: 'Reverse-engineer the shadow spreadsheet: turn the Excel your team still uses
  after go-live into a backlog'
date: '2026-11-13'
source: https://dev.to/juanma_garrido_1974/reverse-engineer-the-shadow-spreadsheet-turn-the-excel-your-team-still-uses-after-go-live-into-a-2m1h
domain: Python
relevance: 🟡
tags:
- '#ai'
- '#python'
- '#sql'
- '#support-analytics'
- '#tool'
related:
- '[[2026-09-27-how-to-optimize-a-database-one-step-at-a-time]]'
- '[[2026-09-01-i-raced-six-models-against-each-other-on-digitalocean-inference-the-cheapest-one-won]]'
- '[[2026-06-09-pandas-vs-sql-when-to-use-each]]'
- '[[2026-10-26-sql-joins-explained-inner-left-right-and-full-with-examples]]'
- '[[2026-10-11-your-chatgpt-api-bill-is-high-because-your-prompts-are-bloated-heres-a-free-checklist-to-fix-it]]'
- '[[2026-08-30-funnel-conversion-in-sql-and-the-step-that-shows-100]]'
status: unread
---

> **TL;DR:** The implementation is done. The consultants closed the project. On Monday, a sales rep opens the same spreadsheet they used before. The usual reaction is to ban the spreadsheet. A more useful one is to treat it as the mo…

## What’s new and why it matters
The implementation is done. The consultants closed the project. On Monday, a sales rep opens the same spreadsheet they used before. The usual reaction is to ban the spreadsheet. A more useful one is to treat it as the most honest requirements document you have. Somebody keeps maintaining that file because it solves a problem the new CRM or ERP does not. This post shows a small, repeatable way to read it. Step 1: get a copy and profile it Ask for the actual file, not a description of it. Then look at what is really in it. A few lines of pandas are enough: import pandas as pd df = pd . read_exce…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Reproduce the example in a notebook; then refactor into a reusable function.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/juanma_garrido_1974/reverse-engineer-the-shadow-spreadsheet-turn-the-excel-your-team-still-uses-after-go-live-into-a-2m1h

## Related notes
- [[2026-09-27-how-to-optimize-a-database-one-step-at-a-time]]
- [[2026-09-01-i-raced-six-models-against-each-other-on-digitalocean-inference-the-cheapest-one-won]]
- [[2026-06-09-pandas-vs-sql-when-to-use-each]]
- [[2026-10-26-sql-joins-explained-inner-left-right-and-full-with-examples]]
- [[2026-10-11-your-chatgpt-api-bill-is-high-because-your-prompts-are-bloated-heres-a-free-checklist-to-fix-it]]
- [[2026-08-30-funnel-conversion-in-sql-and-the-step-that-shows-100]]
