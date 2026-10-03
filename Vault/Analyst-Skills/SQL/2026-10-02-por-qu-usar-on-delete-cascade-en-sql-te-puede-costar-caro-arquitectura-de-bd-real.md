---
title: Por qué usar ON DELETE CASCADE en SQL te puede costar caro (Arquitectura de
  BD real)
date: '2026-10-02'
source: https://dev.to/sergio_leal/por-que-usar-on-delete-cascade-en-sql-te-puede-costar-caro-arquitectura-de-bd-real-574h
domain: SQL
relevance: 🟡
tags:
- '#sql'
- '#tool'
- '#tutorial'
related:
- '[[2026-05-11-cmo-constru-un-morning-briefing-con-ia-que-se-ejecuta-solo-cada-maana]]'
- '[[2026-07-12-mi-insert-tardaba-25-minutos-y-no-era-culpa-de-los-datos-construyendo-un-data-warehouse-de-e-commerce-con-postgresql]]'
- '[[2026-08-06-prediccin-de-riesgo-crediticio-por-qu-eleg-xgboost-para-construir-smartcredit-ml]]'
- '[[2026-07-04-cmo-conversar-con-tu-base-de-datos-usando-ia-un-generador-de-sql-a-partir-de-lenguaje-natural]]'
- '[[2026-09-16-plataforma-gratuita-para-practicar-sql-en-espaol]]'
- '[[2026-07-29-del-navegador-a-la-base-de-datos-el-camino-ms-corto-para-tablas-web]]'
status: unread
---

> **TL;DR:** Veo muchos tutoriales que enseñan a armar tablas relacionales usando INT AUTO_INCREMENT y borrados en cascada. En un proyecto de universidad está bien, pero en un sistema transaccional real (como un e-commerce o una app…

## What’s new and why it matters
Veo muchos tutoriales que enseñan a armar tablas relacionales usando INT AUTO_INCREMENT y borrados en cascada. En un proyecto de universidad está bien, pero en un sistema transaccional real (como un e-commerce o una app de delivery), hacer eso destruye la contabilidad o expone tus métricas de ventas a la competencia. 1. El error de los identificadores: INT vs UUID Si usas INT AUTO_INCREMENT en una tabla de Pedidos, expones métricas de negocio. Si un competidor hace un pedido hoy y su ID es 100, y mañana hace otro y su ID es 150, sabrá exactamente cuántos pedidos procesaste. Solución: Usa UUID…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Write the query in a scratchpad and run EXPLAIN/QUERY PLAN to verify performance.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/sergio_leal/por-que-usar-on-delete-cascade-en-sql-te-puede-costar-caro-arquitectura-de-bd-real-574h

## Related notes
- [[2026-05-11-cmo-constru-un-morning-briefing-con-ia-que-se-ejecuta-solo-cada-maana]]
- [[2026-07-12-mi-insert-tardaba-25-minutos-y-no-era-culpa-de-los-datos-construyendo-un-data-warehouse-de-e-commerce-con-postgresql]]
- [[2026-08-06-prediccin-de-riesgo-crediticio-por-qu-eleg-xgboost-para-construir-smartcredit-ml]]
- [[2026-07-04-cmo-conversar-con-tu-base-de-datos-usando-ia-un-generador-de-sql-a-partir-de-lenguaje-natural]]
- [[2026-09-16-plataforma-gratuita-para-practicar-sql-en-espaol]]
- [[2026-07-29-del-navegador-a-la-base-de-datos-el-camino-ms-corto-para-tablas-web]]
