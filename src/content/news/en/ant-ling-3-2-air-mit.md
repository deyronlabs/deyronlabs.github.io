---
title: "Ant Group releases Ling-3.2-air, a 124B multimodal open-weight model under the MIT license"
summary: "Ant Group's inclusionAI has published Ling-3.2-air on Hugging Face under the MIT license: a hybrid-linear mixture-of-experts multimodal model with 124 billion total and 5.5 billion active parameters. Ant reports large gains on agent benchmarks over its earlier Ling-3.0-flash-VL, such as AutomationBench-AA rising from 15.7% to 61%. All figures are Ant's own."
seoTitle: "Ant Ling-3.2-air: 124B open model, MIT license"
seoDescription: "Ant Group's Ling-3.2-air is a 124B MoE (5.5B active) multimodal model under MIT; Ant reports AutomationBench-AA at 61%, up from 15.7%."
lang: en
publishedAt: 2026-11-25T21:00:00Z
entities:
  - Ant Group
  - inclusionAI
  - Ling-3.2-air
  - Ling-3.0-flash-VL
  - Hugging Face
topics:
  - Models
  - Open-weight
  - China
translationKey: ant-ling-3-2-air-mit
image: /images/news/ant-ling-3-2-air-mit.jpg
imageAlt: "Deyron Labs graphic: Ant Group's Ling-3.2-air, a 124B mixture-of-experts multimodal model with 5.5B active parameters under the MIT license; Ant reports AutomationBench-AA rising from 15.7% to 61%"
sources:
  - title: "inclusionAI/Ling-3.2-air (model card and README)"
    url: "https://huggingface.co/inclusionAI/Ling-3.2-air"
    publisher: "inclusionAI (Ant Group) on Hugging Face, read 25 November 2026"
    primary: true
  - title: "Ant releases Ling-3.2-air multimodal model under MIT license"
    url: "https://technode.com/2026/11/25/ant-releases-ling-3-2-air-multimodal-model-under-mit-license/"
    publisher: "TechNode, 25 November 2026"
    primary: false
---

## What happened

Ant Group's inclusionAI team has published **Ling-3.2-air** on Hugging Face under the MIT license. The model card describes an open-weight model that shares the same native multimodal architecture as Ling-3.0-flash-VL, with improvements in "workflow automation and reasoning over professional documents". The card gives no release date; Hugging Face's metadata dates the repository to 23 November 2026.

We read the model card's README on 25 November 2026. Every number below is reported by Ant; we have not run the model and found no independent evaluation or technical report.

## Key details

- **Architecture:** a hybrid-linear mixture-of-experts model with 124 billion total and 5.5 billion active parameters. Per the README it uses 35 KDA layers and 7 Gated MLA layers (a 5:1 mix), with 512 routed experts, 1 shared expert and 8 active per token, and a vocabulary of 157,184.
- **Reported gains over Ling-3.0-flash-VL (Ant's figures):** AutomationBench-AA from 15.7% to 61%; GDP.pdf all-pass from 8.4% to 16%; AA-Briefcase v1.1 Elo from 987 to 1340 (+353); Terminal-Bench 4.0 from 0% to 27%.
- **Aggregate score:** Ant cites an Artificial Analysis Intelligence Index v5.0.1 score of 23 for the model. This is the figure given on the model card, not a table from an independent evaluator.
- **Document-review caveat in Ant's own numbers:** on Harvey LAB-AA v1.1, Ant reports an 87.7% criterion pass rate and an 8.3% all-pass rate before hallucination checking, and 0.8% all-pass after it.
- **Running it:** the README recommends an SGLang image with four 141 GB GPUs (H20-3e or H200) or Blackwell hardware, a 256K context, and a vLLM fork (`inclusionAI/vllm-ling-v3`).
- **Not on the card:** a technical report and an explicit release date.

## Why it matters

An MIT-licensed multimodal model with 5.5 billion active parameters is cheap to run per token compared with its 124 billion total size, and the license has no custom terms to review. For teams building document and workflow agents, it is a new open-weight option from the same family as Ling-3.2-flash.

The jump from 15.7% to 61% on AutomationBench-AA is large, but it is Ant's own comparison against an older model of its own. The hallucination-check result on Harvey LAB-AA shows how much the headline numbers can change under stricter grading, so independent tests matter before anyone relies on it for professional documents.

> Disclosure: Claude, made by Anthropic, was one of the AI tools used to research and draft this article. Ant Group is not affiliated with Deyron Labs; all claims are Ant's own.
