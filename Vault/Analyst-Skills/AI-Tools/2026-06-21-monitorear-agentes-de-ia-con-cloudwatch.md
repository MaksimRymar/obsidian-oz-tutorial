---
title: Monitorear agentes de IA con CloudWatch
date: '2026-06-21'
source: https://dev.to/aws-builders/monitorear-agentes-de-ia-con-cloudwatch-45c4
domain: AI-Tools
relevance: 🟡
tags:
- '#ai'
- '#best-practice'
- '#python'
- '#sql'
- '#tool'
related:
- '[[2026-06-15-pooling-contra-una-t3micro-el-da-que-se-reventrds-proxy-es-la-salida]]'
- '[[2026-03-12-cmo-validar-nif-nie-cif-e-iban-en-python]]'
- '[[2026-03-09-ajuste-de-rendimiento-en-postgresql-lo-que-aprend-optimizando-consultas-en-una-base-de-datos-de-10tb]]'
- '[[2026-05-11-cmo-constru-un-morning-briefing-con-ia-que-se-ejecuta-solo-cada-maana]]'
- '[[2026-03-03-retro-imprimiendo-y-ii]]'
- '[[2026-05-13-de-tabla-web-a-pandas-dataframe-en-30-segundos]]'
status: unread
---

> **TL;DR:** Las dos ideas que hicieron el trabajo: Los modos de falla ya son líneas de log. Conviértelos en métricas con MetricFilter , no con código. Las dimensiones por agente/por modelo necesitan EMF , no PutMetricData , escribes…

## What’s new and why it matters
Las dos ideas que hicieron el trabajo: Los modos de falla ya son líneas de log. Conviértelos en métricas con MetricFilter , no con código. Las dimensiones por agente/por modelo necesitan EMF , no PutMetricData , escribes una línea JSON y CloudWatch extrae la métrica. El punto de partida: una fila en la base de datos no es telemetría Cada llamada de agente escribía una fila: # 00-starting-point/usage_log.py (abreviado) row = AgentUsageLog ( agent_name = self . name , # "summarizer", "classifier", ... model_used = result . model_used , input_tokens = result . input_tokens , output_tokens = resul…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Reproduce the example in a notebook; then refactor into a reusable function.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/aws-builders/monitorear-agentes-de-ia-con-cloudwatch-45c4

## Related notes
- [[2026-06-15-pooling-contra-una-t3micro-el-da-que-se-reventrds-proxy-es-la-salida]]
- [[2026-03-12-cmo-validar-nif-nie-cif-e-iban-en-python]]
- [[2026-03-09-ajuste-de-rendimiento-en-postgresql-lo-que-aprend-optimizando-consultas-en-una-base-de-datos-de-10tb]]
- [[2026-05-11-cmo-constru-un-morning-briefing-con-ia-que-se-ejecuta-solo-cada-maana]]
- [[2026-03-03-retro-imprimiendo-y-ii]]
- [[2026-05-13-de-tabla-web-a-pandas-dataframe-en-30-segundos]]
