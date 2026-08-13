---
title: My Frontmatter Parser Checks for Too Few Delimiters. It Never Checked for Too
  Many.
date: '2026-08-13'
source: https://dev.to/enjoy_kumawat/my-frontmatter-parser-checks-for-too-few-delimiters-it-never-checked-for-too-many-2j45
domain: SQL
relevance: 🟡
tags:
- '#python'
- '#sql'
- '#tool'
related:
- '[[2026-07-21-my-gitignore-had-a-blanket-rule-one-file-broke-it-and-no-pattern-would-have-caught-that]]'
- '[[2026-06-15-day-01-of-learning-data-engineering-step1-sql-joins-and-set-operators]]'
- '[[2026-08-09-why-your-python-search-cant-find-c-c-or-rd-and-how-to-fix-it]]'
- '[[2026-08-01-my-mcp-servers-two-api-helpers-had-zero-except-blocks-every-bad-call-crashed-with-a-raw-urllib-traceback]]'
- '[[2026-08-09-my-mcp-servers-two-credential-checks-were-flagged-missing-five-days-ago-nobody-fixed-them]]'
- '[[2026-08-12-my-comment-reply-pipeline-picks-one-winner-per-thread-two-commenters-broke-that]]'
status: unread
---

> **TL;DR:** I fixed this script's frontmatter parser a week ago. A draft with an unclosed --- block used to blow up with a bare ValueError: not enough values to unpack , and I patched it to raise a clean, actionable error instead. I…

## What’s new and why it matters
I fixed this script's frontmatter parser a week ago. A draft with an unclosed --- block used to blow up with a bare ValueError: not enough values to unpack , and I patched it to raise a clean, actionable error instead. I wrote that fix up, verified it with a stubbed repro, added a --selftest case for it, called it done. Then I went back to write today's articles and actually looked at the line I "fixed" instead of the error path around it. def parse ( text ): meta = {} body = text if text . lstrip (). startswith ( " --- " ): parts = text . lstrip (). split ( " --- " , 2 ) if len ( parts ) < 3…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Write the query in a scratchpad and run EXPLAIN/QUERY PLAN to verify performance.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/enjoy_kumawat/my-frontmatter-parser-checks-for-too-few-delimiters-it-never-checked-for-too-many-2j45

## Related notes
- [[2026-07-21-my-gitignore-had-a-blanket-rule-one-file-broke-it-and-no-pattern-would-have-caught-that]]
- [[2026-06-15-day-01-of-learning-data-engineering-step1-sql-joins-and-set-operators]]
- [[2026-08-09-why-your-python-search-cant-find-c-c-or-rd-and-how-to-fix-it]]
- [[2026-08-01-my-mcp-servers-two-api-helpers-had-zero-except-blocks-every-bad-call-crashed-with-a-raw-urllib-traceback]]
- [[2026-08-09-my-mcp-servers-two-credential-checks-were-flagged-missing-five-days-ago-nobody-fixed-them]]
- [[2026-08-12-my-comment-reply-pipeline-picks-one-winner-per-thread-two-commenters-broke-that]]
