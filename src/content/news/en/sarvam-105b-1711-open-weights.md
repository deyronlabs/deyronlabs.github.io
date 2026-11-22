---
title: "Sarvam releases Sarvam-105B-1711, an open-weight checkpoint it prices at $0.15 per million tokens"
summary: "India's Sarvam AI published Sarvam-105B-1711 on 22 November 2026, a new checkpoint of its 105B mixture-of-experts model aimed at customer support, voice agents and agentic tasks. Sarvam reports an eight-benchmark average of 73.9, up from 42.6 in March, at a blended $0.15 per million tokens; the Hugging Face card tags the weights Apache-2.0."
seoTitle: "Sarvam-105B-1711: open weights, $0.15/M tokens"
seoDescription: "Sarvam AI's 22 Nov 2026 Sarvam-105B-1711 reports a 73.9 agent-benchmark average at $0.15 per million tokens; weights are on Hugging Face."
lang: en
publishedAt: 2026-11-22T18:30:00Z
entities:
  - Sarvam AI
  - Sarvam-105B-1711
  - Sarvam Token Factory
  - NVIDIA
topics:
  - Models
  - Open-weight
  - India
translationKey: sarvam-105b-1711-open-weights
image: /images/news/sarvam-105b-1711-open-weights-2026-11-22.jpg
imageAlt: "Deyron Labs graphic: Sarvam releases 105B-1711, an open-weight model priced at $0.15 per million tokens, with a lab-reported eight-benchmark average of 73.9 versus 42.6 in March"
sources:
  - title: "Introducing Sarvam-105B-1711 (read 22 November 2026)"
    url: "https://www.sarvam.ai/blogs/sarvam-105b-1711/"
    publisher: "Sarvam AI, 22 November 2026"
    primary: true
  - title: "sarvamai/sarvam-105b-1711 model card (NVFP4 build), read 22 November 2026"
    url: "https://huggingface.co/sarvamai/sarvam-105b-1711"
    publisher: "Hugging Face / Sarvam AI"
    primary: true
---

## What happened

On 22 November 2026 Sarvam AI, an Indian AI lab, announced Sarvam-105B-1711, which it describes as a new open-weight checkpoint of its Sarvam 105B model. Sarvam positions it as a "Flash-Lite"-class model for customer support, voice agents and agentic tasks, and says it was trained on upgraded NVIDIA B200 infrastructure.

All performance and price figures below are Sarvam's own, reported by the lab; we have not independently reproduced them.

## Key details

- **Headline claim:** across eight conversational-agent benchmarks, Sarvam reports an average of 73.9, up from 42.6 for its March 2026 Sarvam-105B. It reports a blended price of $0.15 per million tokens, down from $0.44.
- **Comparison table (Sarvam's):** Gemini 3.5 Flash-Lite 74.0 at $0.85 per million tokens; Qwen3.8 27B (xhigh) 74.6 at $0.96; Gemma 4 31B 73.0 at $0.54; GPT-6 Luna (high) 66.3 at $0.20; Nemotron 3 Super 62.2 at $0.17; Mistral Small 4 49.7 at $0.26. On this table Sarvam's model is level with the best-scoring rivals at the lowest listed price, but two models in it score slightly higher.
- **Selected scores (Sarvam's):** IFEval 96.5; IFBench 82.5 (32.5 in March); Tau2 average 85.5 (Qwen3.8 27B: 85.8); Tau2 telecom 98.9; GPQA Diamond 80.4; MMLU-Pro 85.2; Humanity's Last Exam without tools 12.3; Indic suite 79.1 (30.1 in March).
- **Model:** the Hugging Face card describes a 105B-parameter mixture-of-experts model with 10.3B active parameters (the NVFP4 repository's stored tensors total about 56B). It uses custom code (`trust_remote_code`).
- **Weights and licence:** NVFP4 weights (65 GB) are at `sarvamai/sarvam-105b-1711` and BF16 weights at `sarvamai/sarvam-105b-1711-bf16`. The Hugging Face metadata tags the licence as Apache-2.0; Sarvam's blog post names no licence, so check the repository before relying on it for commercial use.
- **Hardware:** Sarvam says the NVFP4 build runs on a single RTX PRO 6000 Blackwell workstation GPU at 99 tokens per second per user, and reaches about 6,000 tokens per second per B200 at 64 concurrent users. NVFP4 needs Blackwell-class FP4 hardware.
- **Availability:** live on Sarvam Token Factory. Sarvam also lists Sarvam Dictate at $0.32 per hour of audio, with reported character error rates of 5.0% (English) and 2.7% (Indian languages).
- **Training notes (Sarvam's):** 8-bit pretraining raised throughput from 5,500 to 10,900 tokens per second per GPU; context was extended to 160K tokens using 330B tokens. The post closes by saying the stack is ready to train much larger models.

## Why it matters

For teams building voice or support agents, especially in Indian languages, this is a lab-reported case of a small open-weight model approaching larger closed rivals on agent benchmarks at a fraction of the listed price. That claim rests on benchmarks Sarvam chose and ran; independent evaluations have not yet appeared.

Two practical limits: the 4-bit build targets recent NVIDIA Blackwell hardware, and the licence is clear only on the Hugging Face tag, not in the announcement. The hardware point and the closing line about larger models suggest Sarvam's next release may be bigger.

> Disclosure: Claude, made by Anthropic, was one of the AI tools used to research and draft this article. Details come from Sarvam's 22 November 2026 post and Hugging Face model card, read on 22 November 2026.
