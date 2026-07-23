---
title: My Commit Hook Calls an LLM on Every Commit. It Had No Timeout, So Neither
  Did `git commit`.
date: '2026-07-23'
source: https://dev.to/enjoy_kumawat/my-commit-hook-calls-an-llm-on-every-commit-it-had-no-timeout-so-neither-did-git-commit-bpj
domain: AI-Tools
relevance: 🟡
tags:
- '#ai'
- '#python'
- '#sql'
- '#tool'
related:
- '[[2026-07-21-my-gitignore-had-a-blanket-rule-one-file-broke-it-and-no-pattern-would-have-caught-that]]'
- '[[2026-03-13-you-dont-need-a-framework-building-reliable-ai-agents-from-first-principles]]'
- '[[2026-04-21-what-happens-to-your-mutual-fund-between-9-am-and-9-pm]]'
- '[[2026-07-19-my-comment-reply-bot-hit-a-wall-the-docs-never-mentioned-that-wall-turned-out-to-be-a-security-feature]]'
- '[[2026-03-15-i-was-tired-of-writing-fix-as-my-commit-message-so-i-built-this-in-one-afternoon]]'
- '[[2026-03-31-how-i-made-claude-code-and-gpt-54-review-each-others-code]]'
status: unread
---

> **TL;DR:** I have a prepare-commit-msg hook in this repo that shells out to Claude Code to draft the commit message from the staged diff. It's been running quietly for a month, and I never once thought about what happens when the c…

## What’s new and why it matters
I have a prepare-commit-msg hook in this repo that shells out to Claude Code to draft the commit message from the staged diff. It's been running quietly for a month, and I never once thought about what happens when the call doesn't come back. The setup is small on purpose. A shell hook resolves and calls a Python script: #!/bin/sh # AI commit message pre-fill via Claude CLI # Skips merge commits, squash, and amend [ " $2 " = "" ] || exit 0 SCRIPT = " $( cd " $( dirname " $0 " ) /.." && pwd ) /git_commit.py" python " $SCRIPT " > " $1 " 2>/dev/null || true And the script itself: diff = subproces…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Reproduce the example in a notebook; then refactor into a reusable function.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/enjoy_kumawat/my-commit-hook-calls-an-llm-on-every-commit-it-had-no-timeout-so-neither-did-git-commit-bpj

## Related notes
- [[2026-07-21-my-gitignore-had-a-blanket-rule-one-file-broke-it-and-no-pattern-would-have-caught-that]]
- [[2026-03-13-you-dont-need-a-framework-building-reliable-ai-agents-from-first-principles]]
- [[2026-04-21-what-happens-to-your-mutual-fund-between-9-am-and-9-pm]]
- [[2026-07-19-my-comment-reply-bot-hit-a-wall-the-docs-never-mentioned-that-wall-turned-out-to-be-a-security-feature]]
- [[2026-03-15-i-was-tired-of-writing-fix-as-my-commit-message-so-i-built-this-in-one-afternoon]]
- [[2026-03-31-how-i-made-claude-code-and-gpt-54-review-each-others-code]]
