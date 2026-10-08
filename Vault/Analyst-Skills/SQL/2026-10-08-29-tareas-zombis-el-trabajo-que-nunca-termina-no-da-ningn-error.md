---
title: '29 tareas zombis: el trabajo que nunca termina no da ningún error'
date: '2026-10-08'
source: https://dev.to/isazajuancarlos/29-tareas-zombis-el-trabajo-que-nunca-termina-no-da-ningun-error-2594
domain: SQL
relevance: 🟡
tags:
- '#sql'
related:
- '[[2026-07-05-agentes-que-se-auto-corrigen-text-to-sql-con-smolagents-hugging-face]]'
- '[[2026-05-11-cmo-constru-un-morning-briefing-con-ia-que-se-ejecuta-solo-cada-maana]]'
- '[[2026-06-15-pooling-contra-una-t3micro-el-da-que-se-reventrds-proxy-es-la-salida]]'
- '[[2026-10-07-apagu-el-bot-cinco-estrategias-77000-velas-y-cero-ventaja-neta-de-comisiones]]'
- '[[2026-09-21-fastapi-pruebas-de-api-que-sobreviven-al-reintento]]'
- '[[2026-07-30-fastapi-alias-efimeros-para-signup]]'
status: unread
---

> **TL;DR:** Un orquestador de escaneos llevaba 29 tareas en estado «ejecutándose» desde hacía días. Ningún error en el registro, ningún proceso vivo detrás, ninguna alarma. Nadie se enteró, y la razón es la que hace que esta clase d…

## What’s new and why it matters
Un orquestador de escaneos llevaba 29 tareas en estado «ejecutándose» desde hacía días. Ningún error en el registro, ningún proceso vivo detrás, ninguna alarma. Nadie se enteró, y la razón es la que hace que esta clase de defecto sobreviva tanto tiempo: una tarea colgada y una tarea lenta se ven exactamente igual. El estado que miente El diseño es el habitual. Al empezar una tarea se escribe una fila con estado running . Al terminar, se actualiza a completed o a failed . El fallo está en lo que no se escribió: qué pasa si el proceso muere entre las dos escrituras. Si el trabajador cae, si lo m…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Write the query in a scratchpad and run EXPLAIN/QUERY PLAN to verify performance.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/isazajuancarlos/29-tareas-zombis-el-trabajo-que-nunca-termina-no-da-ningun-error-2594

## Related notes
- [[2026-07-05-agentes-que-se-auto-corrigen-text-to-sql-con-smolagents-hugging-face]]
- [[2026-05-11-cmo-constru-un-morning-briefing-con-ia-que-se-ejecuta-solo-cada-maana]]
- [[2026-06-15-pooling-contra-una-t3micro-el-da-que-se-reventrds-proxy-es-la-salida]]
- [[2026-10-07-apagu-el-bot-cinco-estrategias-77000-velas-y-cero-ventaja-neta-de-comisiones]]
- [[2026-09-21-fastapi-pruebas-de-api-que-sobreviven-al-reintento]]
- [[2026-07-30-fastapi-alias-efimeros-para-signup]]
