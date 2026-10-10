---
title: "Cloudflare launches Clef-omni, cuts Clef-flash price by about 58% and makes Clef up to 2x faster"
summary: "On 9 October 2026 Cloudflare released Clef-omni, an open-weight model that takes text, images, audio and video, and cut the price of Clef-flash from $0.09 to $0.038 per million input tokens. Cloudflare says hosted Clef is now about 1.7 to 2x faster. The hosted Clef-flash context window drops from 64k to 24k tokens. Benchmarks are Cloudflare's own."
seoTitle: "Cloudflare Clef-omni; Clef-flash 58% cheaper"
seoDescription: "Cloudflare's Clef-omni takes text, image, audio and video, and Clef-flash now costs $0.038 per million input tokens, down from $0.09, per Cloudflare."
lang: en
publishedAt: 2026-10-10T05:40:00Z
entities:
  - Cloudflare
  - Clef-omni
  - Clef
  - Clef-flash
  - Workers AI
  - Qwen3-Omni
topics:
  - Models
  - Open weights
  - Pricing
translationKey: cloudflare-clef-omni-flash-price-cut
image: /images/news/cloudflare-clef-omni-flash-price-cut-2026-10-09.jpg
imageAlt: "Deyron Labs graphic: Cloudflare launches Clef-omni and cuts Clef-flash to $0.038 per million input tokens from $0.09; hosted Clef-flash context falls from 64k to 24k tokens; figures are Cloudflare's own"
sources:
  - title: "Introducing Clef-omni with full multimodality, plus a faster Clef and a cheaper Clef-flash"
    url: "https://blog.cloudflare.com/clef-faster-cheaper-multimodal/"
    publisher: "Cloudflare"
    primary: true
  - title: "Cloudflare/clef-omni (model metadata)"
    url: "https://huggingface.co/Cloudflare/clef-omni"
    publisher: "Hugging Face"
    primary: true
---

## What happened

On 9 October 2026 Cloudflare published "Introducing Clef-omni with full multimodality, plus a faster Clef and a cheaper Clef-flash". It describes three changes to its Clef family of models, which run on its Workers AI platform and are tagged on Hugging Face as decision models for structured output and classification: a new model, Clef-omni, that accepts text, images, audio and video; faster hosted serving for Clef; and a lower price for Clef-flash.

## Key details

Figures are Cloudflare's unless stated otherwise.

- **Clef-omni:** accepts text, images, audio (WAV or MP3) and video (MP4 or WebM, with synced audio) in one pipeline. Cloudflare says it is built on Qwen3-Omni-30B-A3B-Instruct, a mixture-of-experts model, with the text-to-speech components removed, and was trained with frozen backbone weights and LoRA adapters. Launch price is $0.15 per million input tokens.
- **Licence:** the blog post links to open weights on Hugging Face but does not state a licence. The Hugging Face metadata for Cloudflare/clef-omni (created 9 October 2026) lists apache-2.0 and Qwen/Qwen3-Omni-30B-A3B-Instruct as the base model.
- **Clef-flash price:** $0.038 per million input tokens, down from $0.09, a cut of about 58% (our calculation from Cloudflare's two prices). Cloudflare says it is now cheaper than Jev; the post does not give Jev's price.
- **Clef-flash context:** the hosted context window falls from 64k to 24k tokens. Cloudflare says 0.24% of requests exceed 24k, and that the open weights still support 256k if you self-host.
- **Clef:** price unchanged at $0.24 per million input tokens, context stays at 64k. Cloudflare says hosted median latency fell from 262 to 152 ms at about 800 tokens (1.7x), from 616 to 305 ms at about 3,400 tokens (2.0x) and from 2,721 to 1,635 ms at about 16,000 tokens (1.7x), mostly from moving serving to SGLang.
- **Clef-omni speed:** about 130 ms median for text-only decisions, about 150 ms for images, a few hundred ms for audio clips and about 1.5 seconds for a 21-second video with sound in one call.
- **Benchmarks:** Cloudflare's table compares Clef-omni, Clef, Clef-flash and Jev. Clef-omni scores 98.2 on BFCL (Jev 95.75), 94.8 on BANKING77 (Jev 79.74) and 97.7 on CLINC150+OOS (Jev 89.27). Jev scores higher on When2Call (80.97 against 63.3 for Clef-omni) and BRIGHT (47.52 against 42.0). Clef-flash scores 66.77 on CLINC150+OOS against Jev's 89.27. Cloudflare also says Clef-omni scores below Clef on its invoice-processing and security-incident workflow evaluations.
- **Availability:** Clef-omni is on Workers AI. Clef works through AI Gateway and is Jev-API compatible, so switching needs only a model ID change, according to Cloudflare.

## Why it matters

For teams that use small models for routine decisions such as routing, tagging or screening, the Clef-flash price cut is large, but it comes with a smaller hosted context window. Cloudflare says few requests exceed it, so check your own prompt lengths before switching.

Clef-omni is the more notable change for developers who want one open model that can read audio and video as well as text and images. As with any launch, the comparisons come from the vendor and use a table it chose, and they are mixed: Clef-omni leads on several tests and trails Jev on others. Test it on your own data before relying on it.

> Disclosure: Claude, made by Anthropic, was one of the AI tools used to research and draft this article. Figures and comparisons are Cloudflare's own unless stated otherwise.
