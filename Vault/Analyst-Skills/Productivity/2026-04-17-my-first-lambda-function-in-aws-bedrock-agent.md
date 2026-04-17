---
title: My first Lambda function in AWS Bedrock Agent
date: '2026-04-17'
source: https://dev.to/kyooryoo/my-first-lambda-function-in-aws-bedrock-agent-4ioa
domain: Productivity
relevance: 🟡
tags:
- '#productivity'
- '#python'
- '#tool'
related:
- '[[2026-02-23-getting-started-with-trinity-pattern-in-10-minutes]]'
- '[[2026-04-14-claude-api-tool-use-in-production-retry-logic-token-budgets-error-handling]]'
- '[[2026-02-28-delete-itemsid-removing-data-from-your-api-with-fastapi]]'
- '[[2026-04-06-how-i-built-persistent-memory-for-ai-agents-in-python]]'
- '[[2026-04-09-i-open-sourced-my-ollama-logging-proxy]]'
- '[[2026-04-12-postgresql-jsonb-a-complete-guide-to-storing-and-querying-json-data]]'
status: unread
---

> **TL;DR:** Amazon Bedrock > Agents > Agent Builder > Action Group > Action Group Invocation > Select Lambda function > View import json from datetime import datetime from zoneinfo import ZoneInfo def lambda_handler ( event , contex…

## What’s new and why it matters
Amazon Bedrock > Agents > Agent Builder > Action Group > Action Group Invocation > Select Lambda function > View import json from datetime import datetime from zoneinfo import ZoneInfo def lambda_handler ( event , context ): now_cst = datetime . now ( ZoneInfo ( " Asia/Shanghai " )). strftime ( " %Y-%m-%d %H:%M:%S %Z %z " ) return { " messageVersion " : " 1.0 " , " response " : { " actionGroup " : event . get ( " actionGroup " ), " function " : event . get ( " function " ), " apiPath " : event . get ( " apiPath " ), " httpMethod " : event . get ( " httpMethod " ), " httpStatusCode " : 200 , "…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/kyooryoo/my-first-lambda-function-in-aws-bedrock-agent-4ioa

## Related notes
- [[2026-02-23-getting-started-with-trinity-pattern-in-10-minutes]]
- [[2026-04-14-claude-api-tool-use-in-production-retry-logic-token-budgets-error-handling]]
- [[2026-02-28-delete-itemsid-removing-data-from-your-api-with-fastapi]]
- [[2026-04-06-how-i-built-persistent-memory-for-ai-agents-in-python]]
- [[2026-04-09-i-open-sourced-my-ollama-logging-proxy]]
- [[2026-04-12-postgresql-jsonb-a-complete-guide-to-storing-and-querying-json-data]]
