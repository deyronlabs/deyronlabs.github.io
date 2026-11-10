---
title: "Google introduces TPU 8tx and TPU 8i Max, two new TPU systems"
summary: "On 9 November 2026 Google announced two new TPU systems. TPU 8tx pairs the TPU 8t silicon with 5th Generation AMD EPYC hosts and hardware confidential compute, with up to 2x lower latency than TPU 8t. TPU 8i Max combines two TPU 8i chips on one package for double the compute, SRAM and HBM bandwidth of TPU 8i. The post gives no absolute performance figures or availability dates."
seoTitle: "Google TPU 8tx and TPU 8i Max announced"
seoDescription: "Google announced TPU 8tx and TPU 8i Max on 9 Nov 2026: up to 2x lower latency than TPU 8t, and double the compute of TPU 8i. No absolute specs given."
lang: en
publishedAt: 2026-11-10T08:00:00Z
entities:
  - Google
  - Google Cloud
  - TPU 8tx
  - TPU 8i Max
  - AMD
topics:
  - Infrastructure
  - Hardware
translationKey: google-tpu-8tx-8i-max
image: /images/news/google-tpu-8tx-8i-max-2026-11-09.jpg
imageAlt: "Deyron Labs graphic: Google announces TPU 8tx and TPU 8i Max on 9 November 2026; 8tx up to 2x lower latency than TPU 8t, 8i Max double the compute, SRAM and HBM bandwidth of TPU 8i"
sources:
  - title: "Introducing TPU 8tx and TPU 8i Max (Google Cloud blog, 9 Nov 2026)"
    url: "https://cloud.google.com/blog/topics/ai-infrastructure/tpu-8tx-and-tpu-8i-max"
    publisher: "Google Cloud"
    primary: true
---

## What happened

Google Cloud published "Introducing TPU 8tx and TPU 8i Max", by Amin Vahdat, on 9 November 2026, cross-posted from blog.google. We read the Google Cloud version on 10 November 2026. All claims below are Google's.

## Key details

- **TPU 8tx:** built on the same silicon as TPU 8t and paired with 5th Generation AMD EPYC CPU hosts, with hardware-level confidential compute. Google says it offers up to 2x lower latency than TPU 8t with a near-zero performance penalty.
- **TPU 8i Max:** combines two low-latency TPU 8i chips in one package, giving double the compute, double the SRAM and double the HBM bandwidth of TPU 8i, per Google.
- **Cadence:** Google says it is shipping four new TPU systems in a single year.
- **Not stated:** the post contains no absolute figures such as FLOPS, memory capacity or pod size, and we did not find pricing or general-availability dates in it.

## Why it matters

For most users of AI tools the effect is indirect: lower-latency, confidential serving hardware matters to companies running inference on Google Cloud, not to anyone calling a model through an app. Without absolute specs or dates, the comparisons stay relative to Google's own earlier chips and cannot yet be checked against competing accelerators.

> Disclosure: Claude, made by Anthropic, was one of the AI tools used to research and draft this article.
