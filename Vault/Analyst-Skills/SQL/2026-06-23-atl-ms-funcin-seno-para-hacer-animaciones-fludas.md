---
title: ATL más Función Seno para hacer animaciones fluídas.
date: '2026-06-23'
source: https://dev.to/abrazos_programacion/atl-mas-funcion-seno-para-hacer-animaciones-fluidas-2k9h
domain: SQL
relevance: 🟡
tags:
- '#python'
- '#sql'
- '#tool'
related:
- '[[2026-06-02-rompiendo-la-cuarta-pared-en-renpy-el-efecto-monika-y-la-esfera-matemtica-parte-1]]'
- '[[2026-05-06-de-la-grilla-a-la-pantalla-cmo-centrar-y-alinear-sprites-con-aritmtica-bsica]]'
- '[[2026-05-13-de-tabla-web-a-pandas-dataframe-en-30-segundos]]'
- '[[2026-03-12-cmo-validar-nif-nie-cif-e-iban-en-python]]'
- '[[2026-06-15-pooling-contra-una-t3micro-el-da-que-se-reventrds-proxy-es-la-salida]]'
- '[[2026-05-11-cmo-constru-un-morning-briefing-con-ia-que-se-ejecuta-solo-cada-maana]]'
status: unread
---

> **TL;DR:** # 1. Mantenemos el transform del "Baile de los Números" init python : import math def efecto_holograma_avanzado ( trans , st , at ): # Movimiento vertical usando enteros para cuidar la GPU trans . yoffset = int ( math .…

## What’s new and why it matters
# 1. Mantenemos el transform del "Baile de los Números" init python : import math def efecto_holograma_avanzado ( trans , st , at ): # Movimiento vertical usando enteros para cuidar la GPU trans . yoffset = int ( math . sin ( st * 2.5 ) * 12 ) # Parpadeo de luz con desfase de velocidad (4.0) seno_luz = math . sin ( st * 4.0 ) opacidad_limpia = ( seno_luz + 1.0 ) / 2.0 trans . alpha = 0.4 + ( opacidad_limpia * 0.6 ) return 0 transform baile_holograma : function efecto_holograma_avanzado # 2. Aquí va la lógica de 3 colores (segmentar_en_doble_gradiente) init python : # Función auxiliar para conv…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Write the query in a scratchpad and run EXPLAIN/QUERY PLAN to verify performance.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/abrazos_programacion/atl-mas-funcion-seno-para-hacer-animaciones-fluidas-2k9h

## Related notes
- [[2026-06-02-rompiendo-la-cuarta-pared-en-renpy-el-efecto-monika-y-la-esfera-matemtica-parte-1]]
- [[2026-05-06-de-la-grilla-a-la-pantalla-cmo-centrar-y-alinear-sprites-con-aritmtica-bsica]]
- [[2026-05-13-de-tabla-web-a-pandas-dataframe-en-30-segundos]]
- [[2026-03-12-cmo-validar-nif-nie-cif-e-iban-en-python]]
- [[2026-06-15-pooling-contra-una-t3micro-el-da-que-se-reventrds-proxy-es-la-salida]]
- [[2026-05-11-cmo-constru-un-morning-briefing-con-ia-que-se-ejecuta-solo-cada-maana]]
