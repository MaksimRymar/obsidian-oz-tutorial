---
title: De "se cayó la VM" a "estamos de vuelta"
date: '2026-10-04'
source: https://dev.to/kevin_hinojosa/de-se-cayo-la-vm-a-estamos-de-vuelta-2noi
domain: SQL
relevance: 🟡
tags:
- '#ai'
- '#python'
- '#sql'
- '#tool'
related:
- '[[2026-07-05-agentes-que-se-auto-corrigen-text-to-sql-con-smolagents-hugging-face]]'
- '[[2026-09-21-fastapi-pruebas-de-api-que-sobreviven-al-reintento]]'
- '[[2026-03-12-cmo-validar-nif-nie-cif-e-iban-en-python]]'
- '[[2026-10-02-cmo-automatizar-facturas-pdf-con-python-gua-prctica-para-ahorrar-horas-de-trabajo-manual]]'
- '[[2026-03-24-multi-tenancy-real-con-fastapi-y-postgresql-planes-cuotas-y-aislamiento-de-datos]]'
- '[[2026-08-28-cmo-solucionar-el-error-de-permisos-al-ejecutar-pipexe-en-entorno-virtual-python-310-en-windows]]'
status: unread
---

> **TL;DR:** Diseñando backups y recuperación para un framework de pruebas SQL en Azure 1. Introducción: pensar en el desastre antes de que ocurra Ningún equipo planea perder datos, pero todos deberían planear la recuperación. Dos mé…

## What’s new and why it matters
Diseñando backups y recuperación para un framework de pruebas SQL en Azure 1. Introducción: pensar en el desastre antes de que ocurra Ningún equipo planea perder datos, pero todos deberían planear la recuperación. Dos métricas ordenan la conversación: RPO: la pérdida máxima de datos tolerable. RTO: el tiempo máximo aceptable para recuperar el servicio. Estos valores se acuerdan con quien usa el sistema. Para nuestro prototipo los tratamos como objetivos de diseño por definir y validar , no como cifras medidas. El caso de estudio es un Framework de Pruebas SQL en FastAPI que ejecuta casos contr…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Write the query in a scratchpad and run EXPLAIN/QUERY PLAN to verify performance.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/kevin_hinojosa/de-se-cayo-la-vm-a-estamos-de-vuelta-2noi

## Related notes
- [[2026-07-05-agentes-que-se-auto-corrigen-text-to-sql-con-smolagents-hugging-face]]
- [[2026-09-21-fastapi-pruebas-de-api-que-sobreviven-al-reintento]]
- [[2026-03-12-cmo-validar-nif-nie-cif-e-iban-en-python]]
- [[2026-10-02-cmo-automatizar-facturas-pdf-con-python-gua-prctica-para-ahorrar-horas-de-trabajo-manual]]
- [[2026-03-24-multi-tenancy-real-con-fastapi-y-postgresql-planes-cuotas-y-aislamiento-de-datos]]
- [[2026-08-28-cmo-solucionar-el-error-de-permisos-al-ejecutar-pipexe-en-entorno-virtual-python-310-en-windows]]
