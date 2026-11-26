---
title: "Sand.ai launches MAGI-2, a 480B video generation model, and says open weights will follow"
summary: "Sand.ai announced MAGI-2 on 24 November 2026: a mixture-of-experts video model with about 480 billion total and 28 billion active parameters that generates up to 30 seconds of 1080p video with native audio. Open-source weights and a technical report are promised but not yet released; benchmark figures are Sand.ai's own."
seoTitle: "Sand.ai MAGI-2: 480B video model, no weights"
seoDescription: "Sand.ai's MAGI-2 is a 480B (28B active) video model with native audio, announced 24 Nov 2026; open weights and a report are promised later."
lang: en
publishedAt: 2026-11-26T07:31:00Z
entities:
  - Sand.ai
  - MAGI-2
  - MAGI-2 Preview
  - Artificial Analysis Video Arena
topics:
  - Models
  - Image generation
  - Open-weight
translationKey: sand-ai-magi-2-480b-video-model
image: /images/news/sand-ai-magi-2-480b-video-model.jpg
imageAlt: "Deyron Labs graphic: Sand.ai's MAGI-2 video model, about 480B total and 28B active parameters, up to 30 seconds of 1080p with native audio; weights promised but not yet released"
sources:
  - title: "MAGI-2: A 480B Frontier Video Generation Model"
    url: "https://sand.ai/blog/magi-2/"
    publisher: "Sand.ai, 24 November 2026, read 26 November 2026"
    primary: true
---

## What happened

On 24 November 2026 Sand.ai announced **MAGI-2**, a video generation model it describes as a 480-billion-parameter frontier model. The company's blog post says "Today, we are launching MAGI-2" and that it "will follow up soon with open-source releases and a detailed technical report". At the time we read the post (26 November 2026), no weights, license or technical report were available from that source.

## Key details

- **Size:** about 480 billion total and 28 billion active parameters (the post cites 5.8% sparsity), trained on 4 trillion tokens. The earlier MAGI-2 Preview (August 2026) is listed at about 114 billion total and 6 billion active.
- **Output:** up to 30 seconds of 1080p video at 25 fps with native audio and video, plus timeline and shot-cut control and video editing.
- **Reference inputs:** an "omni-reference" mode accepts up to 20 items per request (up to 10 images, 5 videos and 5 audio clips).
- **Reported benchmark (Sand.ai's figures):** on a four-task average of the Artificial Analysis Video Arena v2.1 (image-to-video with and without audio, text-to-video with and without audio), Sand.ai reports 1150.3 for MAGI-2 against 998.5 for the Preview, a gain of 151.8 points. It also reports a roughly 22% training speedup from its Multi-Head Latent MoE design over LatentMoE.
- **Availability:** the post links to Sand.ai's API platform but does not state that MAGI-2 is available there. Open weights are promised, with no date and no license named.

## Why it matters

A 480B open-weight video model would be among the largest publicly downloadable ones, but today the promise is the news, not the download: until weights and a license appear, builders cannot self-host it and cannot check the claims. The benchmark gain is measured against Sand.ai's own earlier model, and the figures are reported by the company, not an independent evaluator. Watch for the weights, the license terms and any independent arena results.

> Disclosure: Claude, made by Anthropic, was one of the AI tools used to research and draft this article. Sand.ai is not affiliated with Deyron Labs; all claims are Sand.ai's own.
