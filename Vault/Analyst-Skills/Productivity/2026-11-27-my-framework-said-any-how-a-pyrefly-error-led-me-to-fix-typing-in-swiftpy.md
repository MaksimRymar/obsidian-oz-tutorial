---
title: 'My Framework Said Any: How a Pyrefly Error Led Me to Fix Typing in SwiftPY'
date: '2026-11-27'
source: https://dev.to/obrainwave/my-framework-said-any-how-a-pyrefly-error-led-me-to-fix-typing-in-swiftpy-36oo
domain: Productivity
relevance: 🟡
tags:
- '#feature'
- '#library'
- '#productivity'
- '#python'
- '#tool'
related:
- '[[2026-11-17-my-checks-would-have-said-all-passed-two-of-them-were-never-counted]]'
- '[[2026-09-04-i-built-an-offline-document-indexer-and-ollama-taught-me-two-things-i-did-not-expect]]'
- '[[2026-04-26-i-got-tired-of-setting-up-fastapi-projects-manually-so-i-built-a-cli-to-do-it-for-me]]'
- '[[2026-10-15-on-windows-four-processes-appending-to-one-file-lost-37-of-200-lines]]'
- '[[2026-05-20-learning-sql-as-if-you-built-it-yourself]]'
- '[[2026-04-02-how-to-stop-your-ai-agent-from-burning-400month-on-api-calls]]'
status: unread
---

> **TL;DR:** I build SwiftPY , a Python web framework with an async Active Record ORM. Last week I opened one of my own repositories in VS Code and saw this: class DocRepository : model = Doc async def get_doc ( self , doc_id : int )…

## What’s new and why it matters
I build SwiftPY , a Python web framework with an async Active Record ORM. Last week I opened one of my own repositories in VS Code and saw this: class DocRepository : model = Doc async def get_doc ( self , doc_id : int ) -> Doc : doc = await self . model . where ( "is_active" , True ) . with_ ( "group" ) . where ( "id" , doc_id ) . first ( ) if not doc : raise NotFoundError ( "Doc not found" ) return doc Returning implicit Any from function declared to return "Doc" Pyrefly[no-any-return-implicit] (variable) doc: Unknown Every method in the file was red. The code ran fine and the tests passed,…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/obrainwave/my-framework-said-any-how-a-pyrefly-error-led-me-to-fix-typing-in-swiftpy-36oo

## Related notes
- [[2026-11-17-my-checks-would-have-said-all-passed-two-of-them-were-never-counted]]
- [[2026-09-04-i-built-an-offline-document-indexer-and-ollama-taught-me-two-things-i-did-not-expect]]
- [[2026-04-26-i-got-tired-of-setting-up-fastapi-projects-manually-so-i-built-a-cli-to-do-it-for-me]]
- [[2026-10-15-on-windows-four-processes-appending-to-one-file-lost-37-of-200-lines]]
- [[2026-05-20-learning-sql-as-if-you-built-it-yourself]]
- [[2026-04-02-how-to-stop-your-ai-agent-from-burning-400month-on-api-calls]]
