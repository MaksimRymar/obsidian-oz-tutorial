---
title: 'FastAPI: rastrea correos duplicados con run IDs'
date: '2026-07-15'
source: https://dev.to/silviutech/fastapi-rastrea-correos-duplicados-con-run-ids-eec
domain: AI-Tools
relevance: 🟡
tags:
- '#ai'
- '#python'
- '#support-analytics'
related:
- '[[2026-07-07-fastapi-valida-emails-por-entorno-preview]]'
- '[[2026-05-11-cmo-constru-un-morning-briefing-con-ia-que-se-ejecuta-solo-cada-maana]]'
- '[[2026-07-05-agentes-que-se-auto-corrigen-text-to-sql-con-smolagents-hugging-face]]'
- '[[2026-07-04-cmo-conversar-con-tu-base-de-datos-usando-ia-un-generador-de-sql-a-partir-de-lenguaje-natural]]'
- '[[2026-06-15-pooling-contra-una-t3micro-el-da-que-se-reventrds-proxy-es-la-salida]]'
- '[[2026-03-12-cmo-validar-nif-nie-cif-e-iban-en-python]]'
status: unread
---

> **TL;DR:** En varios equipos de backend he visto el mismo bug con distinto disfraz: el endpoint responde bien, el usuario recibe su email, pero a veces recibe dos. O tres. En FastAPI suele pasar cuando mezclamos reintentos del prov…

## What’s new and why it matters
En varios equipos de backend he visto el mismo bug con distinto disfraz: el endpoint responde bien, el usuario recibe su email, pero a veces recibe dos. O tres. En FastAPI suele pasar cuando mezclamos reintentos del proveedor, BackgroundTasks , workers y poca trazabilidad entre eventos. El sistema "funciona", pero nadie sabe con claridad qué corrida generó cada mensaje, y ahí empieza el dolor. La mejora que más me ha servido no fue cambiar de proveedor ni meter una cola enorme. Fue mucho más simple: asignar un run_id por flujo de negocio y arrastrarlo desde la API hasta el correo enviado. Pare…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Reproduce the example in a notebook; then refactor into a reusable function.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/silviutech/fastapi-rastrea-correos-duplicados-con-run-ids-eec

## Related notes
- [[2026-07-07-fastapi-valida-emails-por-entorno-preview]]
- [[2026-05-11-cmo-constru-un-morning-briefing-con-ia-que-se-ejecuta-solo-cada-maana]]
- [[2026-07-05-agentes-que-se-auto-corrigen-text-to-sql-con-smolagents-hugging-face]]
- [[2026-07-04-cmo-conversar-con-tu-base-de-datos-usando-ia-un-generador-de-sql-a-partir-de-lenguaje-natural]]
- [[2026-06-15-pooling-contra-una-t3micro-el-da-que-se-reventrds-proxy-es-la-salida]]
- [[2026-03-12-cmo-validar-nif-nie-cif-e-iban-en-python]]
