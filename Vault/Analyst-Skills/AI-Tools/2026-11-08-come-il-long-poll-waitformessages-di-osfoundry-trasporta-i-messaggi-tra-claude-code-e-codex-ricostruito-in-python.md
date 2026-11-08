---
title: Come il long-poll wait_for_messages di osFoundry trasporta i messaggi tra Claude
  Code e Codex, ricostruito in Python
date: '2026-11-08'
source: https://dev.to/bbt-it/come-il-long-poll-waitformessages-di-osfoundry-trasporta-i-messaggi-tra-claude-code-e-codex-3lhc
domain: AI-Tools
relevance: 🟡
tags:
- '#ai'
- '#best-practice'
- '#career'
- '#python'
- '#sql'
- '#tool'
related:
- '[[2026-10-11-come-scalare-agenti-ai-locali-a-costo-api-zero-guida-architetturale-con-fastapi-llamaindex-e-chromadb]]'
- '[[2026-10-11-localllm-agent-toolkit-guida-architetturale-per-distribuire-agenti-ai-autonomi-in-produzione-a-costo-api-zero]]'
- '[[2026-05-19-come-estrarre-una-singola-tabella-da-un-file-dump-mysql]]'
- '[[2026-10-11-how-to-build-a-production-ready-local-ai-agent-with-zero-api-costs-fastapi-chromadb-e-llamaindex]]'
- '[[2026-09-12-sviluppare-oreste-ai-cosa-sto-imparando-creando-un-assistente-vocale-italiano]]'
- '[[2026-10-11-costruire-un-agente-ai-locale-production-ready-a-costo-api-zero-architettura-tecnica-e-strategia-di-content-marketing-su]]'
status: unread
---

> **TL;DR:** Questo è l'intero lato di ricezione della rete di agenti di osFoundry , così come lo dichiara il suo endpoint MCP pubblico. L'output viene da tools/list su https://api.osfoundry.io/api/v1/external-mcp , che risponde senz…

## What’s new and why it matters
Questo è l'intero lato di ricezione della rete di agenti di osFoundry , così come lo dichiara il suo endpoint MCP pubblico. L'output viene da tools/list su https://api.osfoundry.io/api/v1/external-mcp , che risponde senza token: wait_for_messages: required= [] readOnly=True openWorld=False scope= [ 'osfoundry:read' ] { "after_sequence" : { "type" : "integer" , "minimum" : 0 }, "timeout_s" : { "type" : "integer" , "minimum" : 0 , "maximum" : 50 }, "limit" : { "type" : "integer" , "minimum" : 1 , "maximum" : 50 }} send_agent_message: required= [ 'to' , 'body' , 'idempotency_key' ] readOnly=False…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Reproduce the example in a notebook; then refactor into a reusable function.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/bbt-it/come-il-long-poll-waitformessages-di-osfoundry-trasporta-i-messaggi-tra-claude-code-e-codex-3lhc

## Related notes
- [[2026-10-11-come-scalare-agenti-ai-locali-a-costo-api-zero-guida-architetturale-con-fastapi-llamaindex-e-chromadb]]
- [[2026-10-11-localllm-agent-toolkit-guida-architetturale-per-distribuire-agenti-ai-autonomi-in-produzione-a-costo-api-zero]]
- [[2026-05-19-come-estrarre-una-singola-tabella-da-un-file-dump-mysql]]
- [[2026-10-11-how-to-build-a-production-ready-local-ai-agent-with-zero-api-costs-fastapi-chromadb-e-llamaindex]]
- [[2026-09-12-sviluppare-oreste-ai-cosa-sto-imparando-creando-un-assistente-vocale-italiano]]
- [[2026-10-11-costruire-un-agente-ai-locale-production-ready-a-costo-api-zero-architettura-tecnica-e-strategia-di-content-marketing-su]]
