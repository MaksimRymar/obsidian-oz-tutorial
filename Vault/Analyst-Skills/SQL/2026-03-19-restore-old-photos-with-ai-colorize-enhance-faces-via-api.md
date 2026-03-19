---
title: 'Restore Old Photos with AI: Colorize + Enhance Faces via API'
date: '2026-03-19'
source: https://dev.to/aiengine/restore-old-photos-with-ai-colorize-enhance-faces-via-api-3fmf
domain: SQL
relevance: 🟡
tags:
- '#feature'
- '#python'
- '#sql'
- '#tool'
- '#tutorial'
related:
- '[[2026-03-14-how-to-swap-faces-in-images-with-an-ai-api]]'
- '[[2026-03-14-a-developers-guide-to-image-colorization-apis]]'
- '[[2026-03-17-5-python-scripts-that-automate-your-freelance-workflow-with-ai]]'
- '[[2026-03-02-python-automation-12-scripts-that-save-hours-every-week]]'
- '[[2026-02-22-a-beginners-guide-to-making-data-web-applications-using-python-with-streamlit]]'
- '[[2026-03-08-build-a-website-tech-stack-scanner-in-python-under-50-lines]]'
status: unread
---

> **TL;DR:** Old family photos fade and lose detail over time. Restoring them used to require hours of Photoshop work. With two AI APIs, you can automate the entire process: colorize a black and white photo, then enhance the faces. T…

## What’s new and why it matters
Old family photos fade and lose detail over time. Restoring them used to require hours of Photoshop work. With two AI APIs, you can automate the entire process: colorize a black and white photo, then enhance the faces. The Pipeline Colorize : send the B&W photo to the Image Colorization API Enhance faces : pass the colorized result to the Face Restoration API Download : save the final restored image The second API call uses the output URL from the first step directly. No need to download and re-upload. Python Code import requests from pathlib import Path API_KEY = " YOUR_API_KEY " COLORIZE_URL…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Write the query in a scratchpad and run EXPLAIN/QUERY PLAN to verify performance.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/aiengine/restore-old-photos-with-ai-colorize-enhance-faces-via-api-3fmf

## Related notes
- [[2026-03-14-how-to-swap-faces-in-images-with-an-ai-api]]
- [[2026-03-14-a-developers-guide-to-image-colorization-apis]]
- [[2026-03-17-5-python-scripts-that-automate-your-freelance-workflow-with-ai]]
- [[2026-03-02-python-automation-12-scripts-that-save-hours-every-week]]
- [[2026-02-22-a-beginners-guide-to-making-data-web-applications-using-python-with-streamlit]]
- [[2026-03-08-build-a-website-tech-stack-scanner-in-python-under-50-lines]]
