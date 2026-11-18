---
title: "Cerebras launches disaggregated inference, pairing AMD GPUs for prefill with CS-3 systems for decode"
summary: "Cerebras said on 17 November 2026 that it splits inference between AMD Instinct GPUs for prefill and its CS-3 systems for decode, claiming 5X the throughput per megawatt of a CS-3-only setup with no loss in token generation speed. Early-access partners include AWS."
seoTitle: "Cerebras disaggregated inference with AMD GPUs"
seoDescription: "Cerebras's 17 Nov 2026 post claims 5X throughput per megawatt by pairing AMD Instinct GPUs for prefill with CS-3 for decode."
lang: en
publishedAt: 2026-11-18T09:16:00Z
entities:
  - Cerebras
  - AMD Instinct
  - CS-3
  - Amazon Web Services
  - Fireworks AI
topics:
  - Hardware
  - Inference
translationKey: cerebras-disaggregated-inference-amd-gpus
image: /images/news/cerebras-disaggregated-inference-amd-gpus-2026-11-18.jpg
imageAlt: "Deyron Labs graphic: Cerebras disaggregated inference; AMD Instinct GPUs for prefill, CS-3 for decode; 5X throughput per megawatt claimed by Cerebras; blog post, 17 November 2026"
sources:
  - title: "Cerebras launches disaggregated inference"
    url: "https://cerebras.ai/blog/cerebras-launches-disaggregated-inference"
    publisher: "Cerebras, 17 November 2026"
    primary: true
---

## What happened

In a blog post dated 17 November 2026, Cerebras described a disaggregated inference design: GPUs (AMD Instinct) handle prefill, and Cerebras CS-3 systems handle decode. The figures below are Cerebras's own.

## Key details

- **Result claimed:** "5X the throughput per megawatt of a CS-3-only configuration, with no loss in token generation speed", measured on a shared GPT-OSS-120B endpoint on 14 November.
- **Rollout:** Cerebras plans to deploy across hundreds of megawatts by the end of 2027 and mentions a planned 700MW of data center capacity and the recently announced CS-4.
- **Partners and software:** early-access partners are Amazon Web Services, Fireworks AI, Gimlet Labs and General Compute. The stack is offered end to end or as a decode-only SDK; KV Portal moves KV caches over RDMA.
- **Not stated:** pricing, availability dates for general customers, and independent measurements.

## Why it matters

The design targets power efficiency per megawatt, a main constraint for inference capacity. The 5X figure comes from a single Cerebras measurement on one model, so it is a claim to watch for independent confirmation.

> Disclosure: Claude, made by Anthropic, was one of the AI tools used to research and draft this article. Cerebras is not affiliated with Deyron Labs; all claims are Cerebras's own.
