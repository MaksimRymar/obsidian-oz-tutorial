---
title: 푸시 없이 Claude 채팅이 MCP로 osFoundry 작업을 가져가는 방법
date: '2026-11-07'
source: https://dev.to/bbt-ko/pusi-eobsi-claude-caetingi-mcpro-osfoundry-jageobeul-gajyeoganeun-bangbeob-1i20
domain: AI-Tools
relevance: 🟡
tags:
- '#ai'
- '#feature'
- '#python'
- '#sql'
- '#tool'
related:
- '[[2026-10-25-pagination-that-skips-rows-is-an-off-by-one-in-the-data-model]]'
- '[[2026-06-12-indexes-quickstart-using-postgresql-15-sec-read]]'
- '[[2026-10-30-count-accepted-jobs-not-successful-api-calls-when-comparing-ai-workflows]]'
- '[[2026-09-16-structured-logging-for-data-pipelines-json-logs-correlation-ids]]'
- '[[2026-03-26-sqlite-is-enough-for-your-side-project-full-text-search-json-and-wal-mode-included]]'
- '[[2026-06-13-top-12-sql-interview-problems-for-data-engineers-with-answers]]'
status: unread
---

> **TL;DR:** >> {"jsonrpc": "2.0", "id": 7, "method": "tools/call", "params": {"name": "claim_linked_chat_task", "arguments": {"chat_link_id": "3f6c0b1e-link", "task_id": "d97fd414-3916-4b13-937d-d78de6b3b053"}}} << {"jsonrpc": "2.0"…

## What’s new and why it matters
>> {"jsonrpc": "2.0", "id": 7, "method": "tools/call", "params": {"name": "claim_linked_chat_task", "arguments": {"chat_link_id": "3f6c0b1e-link", "task_id": "d97fd414-3916-4b13-937d-d78de6b3b053"}}} << {"jsonrpc": "2.0", "id": 7, "result": {"content": [{"type": "text", "text": "{\"claim_id\": \"8ffc774f-0a76-4846-9bbd-d66493ca08f4\", \"lease_until\": 1793942663.8222258}"}]}} >> {"jsonrpc": "2.0", "id": 7, "method": "tools/call", "params": {"name": "submit_linked_chat_result", "arguments": {"chat_link_id": "3f6c0b1e-link", "task_id": "d97fd414-…", "claim_id": "8ffc774f-…", "status": "completed…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Reproduce the example in a notebook; then refactor into a reusable function.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/bbt-ko/pusi-eobsi-claude-caetingi-mcpro-osfoundry-jageobeul-gajyeoganeun-bangbeob-1i20

## Related notes
- [[2026-10-25-pagination-that-skips-rows-is-an-off-by-one-in-the-data-model]]
- [[2026-06-12-indexes-quickstart-using-postgresql-15-sec-read]]
- [[2026-10-30-count-accepted-jobs-not-successful-api-calls-when-comparing-ai-workflows]]
- [[2026-09-16-structured-logging-for-data-pipelines-json-logs-correlation-ids]]
- [[2026-03-26-sqlite-is-enough-for-your-side-project-full-text-search-json-and-wal-mode-included]]
- [[2026-06-13-top-12-sql-interview-problems-for-data-engineers-with-answers]]
