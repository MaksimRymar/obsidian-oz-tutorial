---
title: Before trusting a weight edit, I measured the bug it fixes
date: '2026-11-07'
source: https://dev.to/krishanu_das/before-trusting-a-weight-edit-i-measured-the-bug-it-fixes-401f
domain: AI-Tools
relevance: 🟡
tags:
- '#ai'
- '#career'
- '#sql'
- '#tool'
related:
- '[[2026-10-27-48-hour-field-notes-my-prompt-budget-was-in-characters-and-the-overflow-never-raised]]'
- '[[2026-04-02-how-to-stop-your-ai-agent-from-burning-400month-on-api-calls]]'
- '[[2026-09-23-38-of-an-analysts-questions-get-no-records-found-when-the-data-is-right-there]]'
- '[[2026-10-15-free-draft-volume-or-paid-first-passes-a-debate-for-agent-sql-budgets]]'
- '[[2026-09-27-i-built-an-ai-agent-that-snapshots-every-edit-and-runs-your-tests-before-it-says-done]]'
- '[[2026-09-22-we-have-no-marketing-state-table-only-five-sql-windows-over-timestamps-we-already-had]]'
status: unread
---

> **TL;DR:** Krishanu Das · November 2026 · Code, plans and raw records: github.com/Krishanu-das-05/weight-space-training TL;DR. A recent post showed an AI agent editing the weights of Qwen3.5-0.8B and raising its MATH-500 score from…

## What’s new and why it matters
Krishanu Das · November 2026 · Code, plans and raw records: github.com/Krishanu-das-05/weight-space-training TL;DR. A recent post showed an AI agent editing the weights of Qwen3.5-0.8B and raising its MATH-500 score from 7.9% to 48.1%. I tried to check the edit on a laptop GPU, and along the way found that "the model finished" and "the model was right" have to be measured separately. With thinking on, the unedited model finished naturally on only 2 of 30 GSM8K questions at an 8,192-token budget. Giving it more tokens did not help. With the published edit applied, 10 of 30 finished and 9 of 30…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Reproduce the example in a notebook; then refactor into a reusable function.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/krishanu_das/before-trusting-a-weight-edit-i-measured-the-bug-it-fixes-401f

## Related notes
- [[2026-10-27-48-hour-field-notes-my-prompt-budget-was-in-characters-and-the-overflow-never-raised]]
- [[2026-04-02-how-to-stop-your-ai-agent-from-burning-400month-on-api-calls]]
- [[2026-09-23-38-of-an-analysts-questions-get-no-records-found-when-the-data-is-right-there]]
- [[2026-10-15-free-draft-volume-or-paid-first-passes-a-debate-for-agent-sql-budgets]]
- [[2026-09-27-i-built-an-ai-agent-that-snapshots-every-edit-and-runs-your-tests-before-it-says-done]]
- [[2026-09-22-we-have-no-marketing-state-table-only-five-sql-windows-over-timestamps-we-already-had]]
