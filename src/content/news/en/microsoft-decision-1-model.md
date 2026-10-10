---
title: "Microsoft releases Decision-1, a model that scores options instead of writing text, at $0.042 per million input tokens"
summary: "On 9 October 2026 Microsoft announced Microsoft-Decision-1, a model that returns a probability for each option you give it, for routing, classification and workflow control. It costs $0.042 per million input tokens with free output and is available in Microsoft Foundry and OpenRouter. Accuracy and speed claims are Microsoft's own, and no licence is stated."
seoTitle: "Microsoft Decision-1: $0.042 per million tokens"
seoDescription: "Microsoft's Decision-1 returns probabilities for routing and classification, costs $0.042 per million input tokens, and is in Foundry and OpenRouter."
lang: en
publishedAt: 2026-10-10T05:50:00Z
entities:
  - Microsoft
  - Microsoft-Decision-1
  - Microsoft Foundry
  - OpenRouter
  - Qwen3.5-9B
topics:
  - Models
  - Agents
  - Pricing
translationKey: microsoft-decision-1-model
image: /images/news/microsoft-decision-1-model-2026-10-09.jpg
imageAlt: "Deyron Labs graphic: Microsoft releases Decision-1, a model that scores options instead of writing text, at $0.042 per million input tokens with free output; claims are Microsoft's own"
sources:
  - title: "Introducing Microsoft-Decision-1, our model for fast decision-making"
    url: "https://commandline.microsoft.com/microsoft-decision-1-model-foundry/"
    publisher: "Microsoft"
    primary: true
  - title: "Introducing Microsoft-Decision-1 in Microsoft Foundry for decision and classification workloads"
    url: "https://techcommunity.microsoft.com/blog/azure-ai-foundry-blog/introducing-microsoft-decision-1-in-microsoft-foundry-for-decision-and-classific/4562742"
    publisher: "Microsoft Tech Community"
    primary: true
---

## What happened

On 9 October 2026 Microsoft announced Microsoft-Decision-1, a decision-scoring model. Unlike a chat model, it does not write text: given a fixed set of options, it returns a calibrated probability for each one, in a structured form that software can act on. Microsoft positions it for routing, classification, prioritization, verification and workflow control.

## Key details

Figures are Microsoft's unless stated otherwise.

- **What it is:** Microsoft says it post-trained Qwen3.5-9B for fast, single-pass decision scoring, and that it will soon rebase it on other models, including Microsoft AI (MAI) and OpenAI models. It supports yes/no, multiple-choice and rating options, plus rubric-based grading of AI responses and agent actions.
- **Price and availability:** $0.042 per million input tokens, with output tokens free. It is available in Microsoft Foundry and OpenRouter.
- **Licence:** the announcement does not state one.
- **Accuracy claim:** Microsoft says it had the highest accuracy in a 36-benchmark comparison covering nearly 150,000 questions kept out of training. The comparison set is Microsoft's own.
- **Speed claim:** Microsoft says it is about 4.5x faster than the runner-up in that comparison and about 35x faster than GPT-6 Sol at median latency.
- **Robustness:** Microsoft says it changes its decision on 1.3% of perturbed inputs on average, with no changes when option descriptions are paraphrased or the options are reordered or shuffled.
- **Safety testing:** Microsoft says it tested 5,250 requests across 11 benchmarks and that the model refused harmful behavior while staying useful.
- **Internal results:** Microsoft says its XBOX Research group found quality competitive with GPT-6 Sol at over 14x the speed and 200x lower cost.

## Why it matters

A lot of AI spending goes on asking a large model to make small yes-or-no or pick-one decisions, such as which queue a ticket belongs in or whether a response meets a rubric. A small model that returns probabilities for fixed options, at a few cents per million input tokens, is aimed at exactly that work, and the probabilities let a developer set their own thresholds.

All the performance claims come from Microsoft's own announcement and no independent evaluation or licence was published with it. Anyone considering it should test it on their own labelled examples and check the licence terms.

> Disclosure: Claude, made by Anthropic, was one of the AI tools used to research and draft this article. Anthropic is a competitor of Microsoft. Performance claims are Microsoft's own.
