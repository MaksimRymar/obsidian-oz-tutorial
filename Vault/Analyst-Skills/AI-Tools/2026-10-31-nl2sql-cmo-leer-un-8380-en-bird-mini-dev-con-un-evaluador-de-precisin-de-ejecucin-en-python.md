---
title: 'NL2SQL: cómo leer un 83,80 en BIRD Mini-Dev con un evaluador de precisión
  de ejecución en Python'
date: '2026-10-31'
source: https://dev.to/_0e3192755d4df45b92/nl2sql-como-leer-un-8380-en-bird-mini-dev-con-un-evaluador-de-precision-de-ejecucion-en-python-2e78
domain: AI-Tools
relevance: 🟡
tags:
- '#ai'
- '#python'
- '#sql'
- '#support-analytics'
- '#tool'
related:
- '[[2026-07-05-agentes-que-se-auto-corrigen-text-to-sql-con-smolagents-hugging-face]]'
- '[[2026-07-04-cmo-conversar-con-tu-base-de-datos-usando-ia-un-generador-de-sql-a-partir-de-lenguaje-natural]]'
- '[[2026-07-05-cmo-construir-un-agente-de-ia-que-habla-con-tu-base-de-datos-sql-con-smolagents-de-hugging-face]]'
- '[[2026-07-06-cmo-hablar-con-tu-base-de-datos-usando-ia-y-construir-un-extractor-sql-seguro-con-streamlit]]'
- '[[2026-07-05-sql-seguro-con-ia-cmo-construir-un-asistente-que-valida-las-consultas-antes-de-ejecutarlas]]'
- '[[2026-10-08-29-tareas-zombis-el-trabajo-que-nunca-termina-no-da-ningn-error]]'
status: unread
---

> **TL;DR:** TL;DR BIRD Mini-Dev es un benchmark pequeño de texto a SQL (NL2SQL): 500 preguntas sobre bases de datos reales. La métrica es la precisión de ejecución (EX) : una consulta es correcta si, al ejecutarla, devuelve el mismo…

## What’s new and why it matters
TL;DR BIRD Mini-Dev es un benchmark pequeño de texto a SQL (NL2SQL): 500 preguntas sobre bases de datos reales. La métrica es la precisión de ejecución (EX) : una consulta es correcta si, al ejecutarla, devuelve el mismo conjunto de filas que la consulta de referencia. El 29 de octubre de 2026 medimos Darwin-180B-NL2SQL , un sistema de VIDRAFT, sobre la edición revisada del 28 de octubre: 83,80 % (419 de 500) en SQLite. Es una cifra autorreportada , no una puntuación recalculada por BIRD. Lo primero, aunque incomode: en la misma edición, la tabla oficial de líneas base (un solo prompt fijo por…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Reproduce the example in a notebook; then refactor into a reusable function.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/_0e3192755d4df45b92/nl2sql-como-leer-un-8380-en-bird-mini-dev-con-un-evaluador-de-precision-de-ejecucion-en-python-2e78

## Related notes
- [[2026-07-05-agentes-que-se-auto-corrigen-text-to-sql-con-smolagents-hugging-face]]
- [[2026-07-04-cmo-conversar-con-tu-base-de-datos-usando-ia-un-generador-de-sql-a-partir-de-lenguaje-natural]]
- [[2026-07-05-cmo-construir-un-agente-de-ia-que-habla-con-tu-base-de-datos-sql-con-smolagents-de-hugging-face]]
- [[2026-07-06-cmo-hablar-con-tu-base-de-datos-usando-ia-y-construir-un-extractor-sql-seguro-con-streamlit]]
- [[2026-07-05-sql-seguro-con-ia-cmo-construir-un-asistente-que-valida-las-consultas-antes-de-ejecutarlas]]
- [[2026-10-08-29-tareas-zombis-el-trabajo-que-nunca-termina-no-da-ningn-error]]
