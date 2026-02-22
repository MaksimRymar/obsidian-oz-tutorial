---
title: Diagramas de banco sempre ficam desatualizados. Parei de tentar “manter” e
  passei a gerar.
date: '2026-02-21'
source: https://dev.to/thiago_rosadasilva_0688/diagramas-de-banco-sempre-ficam-desatualizados-parei-de-tentar-manter-e-passei-a-gerar-44nl
domain: SQL
relevance: 🟡
tags:
- '#sql'
related:
- '[[2026-02-22-medir-no-es-comprender]]'
status: unread
---

> **TL;DR:** Diagramas de banco sempre ficam desatualizados. Parei de tentar “manter” e passei a gerar. A maioria dos times começa com diagramas bonitos e bem pensados. Alguns meses depois, eles viram referência histórica (quando não…

## What’s new and why it matters
Diagramas de banco sempre ficam desatualizados. Parei de tentar “manter” e passei a gerar. A maioria dos times começa com diagramas bonitos e bem pensados. Alguns meses depois, eles viram referência histórica (quando não são ignorados por completo). O problema não é falta de ferramenta nem falta de boa vontade. É que diagramas mantidos manualmente não escalam com migrations, hotfixes e mudanças constantes. Depois de passar por isso algumas vezes, mudei a abordagem: em vez de “manter” diagramas, passei a gerá-los diretamente a partir do schema, tratando o banco como fonte única de verdade. Isso…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Write the query in a scratchpad and run EXPLAIN/QUERY PLAN to verify performance.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/thiago_rosadasilva_0688/diagramas-de-banco-sempre-ficam-desatualizados-parei-de-tentar-manter-e-passei-a-gerar-44nl

## Related notes
- [[2026-02-22-medir-no-es-comprender]]
