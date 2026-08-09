---
title: '"My Comment-Reply Pipeline Was Feeding Me Garbled HTML Entities Instead of
  the Actual Comment"'
date: '2026-08-09'
source: https://dev.to/enjoy_kumawat/my-comment-reply-pipeline-was-feeding-me-garbled-html-entities-instead-of-the-actual-comment-g43
domain: SQL
relevance: 🟡
tags:
- '#best-practice'
- '#python'
- '#sql'
- '#tool'
related:
- '[[2026-07-21-my-gitignore-had-a-blanket-rule-one-file-broke-it-and-no-pattern-would-have-caught-that]]'
- '[[2026-08-02-my-comment-reply-queue-draft-one-reply-to-a-thread-and-it-went-deaf-to-every-follow-up-after-that]]'
- '[[2026-08-07-my-mcp-tools-docstring-promised-limit-1-100-passing--1-returned-almost-everything-not-nothing]]'
- '[[2026-07-19-my-comment-reply-bot-hit-a-wall-the-docs-never-mentioned-that-wall-turned-out-to-be-a-security-feature]]'
- '[[2026-06-24-i-got-tired-of-cryptic-python-error-messages-so-i-built-a-vs-code-extension-that-fixes-them-automatically]]'
- '[[2026-07-26-my-comment-dedup-check-used-in-on-a-whole-markdown-file-a-date-in-a-sentence-broke-it]]'
status: unread
---

> **TL;DR:** I have a small script, reply_comments.py , that pulls unanswered comments off my DEV.to articles and drafts replies to a markdown file so I can paste them in by hand. The API doesn't let a normal account post comments (t…

## What’s new and why it matters
I have a small script, reply_comments.py , that pulls unanswered comments off my DEV.to articles and drafts replies to a markdown file so I can paste them in by hand. The API doesn't let a normal account post comments (that's its own bug I've written about before), so this draft-then-paste loop is the whole workflow. Every reply I've ever sent has come from reading the body field this script prints. Today I went looking for a bug distinct from everything already logged for this repo, and I ended up re-reading strip_html() , the function that turns a comment's raw body_html into the plain text…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Write the query in a scratchpad and run EXPLAIN/QUERY PLAN to verify performance.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/enjoy_kumawat/my-comment-reply-pipeline-was-feeding-me-garbled-html-entities-instead-of-the-actual-comment-g43

## Related notes
- [[2026-07-21-my-gitignore-had-a-blanket-rule-one-file-broke-it-and-no-pattern-would-have-caught-that]]
- [[2026-08-02-my-comment-reply-queue-draft-one-reply-to-a-thread-and-it-went-deaf-to-every-follow-up-after-that]]
- [[2026-08-07-my-mcp-tools-docstring-promised-limit-1-100-passing--1-returned-almost-everything-not-nothing]]
- [[2026-07-19-my-comment-reply-bot-hit-a-wall-the-docs-never-mentioned-that-wall-turned-out-to-be-a-security-feature]]
- [[2026-06-24-i-got-tired-of-cryptic-python-error-messages-so-i-built-a-vs-code-extension-that-fixes-them-automatically]]
- [[2026-07-26-my-comment-dedup-check-used-in-on-a-whole-markdown-file-a-date-in-a-sentence-broke-it]]
