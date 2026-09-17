---
title: 'Project memory is not chat history: a tiny handoff layer for AI agents'
date: '2026-09-17'
source: https://dev.to/louisen0o0/project-memory-is-not-chat-history-a-tiny-handoff-layer-for-ai-agents-2n03
domain: AI-Tools
relevance: 🟡
tags:
- '#ai'
- '#career'
- '#python'
- '#tool'
related:
- '[[2026-05-15-stop-passing-entire-chat-histories-to-ai-agents]]'
- '[[2026-09-02-from-local-docker-stack-to-a-working-rag-api-with-ollama-qdrant-and-mistral]]'
- '[[2026-08-22-how-i-built-memory-for-a-local-ai-companion-without-sending-chats-to-a-server]]'
- '[[2026-06-01-how-i-built-a-zero-token-memory-layer-for-llms-and-why-it-outperforms-vector-store-approaches]]'
- '[[2026-03-28-soul-engine]]'
- '[[2026-04-03-cathedral-gemma-4-persistent-agent-identity-no-cloud-required]]'
status: unread
---

> **TL;DR:** I kept running into the same failure mode when switching between AI workers, browser sessions, or machines: the files were still there, but the exact working point was gone. Conversation memory can tell a model what was…

## What’s new and why it matters
I kept running into the same failure mode when switching between AI workers, browser sessions, or machines: the files were still there, but the exact working point was gone. Conversation memory can tell a model what was said. RAG can retrieve relevant documents. Neither one is a durable answer to four operational questions: What is true now ? Why is that state trusted? What is already complete and should not be repeated? What should happen next? I built Resume the Scene as a very small, model-agnostic project-memory layer for that gap. GitHub: https://github.com/louisen0o0/resume-the-scene The…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Reproduce the example in a notebook; then refactor into a reusable function.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/louisen0o0/project-memory-is-not-chat-history-a-tiny-handoff-layer-for-ai-agents-2n03

## Related notes
- [[2026-05-15-stop-passing-entire-chat-histories-to-ai-agents]]
- [[2026-09-02-from-local-docker-stack-to-a-working-rag-api-with-ollama-qdrant-and-mistral]]
- [[2026-08-22-how-i-built-memory-for-a-local-ai-companion-without-sending-chats-to-a-server]]
- [[2026-06-01-how-i-built-a-zero-token-memory-layer-for-llms-and-why-it-outperforms-vector-store-approaches]]
- [[2026-03-28-soul-engine]]
- [[2026-04-03-cathedral-gemma-4-persistent-agent-identity-no-cloud-required]]
