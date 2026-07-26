---
title: 'I Gave My MCP Tool an ERROR: Convention. I Only Taught It to One of Its Two
  Failure Paths.'
date: '2026-07-26'
source: https://dev.to/enjoy_kumawat/i-gave-my-mcp-tool-an-error-convention-i-only-taught-it-to-one-of-its-two-failure-paths-4619
domain: AI-Tools
relevance: 🟡
tags:
- '#ai'
- '#python'
- '#tool'
related:
- '[[2026-07-21-my-gitignore-had-a-blanket-rule-one-file-broke-it-and-no-pattern-would-have-caught-that]]'
- '[[2026-07-22-the-backfill-pattern-adding-required-columns-without-downtime]]'
- '[[2026-07-23-btree-height-after-delete-postgresql-fast-root]]'
- '[[2026-07-22-when-to-trust-ai-generated-sql-and-when-not-to]]'
- '[[2026-07-20-df-said-my-sandbox-had-no-disk-left-it-wasnt-wrong-it-just-wasnt-answering-the-question-i-asked]]'
- '[[2026-07-15-i-built-with-both-apis-as-a-bootcamp-grad-heres-what-actually-matters]]'
status: unread
---

> **TL;DR:** Two days ago I found and fixed a real gap in generate_commit_message , the MCP tool in server.py that turns a git diff into a Conventional Commit message via claude -p . Called with an empty diff, it used to hand the who…

## What’s new and why it matters
Two days ago I found and fixed a real gap in generate_commit_message , the MCP tool in server.py that turns a git diff into a Conventional Commit message via claude -p . Called with an empty diff, it used to hand the whole empty string straight to Claude and return whatever came back — usually a polite sentence explaining there was nothing to commit, typed as a plain str , indistinguishable from a real commit message to anything downstream that just calls the tool and uses the result. I fixed that by adding a guard: @mcp.tool () def generate_commit_message ( diff : str ) -> str : """ Generate…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Reproduce the example in a notebook; then refactor into a reusable function.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/enjoy_kumawat/i-gave-my-mcp-tool-an-error-convention-i-only-taught-it-to-one-of-its-two-failure-paths-4619

## Related notes
- [[2026-07-21-my-gitignore-had-a-blanket-rule-one-file-broke-it-and-no-pattern-would-have-caught-that]]
- [[2026-07-22-the-backfill-pattern-adding-required-columns-without-downtime]]
- [[2026-07-23-btree-height-after-delete-postgresql-fast-root]]
- [[2026-07-22-when-to-trust-ai-generated-sql-and-when-not-to]]
- [[2026-07-20-df-said-my-sandbox-had-no-disk-left-it-wasnt-wrong-it-just-wasnt-answering-the-question-i-asked]]
- [[2026-07-15-i-built-with-both-apis-as-a-bootcamp-grad-heres-what-actually-matters]]
