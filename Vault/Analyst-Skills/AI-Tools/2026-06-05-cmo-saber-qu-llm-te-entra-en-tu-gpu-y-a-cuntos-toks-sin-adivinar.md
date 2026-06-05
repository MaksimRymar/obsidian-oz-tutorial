---
title: Cómo saber qué LLM te entra en tu GPU (y a cuántos tok/s) sin adivinar
date: '2026-06-05'
source: https://dev.to/jonimatiin/como-saber-que-llm-te-entra-en-tu-gpu-y-a-cuantos-toks-sin-adivinar-171
domain: AI-Tools
relevance: 🔴
tags:
- '#ai'
- '#feature'
- '#sql'
- '#tool'
related:
- '[[2026-05-11-cmo-constru-un-morning-briefing-con-ia-que-se-ejecuta-solo-cada-maana]]'
- '[[2026-03-12-cmo-validar-nif-nie-cif-e-iban-en-python]]'
- '[[2026-03-24-multi-tenancy-real-con-fastapi-y-postgresql-planes-cuotas-y-aislamiento-de-datos]]'
- '[[2026-05-06-de-la-idea-al-pxel-cmo-implementar-el-acotamiento-de-cmara-usando-min-y-max-en-python]]'
- '[[2026-06-02-rompiendo-la-cuarta-pared-en-renpy-el-efecto-monika-y-la-esfera-matemtica-parte-1]]'
- '[[2026-05-13-de-tabla-web-a-pandas-dataframe-en-30-segundos]]'
status: unread
---

> **TL;DR:** monté InferBench , una app de escritorio open source que, con un click, descarga el motor, baja el modelo, lo arranca con la config óptima para tu hardware y **mide de verdad TTFT, tok/s, VRAM y calidad. Sin Docker, sin…

## What’s new and why it matters
monté InferBench , una app de escritorio open source que, con un click, descarga el motor, baja el modelo, lo arranca con la config óptima para tu hardware y **mide de verdad TTFT, tok/s, VRAM y calidad. Sin Docker, sin CLI, 100% local. El problema: demasiadas variables Correr un LLM en local suena fácil hasta que te enfrentas a la matriz real: Qué modelo (Llama, Qwen, Gemma, Mistral, Phi…). Qué cuantización (Q4_K_M, Q5_K_M, Q8_0, IQ2…). Cada una pesa distinto y degrada distinto. Qué motor (llama.cpp, Ollama, vLLM, SGLang, TGI). Cada uno con sus flags. Tu hardware (¿cuánta VRAM libre tienes de…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Reproduce the example in a notebook; then refactor into a reusable function.
- Add a short note: what changed in your workflow?

## Relevance
🔴

## Source
https://dev.to/jonimatiin/como-saber-que-llm-te-entra-en-tu-gpu-y-a-cuantos-toks-sin-adivinar-171

## Related notes
- [[2026-05-11-cmo-constru-un-morning-briefing-con-ia-que-se-ejecuta-solo-cada-maana]]
- [[2026-03-12-cmo-validar-nif-nie-cif-e-iban-en-python]]
- [[2026-03-24-multi-tenancy-real-con-fastapi-y-postgresql-planes-cuotas-y-aislamiento-de-datos]]
- [[2026-05-06-de-la-idea-al-pxel-cmo-implementar-el-acotamiento-de-cmara-usando-min-y-max-en-python]]
- [[2026-06-02-rompiendo-la-cuarta-pared-en-renpy-el-efecto-monika-y-la-esfera-matemtica-parte-1]]
- [[2026-05-13-de-tabla-web-a-pandas-dataframe-en-30-segundos]]
