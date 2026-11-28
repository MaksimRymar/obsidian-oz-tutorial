---
title: 'De un CSV a un observatorio de energía: DuckDB, SQL y GitHub Actions'
date: '2026-11-28'
source: https://dev.to/durdenxito/de-un-csv-a-un-observatorio-de-energia-duckdb-sql-y-github-actions-1lfk
domain: Python
relevance: 🟡
tags:
- '#python'
- '#sql'
related:
- '[[2026-11-14-constru-una-solucin-olap-con-duckdb-en-el-navegador-y-despliegue-automtico]]'
- '[[2026-11-17-construimos-una-solucin-olap-con-duckdb-que-puedes-explorar-desde-el-navegador]]'
- '[[2026-11-05-del-zip-al-dashboard-pblico-189-millones-de-viajes-con-duckdb-y-dbt]]'
- '[[2026-07-04-cmo-conversar-con-tu-base-de-datos-usando-ia-un-generador-de-sql-a-partir-de-lenguaje-natural]]'
- '[[2026-10-09-fastapi-contratos-para-correos-temporales-en-ci]]'
- '[[2026-09-21-fastapi-pruebas-de-api-que-sobreviven-al-reintento]]'
status: unread
---

> **TL;DR:** Introducción de la aplicación Voltio es un observatorio de datos energéticos. Permite comparar países, elegir un año y explorar generación eléctrica, participación renovable, consumo de energía por habitante e intensidad…

## What’s new and why it matters
Introducción de la aplicación Voltio es un observatorio de datos energéticos. Permite comparar países, elegir un año y explorar generación eléctrica, participación renovable, consumo de energía por habitante e intensidad de carbono. Perú aparece como país inicial y Chile como comparación. El usuario puede descargar el conjunto curado en Parquet o exportar la selección del gráfico como CSV. El repositorio público incluye el pipeline, las consultas SQL, las pruebas y los workflows. El dashboard se publica en GitHub Pages . El procesamiento ocurre antes del despliegue, dentro de GitHub Actions, y…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Reproduce the example in a notebook; then refactor into a reusable function.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/durdenxito/de-un-csv-a-un-observatorio-de-energia-duckdb-sql-y-github-actions-1lfk

## Related notes
- [[2026-11-14-constru-una-solucin-olap-con-duckdb-en-el-navegador-y-despliegue-automtico]]
- [[2026-11-17-construimos-una-solucin-olap-con-duckdb-que-puedes-explorar-desde-el-navegador]]
- [[2026-11-05-del-zip-al-dashboard-pblico-189-millones-de-viajes-con-duckdb-y-dbt]]
- [[2026-07-04-cmo-conversar-con-tu-base-de-datos-usando-ia-un-generador-de-sql-a-partir-de-lenguaje-natural]]
- [[2026-10-09-fastapi-contratos-para-correos-temporales-en-ci]]
- [[2026-09-21-fastapi-pruebas-de-api-que-sobreviven-al-reintento]]
