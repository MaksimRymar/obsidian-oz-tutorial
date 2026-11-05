---
title: 'Del ZIP al dashboard público: 1,89 millones de viajes con DuckDB y dbt'
date: '2026-11-05'
source: https://dev.to/mariela_estefanyramoslo/del-zip-al-dashboard-publico-189-millones-de-viajes-con-duckdb-y-dbt-3bek
domain: SQL
relevance: 🟡
tags:
- '#python'
- '#sql'
related:
- '[[2026-07-05-agentes-que-se-auto-corrigen-text-to-sql-con-smolagents-hugging-face]]'
- '[[2026-11-05-cmo-construir-un-explorador-olap-de-ventas-con-duckdb-y-github-pages]]'
- '[[2026-03-12-cmo-validar-nif-nie-cif-e-iban-en-python]]'
- '[[2026-10-04-de-git-push-a-produccin-sin-sorpresas-sast-con-bandit-en-un-pipeline-de-github-actions]]'
- '[[2026-07-04-cmo-conversar-con-tu-base-de-datos-usando-ia-un-generador-de-sql-a-partir-de-lenguaje-natural]]'
- '[[2026-10-31-nl2sql-cmo-leer-un-8380-en-bird-mini-dev-con-un-evaluador-de-precisin-de-ejecucin-en-python]]'
status: unread
---

> **TL;DR:** Mariela Estefany Ramos Loza Construimos un pipeline que procesa los viajes de Citi Bike de Nueva York de enero de 2024 y genera un dashboard público con las salidas por día, hora y estación. La ejecución publicada conser…

## What’s new and why it matters
Mariela Estefany Ramos Loza Construimos un pipeline que procesa los viajes de Citi Bike de Nueva York de enero de 2024 y genera un dashboard público con las salidas por día, hora y estación. La ejecución publicada conservó 1 888 085 viajes válidos . Carga con Python y DuckDB Python descarga el ZIP mensual, extrae los CSV a un directorio temporal y carga en DuckDB el identificador del viaje, las fechas de inicio y término y la estación de salida. Los campos se leen como texto para que el modelo SQL controle cómo interpretar los valores inválidos. La tabla de origen se reconstruye en cada ejecuc…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Write the query in a scratchpad and run EXPLAIN/QUERY PLAN to verify performance.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/mariela_estefanyramoslo/del-zip-al-dashboard-publico-189-millones-de-viajes-con-duckdb-y-dbt-3bek

## Related notes
- [[2026-07-05-agentes-que-se-auto-corrigen-text-to-sql-con-smolagents-hugging-face]]
- [[2026-11-05-cmo-construir-un-explorador-olap-de-ventas-con-duckdb-y-github-pages]]
- [[2026-03-12-cmo-validar-nif-nie-cif-e-iban-en-python]]
- [[2026-10-04-de-git-push-a-produccin-sin-sorpresas-sast-con-bandit-en-un-pipeline-de-github-actions]]
- [[2026-07-04-cmo-conversar-con-tu-base-de-datos-usando-ia-un-generador-de-sql-a-partir-de-lenguaje-natural]]
- [[2026-10-31-nl2sql-cmo-leer-un-8380-en-bird-mini-dev-con-un-evaluador-de-precisin-de-ejecucin-en-python]]
