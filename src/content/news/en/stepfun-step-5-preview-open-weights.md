---
title: "StepFun publishes Step 5 Preview, a 600B open-weight model with 27B active parameters and a 1M-token context"
summary: "StepFun's Step 5 Preview is a sparse mixture-of-experts model with about 600 billion parameters, 27 billion active per token and a 1-million-token context. Its Hugging Face card lists a StepFun Model License 1.0; the benchmark scores on the card are StepFun's own, and the model trails GLM-5.3 on Terminal-Bench."
seoTitle: "StepFun Step 5 Preview: 600B open-weight MoE"
seoDescription: "StepFun's Step 5 Preview is a 600B mixture-of-experts model with 27B active parameters and 1M context; weights are on Hugging Face under a custom license."
lang: en
publishedAt: 2026-10-18T17:30:00Z
entities:
  - StepFun
  - Step 5 Preview
  - Hugging Face
  - GLM-5.3
  - Artificial Analysis
topics:
  - Models
  - Open-weight
  - China
translationKey: stepfun-step-5-preview-open-weights
image: /images/news/stepfun-step-5-preview-open-weights-2026-10-15.jpg
imageAlt: "Deyron Labs graphic: StepFun Step 5 Preview, 600B-parameter mixture-of-experts model, 27B active, 1M-token context, custom StepFun Model License 1.0"
sources:
  - title: "stepfun-ai/Step-5-Preview model card"
    url: "https://huggingface.co/stepfun-ai/Step-5-Preview"
    publisher: "Hugging Face (StepFun)"
    primary: true
  - title: "Inside Step 5 Preview"
    url: "https://platform.stepfun.ai/blog/inside-step-5-preview"
    publisher: "StepFun"
    primary: true
  - title: "StepFun releases Step 5 Preview open weights: 600B MoE, 27B active, 1M context"
    url: "https://www.marktechpost.com/2026/10/16/stepfun-releases-step-5-preview-open-weights-600b-moe-27b-active-1m-context"
    publisher: "MarkTechPost"
---

## What happened

StepFun, a Chinese AI lab, has published **Step 5 Preview**, a sparse mixture-of-experts language model, on Hugging Face. StepFun's engineering post "Inside Step 5 Preview" is dated 15 October 2026. MarkTechPost reports that the model's API launched on 20 September and that the open weights followed on 14 October; the Hugging Face model card itself gives no release date, so we cannot confirm the weights date from the primary page.

## Key details

- **Size and context (model card):** about 600 billion parameters in total (the Hugging Face listing shows 604 billion), 27 billion active per token, and a context window of up to 1 million tokens. The card lists text and image input with text output and mentions video input.
- **Architecture (StepFun's post):** 92 transformer blocks in a narrow, deep design, with gated sliding-window attention and sparse full-attention layers interleaved 3:1. StepFun says an MTP-3 speculative-decoding head gives roughly 30% end-to-end speedup. The post does not give benchmark scores or say whether the weights are released.
- **License:** the card names StepFun Model License 1.0 and describes it as Apache-2.0-style with extra attribution and commercial-license conditions. We did not read the full license text, so check it before commercial use.
- **Benchmarks are StepFun's own.** The card lists 67.7 on DeepSWE, 33.3 on Terminal-Bench and 29.5 on Agents' Last Exam (CLI), and recommends the "High" reasoning setting. MarkTechPost notes that rivals in StepFun's chart were run at "Max" effort, so the comparison is not like-for-like, and that GLM-5.3 scores 41.9 on Terminal-Bench. MarkTechPost also cites an Artificial Analysis Intelligence Index of 43.7 and weak results on two Vals AI benchmarks; we could not open the Artificial Analysis page, so those figures are unverified by us.
- **Running it:** the card's examples use one node with four B300 GPUs or eight H200 GPUs for FP8, and larger setups for BF16. It says these setups do not guarantee room for a full 1M-token request. MarkTechPost puts the FP8 checkpoint at about 650 GB.
- **API price (MarkTechPost):** $1.00 per million input tokens and $2.70 per million output tokens; we did not confirm this on StepFun's pricing page.

Checked against the Hugging Face model card and StepFun's post on 18 October 2026.

## Why it matters

Open weights from Chinese labs keep arriving at a pace that gives developers more choice, and Step 5 Preview adds a 1M-context agent-oriented model to that list. Its weights are public, but a roughly 650 GB checkpoint means most people will reach it through a hosted API, not their own hardware.

The honest reading of the numbers is mixed. On the one agent benchmark where MarkTechPost compares it with GLM-5.3, Step 5 Preview scores lower, and the scores that make it look strong are StepFun's own. The license is custom rather than a standard permissive one. If you plan to build on it, test it on your own tasks and read the license first.

> Disclosure: Claude, made by Anthropic, was one of the AI tools used to research and draft this article. Performance claims are StepFun's own unless stated otherwise.
