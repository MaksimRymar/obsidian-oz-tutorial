---
title: My Comment-Reply Pipeline Picks One Winner Per Thread. Two Commenters Broke
  That.
date: '2026-08-12'
source: https://dev.to/enjoy_kumawat/my-comment-reply-pipeline-picks-one-winner-per-thread-two-commenters-broke-that-5ck7
domain: AI-Tools
relevance: 🟡
tags:
- '#ai'
- '#python'
- '#tool'
related:
- '[[2026-08-02-my-comment-reply-queue-draft-one-reply-to-a-thread-and-it-went-deaf-to-every-follow-up-after-that]]'
- '[[2026-08-09-my-comment-reply-pipeline-was-feeding-me-garbled-html-entities-instead-of-the-actual-comment]]'
- '[[2026-07-21-my-gitignore-had-a-blanket-rule-one-file-broke-it-and-no-pattern-would-have-caught-that]]'
- '[[2026-07-26-my-comment-dedup-check-used-in-on-a-whole-markdown-file-a-date-in-a-sentence-broke-it]]'
- '[[2026-08-08-my-mcp-tool-fetches-before-it-writes-and-logs-every-change-it-never-checked-whether-there-was-anything-to-change]]'
- '[[2026-07-15-i-built-with-both-apis-as-a-bootcamp-grad-heres-what-actually-matters]]'
status: unread
---

> **TL;DR:** reply_comments.py is the script that tells me which DEV.to comments still need a reply. It walks every comment tree on every article I've published and reports the ones I haven't answered yet. I've fixed two bugs in it a…

## What’s new and why it matters
reply_comments.py is the script that tells me which DEV.to comments still need a reply. It walks every comment tree on every article I've published and reports the ones I haven't answered yet. I've fixed two bugs in it already: needs_reply() used to think a thread was "handled" forever after a single reply, even if the other person followed up again, and a dedup check was keyed on the thread's root comment instead of whichever message actually needed the reply, so a second round of conversation went permanently invisible. Both fixes are in --selftest now, and both looked, from the outside, lik…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Reproduce the example in a notebook; then refactor into a reusable function.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/enjoy_kumawat/my-comment-reply-pipeline-picks-one-winner-per-thread-two-commenters-broke-that-5ck7

## Related notes
- [[2026-08-02-my-comment-reply-queue-draft-one-reply-to-a-thread-and-it-went-deaf-to-every-follow-up-after-that]]
- [[2026-08-09-my-comment-reply-pipeline-was-feeding-me-garbled-html-entities-instead-of-the-actual-comment]]
- [[2026-07-21-my-gitignore-had-a-blanket-rule-one-file-broke-it-and-no-pattern-would-have-caught-that]]
- [[2026-07-26-my-comment-dedup-check-used-in-on-a-whole-markdown-file-a-date-in-a-sentence-broke-it]]
- [[2026-08-08-my-mcp-tool-fetches-before-it-writes-and-logs-every-change-it-never-checked-whether-there-was-anything-to-change]]
- [[2026-07-15-i-built-with-both-apis-as-a-bootcamp-grad-heres-what-actually-matters]]
