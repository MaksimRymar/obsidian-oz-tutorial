---
title: Pooling contra una t3.micro, el día que se reventó...RDS Proxy es la salida?
date: '2026-06-15'
source: https://dev.to/aws-builders/pooling-contra-una-t3micro-el-dia-que-se-reventords-proxy-es-la-salida-46nn
domain: SQL
relevance: 🟡
tags:
- '#ai'
- '#best-practice'
- '#python'
- '#sql'
- '#support-analytics'
- '#tool'
related:
- '[[2026-03-09-ajuste-de-rendimiento-en-postgresql-lo-que-aprend-optimizando-consultas-en-una-base-de-datos-de-10tb]]'
- '[[2026-03-12-cmo-validar-nif-nie-cif-e-iban-en-python]]'
- '[[2026-05-11-cmo-constru-un-morning-briefing-con-ia-que-se-ejecuta-solo-cada-maana]]'
- '[[2026-05-13-de-tabla-web-a-pandas-dataframe-en-30-segundos]]'
- '[[2026-03-03-retro-imprimiendo-y-ii]]'
- '[[2026-05-06-de-la-idea-al-pxel-cmo-implementar-el-acotamiento-de-cmara-usando-min-y-max-en-python]]'
status: unread
---

> **TL;DR:** Cómo un backend de FastAPI + asyncpg comparte un solo Postgres chiquito con sus propios trabajadores en segundo plano y un segundo servicio, por qué el techo de conexiones, no el CPU, es lo que de verdad le pone tope a n…

## What’s new and why it matters
Cómo un backend de FastAPI + asyncpg comparte un solo Postgres chiquito con sus propios trabajadores en segundo plano y un segundo servicio, por qué el techo de conexiones, no el CPU, es lo que de verdad le pone tope a nuestro autoescalado, la caída en el cambio de hora que nos enseñó la cuenta, y una mirada honesta a RDS Proxy como la válvula de escape (incluyendo la trampa de asyncpg que lo puede dejar sin hacer nada). TL;DR Ajuste Valor Por qué Driver postgresql+asyncpg asíncrono hasta el fondo pool_size / max_overflow 8 / 12 (20 por proceso) subido desde 3/5 después de una caída pool_pre_p…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Write the query in a scratchpad and run EXPLAIN/QUERY PLAN to verify performance.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/aws-builders/pooling-contra-una-t3micro-el-dia-que-se-reventords-proxy-es-la-salida-46nn

## Related notes
- [[2026-03-09-ajuste-de-rendimiento-en-postgresql-lo-que-aprend-optimizando-consultas-en-una-base-de-datos-de-10tb]]
- [[2026-03-12-cmo-validar-nif-nie-cif-e-iban-en-python]]
- [[2026-05-11-cmo-constru-un-morning-briefing-con-ia-que-se-ejecuta-solo-cada-maana]]
- [[2026-05-13-de-tabla-web-a-pandas-dataframe-en-30-segundos]]
- [[2026-03-03-retro-imprimiendo-y-ii]]
- [[2026-05-06-de-la-idea-al-pxel-cmo-implementar-el-acotamiento-de-cmara-usando-min-y-max-en-python]]
