---
title: I pointed Claude at 16,739 job postings and it answers with SQL
date: '2026-11-21'
source: https://dev.to/reaver1000/i-pointed-claude-at-16739-job-postings-and-it-answers-with-sql-3d25
domain: AI-Tools
relevance: 🟡
tags:
- '#ai'
- '#best-practice'
- '#career'
- '#library'
- '#python'
- '#sql'
- '#tool'
related:
- '[[2026-11-18-i-built-one-job-market-dashboard-in-tableau-and-power-bi-to-learn-both-properly]]'
- '[[2026-09-09-six-tables-out-of-260]]'
- '[[2026-09-07-bloom-filters-for-data-engineers-cheap-membership-tests]]'
- '[[2026-09-07-query1ai-ask-your-database-anything-in-plain-english]]'
- '[[2026-11-05-224-new-remote-jobs-in-twelve-days-thirty-one-were-posted-in-the-last-24-hours]]'
- '[[2026-10-14-43-days-17040-ai-signals-four-things-the-data-says-that-trend-lists-wont-tell-you]]'
status: unread
---

> **TL;DR:** My job discovery pipeline sweeps roughly 17,000 postings a day. A dashboard shows the shapes, but sometimes I want one specific answer: how many junior remote roles are up today, which companies are hiring data engineers…

## What’s new and why it matters
My job discovery pipeline sweeps roughly 17,000 postings a day. A dashboard shows the shapes, but sometimes I want one specific answer: how many junior remote roles are up today, which companies are hiring data engineers, what the remote share actually is. So I built a small layer that answers questions in plain English over that data: job-market-qa . The chain is short. The question goes to Claude along with the table schema and a few rules. The model replies with SQL. The SQL passes a guard. DuckDB runs it. The answer comes back as a number or a small table. The guard is the product A text-t…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Reproduce the example in a notebook; then refactor into a reusable function.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/reaver1000/i-pointed-claude-at-16739-job-postings-and-it-answers-with-sql-3d25

## Related notes
- [[2026-11-18-i-built-one-job-market-dashboard-in-tableau-and-power-bi-to-learn-both-properly]]
- [[2026-09-09-six-tables-out-of-260]]
- [[2026-09-07-bloom-filters-for-data-engineers-cheap-membership-tests]]
- [[2026-09-07-query1ai-ask-your-database-anything-in-plain-english]]
- [[2026-11-05-224-new-remote-jobs-in-twelve-days-thirty-one-were-posted-in-the-last-24-hours]]
- [[2026-10-14-43-days-17040-ai-signals-four-things-the-data-says-that-trend-lists-wont-tell-you]]
