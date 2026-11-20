---
title: 'Quita tus 3 mejores trades: la prueba de 5 minutos que desarma un backtest'
date: '2026-11-20'
source: https://dev.to/jesusaco/quita-tus-3-mejores-trades-la-prueba-de-5-minutos-que-desarma-un-backtest-3b0a
domain: Python
relevance: 🟡
tags:
- '#ai'
- '#career'
- '#python'
related:
- '[[2026-07-04-cmo-conversar-con-tu-base-de-datos-usando-ia-un-generador-de-sql-a-partir-de-lenguaje-natural]]'
- '[[2026-05-13-de-tabla-web-a-pandas-dataframe-en-30-segundos]]'
- '[[2026-11-15-cmo-calcular-las-horas-de-luz-con-python-sin-usar-una-api]]'
- '[[2026-03-12-cmo-validar-nif-nie-cif-e-iban-en-python]]'
- '[[2026-07-05-cmo-construir-un-agente-de-ia-que-habla-con-tu-base-de-datos-sql-con-smolagents-de-hugging-face]]'
- '[[2026-07-12-detecta-si-tu-modelo-de-materiales-hace-trampa-con-la-huella-bibliogrfica]]'
status: unread
---

> **TL;DR:** En corto: antes de creerle a un backtest, borra sus 3 mejores operaciones y vuelve a calcular. Si el resultado cambia de signo, lo más probable es que no tengas una estrategia, sino tres golpes de suerte (hay una excepci…

## What’s new and why it matters
En corto: antes de creerle a un backtest, borra sus 3 mejores operaciones y vuelve a calcular. Si el resultado cambia de signo, lo más probable es que no tengas una estrategia, sino tres golpes de suerte (hay una excepción, la explico más abajo). Abajo está el código en pandas, un ejemplo que se puede reproducir y los casos en que esta prueba engaña. El problema: el promedio esconde de dónde viene la ganancia Un backtest te devuelve un número: ganancia total, profit factor, Sharpe. Lo que no te dice es cómo se reparte esa ganancia entre las operaciones. Dos estrategias pueden terminar con el m…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Reproduce the example in a notebook; then refactor into a reusable function.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/jesusaco/quita-tus-3-mejores-trades-la-prueba-de-5-minutos-que-desarma-un-backtest-3b0a

## Related notes
- [[2026-07-04-cmo-conversar-con-tu-base-de-datos-usando-ia-un-generador-de-sql-a-partir-de-lenguaje-natural]]
- [[2026-05-13-de-tabla-web-a-pandas-dataframe-en-30-segundos]]
- [[2026-11-15-cmo-calcular-las-horas-de-luz-con-python-sin-usar-una-api]]
- [[2026-03-12-cmo-validar-nif-nie-cif-e-iban-en-python]]
- [[2026-07-05-cmo-construir-un-agente-de-ia-que-habla-con-tu-base-de-datos-sql-con-smolagents-de-hugging-face]]
- [[2026-07-12-detecta-si-tu-modelo-de-materiales-hace-trampa-con-la-huella-bibliogrfica]]
