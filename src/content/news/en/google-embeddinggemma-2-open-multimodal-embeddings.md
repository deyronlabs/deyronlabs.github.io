---
title: "Google releases EmbeddingGemma 2, an open 740M-parameter embedding model for text, images, video and audio"
summary: "Google DeepMind's EmbeddingGemma 2 maps text, code, images, video and audio into one 768-dimension embedding space. It has 740 million parameters in total, is released under Apache 2.0, and its encoders can be loaded selectively. The benchmark scores are Google's own."
lang: en
publishedAt: 2026-10-09T05:30:00Z
entities:
  - Google DeepMind
  - EmbeddingGemma 2
  - Gemma 4
topics:
  - Models
  - Open weights
  - Embeddings
translationKey: google-embeddinggemma-2-open-multimodal-embeddings
image: /images/news/google-embeddinggemma-2-open-multimodal-embeddings-2026-10-09.jpg
imageAlt: "Deyron Labs graphic: Google's EmbeddingGemma 2 is an open 740M embedding model for text, images, video and audio under Apache 2.0"
sources:
  - title: "EmbeddingGemma 2 model card"
    url: "https://ai.google.dev/gemma/docs/embeddinggemma/model_card_2"
    publisher: "Google AI for Developers"
    primary: true
---

## What happened

Google DeepMind published the model card for EmbeddingGemma 2, a multimodal embedding model that, according to the card, "builds upon the architectural and capability advancements of Gemma 4". The card is marked as last updated on 6 October 2026 and does not give a separate release date. We read it on 9 October 2026.

## Key details

- **Size and modalities:** 740 million parameters in total. Text and code (a 270M text model), images (a 170M encoder), video and audio (a 300M encoder) are mapped into one shared embedding space. The card says the model understands more than 100 languages.
- **Selective loading:** the encoders can be loaded separately, so the effective size is 270M for text only, 440M for text and images, 570M for text and audio, and 740M for everything.
- **Format:** 768 dimensions by default, with truncation to 512, 256 or 128 supported (embeddings must be re-normalized afterwards). The context length is 8,192 tokens, shared across modalities.
- **License and access:** Apache 2.0, with weights linked from Hugging Face and GitHub.
- **Benchmarks reported by Google (768 dimensions):** 61.36 on MTEB multilingual v2 (EmbeddingGemma 1: 61.15) and 78.68 on MTEB code (EmbeddingGemma 1: 68.76). The card says this is about a 14% improvement on code tasks. It also lists multimodal scores such as 57.28 on MMEB v2 image tasks.
- **Limitations named on the card:** performance may differ across languages, open-ended or highly complex tasks can be hard, 128 dimensions "degrades multimodal quality substantially", and float16 should not be used because it can return NaN or silently degraded embeddings.

## Why it matters

Embedding models sit behind search and retrieval-augmented generation. A single open model that covers text, images, video and audio, with a text-only configuration of 270M parameters, gives developers a permissively licensed option for searching mixed collections, for example spoken queries against an audio archive, which the card lists as a use case.

The text-only gain is small on the multilingual benchmark, and the larger gain is on code. All scores come from Google's model card; the card gives no independent comparison with models from other labs, so test it on your own data before switching.

> Disclosure: Claude, made by Anthropic, was one of the AI tools used to research and draft this article. Claims about the model are Google's own.
