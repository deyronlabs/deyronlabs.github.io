---
title: "Liquid AI releases d1.2 and d1.2-ultra, decision models that add audio and claim first place on a decision index"
summary: "On 16 November 2026 Liquid AI released d1.2 and d1.2-ultra, decision models that add audio input and five new tasks. Liquid says d1.2-ultra scores 75 on Artificial Analysis Decision Index v2.1, two points above the previous best decision model. Both are on the Liquid API; weights and licence are not stated."
seoTitle: "Liquid AI d1.2-ultra tops Decision Index at 75"
seoDescription: "Liquid AI released d1.2 and d1.2-ultra on 16 Nov 2026; it says d1.2-ultra scores 75 on the Decision Index and both models now accept audio."
lang: en
publishedAt: 2026-11-17T06:50:00Z
entities:
  - Liquid AI
  - d1.2
  - d1.2-ultra
  - Artificial Analysis
topics:
  - Models
  - Products
translationKey: liquid-ai-d1-2-omnimodal-decision-models
image: /images/news/liquid-ai-d1-2-omnimodal-decision-models-2026-11-17.jpg
imageAlt: "Deyron Labs graphic: Liquid AI d1.2 and d1.2-ultra; omnimodal decision models; Decision Index score 75 reported by Liquid; Liquid AI blog, 16 November 2026"
sources:
  - title: "d1.2: State-of-the-Art Omnimodal Decision Models"
    url: "https://www.liquid.ai/blog/d1-2"
    publisher: "Liquid AI, 16 November 2026"
    primary: true
---

## What happened

On 16 November 2026 Liquid AI published "d1.2: State-of-the-Art Omnimodal Decision Models", releasing d1.2 and d1.2-ultra. Liquid says the models now accept audio input and add five new tasks. The post says both are available on the Liquid API now, with OpenRouter and Vercel "coming soon".

## Key details

- **Ranking claim:** Liquid says d1.2-ultra ranks first among decision models on the Artificial Analysis Decision Index v2.1 with a score of 75, two points ahead of the previous best. We have not checked the index page; this is Liquid's statement.
- **Calibration error (Liquid's table, 13 benchmarks, 22,505 questions):** d1.2-ultra 0.8, d1.2 1.2, Jev 1.14 2.7, Perplexity Decider v1.3 3.7 and GPT-6 Luna (Decisions API) 7.2.
- **New tasks:** read a value, find spans, locate boxes, estimate a number with a range, and multi-choice. On Liquid's internal tests, d1.2-ultra vs d1.2 scored 98% vs 96% on receipts, 94/93 vs 92/88 PII precision/recall, and 87% vs 90% on multi-select.
- **Audio:** Liquid reports 95% to 97% on ESC-50 and FLEURS (43 languages).
- **Pricing as written:** "$0.02 for d1.2 and $0.042 per million input tokens for d1.2-ultra"; the unit for d1.2 is not explicit in that sentence. Both models bill input tokens only, and a 1024x1024 image costs 1,536 tokens.
- **Not stated:** whether weights are released, and which licence applies.

## Why it matters

Decision models return a structured answer in one pass rather than generating text, which suits classification, extraction and routing steps inside larger agent pipelines. Adding audio and a calibration metric makes d1.2 relevant for teams that need confidence scores they can act on.

Most numbers here are Liquid's own, including comparisons against competitors' models and internal task accuracy. Treat the ranking and calibration table as claims to reproduce on your own data before switching.

> Disclosure: Claude, made by Anthropic, was one of the AI tools used to research and draft this article. Liquid AI is not affiliated with Deyron Labs; all claims are Liquid's own.
