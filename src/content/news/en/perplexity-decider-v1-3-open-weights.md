---
title: "Perplexity releases Decider v1.3, an open-weight decision model, and reports 91.6% on 63 classification tasks"
summary: "On 12 November 2026 Perplexity published Decider v1.3 and a smaller Decider Flash v1.3, models that return probabilities for yes/no, multiple-choice and score questions and can extract exact text spans. Perplexity says the weights are on Hugging Face under an Apache license and reports its own benchmark results."
seoTitle: "Perplexity Decider v1.3 open-weight model"
seoDescription: "Perplexity's Decider v1.3 (12 Nov 2026) scores yes/no and choice questions; weights on Hugging Face under Apache, per Perplexity. Figures are its own."
lang: en
publishedAt: 2026-11-14T07:05:00Z
entities:
  - Perplexity
  - Decider v1.3
  - Decider Flash v1.3
  - Hugging Face
  - OpenRouter
  - Qwen
topics:
  - Models
  - Open-weight
  - Agents
translationKey: perplexity-decider-v1-3-open-weights
image: /images/news/perplexity-decider-v1-3-open-weights-2026-11-12.jpg
imageAlt: "Deyron Labs graphic: Perplexity Decider v1.3: open-weight decision model; Yes/no, choice and score questions with probabilities; Weights on Hugging Face under Apache, per Perplexity; 91.6% mean accuracy on 63 tasks (Perplexity's own); Cost for 1M requests: $26.47 (Flash $13.24)"
sources:
  - title: "Perplexity Decider v1.3: Training, eval, and use cases"
    url: "https://www.perplexity.ai/hub/blog/perplexity-decider"
    publisher: "Perplexity Research, 12 November 2026"
    primary: true
---

## What happened

On 12 November 2026 Perplexity Research published "Perplexity Decider v1.3: Training, eval, and use cases". Decider is a general-purpose classifier: for yes/no, multiple-choice and score questions it returns a probability distribution over the answers. Version 1.3 also adds a "locate" feature that extracts exact text spans, such as named entities, personal data or answers to extractive questions. A smaller Decider Flash v1.3 is distilled from it.

## Key details

All figures are Perplexity's own, from its post read on 14 November 2026. We have not run the models.

- **Availability:** Perplexity says the weights are downloadable from Hugging Face under an Apache license, and that the models are also offered through OpenRouter and the Perplexity Decisions API.
- **Base models (as stated):** Decider was trained from Qwen3.8-27B and Flash was distilled to Qwen3.5-4B. Perplexity says the design was inspired by TypeSafe AI's Jev.
- **Accuracy claims:** 91.6% mean accuracy over 63 classification tasks (6.54 points above Perplexity's production classifiers); 83.99 mean nDCG@10 over 72 retrieval tasks (1.81 above Qwen3-Reranker-8B); 88.16% mean multilingual accuracy; 93.98% agreement with LLM judges on 1 million real requests (93.35% for Jev 1.14).
- **Locate:** an average score of 69.0 versus 43.3 for Liquid's d1, per Perplexity.
- **Cost comparison for 1 million requests:** $26.47 for Decider v1.3, $13.24 for Flash, $68.10 for Jev 1.14, $312.21 for GLM-5.3-Flash and $349.48 for DeepSeek V4.1 Flash. Perplexity notes these are workload-specific.
- **Not stated:** a per-token API price, and independent evaluations.

## Why it matters

Decision models are becoming a standard category: small, cheap models for routing, grading and checking rather than for chat. Google, Microsoft and OpenAI have launched their own versions and Liquid released open d1 models; all but the last are covered on this site. Perplexity's entry is notable for open weights under a permissive license, which lets developers run it themselves.

The comparisons are against Perplexity's own baselines and chosen tasks, so a test on your own labelled data is the fair check. The license and exact weights listing on Hugging Face should be confirmed before use in a product.

> Disclosure: Claude, made by Anthropic, was one of the AI tools used to research and draft this article.