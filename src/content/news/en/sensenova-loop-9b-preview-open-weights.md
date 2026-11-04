---
title: "SenseNova-Loop-9B-Preview: a looped multimodal model that reuses 24 layers twice, released under Apache 2.0"
summary: "SenseNova-Loop-9B-Preview, released on 30 October 2026 under the OpenSenseNova project, is a roughly 9-billion-parameter model that takes text and images and reuses 24 decoder layers twice. Its model card lists a 262,144-token training context and an Apache 2.0 license. The card gives no benchmark figures in text and says the technical report is still to come."
seoTitle: "SenseNova-Loop-9B-Preview: looped 9B, Apache 2.0"
seoDescription: "SenseNova-Loop-9B-Preview, released 30 Oct 2026 under Apache 2.0, reuses 24 decoder layers twice and supports a 262,144-token training context."
lang: en
publishedAt: 2026-11-04T00:27:00Z
entities:
  - SenseTime
  - SenseNova
  - SenseNova-Loop-9B-Preview
  - OpenSenseNova
  - Hugging Face
topics:
  - Models
  - Open-weight
  - China
translationKey: sensenova-loop-9b-preview-open-weights
image: /images/news/sensenova-loop-9b-preview-open-weights-2026-10-30.jpg
imageAlt: "Deyron Labs graphic: SenseNova-Loop-9B-Preview, about 9 billion parameters, 24 layers applied twice, 262,144-token training context, Apache 2.0, technical report still to come"
sources:
  - title: "SenseNova-Loop-9B-Preview (Hugging Face model card)"
    url: "https://huggingface.co/sensenova/SenseNova-Loop-9B-Preview"
    publisher: "SenseNova"
    primary: true
  - title: "OpenSenseNova/SenseNova-Loop (GitHub)"
    url: "https://github.com/OpenSenseNova/SenseNova-Loop"
    publisher: "OpenSenseNova"
    primary: true
  - title: "SenseTime open-sources 9-billion-parameter AI model that reuses layers for deeper processing"
    url: "https://technode.com/2026/11/02/sensetime-open-sources-9-billion-parameter-ai-model-that-reuses-layers-for-deeper-processing/"
    publisher: "TechNode"
---

## What happened

The model card and GitHub repository for SenseNova-Loop-9B-Preview carry the entry "[2026.10.30] We release SenseNova-Loop-9B-Preview, a looped multimodal model for long-context and agentic workflows." The repository sits under the OpenSenseNova organization; the technology outlet TechNode, in an article of 2 November 2026, attributes the release to the Chinese company SenseTime. The model card is the primary source for the details below.

## Key details

- **Size:** "~9B total parameters; ~14.6B inference parameters", the second figure counting the reused layers. Hugging Face's metadata lists 10 billion parameters.
- **Looped design:** the model applies 24 decoder layers twice in sequence, which the card says produces 56 decoder-layer executions from 32 distinct layers. It also uses a hybrid attention pattern of three linear-attention layers followed by one full-attention layer.
- **Inputs and outputs:** text and images in, text out. Training sequence length is up to 262,144 tokens.
- **License:** Apache 2.0, on both the model card and the repository.
- **Benchmarks:** the card shows a results table only as an image, listing tests including BIRD-Dev, Terminal Bench 2.1 and AutomationBench. We could not read the numbers, so we do not report them. Any scores are SenseNova's own.
- **Still missing:** the card says "Technical report: TBD". Faster-decoding options named Dspark and Dflash2 are listed as "Training in progress".
- **Running it:** the card's checked environment uses Transformers 5.18.0 and PyTorch 2.11.0 with CUDA 13.0, and the repository describes deployment through LightLLM or an SGLang pull request.

## Why it matters

Looping layers lets a small model do more computation per token without storing more weights, which is attractive for people who run models themselves. Whether that trade pays off for this model is not yet shown: without readable benchmarks or a technical report, there is no evidence here about quality. The Apache 2.0 license is permissive, so teams can test it directly.

> Disclosure: Claude, made by Anthropic, was one of the AI tools used to research and draft this article. Specifications are SenseNova's, read from its model card and repository on 3 November 2026. The attribution to SenseTime comes from TechNode.
