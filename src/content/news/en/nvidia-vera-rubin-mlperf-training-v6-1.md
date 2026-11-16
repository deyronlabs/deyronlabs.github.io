---
title: "NVIDIA says Vera Rubin NVL72 debuts in MLPerf Training v6.1 with up to 2x per-GPU gain over GB300, pending verification"
summary: "NVIDIA reports that it swept every MLPerf Training v6.1 benchmark and that its Vera Rubin NVL72 delivered up to 2x more performance per GPU than GB300 NVL72 in its debut. The Vera Rubin results are early and pending MLCommons verification, and the figures come from NVIDIA's own blog post of 16 November 2026."
seoTitle: "NVIDIA Vera Rubin in MLPerf Training v6.1"
seoDescription: "NVIDIA says Vera Rubin NVL72 delivered up to 2x per-GPU performance over GB300 in MLPerf Training v6.1 (16 Nov 2026); results await MLCommons verification."
lang: en
publishedAt: 2026-11-16T19:32:00Z
entities:
  - NVIDIA
  - Vera Rubin NVL72
  - GB300 NVL72
  - MLPerf Training v6.1
  - MLPerf Endpoints
  - MLCommons
  - Kimi K3
  - DeepSeek-V3
topics:
  - Hardware
  - Benchmarks
translationKey: nvidia-vera-rubin-mlperf-training-v6-1
image: /images/news/nvidia-vera-rubin-mlperf-training-v6-1-2026-11-16.jpg
imageAlt: "Deyron Labs graphic: NVIDIA says Vera Rubin NVL72 delivered up to 2x per-GPU performance over GB300 NVL72 in MLPerf Training v6.1; results pending MLCommons verification; NVIDIA blog, 16 November 2026"
sources:
  - title: "NVIDIA Sweeps MLPerf Training and Endpoints as Vera Rubin Debuts With Leading Performance"
    url: "https://blogs.nvidia.com/blog/mlperf-training-endpoints-vera-rubin/"
    publisher: "NVIDIA blog (Shruti Koparkar), 16 November 2026"
    primary: true
---

## What happened

On 16 November 2026 NVIDIA published a blog post reporting its results in MLPerf Training v6.1 and in the first round of MLPerf Endpoints, a benchmark for agentic AI inference. NVIDIA says it "swept every MLPerf Training v6.1 benchmark" and that its new Vera Rubin NVL72 system made its debut in the round. We read the post on 16 November 2026; it was modified later the same day.

## Key details

- **Training, per-GPU gain:** NVIDIA reports that in its debut Vera Rubin NVL72 delivered up to 2x more performance per GPU than GB300 NVL72. The post calls these "early results".
- **Scaling:** on the DeepSeek-V3 benchmark NVIDIA reports that Vera Rubin NVL72 scaled from 256 to 1,024 GPUs with about 97% efficiency, cutting time to train from 16 minutes to about four.
- **Largest scale:** NVIDIA says it ran 10,240 GPUs on GB300 systems. It adds that Microsoft Azure matched that count with 10,240 GPUs on GB200 systems.
- **Coverage:** NVIDIA says its platform was the only one with results on every benchmark in the round, spanning large language models, image generation, recommender systems and reinforcement learning post-training.
- **Endpoints:** in its first MLPerf Endpoints submission NVIDIA reports "more than 10x generational gains in throughput per watt for agentic AI". The provisional result uses a Kimi K3 workload and compares Vera Rubin NVL72 with GB300 NVL72 at a shared minimum of 50 tokens per second per user.
- **Verification status:** a footnote says the Vera Rubin results are "pending MLCommons Association verification" and "subject to change pending peer review". The GB300 results are described as verified.
- **Partners:** the post says submissions came from 20 organizations; the list it prints names 19, including Dell Technologies, Google Cloud, Microsoft Azure, Oracle, CoreWeave and Supermicro.
- **Not stated:** pricing, availability dates for Vera Rubin NVL72 systems, and any independent evaluation of the Vera Rubin numbers.

## Why it matters

MLPerf is a shared benchmark suite, which makes it one of the few places where chips from different vendors are compared on the same tasks. NVIDIA's claim of a roughly 2x per-GPU step from GB300 to Vera Rubin, if it holds after verification, bears on how quickly AI training and inference capacity can grow for the same number of chips.

Until MLCommons verifies the Vera Rubin entries, the numbers are NVIDIA's own, published by the company that makes the hardware. The Endpoints comparison is described as provisional and rests on one workload, so readers planning capacity should wait for the verified results and for pricing and availability.

> Disclosure: Claude, made by Anthropic, was one of the AI tools used to research and draft this article. NVIDIA is not affiliated with Deyron Labs; all performance claims are NVIDIA's own.
