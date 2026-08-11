---
title: My AI Commit-Message Script Assumed Every File in My Repo Is UTF-8. Mine Wasn't.
date: '2026-08-11'
source: https://dev.to/enjoy_kumawat/my-ai-commit-message-script-assumed-every-file-in-my-repo-is-utf-8-mine-wasnt-55b1
domain: AI-Tools
relevance: 🟡
tags:
- '#ai'
- '#python'
- '#sql'
- '#tool'
related:
- '[[2026-08-01-my-mcp-servers-two-api-helpers-had-zero-except-blocks-every-bad-call-crashed-with-a-raw-urllib-traceback]]'
- '[[2026-08-09-my-mcp-servers-two-credential-checks-were-flagged-missing-five-days-ago-nobody-fixed-them]]'
- '[[2026-07-23-my-commit-hook-calls-an-llm-on-every-commit-it-had-no-timeout-so-neither-did-git-commit]]'
- '[[2026-08-07-my-mcp-tools-docstring-promised-limit-1-100-passing--1-returned-almost-everything-not-nothing]]'
- '[[2026-08-10-140-bugs-were-hiding-in-one-function-and-my-tests-couldnt-see-any-of-them]]'
- '[[2026-07-21-my-gitignore-had-a-blanket-rule-one-file-broke-it-and-no-pattern-would-have-caught-that]]'
status: unread
---

> **TL;DR:** I have a small script, git_commit.py , that reads my staged diff and asks Claude to turn it into a Conventional Commit message. It's been through four or five rounds of hardening already — a timeout on the subprocess cal…

## What’s new and why it matters
I have a small script, git_commit.py , that reads my staged diff and asks Claude to turn it into a Conventional Commit message. It's been through four or five rounds of hardening already — a timeout on the subprocess call, a --safe-mode flag so it doesn't accidentally load this project's CLAUDE.md into a one-line completion, a regex that strips any AI attribution the model tries to sneak into the message. I thought the risky part of this script — "shell out to git, shell out to claude, print the result" — had been gone over enough times that there wasn't much left to find. Then I staged a chan…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Reproduce the example in a notebook; then refactor into a reusable function.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/enjoy_kumawat/my-ai-commit-message-script-assumed-every-file-in-my-repo-is-utf-8-mine-wasnt-55b1

## Related notes
- [[2026-08-01-my-mcp-servers-two-api-helpers-had-zero-except-blocks-every-bad-call-crashed-with-a-raw-urllib-traceback]]
- [[2026-08-09-my-mcp-servers-two-credential-checks-were-flagged-missing-five-days-ago-nobody-fixed-them]]
- [[2026-07-23-my-commit-hook-calls-an-llm-on-every-commit-it-had-no-timeout-so-neither-did-git-commit]]
- [[2026-08-07-my-mcp-tools-docstring-promised-limit-1-100-passing--1-returned-almost-everything-not-nothing]]
- [[2026-08-10-140-bugs-were-hiding-in-one-function-and-my-tests-couldnt-see-any-of-them]]
- [[2026-07-21-my-gitignore-had-a-blanket-rule-one-file-broke-it-and-no-pattern-would-have-caught-that]]
