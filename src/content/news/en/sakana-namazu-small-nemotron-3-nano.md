---
title: "Sakana AI announces Namazu Small, a 30B reasoning model built on NVIDIA's Nemotron 3 Nano base"
summary: "Sakana AI announced Namazu Small on 25 November 2026, a 30-billion-parameter reasoning model built on the pretrained base of NVIDIA Nemotron 3 Nano. Sakana reports it beats Nemotron 3 Nano and Super on average across 25 benchmarks, mainly in web search and long-document tasks; on-premises delivery is planned for December."
seoTitle: "Sakana Namazu Small: 30B on Nemotron 3 Nano"
seoDescription: "Sakana AI's Namazu Small is a 30B reasoning model built on Nemotron 3 Nano; Sakana reports BrowseComp 73.5 versus 29.3 for Nemotron Nano."
lang: en
publishedAt: 2026-11-26T07:31:00Z
entities:
  - Sakana AI
  - Namazu Small
  - NVIDIA
  - Nemotron 3 Nano
  - Nemotron 3 Super
topics:
  - Models
  - Enterprise
translationKey: sakana-namazu-small-nemotron-3-nano
image: /images/news/sakana-namazu-small-nemotron-3-nano.jpg
imageAlt: "Deyron Labs graphic: Sakana AI's Namazu Small, a 30B reasoning model on NVIDIA's Nemotron 3 Nano base; Sakana reports BrowseComp 73.5 versus 29.3 for Nemotron 3 Nano"
sources:
  - title: "Sakana Namazu Small"
    url: "https://sakana.ai/namazu-small/"
    publisher: "Sakana AI, 25 November 2026, read 26 November 2026"
    primary: true
---

## What happened

On 25 November 2026 Sakana AI announced **Namazu Small**, a reasoning model with 30 billion parameters. According to Sakana, it is built on the pretrained base of NVIDIA's Nemotron 3 Nano, with continued pretraining and post-training done by Sakana. The announcement page states no license, price or public download; it says on-premises delivery is planned and that details will follow in "early-to-mid December 2026".

## Key details

- **Comparison set:** Sakana compares Namazu Small with NVIDIA's own post-trained Nemotron 3 Nano (30B-A3B) and Nemotron 3 Super (120B-A12B), and says it "outperformed" both on average across 25 benchmarks.
- **Selected figures (Nano / Super / Namazu Small, from Sakana's table):** BrowseComp 29.3 / 36.1 / 73.5; FRAMES 82.2 / 86.0 / 85.0; LongBench v2 44.3 / 53.1 / 45.7; LLM-jp LongBench 67.0 / 60.0 / 86.0; SimpleQA Verified 9.1 / 18.1 / 6.8.
- **Where it does not improve:** Sakana says the gains are mainly in web search and long-document tasks, and that knowledge tasks improved little. Its own table shows Namazu Small below Nemotron 3 Super on FRAMES, LongBench v2 and SimpleQA Verified.
- **Verification:** all numbers are reported by Sakana; we found no independent evaluation.

## Why it matters

The result shows how much post-training can change a small base model on agentic web-search tasks, at least on Sakana's chosen benchmarks. For buyers in Japan, the planned on-premises delivery is the practical detail, but without a stated license, price or open weights, the model cannot yet be tried outside Sakana's own channels. Independent tests of BrowseComp-style tasks would show whether the gap holds.

> Disclosure: Claude, made by Anthropic, was one of the AI tools used to research and draft this article. Sakana AI is not affiliated with Deyron Labs; all claims are Sakana AI's own.
