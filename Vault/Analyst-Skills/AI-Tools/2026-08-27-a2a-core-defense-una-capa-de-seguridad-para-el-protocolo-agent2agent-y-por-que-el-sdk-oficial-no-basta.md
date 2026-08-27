---
title: 'A2A Core Defense: una capa de seguridad para el protocolo Agent2Agent (y por
  que el SDK oficial no basta)'
date: '2026-08-27'
source: https://dev.to/magopredator/a2a-core-defense-una-capa-de-seguridad-para-el-protocolo-agent2agent-y-por-que-el-sdk-oficial-no-58kc
domain: AI-Tools
relevance: 🔴
tags:
- '#ai'
- '#python'
- '#sql'
- '#tool'
related:
- '[[2026-03-12-cmo-validar-nif-nie-cif-e-iban-en-python]]'
- '[[2026-07-05-agentes-que-se-auto-corrigen-text-to-sql-con-smolagents-hugging-face]]'
- '[[2026-07-06-cmo-hablar-con-tu-base-de-datos-usando-ia-y-construir-un-extractor-sql-seguro-con-streamlit]]'
- '[[2026-05-11-cmo-constru-un-morning-briefing-con-ia-que-se-ejecuta-solo-cada-maana]]'
- '[[2026-06-15-pooling-contra-una-t3micro-el-da-que-se-reventrds-proxy-es-la-salida]]'
- '[[2026-07-07-fastapi-valida-emails-por-entorno-preview]]'
status: unread
---

> **TL;DR:** El gap que nadie había cerrado El ecosistema Agent2Agent (A2A) está explotando en 2025-2026. Los agentes ya no se hablan solo con un LLM: se coordinan entre sí, delegan tareas, disparan pagos (AP2 de Google) y suscriben…

## What’s new and why it matters
El gap que nadie había cerrado El ecosistema Agent2Agent (A2A) está explotando en 2025-2026. Los agentes ya no se hablan solo con un LLM: se coordinan entre sí, delegan tareas, disparan pagos (AP2 de Google) y suscriben webhooks de notificación. Pero el SDK de referencia oficial, a2aproject/a2a-python , tiene huecos de seguridad abiertos y confirmados por el propio mantenedor . El más claro: issue #786 (OPEN). El servidor pasa la URL de PushNotificationConfig directo a httpx.post() sin validar nada. Un cliente malicioso puede registrar un webhook que apunte a la metadata cloud interna ( 169.25…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Reproduce the example in a notebook; then refactor into a reusable function.
- Add a short note: what changed in your workflow?

## Relevance
🔴

## Source
https://dev.to/magopredator/a2a-core-defense-una-capa-de-seguridad-para-el-protocolo-agent2agent-y-por-que-el-sdk-oficial-no-58kc

## Related notes
- [[2026-03-12-cmo-validar-nif-nie-cif-e-iban-en-python]]
- [[2026-07-05-agentes-que-se-auto-corrigen-text-to-sql-con-smolagents-hugging-face]]
- [[2026-07-06-cmo-hablar-con-tu-base-de-datos-usando-ia-y-construir-un-extractor-sql-seguro-con-streamlit]]
- [[2026-05-11-cmo-constru-un-morning-briefing-con-ia-que-se-ejecuta-solo-cada-maana]]
- [[2026-06-15-pooling-contra-una-t3micro-el-da-que-se-reventrds-proxy-es-la-salida]]
- [[2026-07-07-fastapi-valida-emails-por-entorno-preview]]
