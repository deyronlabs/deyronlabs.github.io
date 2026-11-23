---
title: "Tencent releases Hy4 flash as open weights: a 220B-parameter model with 12B active and a 1M-token context"
summary: "Tencent launched Hy4 flash on 16 November 2026 and published its weights on Hugging Face under a custom Tencent Hy License. The model card lists 220B total parameters, 12B active per token and a 1,048,576-token context. Cost and quality claims come from Tencent's own tests and are not independently verified."
seoTitle: "Tencent Hy4 flash: 220B open weights, 1M context"
seoDescription: "Tencent launched Hy4 flash on 16 Nov 2026; Hugging Face weights list 220B parameters, 12B active, 1M-token context. Benchmarks are Tencent's own."
lang: en
publishedAt: 2026-11-20T09:15:00Z
updatedAt: 2026-11-23T20:50:00Z
entities:
  - Tencent
  - Hy4 flash
  - Hunyuan
  - WorkBuddy
  - Hugging Face
topics:
  - Models
  - Open-weight
  - China
translationKey: tencent-hy4-flash-open-weights
image: /images/news/tencent-hy4-flash-open-weights-2026-11-20.jpg
imageAlt: "Deyron Labs graphic: Tencent Hy4 flash open weights, 20 Nov 2026; 220B total parameters, 12B active per token; 1M-token context; Tencent Hy License (custom); Benchmarks are Tencent's own"
sources:
  - title: "tencent/Hy4-flash model card"
    url: "https://huggingface.co/tencent/Hy4-flash"
    publisher: "Tencent on Hugging Face (repository created 17 November 2026)"
    primary: true
  - title: "Tencent touts independent safety assessments of latest AI model Hy4 (SCMP, 22 November 2026; read only the opening because of a paywall; the 82-page report itself was not read)"
    url: "https://www.scmp.com/tech/tech-trends/article/3375374/tencent-touts-latest-ai-model-hy4s-performance-independent-safety-assessment"
    publisher: "South China Morning Post"
    primary: false
  - title: "Tencent says Hunyuan Hy4 flash surpasses 50 trillion tokens in first-day usage"
    url: "https://technode.com/2026/11/19/tencent-says-hunyuan-hy4-flash-surpasses-50-trillion-tokens-in-first-day-usage/"
    publisher: "TechNode, 19 November 2026"
    primary: false
  - title: "Tencent releases Hy4 flash model weights for local deployment"
    url: "https://technode.com/2026/11/19/tencent-releases-hy4-flash-model-weights-for-local-deployment/"
    publisher: "TechNode, 19 November 2026"
    primary: false
---

## What happened

Tencent launched Hy4 flash, a model in its Hunyuan family aimed at everyday work tasks, on 16 November 2026 through its apps and cloud API, according to TechNode. The weights are published on Hugging Face under `tencent/Hy4-flash`, with an FP8 version and a base (not chat-tuned) version. We read the model card on 20 November 2026; we have not run the model, and we could not read Tencent's own press release.

Update, 23 November 2026: the South China Morning Post reported on 22 November that Tencent has published a safety report of 82 pages with two outside evaluators, Fangcun AI (China) and Alice (Israel and US), covering the open-weight version of Hy4. The details are in the update bullet below. We read only the opening of the SCMP article, which is behind a paywall, and not the report.

## Key details

From the model card, unless noted. Benchmark and cost figures are Tencent's own and have not been independently checked.

- **Size:** 220B total parameters, including 64B "Engram" parameters, with 12B active per token (the card also lists 155.5B excluding Engram, vision encoder and drafter). TechNode's articles say about 224B; we use the card's figure.
- **Inputs and context:** text and images; a 1M-token context (1,048,576 tokens). Architecture listed: 42 layers, 512 routed experts per MoE layer with 16 active plus one shared expert.
- **Speed and efficiency (Tencent):** decoding "past 150 tokens/s"; KV cache described as 1/24 of Hy3 and 1/6 of Hy4; reinforcement learning said to cut average output tokens by 50%.
- **WorkIndex (Tencent's internal benchmark):** Hy4 flash 42.1, Hy4 preview 39.7, Hy4 51.4. Tencent says the average cost per task is 1/13 of Hy4 preview, 1/20 of Hy4 and 1/8 of DeepSeek-V4.1-Flash-1017 under the conditions it lists.
- **Blind user test (Tencent):** 85 internal WorkBuddy users, 259 tasks, 27 categories; satisfaction 2.79 out of 4 for Hy4 flash versus 2.81 for Claude Haiku 5.5.
- **Usage claims (Tencent via TechNode):** more than 50 trillion tokens on the first day, and first place on the OpenRouter daily leaderboard on 17 November. We did not verify either.
- **Price (TechNode):** 0.5 yuan (about $0.07) per million input tokens and 2 yuan (about $0.30) per million output tokens; we did not confirm this on a Tencent page.
- **Update, safety assessments (SCMP, Tencent's report not read):** per SCMP, Tencent published the report on Friday 20 November, and this is the first time a major Chinese tech company has named third-party evaluators before a release. The evaluators say the model has "limited" hacking capabilities and a low risk of deception or loss of control. Those conclusions are the evaluators' and Tencent's own; we have not read the report, so we cannot say which Hy4 variant each test covered or how the tests were run.
- **License:** "Tencent Hy License", a custom license (Hugging Face tag `other`). We have not reviewed its terms, so check them before commercial use.

## Why it matters

Open weights at this size with a million-token context give developers outside Tencent's cloud a way to run and fine-tune a model that Tencent positions around low cost per task. Because the license is custom, it is not the same as Apache 2.0 or MIT, and the terms decide what you can do with it.

The headline comparisons (cost per task, user satisfaction versus Claude Haiku 5.5) come from Tencent's internal tests, so treat them as claims until independent evaluations appear.

> Disclosure: Claude, made by Anthropic, was one of the AI tools used to research and draft this article. Claude Haiku 5.5, an Anthropic model, is mentioned only as a comparison reported by Tencent.
