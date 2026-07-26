---
title: My Comment-Dedup Check Used "in" on a Whole Markdown File. A Date in a Sentence
  Broke It.
date: '2026-07-26'
source: https://dev.to/enjoy_kumawat/my-comment-dedup-check-used-in-on-a-whole-markdown-file-a-date-in-a-sentence-broke-it-gmf
domain: SQL
relevance: 🟡
tags:
- '#python'
- '#sql'
- '#support-analytics'
- '#tool'
related:
- '[[2026-07-21-my-gitignore-had-a-blanket-rule-one-file-broke-it-and-no-pattern-would-have-caught-that]]'
- '[[2026-06-15-day-01-of-learning-data-engineering-step1-sql-joins-and-set-operators]]'
- '[[2026-07-18-im-not-a-real-developer-so-i-built-my-app-the-simplest-way-possible]]'
- '[[2026-07-09-dashboards-dont-get-opened-building-a-weekly-lapse-risk-pipeline-that-pushes-work-instead-of-waiting-for-logins]]'
- '[[2026-07-24-ai-generated-sql-has-a-silent-failure-problem-heres-a-way-to-catch-it]]'
- '[[2026-06-16-sql-or-python-the-line-is-sharper-than-you-think-with-code]]'
status: unread
---

> **TL;DR:** I have a small script, reply_comments.py , that keeps my DEV.to comment-reply backlog from turning invisible. It runs in an unattended pipeline twice a day: pull every comment on my articles, skip the ones I've already r…

## What’s new and why it matters
I have a small script, reply_comments.py , that keeps my DEV.to comment-reply backlog from turning invisible. It runs in an unattended pipeline twice a day: pull every comment on my articles, skip the ones I've already replied to, skip the ones I've already drafted a reply for, and print whatever's left as JSON so I can act on it. The dedup for "already drafted" is supposed to be simple: every drafted reply gets a markdown header in drafts/comment_replies.md like ## 3b908 — mads_hansen on "..." , keyed by the comment's id_code . If a comment's id_code has a header, it's drafted. If not, it's p…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Write the query in a scratchpad and run EXPLAIN/QUERY PLAN to verify performance.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/enjoy_kumawat/my-comment-dedup-check-used-in-on-a-whole-markdown-file-a-date-in-a-sentence-broke-it-gmf

## Related notes
- [[2026-07-21-my-gitignore-had-a-blanket-rule-one-file-broke-it-and-no-pattern-would-have-caught-that]]
- [[2026-06-15-day-01-of-learning-data-engineering-step1-sql-joins-and-set-operators]]
- [[2026-07-18-im-not-a-real-developer-so-i-built-my-app-the-simplest-way-possible]]
- [[2026-07-09-dashboards-dont-get-opened-building-a-weekly-lapse-risk-pipeline-that-pushes-work-instead-of-waiting-for-logins]]
- [[2026-07-24-ai-generated-sql-has-a-silent-failure-problem-heres-a-way-to-catch-it]]
- [[2026-06-16-sql-or-python-the-line-is-sharper-than-you-think-with-code]]
