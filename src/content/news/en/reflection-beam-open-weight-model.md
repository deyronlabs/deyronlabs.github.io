---
title: "Reflection announces Beam, a 501B open-weight model it says matches GLM-5.2 at 3–4x less compute"
summary: "Reflection announced Beam on 5 October 2026, a 501-billion-parameter mixture-of-experts model with 23 billion active parameters. The company says it will release the weights under Apache 2.0 later in October. The benchmark scores are Reflection's own, and in its table Beam trails several newer Chinese models."
lang: en
publishedAt: 2026-10-07T17:00:00Z
entities:
  - Reflection
  - Beam
  - GLM-5.2
  - GLM-5.3
  - Z.ai
  - Kimi K3
  - Qwen 3.8 Max
  - DeepSeek V4.1 Flash
  - Inkling
  - Nemotron 3 Ultra
topics:
  - Models
  - Open-weight
  - Coding
translationKey: reflection-beam-open-weight-model
image: /images/news/reflection-beam-2026-10-05.jpg
imageAlt: "Deyron Labs graphic: Reflection's Beam weights are promised under Apache 2.0 later in October, and the benchmark scores are the lab's own"
sources:
  - title: "Introducing Beam: Reflection's 501B open-weight model"
    url: "https://reflection.ai/blog/introducing-beam"
    publisher: "Reflection"
    primary: true
  - title: "Reflection debuts Beam, an open-weight AI model to rival Chinese models at lower compute cost"
    url: "https://techcrunch.com/2026/10/05/reflection-debuts-beam-a-open-weight-ai-model-to-rival-chinese-models-at-lower-compute-cost/"
    publisher: "TechCrunch"
---

## What happened

On 5 October 2026, the AI lab Reflection announced Beam, a text model built for reasoning, coding and agentic tasks. Reflection describes it as a sparse mixture-of-experts model with 501 billion parameters in total and 23 billion active for each token. TechCrunch reports a training run of 23.8 trillion tokens and a context window of 1 million tokens.

The weights are not out yet. Reflection says it will release them under an Apache 2.0 license, with documentation, later in October, and that Beam is going through final red-teaming and evaluation. For now it offers a sign-up for early access.

## Key details

- **Efficiency claim, as reported by Reflection:** Beam reaches scores comparable to Z.ai's GLM-5.2 on advanced reasoning benchmarks while using 3–4 times less inference compute. We found no independent measurement of this.
- **Coding scores in Reflection's own table:** Beam scores 44.4 on DeepSWE v1.1 (GLM-5.2: 44.0), 77.2 on SWE Bench Pro v2-Hard, 65.5 on SWE Bench Pro v1, 80.1 on Terminal Bench v2.1 and 80.9 on SWEBench Verified.
- **Against the other open models in that table:** Beam is ahead of Inkling and Nemotron 3 Ultra on every benchmark where they have a score (for example 80.9 versus 77.6 and 70.7 on SWEBench Verified).
- **Against newer Chinese models:** in the same table Beam is behind Kimi K3 (68.0 on DeepSWE v1.1, 88.3 on Terminal Bench v2.1), GLM-5.3 (61.0 and 88.2) and DeepSeek V4.1 Flash (74.2 and 90.6) on the benchmarks where those models have a score. Many cells in the table are marked not reported.
- **Not yet public:** the license, the weights and the technical report are promised, not released. Reflection gives no API price in the announcement.
- **Company background (TechCrunch):** Reflection has raised about $4.7 billion, with Nvidia, Sequoia Capital and Lightspeed Venture Partners among its investors, and has compute deals with SpaceX and Nebius.

## Why it matters

If Reflection keeps its word, Apache 2.0 is one of the most permissive licenses a model of this size can carry: you could run it, change it and use it commercially without asking. That is the main reason to watch this release. Until the weights are public, though, Beam is an announcement, and the date is only "later this month".

The benchmark story needs care. The headline claim is about efficiency, not about beating the best models: Reflection's own table shows Beam below several newer Chinese models on the coding tests where both have scores. If the 3–4 times lower inference cost holds up, that could matter more to anyone paying for GPUs than a few benchmark points. All the numbers here come from Reflection, so wait for independent evaluations, and test the model on your own tasks once the weights are available.

> Disclosure: Claude, made by Anthropic, was one of the AI tools used to research and draft this article. Performance claims are Reflection's own unless stated otherwise.
