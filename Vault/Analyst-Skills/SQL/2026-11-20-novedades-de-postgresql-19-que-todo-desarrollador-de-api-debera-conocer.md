---
title: Novedades de PostgreSQL 19 que todo desarrollador de API debería conocer
date: '2026-11-20'
source: https://dev.to/roobia/novedades-de-postgresql-19-que-todo-desarrollador-de-api-deberia-conocer-32ln
domain: SQL
relevance: 🟡
tags:
- '#ai'
- '#feature'
- '#sql'
- '#tool'
- '#tutorial'
related:
- '[[2026-07-06-cmo-hablar-con-tu-base-de-datos-usando-ia-y-construir-un-extractor-sql-seguro-con-streamlit]]'
- '[[2026-09-21-fastapi-pruebas-de-api-que-sobreviven-al-reintento]]'
- '[[2026-07-05-agentes-que-se-auto-corrigen-text-to-sql-con-smolagents-hugging-face]]'
- '[[2026-07-03-vanna-ai-el-estndar-de-la-industria-para-text-to-sql]]'
- '[[2026-06-15-pooling-contra-una-t3micro-el-da-que-se-reventrds-proxy-es-la-salida]]'
- '[[2026-07-15-fastapi-rastrea-correos-duplicados-con-run-ids]]'
status: unread
---

> **TL;DR:** Las nuevas funciones de PostgreSQL 19 que más importan a los desarrolladores de API: INSERT ... ON CONFLICT DO SELECT para endpoints de get-or-create en una sola instrucción, WAIT FOR LSN para read-your-writes en réplica…

## What’s new and why it matters
Las nuevas funciones de PostgreSQL 19 que más importan a los desarrolladores de API: INSERT ... ON CONFLICT DO SELECT para endpoints de get-or-create en una sola instrucción, WAIT FOR LSN para read-your-writes en réplicas, REPACK (CONCURRENTLY) para limpiar la fragmentación en línea, salida JSON desde COPY , nuevos métodos de cadena en jsonpath y verificaciones de claves foráneas más rápidas en inserciones masivas. Prueba Apidog hoy Esta guía cubre qué cambia en tus handlers, réplicas y plan de actualización. Todos los ejemplos de sintaxis provienen de las notas de la versión de PostgreSQL 19…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Write the query in a scratchpad and run EXPLAIN/QUERY PLAN to verify performance.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/roobia/novedades-de-postgresql-19-que-todo-desarrollador-de-api-deberia-conocer-32ln

## Related notes
- [[2026-07-06-cmo-hablar-con-tu-base-de-datos-usando-ia-y-construir-un-extractor-sql-seguro-con-streamlit]]
- [[2026-09-21-fastapi-pruebas-de-api-que-sobreviven-al-reintento]]
- [[2026-07-05-agentes-que-se-auto-corrigen-text-to-sql-con-smolagents-hugging-face]]
- [[2026-07-03-vanna-ai-el-estndar-de-la-industria-para-text-to-sql]]
- [[2026-06-15-pooling-contra-una-t3micro-el-da-que-se-reventrds-proxy-es-la-salida]]
- [[2026-07-15-fastapi-rastrea-correos-duplicados-con-run-ids]]
