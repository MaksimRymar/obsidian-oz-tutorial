---
title: Qué envía Claude Code cuando propone una app a un Room de osFoundry
date: '2026-11-12'
source: https://dev.to/bbt-es/que-envia-claude-code-cuando-propone-una-app-a-un-room-de-osfoundry-3g5m
domain: AI-Tools
relevance: 🔴
tags:
- '#ai'
- '#python'
- '#sql'
- '#support-analytics'
- '#tool'
- '#zendesk'
related:
- '[[2026-09-21-fastapi-pruebas-de-api-que-sobreviven-al-reintento]]'
- '[[2026-07-05-agentes-que-se-auto-corrigen-text-to-sql-con-smolagents-hugging-face]]'
- '[[2026-10-02-cmo-automatizar-facturas-pdf-con-python-gua-prctica-para-ahorrar-horas-de-trabajo-manual]]'
- '[[2026-03-12-cmo-validar-nif-nie-cif-e-iban-en-python]]'
- '[[2026-06-15-pooling-contra-una-t3micro-el-da-que-se-reventrds-proxy-es-la-salida]]'
- '[[2026-11-03-fastapi-un-lease-para-emails-de-verificacin]]'
status: unread
---

> **TL;DR:** Esta es la herramienta que Claude Code llama para meter una app pequeña en un Room en la nube de osFoundry , tal como la lista el servidor en producción en tools/list (obtenida sin token y recortada a lo que importa): {…

## What’s new and why it matters
Esta es la herramienta que Claude Code llama para meter una app pequeña en un Room en la nube de osFoundry , tal como la lista el servidor en producción en tools/list (obtenida sin token y recortada a lo que importa): { "name" : "propose_room_snippet_app" , "description" : "Prepare a Room snippet with source files. It appears in the cloud Room launcher only after its owner reviews and approves the full code in osFoundry." , "inputSchema" : { "type" : "object" , "properties" : { "room_id" : { "type" : "string" } , "name" : { "type" : "string" , "maxLength" : 200 } , "files" : { "type" : "object…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Reproduce the example in a notebook; then refactor into a reusable function.
- Add a short note: what changed in your workflow?

## Relevance
🔴

## Source
https://dev.to/bbt-es/que-envia-claude-code-cuando-propone-una-app-a-un-room-de-osfoundry-3g5m

## Related notes
- [[2026-09-21-fastapi-pruebas-de-api-que-sobreviven-al-reintento]]
- [[2026-07-05-agentes-que-se-auto-corrigen-text-to-sql-con-smolagents-hugging-face]]
- [[2026-10-02-cmo-automatizar-facturas-pdf-con-python-gua-prctica-para-ahorrar-horas-de-trabajo-manual]]
- [[2026-03-12-cmo-validar-nif-nie-cif-e-iban-en-python]]
- [[2026-06-15-pooling-contra-una-t3micro-el-da-que-se-reventrds-proxy-es-la-salida]]
- [[2026-11-03-fastapi-un-lease-para-emails-de-verificacin]]
