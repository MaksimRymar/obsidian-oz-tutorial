---
title: My MCP Server's Two API Helpers Had Zero except Blocks. Every Bad Call Crashed
  With a Raw urllib Traceback.
date: '2026-08-01'
source: https://dev.to/enjoy_kumawat/my-mcp-servers-two-api-helpers-had-zero-except-blocks-every-bad-call-crashed-with-a-raw-urllib-102n
domain: AI-Tools
relevance: 🟡
tags:
- '#ai'
- '#best-practice'
- '#python'
- '#sql'
- '#tool'
related:
- '[[2026-08-01-my-publish-script-truncates-tags-to-4-my-mcp-tool-that-does-the-same-job-never-learned-that-rule]]'
- '[[2026-07-21-my-gitignore-had-a-blanket-rule-one-file-broke-it-and-no-pattern-would-have-caught-that]]'
- '[[2026-07-26-i-gave-my-mcp-tool-an-error-convention-i-only-taught-it-to-one-of-its-two-failure-paths]]'
- '[[2026-07-07-the-content-audit-that-didnt-need-me-to-build-a-scraper]]'
- '[[2026-07-30-i-wrote-integration-tests-for-my-mcp-failure-library-heres-the-pattern-that-caught-3-hidden-bugs]]'
- '[[2026-03-13-you-dont-need-a-framework-building-reliable-ai-agents-from-first-principles]]'
status: unread
---

> **TL;DR:** I've spent the last few weeks hardening one function in my MCP server's claude -p wrapper. First a timeout fix. Then it turned out the timeout fix didn't cover a non-zero exit code. Then it turned out that fix still didn…

## What’s new and why it matters
I've spent the last few weeks hardening one function in my MCP server's claude -p wrapper. First a timeout fix. Then it turned out the timeout fix didn't cover a non-zero exit code. Then it turned out that fix still didn't cover a missing binary. Three separate posts, three separate except clauses, all on the same six-line try block, until _claude() finally had a clean, consistent failure path: catch everything plausible, return a string prefixed ERROR: , never let a raw exception reach the MCP client. While going back through the rest of server.py to see if that pattern had actually spread an…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Reproduce the example in a notebook; then refactor into a reusable function.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/enjoy_kumawat/my-mcp-servers-two-api-helpers-had-zero-except-blocks-every-bad-call-crashed-with-a-raw-urllib-102n

## Related notes
- [[2026-08-01-my-publish-script-truncates-tags-to-4-my-mcp-tool-that-does-the-same-job-never-learned-that-rule]]
- [[2026-07-21-my-gitignore-had-a-blanket-rule-one-file-broke-it-and-no-pattern-would-have-caught-that]]
- [[2026-07-26-i-gave-my-mcp-tool-an-error-convention-i-only-taught-it-to-one-of-its-two-failure-paths]]
- [[2026-07-07-the-content-audit-that-didnt-need-me-to-build-a-scraper]]
- [[2026-07-30-i-wrote-integration-tests-for-my-mcp-failure-library-heres-the-pattern-that-caught-3-hidden-bugs]]
- [[2026-03-13-you-dont-need-a-framework-building-reliable-ai-agents-from-first-principles]]
