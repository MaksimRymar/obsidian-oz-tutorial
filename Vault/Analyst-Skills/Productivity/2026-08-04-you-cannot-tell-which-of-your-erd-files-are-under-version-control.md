---
title: You Cannot Tell Which of Your ERD Files Are Under Version Control
date: '2026-08-04'
source: https://dev.to/tbson87/you-cannot-tell-which-of-your-erd-files-are-under-version-control-2o6c
domain: Productivity
relevance: 🟡
tags:
- '#ai'
- '#feature'
- '#productivity'
- '#sql'
- '#support-analytics'
- '#tool'
related:
- '[[2026-08-02-ssms-database-diagrams-your-erd-is-trapped-inside-the-database-it-documents]]'
- '[[2026-07-18-the-data-dictionary-should-live-in-the-erd-not-in-a-spreadsheet]]'
- '[[2026-07-25-lucidchart-erd-alternative-a-desktop-erd-tool-that-connects-to-your-database]]'
- '[[2026-05-20-learning-sql-as-if-you-built-it-yourself]]'
- '[[2026-07-21-my-gitignore-had-a-blanket-rule-one-file-broke-it-and-no-pattern-would-have-caught-that]]'
- '[[2026-03-13-i-built-and-launched-a-mobile-app-in-3-months-as-a-solo-engineer-heres-exactly-what-happened]]'
status: unread
---

> **TL;DR:** Disclosure: I build Schemity , a desktop ERD tool - this post is from our blog and uses it for the examples. TL;DR: A diagram stored as a file is only version controlled if its folder happens to sit inside a Git reposito…

## What’s new and why it matters
Disclosure: I build Schemity , a desktop ERD tool - this post is from our blog and uses it for the examples. TL;DR: A diagram stored as a file is only version controlled if its folder happens to sit inside a Git repository, and nothing in the tool tells you whether it does - so the safest-feeling diagrams are often the untracked ones. Schemity now shows a Git branch icon beside every workspace that lives inside a repository, detected by walking up the directory tree so a workspace nested deep inside a project counts too, and marks imported workspaces with their own icon so the ones you deliber…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/tbson87/you-cannot-tell-which-of-your-erd-files-are-under-version-control-2o6c

## Related notes
- [[2026-08-02-ssms-database-diagrams-your-erd-is-trapped-inside-the-database-it-documents]]
- [[2026-07-18-the-data-dictionary-should-live-in-the-erd-not-in-a-spreadsheet]]
- [[2026-07-25-lucidchart-erd-alternative-a-desktop-erd-tool-that-connects-to-your-database]]
- [[2026-05-20-learning-sql-as-if-you-built-it-yourself]]
- [[2026-07-21-my-gitignore-had-a-blanket-rule-one-file-broke-it-and-no-pattern-would-have-caught-that]]
- [[2026-03-13-i-built-and-launched-a-mobile-app-in-3-months-as-a-solo-engineer-heres-exactly-what-happened]]
