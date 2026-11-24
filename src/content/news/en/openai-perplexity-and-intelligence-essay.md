---
title: "OpenAI's chief scientist proposes perplexity as a shared yardstick and floats 'common limits' for AI labs"
summary: "In a 22 November 2026 essay, OpenAI chief scientist Jakub Pachocki argues that perplexity, or cross-entropy loss, should be established as a metric for comparing developers and informing shared safety standards. He says models below about 0.8 log-perplexity on OpenAI's internal code data showed emerging cybersecurity and math capabilities, and that a wave of pretraining advances is possible as soon as 2027."
seoTitle: "OpenAI essay: perplexity as a shared yardstick"
seoDescription: "OpenAI's Jakub Pachocki argued on 22 Nov 2026 for perplexity as a common metric, tying sub-0.8 log-perplexity to emerging cyber and math skills."
lang: en
publishedAt: 2026-11-22T19:17:00Z
updatedAt: 2026-11-24T09:56:00Z
entities:
  - OpenAI
  - Jakub Pachocki
  - Microsoft AI
  - MAI-2 Base
topics:
  - Research
  - Safety
  - Policy
translationKey: openai-perplexity-and-intelligence-essay
image: /images/news/openai-perplexity-and-intelligence-2026-11-22.jpg
imageAlt: "Deyron Labs graphic: OpenAI's chief scientist proposes perplexity as a shared yardstick for AI progress and predicts possible pretraining advances as soon as 2027"
sources:
  - title: "Perplexity and Intelligence (read 22 November 2026)"
    url: "https://openai.com/index/perplexity-and-intelligence/"
    publisher: "OpenAI, Jakub Pachocki, 22 November 2026"
    primary: true
  - title: "Post by Mustafa Suleyman on MAI-2 Base log-perplexity (read 24 November 2026; figure is self-reported)"
    url: "https://x.com/mustafasuleyman/status/2124663594449318173"
    publisher: "Mustafa Suleyman (Microsoft AI) on X, 23 November 2026"
    primary: true
---

## What happened

On 22 November 2026 OpenAI published "Perplexity and Intelligence", an essay by its chief scientist, Jakub Pachocki. The piece is about the perplexity metric (how well a language model predicts text), not about the company Perplexity. It argues for establishing perplexity, or equivalently cross-entropy loss, as a metric for comparing AI developers and informing shared safety standards.

This is a position essay from OpenAI. The figures and predictions below are OpenAI's own, and we have not verified them.

## Update, 24 November 2026

Microsoft AI CEO Mustafa Suleyman said on X on 23 November that Microsoft AI "fully support[s] OpenAI's transparency initiative" and, with OpenAI's permission, reported its MAI-2 Base model at a log-perplexity of 0.819 on OpenAI's evaluation set, which he described as "in the same ballpark as the GPT-5.6 Sol base model". He wrote that the model uses the same tokenizer as OpenAI, so the numbers are directly comparable, and floated bits-per-byte and other evaluation sets for the future. The figure is Microsoft AI's own, was not independently evaluated, and we did not read a Microsoft AI web page. The post states support for the transparency initiative; it does not say Microsoft agreed to the "common limits" proposal.

## Key details

- **Measurements OpenAI cites:** log-perplexity on an OpenAI internal held-out codebase dataset of roughly 0.99 for GPT-3.5 and 0.91 for GPT-4. OpenAI says models below about 0.8 are linked to emerging cybersecurity and math capabilities, and that a model near 0.76 started producing groundbreaking results on open math problems.
- **Forecast:** the essay says a sudden wave of pretraining advances is possible as soon as 2027, and expects further capabilities in a window of roughly 0.68 to 0.7 log-perplexity.
- **Proposal:** "common limits" based on perplexity and other metrics, which labs would agree not to cross.
- **Caveats stated by the author:** labs use different datasets, perplexity is not tied to specific tasks, chain-of-thought reasoning does not reduce perplexity, and the entropy floor is unknown.

## Why it matters

If labs accepted a common loss-based yardstick, it would give regulators and outside evaluators a number that does not depend on a specific benchmark. It would also expose how far each lab's models have moved, which labs may not want to disclose.

The proposal is early. The numbers come from one lab's private dataset, so they cannot be compared across labs today, and the essay itself lists reasons the metric is incomplete. The essay does not say whether other labs will adopt such limits; Microsoft AI has so far backed the transparency effort and shared one number, and we have not seen a statement from Anthropic, which makes Claude.

> Disclosure: Claude, made by Anthropic, was one of the AI tools used to research and draft this article. Anthropic is a competitor of OpenAI. Details come from OpenAI's 22 November 2026 essay, read on 22 November 2026, and Mustafa Suleyman's 23 November 2026 post, read on 24 November 2026.
