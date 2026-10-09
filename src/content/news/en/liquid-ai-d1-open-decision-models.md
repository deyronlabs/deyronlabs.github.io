---
title: "Liquid AI releases d1-3B and d1-omni-600M, open-weight decision models that answer in a single forward pass"
summary: "On 7 October 2026 Liquid AI released two open-weight decision models on Hugging Face: d1-3B (text and image) and d1-omni-600M, an experimental checkpoint (text with image or audio). Liquid says they produce an answer in a single forward pass, with d1-3B answering in under 50 ms on every measured device. Benchmarks are Liquid's own."
seoTitle: "Liquid AI d1 open models decide in one pass"
seoDescription: "On 7 October 2026 Liquid AI released two open-weight decision models on Hugging Face: d1-3B (text and image) and d1-omni-600M, an experimental…"
lang: en
publishedAt: 2026-10-09T05:30:00Z
entities:
  - Liquid AI
  - d1-3B
  - d1-omni-600M
  - Hugging Face
topics:
  - Models
  - Open weights
  - Edge
translationKey: liquid-ai-d1-open-decision-models
image: /images/news/liquid-ai-d1-open-decision-models-2026-10-09.jpg
imageAlt: "Deyron Labs graphic: Liquid AI releases open-weight decision models d1-3B and d1-omni-600M that answer in one forward pass; benchmarks are Liquid's own"
sources:
  - title: "Open d1: edge decision models for text, vision, and audio"
    url: "https://www.liquid.ai/blog/d1-open"
    publisher: "Liquid AI"
    primary: true
---

## What happened

On 7 October 2026, Liquid AI published "Open d1: edge decision models for text, vision, and audio", releasing two decision models on Hugging Face. Unlike its generative models, Liquid says they "don't produce tokens" and "produce an answer in a single forward pass". Both have day-one llama.cpp support, according to the post.

## Key details

All figures below are Liquid AI's own.

- **d1-3B:** trained from LFM2.5-VL-3B, accepts text and image inputs.
- **d1-omni-600M:** trained from LFM2.5-Encoder-350M, accepts text with image or text with audio, and is called "our first experimental checkpoint".
- **Decision Index v0.2.1 (public split):** d1-3B scores 48.57, which Liquid says is "ahead of every model under 10B and on par with Decider 35B-A3B". d1-omni-600M scores 15.95.
- **Text benchmarks (mean of seven tasks):** d1-3B 82.9 versus 81.1 for Decider 4B; d1-omni-600M 78.4 versus 77.1 for Decider 2B, at about a quarter of the parameters.
- **Latency for d1-3B (single question):** 8 ms on an RTX 4090, 16 ms on a Jetson AGX Thor, 26 ms on a Jetson AGX Orin and 50 ms on a Jetson Orin Nano.
- **License:** the post calls the models open-weight and says users can download, fine-tune and deploy them "without restrictions". It does not name a license, so check the model cards.

## Why it matters

Decision models target tasks where an application needs a choice or a label, such as routing or classification, rather than free text. Latencies of tens of milliseconds on edge hardware make that practical for devices without a data-center GPU.

The "Decision Index" and the "Decider" comparison models belong to Liquid's own evaluation, and we found no independent results. The 600M model is explicitly experimental.

> Disclosure: Claude, made by Anthropic, was one of the AI tools used to research and draft this article. Claims and benchmarks are Liquid AI's own.
