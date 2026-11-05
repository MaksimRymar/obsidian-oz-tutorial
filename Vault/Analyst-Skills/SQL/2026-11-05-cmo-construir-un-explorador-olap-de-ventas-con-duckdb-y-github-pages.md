---
title: Cómo construir un explorador OLAP de ventas con DuckDB y GitHub Pages
date: '2026-11-05'
source: https://dev.to/mariela_estefanyramoslo/como-construir-un-explorador-olap-de-ventas-con-duckdb-y-github-pages-56a3
domain: SQL
relevance: 🟡
tags:
- '#python'
- '#sql'
related:
- '[[2026-11-01-constru-un-panel-olap-con-duckdb-que-consulta-datos-en-el-navegador]]'
- '[[2026-10-02-cmo-automatizar-facturas-pdf-con-python-gua-prctica-para-ahorrar-horas-de-trabajo-manual]]'
- '[[2026-03-12-cmo-validar-nif-nie-cif-e-iban-en-python]]'
- '[[2026-05-11-cmo-constru-un-morning-briefing-con-ia-que-se-ejecuta-solo-cada-maana]]'
- '[[2026-09-21-fastapi-pruebas-de-api-que-sobreviven-al-reintento]]'
- '[[2026-10-04-de-git-push-a-produccin-sin-sorpresas-sast-con-bandit-en-un-pipeline-de-github-actions]]'
status: unread
---

> **TL;DR:** Mariela Estefany Ramos Loza Este proyecto permite comparar las ventas de distintas regiones y categorías sin descargar los pedidos individuales. DuckDB transforma 120 000 pedidos sintéticos de 2025 en 144 celdas que se p…

## What’s new and why it matters
Mariela Estefany Ramos Loza Este proyecto permite comparar las ventas de distintas regiones y categorías sin descargar los pedidos individuales. DuckDB transforma 120 000 pedidos sintéticos de 2025 en 144 celdas que se pueden consultar desde un explorador web. Diseñar el cubo La unidad de análisis es un pedido de una sola categoría. Las dimensiones son mes, región y categoría. Cada celda guarda tres medidas aditivas: cantidad de pedidos, unidades vendidas e ingresos en centavos de dólar. Con 12 meses, 4 regiones y 3 categorías, se generan 144 combinaciones. select month , region , category , c…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Write the query in a scratchpad and run EXPLAIN/QUERY PLAN to verify performance.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/mariela_estefanyramoslo/como-construir-un-explorador-olap-de-ventas-con-duckdb-y-github-pages-56a3

## Related notes
- [[2026-11-01-constru-un-panel-olap-con-duckdb-que-consulta-datos-en-el-navegador]]
- [[2026-10-02-cmo-automatizar-facturas-pdf-con-python-gua-prctica-para-ahorrar-horas-de-trabajo-manual]]
- [[2026-03-12-cmo-validar-nif-nie-cif-e-iban-en-python]]
- [[2026-05-11-cmo-constru-un-morning-briefing-con-ia-que-se-ejecuta-solo-cada-maana]]
- [[2026-09-21-fastapi-pruebas-de-api-que-sobreviven-al-reintento]]
- [[2026-10-04-de-git-push-a-produccin-sin-sorpresas-sast-con-bandit-en-un-pipeline-de-github-actions]]
