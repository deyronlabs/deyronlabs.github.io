---
title: "Anthropic releases FlashProve, an open-source prototype that proves which model produced an output, at 70-95x the GPU time"
summary: "Anthropic and researchers from EPFL and MIT published FlashProve on 2 November 2026, a zkSNARK research prototype that proves a specific Llama 4 Maverick model generated a given output. Anthropic reports about 110 tokens per second on one H100 and roughly 19 MB per proof, at 70-95 times the GPU time of ordinary serving. Code is Apache 2.0; it is a research prototype with a 1,024-token limit."
seoTitle: "Anthropic FlashProve proves which model answered"
seoDescription: "Anthropic's FlashProve (2 Nov 2026) is an Apache 2.0 prototype that proves a Llama 4 Maverick output, at 70-95x the GPU time of normal serving."
lang: en
publishedAt: 2026-11-04T17:30:00Z
entities:
  - Anthropic
  - FlashProve
  - EPFL
  - MIT
  - Llama 4 Maverick
topics:
  - Research
  - Safety
  - Provenance
translationKey: anthropic-flashprove-provable-inference
image: /images/news/anthropic-flashprove-provable-inference-2026-11-04.jpg
imageAlt: "Deyron Labs graphic: Anthropic FlashProve, about 110 tokens per second on one H100, roughly 19 MB per proof, 70-95x the GPU time of vLLM, Apache 2.0 research prototype"
sources:
  - title: "Progress on provable inference for large language models"
    url: "https://www.anthropic.com/research/provable-inference"
    publisher: "Anthropic"
    primary: true
  - title: "FlashProve technical report"
    url: "https://www.anthropic.com/document/flashprove-technical-report"
    publisher: "Anthropic"
    primary: true
---

## What happened

On 2 November 2026 Anthropic published "Progress on provable inference for large language models" from its Frontier Red Team, with co-authors from EPFL, MIT and Anthropic's fellows programs. It introduces FlashProve, which Anthropic calls an open-source research prototype of a zkSNARK (a short cryptographic proof) for provable inference on mixture-of-experts models. The idea is that a provider can prove that a specific, committed model produced a specific output, so a user does not have to take that on trust.

## Key details

- **Reported performance:** on Llama 4 Maverick (a 400B-parameter MoE with about 17B active parameters per token, 4-bit weights) running on one H100, Anthropic reports proof generation at about 110 tokens per second and a proof of about 19 MB per 1,024-token request.
- **Cost:** Anthropic reports roughly 70-95 times the GPU time of running the same model in vLLM. Verification takes about 17 seconds on 24 threads (21 seconds on one thread). A one-time offline setup per model takes about 39 minutes, and one commitment covers about 16 million requests.
- **Hardware:** one 80 GB GPU plus about 290 GB of host memory.
- **Availability:** "We release our code, Lean proofs, and documentation under the Apache 2.0 license", with a technical report, protocol specification and code on GitHub (anthropics/FlashProve). Model weights are not included; Llama 4 Maverick is downloaded separately under Meta's Llama 4 license.
- **Limits stated by Anthropic:** it is a research prototype; the fast C++ verifier has no formal guarantees; the proof covers an integer version of the model under greedy decoding, not floating-point or sampled decoding; the model architecture is not hidden; side-channel attacks are out of scope; context is limited to 1,024 tokens.
- **Not stated:** any plan to deploy it in Anthropic products, or independent replication. All figures are the authors' own measurements.

## Why it matters

Today there is almost no way for a user of a hosted model to check that the answer came from the model they were promised rather than a cheaper substitute. FlashProve shows this can be done in principle for a large open-weight model, but at a cost of tens of times the compute and with a short context, so it is groundwork rather than something users can switch on. The open licence lets other researchers test and improve the approach.

> Disclosure: Claude is made by Anthropic and is one of the AI tools Deyron Labs uses to research and draft articles, including this one, which is about Anthropic research. All figures are Anthropic's, read from its pages on 4 November 2026.
