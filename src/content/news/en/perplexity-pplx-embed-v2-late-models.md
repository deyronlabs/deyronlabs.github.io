---
title: "Perplexity releases pplx-embed-v2-late, 9B and 0.6B late-interaction embedding models for text and images"
summary: "On 7 October 2026 Perplexity published two ColBERT-style late-interaction embedding models, pplx-embed-v2-late-9B and 0.6B, for text and image retrieval with a shared embedding space. Both are on Hugging Face; the post names no license or price. Benchmark numbers are Perplexity's own."
lang: en
publishedAt: 2026-10-09T05:30:00Z
entities:
  - Perplexity
  - pplx-embed-v2-late-9B
  - pplx-embed-v2-late-0.6B
  - Hugging Face
topics:
  - Models
  - Embeddings
  - Retrieval
translationKey: perplexity-pplx-embed-v2-late-models
image: /images/news/perplexity-pplx-embed-v2-late-models-2026-10-09.jpg
imageAlt: "Deyron Labs graphic: Perplexity releases pplx-embed-v2-late, two late-interaction embedding models for text and images; benchmarks are Perplexity's own"
sources:
  - title: "Multimodal embeddings beyond a single vector"
    url: "https://www.perplexity.ai/hub/blog/multimodal-embeddings-beyond-a-single-vector"
    publisher: "Perplexity"
    primary: true
---

## What happened

On 7 October 2026, Perplexity Research published "Multimodal embeddings beyond a single vector", introducing a family of late-interaction models for text and image retrieval. Late interaction keeps token-level vectors instead of compressing a document into one vector. The post says both models "are publicly available on Hugging Face".

## Key details

All numbers below are Perplexity's own, as reported in its post.

- **Models:** pplx-embed-v2-late-9B, described as the maximum-quality option and distilled from an 18B teacher, and pplx-embed-v2-late-0.6B, with 594M total parameters, pruned from a Qwen3.5-0.8B starting point. Both output 128-dimensional token embeddings and share one embedding space.
- **Retrieval results:** on domain-specific text retrieval (72 tasks, nDCG@10), 81.3% for the 9B model and 78.0% for the 0.6B model; on ViDoRe(V3) visual documents (nDCG@10), 65.2% and 62.3%.
- **Other results:** Q2D-Web Recall@1000 of 74.8% (9B) and 73.6% (0.6B) against a previous best of 69.3%; MADQA accuracy of 92.4% and 90.1%; and BrowseComp+ accuracy of 64.0% for the 9B model.
- **Claim about the small model:** Perplexity says its 0.6B model "matches models with five times as many active parameters".
- **Not in the post:** a license, a price, and a timeline for the API. Perplexity says it plans to offer late-interaction, dense and contextual embeddings on its API Platform later.

## Why it matters

Late-interaction models can retrieve more precisely than single-vector embeddings, at the cost of storing many vectors per document. A 0.6B model that Perplexity says holds up against much larger ones would be easier to run, if the results replicate.

Without a stated license, developers should read the Hugging Face model cards before using the models commercially, and test them on their own data, since all benchmarks come from Perplexity.

> Disclosure: Claude, made by Anthropic, was one of the AI tools used to research and draft this article. Claims and benchmarks are Perplexity's own.
