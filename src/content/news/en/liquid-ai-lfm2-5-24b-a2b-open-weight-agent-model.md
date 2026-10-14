---
title: "Liquid AI releases LFM2.5-24B-A2B, an open-weight reasoning model with 2B active parameters built for on-device agents"
summary: "On 13 October 2026 Liquid AI published LFM2.5-24B-A2B, a 24B-parameter mixture-of-experts reasoning model that activates about 2B parameters per token, with a 131K-token context. Liquid reports it leads three larger open models on five of eight agentic benchmarks but trails them on coding and knowledge tests. All benchmark figures are Liquid's own."
seoTitle: "Liquid AI LFM2.5-24B-A2B: 24B model, 2B active"
seoDescription: "Liquid AI released open-weight LFM2.5-24B-A2B on 13 Oct 2026: 24B parameters, about 2B active, 131K context; benchmarks are Liquid's own."
lang: en
publishedAt: 2026-10-14T06:45:00Z
entities:
  - Liquid AI
  - LFM2.5-24B-A2B
  - Hugging Face
  - Qwen3.6-35B-A3B
  - Gemma-4-26B-A4B
  - Nemotron-3.5-Lightning
topics:
  - Models
  - Open weights
  - Edge
translationKey: liquid-ai-lfm2-5-24b-a2b-open-weight-agent-model
image: /images/news/liquid-ai-lfm2-5-24b-a2b-open-weight-agent-model-2026-10-13.jpg
imageAlt: "Deyron Labs graphic: Liquid AI releases LFM2.5-24B-A2B, 24B parameters with about 2B active and 131K context; it leads on tool-use benchmarks but trails on coding; figures are Liquid's own"
sources:
  - title: "Run fast, private agents on-device with LFM2.5-24B-A2B"
    url: "https://huggingface.co/blog/LiquidAI/lfm25-24b-a2b"
    publisher: "Liquid AI (Hugging Face blog)"
    primary: true
  - title: "LiquidAI/LFM2.5-24B-A2B model card"
    url: "https://huggingface.co/LiquidAI/LFM2.5-24B-A2B"
    publisher: "Liquid AI (Hugging Face)"
    primary: true
---

## What happened

On 13 October 2026 Liquid AI published LFM2.5-24B-A2B on Hugging Face, together with a base checkpoint, LFM2.5-24B-A2B-Base. It is a reasoning-only model: it writes out a chain of thought before its final answer. Liquid describes it as built for fast, private agents that run on a user's own device, and calls the weights open.

It follows Liquid's d1 decision models, which we covered on 9 October, but is a different and much larger model aimed at agent workloads.

## Key details

All figures below are Liquid's, from its blog post and model card. We have not run the model.

- **Size and design:** 24B total parameters with about 2B active per token (the model card lists 2.45B). It uses a mixture of experts with 64 experts per block and top-4 routing, 40 layers mixing short-convolution and grouped-query attention blocks, and a 128K-token vocabulary.
- **Context:** 131K tokens, up from 32K in the earlier LFM2-24B-A2B.
- **Training:** pre-training scaled to about 33T tokens, with mid-training adding 2T tokens at 32K context and 300B tokens at 131K context.
- **Benchmarks (Liquid's comparison with Qwen3.6-35B-A3B, Gemma-4-26B-A4B-it and Nemotron-3.5-Lightning):** Liquid says the model leads or matches on five of eight tool-use and agentic benchmarks. It reports 27.69 on AutomationBench (next best 8.72), 65.01 on BFCLv4 (Qwen3.6: 65.00), 80.71 on ToolSandbox and 96.75 on IFEval.
- **Where it trails:** Qwen3.6-35B-A3B scores higher on GPQA Diamond (83.69 vs 74.42), SWE-Bench Verified with OpenCode (66.20 vs 51.00), WebArena Verified (37.62 vs 26.75) and PinchBench (89.93 vs 83.18). The model card says it is not recommended for knowledge-heavy tasks on its own and suggests pairing it with retrieval or web search.
- **Speed (Liquid's measurements):** 184 tokens/s on an Apple M5 Max, 114 tokens/s on a Ryzen AI Max+ 395, and over 21K output tokens/s at high concurrency on one NVIDIA B300.
- **Availability:** weights on Hugging Face; supported by llama.cpp, MLX, vLLM, SGLang and ONNX; text-only. The model card lists the license as "lfm1.0". We did not read its terms, so we cannot say what commercial use it allows.

## Why it matters

Small active-parameter models are what make local agents practical, because speed and memory use depend on the active parameters rather than the 24B total. If Liquid's numbers hold, this one targets the tool-calling steps of an agent rather than hard coding or knowledge questions, where its own table shows larger models ahead.

Treat the comparison with caution: the benchmarks were run and chosen by Liquid, and an independent evaluation has not appeared yet. Anyone planning to build on it should read the lfm1.0 license first.

> Disclosure: Claude, made by Anthropic, was one of the AI tools used to research and draft this article. Figures are Liquid AI's own, taken from its 13 October 2026 blog post and model card.
