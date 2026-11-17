---
title: "Google Cloud publishes 10 MLPerf Training v6.1 results for Ironwood TPUs and NVIDIA GB300 GPUs"
summary: "On 16 November 2026 Google Cloud reported 10 MLPerf Training v6.1 Closed-division results on seventh-generation Ironwood TPUs and NVIDIA Grace Blackwell GPUs. Google says 8,192 Ironwood TPUs reached the pre-training target in 1.70 minutes and 640 TPUs finished an agentic reinforcement-learning run in 18.02 minutes."
seoTitle: "Google Ironwood TPUs in MLPerf Training v6.1"
seoDescription: "Google Cloud reported 10 MLPerf Training v6.1 results on 16 Nov 2026, including 8,192 Ironwood TPUs hitting a pre-training target in 1.70 minutes."
lang: en
publishedAt: 2026-11-17T08:07:00Z
entities:
  - Google Cloud
  - Ironwood TPU
  - MLPerf Training v6.1
  - MLCommons
  - NVIDIA GB300
topics:
  - Hardware
  - Research
translationKey: google-ironwood-tpu-mlperf-training-v6-1
image: /images/news/google-ironwood-tpu-mlperf-training-v6-1-2026-11-17.jpg
imageAlt: "Deyron Labs graphic: Google Cloud MLPerf Training v6.1 results; 8,192 Ironwood TPUs in 1.70 minutes; 640 TPUs agentic RL in 18.02 minutes; Google blog, 16 November 2026"
sources:
  - title: "New AI training performance benchmarks for Google TPUs"
    url: "https://blog.google/innovation-and-ai/infrastructure-and-cloud/google-cloud/training-performance-benchmarks-tpus/"
    publisher: "Google, 16 November 2026"
    primary: true
---

## What happened

On 16 November 2026 Google published "New AI training performance benchmarks for Google TPUs". The post says Google Cloud submitted 10 results in the Closed division of MLPerf Training v6.1, using seventh-generation Ironwood TPUs and NVIDIA Grace Blackwell GPUs. The full results are listed on the MLCommons site, which we have not read; the figures below are as reported by Google.

## Key details

- **Pre-training on Ironwood:** Google says 8,192 Ironwood TPUs reached the target quality in 1.70 minutes, and that scaling to 4,096 chips gave 96% efficiency.
- **Agentic reinforcement learning on Ironwood:** 640 Ironwood TPUs reached the coding benchmark's target accuracy in 18.02 minutes, scoring 0.765 against a 0.69 goal. Google says training chips waited under 3% of the time.
- **NVIDIA GPUs on Google Cloud:** 256 GB300 GPUs on A4X Max instances reached the target in 31.96 minutes, and Google made five A4X and A4X Max submissions on the agentic RL benchmark.
- **Models used:** the result IDs include a Qwen3.5-397B reinforcement-learning run and DeepSeek-V3 runs.
- **Not stated:** pricing, instance availability dates and a licence.

## Why it matters

MLPerf Training results are one of the few places where vendors report time-to-train on a shared set of tasks, so Google's numbers give a data point for Ironwood against its own NVIDIA-based instances. The agentic RL benchmark is notable because it measures the kind of coding-agent training loop that labs now care about.

Because the figures come from Google's post, buyers comparing platforms should check the official MLCommons tables for system sizes, software stacks and which results are Closed-division, and should not read one cluster size as a like-for-like comparison with another.

> Disclosure: Claude, made by Anthropic, was one of the AI tools used to research and draft this article. Google is not affiliated with Deyron Labs; all claims are Google's own.
