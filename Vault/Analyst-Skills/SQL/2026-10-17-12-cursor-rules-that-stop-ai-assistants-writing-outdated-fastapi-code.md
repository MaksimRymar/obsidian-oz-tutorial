---
title: 12 Cursor rules that stop AI assistants writing outdated FastAPI code
date: '2026-10-17'
source: https://dev.to/rdj/12-cursor-rules-that-stop-ai-assistants-writing-outdated-fastapi-code-1bc2
domain: SQL
relevance: 🟡
tags:
- '#ai'
- '#best-practice'
- '#feature'
- '#python'
- '#sql'
- '#tool'
related:
- '[[2026-05-18-how-i-stopped-losing-context-with-ai-coding-assistants-and-built-6-agentsmd-templates-to-share]]'
- '[[2026-08-20-a-benchmark-is-only-as-good-as-the-model-you-use-to-grade-it]]'
- '[[2026-05-22-i-built-a-type-safe-sql-library-for-bun-no-orm-no-codegen-just-sql-using-claude-code]]'
- '[[2026-09-03-building-an-ast-code-verifier-without-networkx-gitpython-or-any-dependencies]]'
- '[[2026-10-05-queuepool-limit-reached---when-fastapi-runs-out-of-database-connections]]'
- '[[2026-03-16-stop-sending-your-code-to-the-cloud-to-find-bugs]]'
status: unread
---

> **TL;DR:** AI coding assistants still reach for FastAPI patterns from a few years ago: .dict() , orm_mode , session.query() , HTTPException raised deep inside service code, SQLite in tests. The code runs, but it isn't the code you'…

## What’s new and why it matters
AI coding assistants still reach for FastAPI patterns from a few years ago: .dict() , orm_mode , session.query() , HTTPException raised deep inside service code, SQLite in tests. The code runs, but it isn't the code you'd write today. Cursor's project rules fix most of this. A rule is a small .mdc file in .cursor/rules/ with a glob, so it loads only when you edit matching files: --- description : " FastAPI routers, dependencies and Pydantic v2 schemas" globs : src/app/**/router.py,src/app/**/schemas.py,src/app/**/deps.py alwaysApply : false --- - One APIRouter(prefix="/<plural-resource>") per…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Write the query in a scratchpad and run EXPLAIN/QUERY PLAN to verify performance.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/rdj/12-cursor-rules-that-stop-ai-assistants-writing-outdated-fastapi-code-1bc2

## Related notes
- [[2026-05-18-how-i-stopped-losing-context-with-ai-coding-assistants-and-built-6-agentsmd-templates-to-share]]
- [[2026-08-20-a-benchmark-is-only-as-good-as-the-model-you-use-to-grade-it]]
- [[2026-05-22-i-built-a-type-safe-sql-library-for-bun-no-orm-no-codegen-just-sql-using-claude-code]]
- [[2026-09-03-building-an-ast-code-verifier-without-networkx-gitpython-or-any-dependencies]]
- [[2026-10-05-queuepool-limit-reached---when-fastapi-runs-out-of-database-connections]]
- [[2026-03-16-stop-sending-your-code-to-the-cloud-to-find-bugs]]
