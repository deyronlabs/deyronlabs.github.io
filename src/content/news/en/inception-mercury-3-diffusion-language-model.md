---
title: "Inception launches Mercury 3, a diffusion language model it says runs at over 1,000 tokens per second"
summary: "Inception Labs says Mercury 3 generates 1,068 tokens per second on NVIDIA GPUs and is on par or better on quality than GPT-6 Luna and Claude Haiku 5.5. It costs $0.20 per million input and $0.70 per million output tokens, with a 1M-token context window."
seoTitle: "Inception Mercury 3: 1,068 tokens per second"
seoDescription: "Inception Labs' diffusion-based Mercury 3, announced 19 October 2026, claims 1,068 tokens per second at $0.20 per million input tokens."
lang: en
publishedAt: 2026-10-20T17:30:00Z
entities:
  - Inception Labs
  - Mercury 3
  - GPT-6 Luna
  - Claude Haiku 5.5
  - OpenRouter
  - Baseten
  - Vercel
topics:
  - Models
  - Pricing
  - Research
translationKey: inception-mercury-3
image: /images/news/inception-mercury-3-diffusion-llm-2026-10-19.jpg
imageAlt: "Deyron Labs graphic: Inception Mercury 3 reaches 1,068 tokens per second on NVIDIA GPUs, costs $0.20 per million input tokens and offers a 1M-token context window"
sources:
  - title: "Diffusion at Scale: Introducing Mercury 3"
    url: "https://www.inceptionlabs.ai/blog/introducing-mercury-3"
    publisher: "Inception Labs"
    primary: true
  - title: "TLDR AI, 20 October 2026 (newsletter, secondary)"
    url: "https://tldr.tech/ai"
    publisher: "TLDR"
    primary: false
---

## What happened

Inception Labs published "Diffusion at Scale: Introducing Mercury 3" on 19 October 2026. Mercury is a family of language models that generate text with diffusion rather than one token at a time, and Inception says Mercury 3 is on par or better on quality than GPT-6 Luna and Claude Haiku 5.5 while being 4 to 8 times faster at "1,000+ tokens per second".

## Key details

- **Speed (Inception):** 1,068 tokens per second on NVIDIA GPUs.
- **Quality (Inception):** the post describes Mercury 3 as "on par or better" than GPT-6 Luna and Claude Haiku 5.5. The benchmark scores appear only in an image in the announcement, not in its text, so we do not quote them.
- **Price:** $0.20 per million input tokens and $0.70 per million output tokens. A launch promotion of 50% off brings that to $0.10 and $0.35. Cached input tokens are 90% cheaper than the input price.
- **Context window:** 1M tokens, up from 260K for Mercury 2.5.
- **Availability:** Inception's API platform, OpenRouter, Baseten and Vercel; the API is OpenAI-compatible and the platform offers 100 million free tokens. Enterprise options include dedicated capacity, autoscaling, compliance controls and configurable data retention.
- **Not stated:** the announcement does not publish model size, weights or an independent evaluation.

## Why it matters

Latency is the main cost of long agent loops and voice or coding tools, and a model that returns text several times faster than comparable small models changes what is practical to build interactively. The comparison is Inception's own, made against smaller models from OpenAI and Anthropic rather than their largest ones, and the supporting numbers are in an image, so developers should test Mercury 3 on their own tasks before relying on the quality claim. The OpenAI-compatible API and the free-token allowance make that test cheap.

> Disclosure: Claude, made by Anthropic, was one of the AI tools used to research and draft this article. Claude Haiku 5.5 is an Anthropic model and is named here only because Inception's announcement compares against it. Prices and figures are Inception's own and were read from its announcement on 20 October 2026.
