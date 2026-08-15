---
title: 'Building ShikshaBharat: How I Built an AI Voice Companion for Rural Primary
  Education in 10 Days'
date: '2026-08-15'
source: https://dev.to/ishan_singh_1f625ad095134/building-shikshabharat-how-i-built-an-ai-voice-companion-for-rural-primary-education-in-10-days-12e9
domain: AI-Tools
relevance: 🟡
tags:
- '#ai'
- '#python'
- '#sql'
- '#tool'
- '#tutorial'
related:
- '[[2026-08-15-building-krishi-mitra-an-ai-voice-agent-for-indian-farmers-with-livekit-gemini-and-murf-falcon]]'
- '[[2026-07-18-im-not-a-real-developer-so-i-built-my-app-the-simplest-way-possible]]'
- '[[2026-04-04-build-your-first-ai-agent-with-langgraph-step-by-step-python-tutorial-2026]]'
- '[[2026-05-19-doubling-the-speed-of-an-already-fast-sql-parser-using-ai]]'
- '[[2026-04-27-i-built-a-pay-per-call-trading-signal-api-for-ai-agents]]'
- '[[2026-03-05-build-a-profitable-ai-agent-with-langchain-a-step-by-step-tutorial]]'
status: unread
---

> **TL;DR:** Core Agent Pipeline Setup ( backend/src/agent.py ) session = AgentSession ( stt = deepgram . STT ( model = " nova-3 " , language = " multi " ), llm = google . LLM ( model = " gemini-3.5-flash-lite " ), tts = murf . TTS (…

## What’s new and why it matters
Core Agent Pipeline Setup ( backend/src/agent.py ) session = AgentSession ( stt = deepgram . STT ( model = " nova-3 " , language = " multi " ), llm = google . LLM ( model = " gemini-3.5-flash-lite " ), tts = murf . TTS ( voice = " Anisha " , locale = " en-IN " , style = " Conversation " , tokenizer = tokenize . basic . SentenceTokenizer ( min_sentence_len = 2 ), text_pacing = True , ), turn_detection = MultilingualModel (), vad = ctx . proc . userdata [ " vad " ], preemptive_generation = True , ) Dynamic Voice & Agent Handoff Tool ( backend/src/tools.py ) async def _transfer_to_science_special…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Reproduce the example in a notebook; then refactor into a reusable function.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/ishan_singh_1f625ad095134/building-shikshabharat-how-i-built-an-ai-voice-companion-for-rural-primary-education-in-10-days-12e9

## Related notes
- [[2026-08-15-building-krishi-mitra-an-ai-voice-agent-for-indian-farmers-with-livekit-gemini-and-murf-falcon]]
- [[2026-07-18-im-not-a-real-developer-so-i-built-my-app-the-simplest-way-possible]]
- [[2026-04-04-build-your-first-ai-agent-with-langgraph-step-by-step-python-tutorial-2026]]
- [[2026-05-19-doubling-the-speed-of-an-already-fast-sql-parser-using-ai]]
- [[2026-04-27-i-built-a-pay-per-call-trading-signal-api-for-ai-agents]]
- [[2026-03-05-build-a-profitable-ai-agent-with-langchain-a-step-by-step-tutorial]]
