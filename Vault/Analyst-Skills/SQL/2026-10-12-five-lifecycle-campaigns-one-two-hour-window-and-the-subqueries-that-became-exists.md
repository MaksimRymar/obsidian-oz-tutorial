---
title: Five lifecycle campaigns, one two-hour window, and the subqueries that became
  EXISTS
date: '2026-10-12'
source: https://dev.to/daniel_pertu/five-lifecycle-campaigns-one-two-hour-window-and-the-subqueries-that-became-exists-kgg
domain: SQL
relevance: 🟡
tags:
- '#career'
- '#sql'
- '#tool'
related:
- '[[2026-09-22-we-have-no-marketing-state-table-only-five-sql-windows-over-timestamps-we-already-had]]'
- '[[2026-08-31-running-total-in-sql-the-window-frame-that-decides-the-answer]]'
- '[[2026-08-12-sql-foundations-start-to-finish]]'
- '[[2026-08-11-sql-aliases-how-to-read-a-query-out-loud]]'
- '[[2026-09-04-i-built-an-offline-document-indexer-and-ollama-taught-me-two-things-i-did-not-expect]]'
- '[[2026-08-21-how-to-find-duplicate-rows-in-sql-and-decide-what-counts-as-one]]'
status: unread
---

> **TL;DR:** CogniPrep sends a small set of lifecycle emails. An hourly cron selects an audience per campaign, mints a single-use code, and sends. There are five campaigns and they are processed in a fixed priority order: const CAMPA…

## What’s new and why it matters
CogniPrep sends a small set of lifecycle emails. An hourly cron selects an audience per campaign, mints a single-use code, and sends. There are five campaigns and they are processed in a fixed priority order: const CAMPAIGNS = [ { campaign : ' assessment_centre ' , candidates : assessmentCentreCandidates }, { campaign : ' interview ' , candidates : interviewCandidates }, { campaign : ' scores_feedback ' , candidates : scoresFeedbackCandidates }, { campaign : ' win_back ' , candidates : winBackCandidates }, { campaign : ' referral ' , candidates : referralCandidates , sendLogOnly : true }, ]; U…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Write the query in a scratchpad and run EXPLAIN/QUERY PLAN to verify performance.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/daniel_pertu/five-lifecycle-campaigns-one-two-hour-window-and-the-subqueries-that-became-exists-kgg

## Related notes
- [[2026-09-22-we-have-no-marketing-state-table-only-five-sql-windows-over-timestamps-we-already-had]]
- [[2026-08-31-running-total-in-sql-the-window-frame-that-decides-the-answer]]
- [[2026-08-12-sql-foundations-start-to-finish]]
- [[2026-08-11-sql-aliases-how-to-read-a-query-out-loud]]
- [[2026-09-04-i-built-an-offline-document-indexer-and-ollama-taught-me-two-things-i-did-not-expect]]
- [[2026-08-21-how-to-find-duplicate-rows-in-sql-and-decide-what-counts-as-one]]
