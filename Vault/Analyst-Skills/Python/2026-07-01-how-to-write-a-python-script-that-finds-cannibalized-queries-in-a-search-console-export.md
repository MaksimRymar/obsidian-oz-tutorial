---
title: How to Write a Python Script That Finds Cannibalized Queries in a Search Console
  Export
date: '2026-07-01'
source: https://dev.to/137foundry/how-to-write-a-python-script-that-finds-cannibalized-queries-in-a-search-console-export-3o1g
domain: Python
relevance: 🟡
tags:
- '#ai'
- '#python'
- '#support-analytics'
- '#tool'
- '#tutorial'
related:
- '[[2026-04-13-from-data-to-decisions-designing-an-ai-seo-agent-with-azure-openai-python]]'
- '[[2026-06-10-sql-for-data-analysis-the-10-query-patterns-that-matter]]'
- '[[2026-04-08-i-built-a-bot-that-answers-github-discussions-using-free-ai-models-heres-what-i-learned]]'
- '[[2026-03-30-database-indexing-explained-whats-actually-happening-under-the-hood]]'
- '[[2026-04-30-the-database-is-where-ai-agents-in-production-get-weird]]'
- '[[2026-05-12-10-sql-changes-one-took-30-seconds-it-cut-query-time-by-85]]'
status: unread
---

> **TL;DR:** If you manage SEO for a site with more than a few hundred pages, running the cannibalization checks manually in Google Search Console gets old fast. The good news is that Search Console exports its Performance data in a…

## What’s new and why it matters
If you manage SEO for a site with more than a few hundred pages, running the cannibalization checks manually in Google Search Console gets old fast. The good news is that Search Console exports its Performance data in a format that pandas will happily chew through, and about 30 lines of Python will surface every cannibalized query on your site sorted by impact. This walkthrough builds that script from scratch, explains what each check is doing, and produces a CSV you can hand to a content strategist. What you need before you start Two exports from Search Console. Open the Performance report, s…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Reproduce the example in a notebook; then refactor into a reusable function.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/137foundry/how-to-write-a-python-script-that-finds-cannibalized-queries-in-a-search-console-export-3o1g

## Related notes
- [[2026-04-13-from-data-to-decisions-designing-an-ai-seo-agent-with-azure-openai-python]]
- [[2026-06-10-sql-for-data-analysis-the-10-query-patterns-that-matter]]
- [[2026-04-08-i-built-a-bot-that-answers-github-discussions-using-free-ai-models-heres-what-i-learned]]
- [[2026-03-30-database-indexing-explained-whats-actually-happening-under-the-hood]]
- [[2026-04-30-the-database-is-where-ai-agents-in-production-get-weird]]
- [[2026-05-12-10-sql-changes-one-took-30-seconds-it-cut-query-time-by-85]]
