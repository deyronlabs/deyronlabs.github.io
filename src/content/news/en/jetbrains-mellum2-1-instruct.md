---
title: "JetBrains releases Mellum2.1 Instruct, a 12B open-weight coding model that answers without chain-of-thought"
summary: "JetBrains published Mellum2.1 Instruct on 25 November 2026: a 12B mixture-of-experts coding model with 2.5B active parameters, released under Apache 2.0 on Hugging Face. It answers without chain-of-thought, which JetBrains says uses about half the tokens of its Thinking sibling while scoring almost as well on SWE-bench Verified. All figures are JetBrains' own."
seoTitle: "JetBrains Mellum2.1 Instruct: 12B coding model"
seoDescription: "JetBrains' Mellum2.1 Instruct is a 12B MoE (2.5B active) open-weight coding model under Apache 2.0, announced 25 Nov 2026, with no chain-of-thought."
lang: en
publishedAt: 2026-11-26T12:00:00Z
entities:
  - JetBrains
  - Mellum2.1 Instruct
  - Mellum2.1 Thinking
  - Qwen3.5 9B
  - Gemma 4 E4B
  - NVIDIA NeMo RL
topics:
  - Models
  - Open-weight
  - Coding
translationKey: jetbrains-mellum2-1-instruct
image: /images/news/jetbrains-mellum2-1-instruct.jpg
imageAlt: "Deyron Labs graphic: JetBrains Mellum2.1 Instruct, a 12B mixture-of-experts coding model with 2.5B active parameters under Apache 2.0, answering without chain-of-thought; figures are JetBrains' own"
sources:
  - title: "Mellum2.1 Instruct is out, bringing faster answers for coding agents"
    url: "https://blog.jetbrains.com/ai/2026/11/mellum2-1-instruct-is-out-bringing-faster-answers-for-coding-agents/"
    publisher: "JetBrains AI Blog (Gleb Ingman), 25 November 2026, read 26 November 2026"
    primary: true
---

## What happened

On 25 November 2026 JetBrains published **Mellum2.1 Instruct**, the sibling of Mellum2.1 Thinking (released on 8 October 2026). It uses the same architecture and the same training recipe, but it responds directly instead of producing a chain of thought first. JetBrains positions it for sub-agents, tool-calling loops and chat, where a long reasoning trace costs time and tokens.

## Key details

- **Architecture:** a 12-billion-parameter mixture-of-experts model with 2.5 billion active parameters, the same as Mellum2.1 Thinking.
- **Training:** large-scale reinforcement learning on repository-level tasks in real environments, using NVIDIA NeMo RL and NeMo Megatron-Bridge on H200 and B300 clusters; JetBrains says this involved about half a million agent trajectories from 10,000 concurrent sandboxes.
- **Token use and accuracy (JetBrains' figures):** on agentic tasks it generates about half the tokens of the Thinking variant and "performs almost as well" on SWE-bench Verified. Its SWE-bench Verified score is double that of Mellum2 Instruct. JetBrains says Qwen3.5 9B still scores higher on SWE-bench Verified, that Mellum2.1 Instruct leads the compared group on code generation and is on par with Qwen3.5 9B on multi-step tool use. The comparison also includes Gemma 4 E4B with thinking switched off. The benchmark table is an image, and we could not read exact values from it.
- **Speed:** about 1.4x faster than Qwen3.5 9B for a single request. The post also cites 1.8x under load, a figure taken from JetBrains' October post on the Thinking model.
- **Availability:** both variants are on Hugging Face under Apache 2.0, with GGUF builds for Instruct and Thinking and a multi-token-prediction (MTP) head that JetBrains says can be up to 1.8x faster. Mellum2.1 Thinking remains stronger on LiveCodeBench and AIME, according to JetBrains.
- **Not stated:** the post gives no independent evaluation, no API pricing and no context length.

## Why it matters

Small open-weight coding models matter most when they run cheaply inside agent loops, and skipping chain-of-thought is a direct lever on that cost. Apache 2.0 weights and GGUF builds mean teams can try it locally without a licensing review. The trade-off is visible in JetBrains' own numbers: it gives up some accuracy to Thinking and trails Qwen3.5 9B on SWE-bench Verified, so the speed gain is only worth it for tasks where that gap does not decide the outcome. Independent benchmark runs are the missing piece.

> Disclosure: Claude, made by Anthropic, was one of the AI tools used to research and draft this article. JetBrains is not affiliated with Deyron Labs; all claims are JetBrains' own.
