---
title: Why the same face doesn't score 1.0 – lessons from building a face-similarity
  search in Python
date: '2026-10-19'
source: https://dev.to/narehate78/why-the-same-face-doesnt-score-10-lessons-from-building-a-face-similarity-search-in-python-4ah3
domain: AI-Tools
relevance: 🔴
tags:
- '#ai'
- '#feature'
- '#python'
- '#sql'
- '#tool'
related:
- '[[2026-09-24-my-alert-fired-7-times-across-1963-pairs-i-assumed-the-thresholds-were-too-high-they-were-and-it-didnt-matter]]'
- '[[2026-09-01-i-raced-six-models-against-each-other-on-digitalocean-inference-the-cheapest-one-won]]'
- '[[2026-08-21-how-to-find-duplicate-rows-in-sql-and-decide-what-counts-as-one]]'
- '[[2026-10-15-see-every-google-ad-a-competitor-runs-from-just-their-domain-curl-python-n8n]]'
- '[[2026-04-22-your-pytest-retries-are-lying-to-you-the-hidden-cost-of---reruns-and-the-plugin-i-wrote-so-i-could-actually-see-what-my-]]'
- '[[2026-10-05-how-to-get-a-transcript-of-any-spotify-podcast-episode-3-ways-with-and-without-code]]'
status: unread
---

> **TL;DR:** I built FaceMatch as a portfolio project: you give it a photo, pick a face, and it ranks the followers or following of an Instagram profile by how similar their profile pictures (and optionally their recent posts) look t…

## What’s new and why it matters
I built FaceMatch as a portfolio project: you give it a photo, pick a face, and it ranks the followers or following of an Instagram profile by how similar their profile pictures (and optionally their recent posts) look to that face. Before anything else: a similarity score is not proof of identity. The tool ranks visual similarity, nothing more. I'll come back to the privacy side at the end. Repo: github.com/Eight7Six/insta-facematch How it works Detect all faces in the target image (RetinaFace, with MTCNN and OpenCV as fallbacks) and let the user click the one to search for. Compute a 512-dim…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Reproduce the example in a notebook; then refactor into a reusable function.
- Add a short note: what changed in your workflow?

## Relevance
🔴

## Source
https://dev.to/narehate78/why-the-same-face-doesnt-score-10-lessons-from-building-a-face-similarity-search-in-python-4ah3

## Related notes
- [[2026-09-24-my-alert-fired-7-times-across-1963-pairs-i-assumed-the-thresholds-were-too-high-they-were-and-it-didnt-matter]]
- [[2026-09-01-i-raced-six-models-against-each-other-on-digitalocean-inference-the-cheapest-one-won]]
- [[2026-08-21-how-to-find-duplicate-rows-in-sql-and-decide-what-counts-as-one]]
- [[2026-10-15-see-every-google-ad-a-competitor-runs-from-just-their-domain-curl-python-n8n]]
- [[2026-04-22-your-pytest-retries-are-lying-to-you-the-hidden-cost-of---reruns-and-the-plugin-i-wrote-so-i-could-actually-see-what-my-]]
- [[2026-10-05-how-to-get-a-transcript-of-any-spotify-podcast-episode-3-ways-with-and-without-code]]
