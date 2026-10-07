---
title: "Mistral releases Mistral Large 4, a 1-trillion-parameter model, in public preview"
summary: "Mistral AI released Mistral Large 4 in public preview on 6 October 2026: a natively multimodal mixture-of-experts model with 1 trillion parameters, 49 billion of them active, priced at $1.36 per million input tokens and $4.18 per million output tokens. Mistral says the weights will follow by the end of October."
lang: en
publishedAt: 2026-10-07T09:20:00Z
updatedAt: 2026-10-07T14:25:00Z
entities:
  - Mistral AI
  - Mistral Large 4
  - Mistral Studio
  - NVIDIA Grace Blackwell
  - GPT-6 Astra
  - Claude Opus 5.5
topics:
  - Models
  - Europe
  - Open weights
  - Cybersecurity
translationKey: mistral-large-4-public-preview
video: "https://www.youtube.com/shorts/lLlb8gijzTg"
videoPublishedAt: 2026-10-07
image: /images/news/mistral-large-4-2026-10-06.jpg
imageAlt: "Deyron Labs graphic: Mistral Large 4 has 1 trillion parameters and its weights are due by the end of October"
sources:
  - title: "Introducing Mistral Large 4"
    url: "https://mistral.ai/news/mistral-large-4/"
    publisher: "Mistral AI"
    primary: true
  - title: "OpenAI launches GPT-6 Astra"
    url: "https://www.constellationr.com/insights/news/openai-launches-gpt-6-astra"
    publisher: "Constellation Research"
  - title: "OpenAI Launches GPT-6 Astra: Pricing, Benchmarks and Who Gets It First"
    url: "https://pasqualepillitteri.it/en/news/14246/openai-launches-gpt-6-astra-pricing-benchmarks"
    publisher: "Pasquale Pillitteri"
---

## What happened

On 6 October 2026, Mistral AI announced Mistral Large 4, which the company nicknames "le Chonk" in its post. It is a natively multimodal model with 1 trillion parameters, of which 49 billion are active at a time, and it combines instruction-following and reasoning in one mixture-of-experts design aimed at enterprise workloads.

The model is available now as a public preview through the Mistral Studio API. Mistral says the weights "drop end of this month," with technical details on the architecture and post-training to follow. The company says it trained the model on 3,800 NVIDIA Grace Blackwell GPUs in its own datacenters in Europe, and that it supports more than 160 languages, including every official language of the European Union.

## Key details

- **Price:** $1.36 per million input tokens and $4.18 per million output tokens (Mistral).
- **Availability:** several regions worldwide, including a European deployment that Mistral says it operates end to end by itself.
- **Weights:** promised by the end of October 2026. The announcement does not state a license, so it is not yet clear how freely the weights can be used.
- **Cybersecurity, as reported by Mistral:** 82% on a vulnerability reproduction and patching test, which Mistral calls the highest of any model; 93% of the challenges in Cybench; and 93.3% resistance to attacks on the B3 benchmark. Mistral says Claude Opus 5.5 and GPT-6 Astra score close to zero on the same vulnerability test because they refuse the task.
- **Coding, as reported by Mistral:** 61.7% on DeepSWE v1.1, 59.4% on SWE-Atlas-QnA and 28.3% on Terminal-Bench 4.
- **Other claims from Mistral:** 59.9% on AutomationBench across 657 business workflows, and 42% versus 41% for GPT-6 Astra on the Dense 200 visual grounding test.
- **What is still open:** Mistral says its reinforcement learning run is still in progress and that the model continues to improve. We found no independent evaluations at the time of writing, so every benchmark figure above comes from Mistral itself.

## Why it matters

Price is the clearest signal. At $1.36 and $4.18, Mistral Large 4 costs roughly one seventh as much per input token and one twelfth as much per output token as GPT-6 Astra's reported standard rates of $10 and $50. Per-token price is only half of the picture, since OpenAI argues that cost per completed task is the better measure. Run your own tasks before you compare.

The weights are the second signal. If they arrive by the end of October and the license allows it, teams that need to run a model on their own infrastructure or inside the EU gain a very large option. Until the license is published, treat "open weights" as a promise, not a product.

The cybersecurity result deserves care. Higher scores on a test that rivals refuse may reflect a different safety policy rather than a stronger model, and a model that does not refuse is a different tool for defenders and for attackers. Wait for independent tests before you rely on it for that work.

> Disclosure: Anthropic, the maker of Claude, is named in Mistral's comparison above, and Claude was one of the AI tools used to research and draft this article. Performance and pricing claims are the companies' own unless stated otherwise.
