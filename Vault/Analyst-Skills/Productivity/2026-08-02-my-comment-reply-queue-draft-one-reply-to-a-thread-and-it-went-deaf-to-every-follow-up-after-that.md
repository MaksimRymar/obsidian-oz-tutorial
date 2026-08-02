---
title: My Comment-Reply Queue Draft One Reply to a Thread and It Went Deaf to Every
  Follow-Up After That
date: '2026-08-02'
source: https://dev.to/enjoy_kumawat/my-comment-reply-queue-draft-one-reply-to-a-thread-and-it-went-deaf-to-every-follow-up-after-that-2dlc
domain: Productivity
relevance: 🟡
tags:
- '#productivity'
- '#python'
- '#tool'
related:
- '[[2026-07-21-my-gitignore-had-a-blanket-rule-one-file-broke-it-and-no-pattern-would-have-caught-that]]'
- '[[2026-07-26-my-comment-dedup-check-used-in-on-a-whole-markdown-file-a-date-in-a-sentence-broke-it]]'
- '[[2026-07-20-df-said-my-sandbox-had-no-disk-left-it-wasnt-wrong-it-just-wasnt-answering-the-question-i-asked]]'
- '[[2026-07-15-i-built-with-both-apis-as-a-bootcamp-grad-heres-what-actually-matters]]'
- '[[2026-03-13-you-dont-need-a-framework-building-reliable-ai-agents-from-first-principles]]'
- '[[2026-06-29-i-wish-id-known-about-ai-api-speed-sooner-heres-my-honest-breakdown]]'
status: unread
---

> **TL;DR:** I have a small script, reply_comments.py , that keeps me from having to re-scan every DEV.to article for new comments by hand. It has two commands: pending (unanswered comments I haven't drafted a reply to yet) and audit…

## What’s new and why it matters
I have a small script, reply_comments.py , that keeps me from having to re-scan every DEV.to article for new comments by hand. It has two commands: pending (unanswered comments I haven't drafted a reply to yet) and audit (drafted replies I said I'd paste manually but apparently never did). I've already fixed two bugs in this file — one in needs_reply() (a thread stayed "handled" forever after a single reply, even when the other person followed up again) and one in audit() (it only checked direct children, so a reply nested two levels deep was invisible). Today I found a third, in pending() its…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/enjoy_kumawat/my-comment-reply-queue-draft-one-reply-to-a-thread-and-it-went-deaf-to-every-follow-up-after-that-2dlc

## Related notes
- [[2026-07-21-my-gitignore-had-a-blanket-rule-one-file-broke-it-and-no-pattern-would-have-caught-that]]
- [[2026-07-26-my-comment-dedup-check-used-in-on-a-whole-markdown-file-a-date-in-a-sentence-broke-it]]
- [[2026-07-20-df-said-my-sandbox-had-no-disk-left-it-wasnt-wrong-it-just-wasnt-answering-the-question-i-asked]]
- [[2026-07-15-i-built-with-both-apis-as-a-bootcamp-grad-heres-what-actually-matters]]
- [[2026-03-13-you-dont-need-a-framework-building-reliable-ai-agents-from-first-principles]]
- [[2026-06-29-i-wish-id-known-about-ai-api-speed-sooner-heres-my-honest-breakdown]]
