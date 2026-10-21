---
title: "DeepSeek open-sources DeepInfer, the inference framework it says powers its production services"
summary: "DeepSeek has published DeepInfer on GitHub under Apache 2.0. The README calls it the framework behind DeepSeek's large-scale production services; this release supports DeepSeek-V4.1-Flash on NVIDIA SM100 GPUs and Huawei Ascend 950 NPUs and covers offline inference only, without a KV-cache system or load balancing."
seoTitle: "DeepSeek open-sources DeepInfer"
seoDescription: "DeepSeek released DeepInfer on GitHub under Apache 2.0 in October 2026: offline inference for V4.1-Flash on NVIDIA SM100 and Huawei Ascend 950."
lang: en
publishedAt: 2026-10-21T16:30:00Z
entities:
  - DeepSeek
  - DeepInfer
  - DeepSeek-V4.1-Flash
  - NVIDIA
  - Huawei
  - vLLM
topics:
  - China
  - Open-weight
  - Hardware
translationKey: deepseek-deepinfer-open-source-inference
image: /images/news/deepseek-deepinfer-open-source-inference-2026-10-21.jpg
imageAlt: "Deyron Labs graphic: DeepSeek DeepInfer open-source inference code; Apache 2.0 license, supports DeepSeek-V4.1-Flash, NVIDIA SM100 and Huawei Ascend 950"
sources:
  - title: "deepseek-ai/DeepInfer (GitHub repository and README)"
    url: "https://github.com/deepseek-ai/DeepInfer"
    publisher: "DeepSeek"
    primary: true
  - title: "DeepSeek API docs news: DeepSeek-V4.1-Flash-1017"
    url: "https://api-docs.deepseek.com/news/news261017"
    publisher: "DeepSeek"
    primary: true
---

## What happened

DeepSeek has made DeepInfer public on GitHub. The repository describes it as a "high-performance, large-scale inference framework for DeepSeek models," and the README says it is "the high-performance inference framework that powers DeepSeek's large-scale production services." According to the GitHub API, the repository's first commit is dated 20 October 2026 (UTC); the repository has two commits as of our reading on 21 October.

## Key details

- **License:** Apache 2.0, per the README.
- **Supported model:** DeepSeek-V4.1-Flash; the default checkpoint is DeepSeek-V4.1-Flash-1017.
- **Hardware:** NVIDIA SM100 GPUs and Huawei Ascend 950 NPUs. Prerequisites listed include Linux, Python 3.12, CUDA 13 (NVIDIA) and CANN 9.2 (Ascend).
- **Features listed:** optimised kernels, attention data parallelism, MoE expert parallelism with load balancing, asynchronous scheduling, batch-invariant inference, deterministic sampling and structured outputs.
- **What this release leaves out:** the README lists a KV-cache system, prefill/decode disaggregation and load balancing across data-parallel replicas as "required for a complete inference service (not included in this release)." It describes the release as offline inference.
- **Lineage:** the README says the code was "originally built primarily on vLLM," with inspiration from SGLang and TensorRT-LLM.
- **Benchmarks:** the README shows charts measured on 4 SM100 GPUs for prefill and 64 for decode; the charts are images, and we did not extract numbers from them.
- **Unconfirmed figures:** some newsletters have circulated large daily-token and revenue numbers in connection with the release. We did not find them in the README or in DeepSeek's news posts we read, so we do not report them.

## Why it matters

Inference code is the part that determines how cheaply a model can be served, and DeepSeek is publishing a version of its own production stack rather than only model weights. Because this release omits the KV-cache system and request routing, it is a building block for offline or research use rather than a ready-made serving platform. Support for Huawei Ascend 950 alongside NVIDIA hardware is stated in the README; real-world performance on either was not independently measured here.

> Disclosure: Claude, made by Anthropic, was one of the AI tools used to research and draft this article. Details come from DeepSeek's GitHub repository, read on 21 October 2026; DeepSeek's own announcement post on X could not be fetched. Repository dates come from the GitHub API.
