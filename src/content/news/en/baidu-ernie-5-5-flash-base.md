---
title: "Baidu releases ERNIE 5.5 Flash Base, a 280B-parameter pre-trained MoE checkpoint, on Hugging Face"
summary: "On 5 November 2026 Baidu published ERNIE 5.5 Flash Base, a base checkpoint with no post-training: a sparse mixture-of-experts model with 280 billion total and 14 billion active parameters, trained on 33.5 trillion tokens. Weights are on Hugging Face under Baidu's own license. The benchmark scores come from Baidu's own evaluation."
seoTitle: "Baidu ERNIE 5.5 Flash Base: 280B open MoE"
seoDescription: "Baidu released ERNIE 5.5 Flash Base on 5 Nov 2026: a 280B-parameter MoE base model with 14B active, on Hugging Face under a custom license."
lang: en
publishedAt: 2026-11-06T19:36:00Z
entities:
  - Baidu
  - ERNIE 5.5 Flash Base
  - DeepSeek-V4-Flash-Base
  - MiMo-V2.5-Base
  - Hugging Face
topics:
  - Models
  - Open-weight
  - China
translationKey: baidu-ernie-5-5-flash-base
image: /images/news/baidu-ernie-5-5-flash-base-2026-11-05.jpg
imageAlt: "Deyron Labs graphic: Baidu ERNIE 5.5 Flash Base has 280B total and 14B active parameters, was trained on 33.5T tokens and is a pre-trained base checkpoint on Hugging Face"
sources:
  - title: "Introducing ERNIE 5.5 Flash Base"
    url: "https://ernie.baidu.com/release/ernie-5-5-flash-base/"
    publisher: "Baidu ERNIE Team"
    primary: true
---

## What happened

On 5 November 2026 Baidu's ERNIE team released **ERNIE 5.5 Flash Base**. It is a base checkpoint: pre-trained from scratch, with no mid-training or post-training, so it is a starting point for fine-tuning rather than a ready-made chat assistant. Baidu publishes the weights on Hugging Face in two versions, FP8 (`baidu/ERNIE-5.5-Flash-Base`) and BF16 (`baidu/ERNIE-5.5-Flash-Base-BF16`), and says the model can be served with SGLang and vLLM.

We read Baidu's release page on 6 November 2026. Figures below are Baidu's own, reported by the lab; we have not seen independent evaluations.

## Key details

- **Size:** a sparse mixture-of-experts model with 280 billion total parameters and 14 billion activated per token. It has 43 layers, 64 attention heads, 512 routed experts (top 10 per token) plus one shared expert, and a vocabulary of about 200,000.
- **Training:** 33.5 trillion tokens, with the Muon optimizer and FP8 mixed precision. Context is up to 128K tokens in training and 1 million tokens for fine-tuning and inference, according to Baidu.
- **License:** the “ERNIE 5.5 Flash Base Model License Agreement v1.0”, a custom license, not Apache 2.0 or MIT. We did not read its terms.
- **Baidu's benchmarks (base models, Baidu's own evaluation):** against DeepSeek-V4-Flash-Base, Hy3-preview-Base and MiMo-V2.5-Base, Baidu reports, in that order after its own score: MMLU 93.3 (89.4 / 87.5 / 87.6), MMLU-Pro 78.4 (69.2 / 66.9 / 65.7), GPQA 60.2 (55.9 / 50.2 / 51.4), SimpleQA 34.1 (29.1 / 25.9 / 20.8), HumanEval+ 82.3 (69.5 / 78.0 / 74.4), LiveCodeBench 40.1 (31.9 / 33.5 / 32.4) and LongBench-v2 48.7 (44.5 / 39.8 / 44.6). The page covers about 30 benchmarks; we list only these seven.
- **Not stated:** pricing or a hosted API for this checkpoint, and any independent test results.

## Why it matters

Open base checkpoints are what researchers and companies use to build their own tuned models, so a 280B model with only 14B parameters active per token is relevant to anyone who wants strong results without serving a dense model of the same size. Baidu's comparison is against three other recent Chinese base models of similar size, which is a fair frame, though a lab choosing its own comparison set and benchmarks tends to show its model well.

Two caveats matter for users. First, this is a base model: it has not been tuned to follow instructions, so it is not directly comparable with chat models. Second, the custom license decides what you may do with the weights, and we have not reviewed it, so read it before building a product on it.

> Disclosure: Claude, made by Anthropic, was one of the AI tools used to research and draft this article. Baidu is not affiliated with Deyron Labs; all performance claims are Baidu's own.
