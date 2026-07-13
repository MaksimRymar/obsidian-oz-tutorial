---
title: 'Mi INSERT tardaba 25 minutos y no era culpa de los datos: construyendo un
  Data Warehouse de e-commerce con PostgreSQL'
date: '2026-07-12'
source: https://dev.to/dnarram/mi-insert-tardaba-25-minutos-y-no-era-culpa-de-los-datos-construyendo-un-data-warehouse-de-4e14
domain: SQL
relevance: 🟡
tags:
- '#ai'
- '#sql'
- '#tool'
related:
- '[[2026-07-05-agentes-que-se-auto-corrigen-text-to-sql-con-smolagents-hugging-face]]'
- '[[2026-05-11-cmo-constru-un-morning-briefing-con-ia-que-se-ejecuta-solo-cada-maana]]'
- '[[2026-07-03-vanna-ai-el-estndar-de-la-industria-para-text-to-sql]]'
- '[[2026-03-09-ajuste-de-rendimiento-en-postgresql-lo-que-aprend-optimizando-consultas-en-una-base-de-datos-de-10tb]]'
- '[[2026-03-12-cmo-validar-nif-nie-cif-e-iban-en-python]]'
- '[[2026-06-15-pooling-contra-una-t3micro-el-da-que-se-reventrds-proxy-es-la-salida]]'
status: unread
---

> **TL;DR:** Cargar 112.647 filas en una tabla de hechos debería tardar segundos. A mí me tardaba más de 25 minutos, y acababa cancelando la query. Los datos estaban bien, el SQL estaba bien, las dimensiones se poblaban sin problema.…

## What’s new and why it matters
Cargar 112.647 filas en una tabla de hechos debería tardar segundos. A mí me tardaba más de 25 minutos, y acababa cancelando la query. Los datos estaban bien, el SQL estaba bien, las dimensiones se poblaban sin problema. El culpable era otro, y descubrirlo fue la parte más instructiva de todo el proyecto. Todo esto surgió construyendo un Data Warehouse en estrella sobre datos reales de e-commerce: no una tabla bonita para hacer un SELECT * , sino un modelo dimensional completo, reproducible desde cero, capaz de responder preguntas de negocio de verdad. El dataset Trabajé con el Brazilian E-Com…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Write the query in a scratchpad and run EXPLAIN/QUERY PLAN to verify performance.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/dnarram/mi-insert-tardaba-25-minutos-y-no-era-culpa-de-los-datos-construyendo-un-data-warehouse-de-4e14

## Related notes
- [[2026-07-05-agentes-que-se-auto-corrigen-text-to-sql-con-smolagents-hugging-face]]
- [[2026-05-11-cmo-constru-un-morning-briefing-con-ia-que-se-ejecuta-solo-cada-maana]]
- [[2026-07-03-vanna-ai-el-estndar-de-la-industria-para-text-to-sql]]
- [[2026-03-09-ajuste-de-rendimiento-en-postgresql-lo-que-aprend-optimizando-consultas-en-una-base-de-datos-de-10tb]]
- [[2026-03-12-cmo-validar-nif-nie-cif-e-iban-en-python]]
- [[2026-06-15-pooling-contra-una-t3micro-el-da-que-se-reventrds-proxy-es-la-salida]]
