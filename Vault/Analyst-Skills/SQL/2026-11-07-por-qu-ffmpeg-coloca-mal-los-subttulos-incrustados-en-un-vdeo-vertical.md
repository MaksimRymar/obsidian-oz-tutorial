---
title: ¿Por qué ffmpeg coloca mal los subtítulos incrustados en un vídeo vertical?
date: '2026-11-07'
source: https://dev.to/bestaitools-es/por-que-ffmpeg-coloca-mal-los-subtitulos-incrustados-en-un-video-vertical-17i6
domain: SQL
relevance: 🟡
tags:
- '#ai'
- '#feature'
- '#python'
- '#sql'
- '#tool'
related:
- '[[2026-10-02-por-qu-usar-on-delete-cascade-en-sql-te-puede-costar-caro-arquitectura-de-bd-real]]'
- '[[2026-10-08-29-tareas-zombis-el-trabajo-que-nunca-termina-no-da-ningn-error]]'
- '[[2026-06-15-pooling-contra-una-t3micro-el-da-que-se-reventrds-proxy-es-la-salida]]'
- '[[2026-03-03-retro-imprimiendo-y-ii]]'
- '[[2026-07-29-del-navegador-a-la-base-de-datos-el-camino-ms-corto-para-tablas-web]]'
- '[[2026-10-31-nl2sql-cmo-leer-un-8380-en-bird-mini-dev-con-un-evaluador-de-precisin-de-ejecucin-en-python]]'
status: unread
---

> **TL;DR:** Incrustar subtítulos en un vídeo de 1080×1920 para TikTok o Reels suele empezar con un plan razonable: el feed tapa más o menos la quinta parte inferior del encuadre, así que el subtítulo tiene que quedar por encima. Con…

## What’s new and why it matters
Incrustar subtítulos en un vídeo de 1080×1920 para TikTok o Reels suele empezar con un plan razonable: el feed tapa más o menos la quinta parte inferior del encuadre, así que el subtítulo tiene que quedar por encima. Con el filtro subtitles de ffmpeg recurres a force_style y ajustas MarginV . Renderizas, y el subtítulo aparece en otro sitio completamente distinto, y bastante más grande de lo esperado. El motivo es que un archivo .srt no sabe nada del tamaño de tu vídeo. ffmpeg lo convierte en un script ASS con un lienzo fijo y diminuto, y cada número de force_style se interpreta en las unidade…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Write the query in a scratchpad and run EXPLAIN/QUERY PLAN to verify performance.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/bestaitools-es/por-que-ffmpeg-coloca-mal-los-subtitulos-incrustados-en-un-video-vertical-17i6

## Related notes
- [[2026-10-02-por-qu-usar-on-delete-cascade-en-sql-te-puede-costar-caro-arquitectura-de-bd-real]]
- [[2026-10-08-29-tareas-zombis-el-trabajo-que-nunca-termina-no-da-ningn-error]]
- [[2026-06-15-pooling-contra-una-t3micro-el-da-que-se-reventrds-proxy-es-la-salida]]
- [[2026-03-03-retro-imprimiendo-y-ii]]
- [[2026-07-29-del-navegador-a-la-base-de-datos-el-camino-ms-corto-para-tablas-web]]
- [[2026-10-31-nl2sql-cmo-leer-un-8380-en-bird-mini-dev-con-un-evaluador-de-precisin-de-ejecucin-en-python]]
