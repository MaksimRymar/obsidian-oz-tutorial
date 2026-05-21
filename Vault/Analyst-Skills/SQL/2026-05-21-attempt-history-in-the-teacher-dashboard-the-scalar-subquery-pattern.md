---
title: Attempt history in the teacher dashboard — the scalar subquery pattern
date: '2026-05-21'
source: https://dev.to/orieken/attempt-history-in-the-teacher-dashboard-the-scalar-subquery-pattern-4an
domain: SQL
relevance: 🟡
tags:
- '#ai'
- '#best-practice'
- '#python'
- '#sql'
- '#support-analytics'
- '#tool'
related:
- '[[2026-04-23-i-built-a-browser-only-sql-practice-tool-because-installing-dbeaver-is-a-productivity-tax]]'
- '[[2026-04-21-sql-window-functions-and-ctes]]'
- '[[2026-04-11-i-trusted-the-code-ai-wrote-for-me-my-data-was-silently-broken-the-whole-time]]'
- '[[2026-03-10-pdf-ocr-extract-text-from-scanned-pdfs-with-an-api]]'
- '[[2026-04-15-sql-limit-and-offset-paginate-your-query-results-like-a-pro]]'
- '[[2026-03-03-sql-joins-window-functions-the-skills-that-separate-analysts-from-beginners]]'
status: unread
---

> **TL;DR:** What We Built In Phase 1 of the KC dashboard we gave teachers per-skill mastery states for each student — colour-coded bars showing Novice / Developing / Mastered. That answered "where is this student stuck?" Phase 2 ans…

## What’s new and why it matters
What We Built In Phase 1 of the KC dashboard we gave teachers per-skill mastery states for each student — colour-coded bars showing Novice / Developing / Mastered. That answered "where is this student stuck?" Phase 2 answers "what exactly did they do wrong?" We added a paginated attempt history table below the KC panel. For the selected student, teachers see every attempt in reverse-chronological order: the problem question, the student's answer, whether it was correct, the timestamp, which Knowledge Component was being practised, and — when the classifier fired — the mistake code (e.g. BORROW…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Write the query in a scratchpad and run EXPLAIN/QUERY PLAN to verify performance.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/orieken/attempt-history-in-the-teacher-dashboard-the-scalar-subquery-pattern-4an

## Related notes
- [[2026-04-23-i-built-a-browser-only-sql-practice-tool-because-installing-dbeaver-is-a-productivity-tax]]
- [[2026-04-21-sql-window-functions-and-ctes]]
- [[2026-04-11-i-trusted-the-code-ai-wrote-for-me-my-data-was-silently-broken-the-whole-time]]
- [[2026-03-10-pdf-ocr-extract-text-from-scanned-pdfs-with-an-api]]
- [[2026-04-15-sql-limit-and-offset-paginate-your-query-results-like-a-pro]]
- [[2026-03-03-sql-joins-window-functions-the-skills-that-separate-analysts-from-beginners]]
