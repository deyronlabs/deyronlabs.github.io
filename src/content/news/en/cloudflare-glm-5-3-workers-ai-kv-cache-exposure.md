---
title: "Cloudflare discloses GLM-5.3 Workers AI bug that exposed cached data across requests in 155 responses"
summary: "Cloudflare says a configuration mismatch on its hosted GLM-5.3 model triggered an SGLang bug that exposed KV cache pages across requests, affecting 155 responses between 27 August and 9 September 2026. Cloudflare reports no evidence of deliberate exploitation and says the model was restored on 9 September."
seoTitle: "Cloudflare GLM-5.3 Workers AI cache exposure"
seoDescription: "Cloudflare reports an SGLang bug on its hosted GLM-5.3 exposed KV cache across requests in 155 responses, from 27 August to 9 September 2026."
lang: en
publishedAt: 2026-10-28T18:00:00Z
entities:
  - Cloudflare
  - Workers AI
  - GLM-5.3
  - Z.ai
  - SGLang
  - RadixArk
  - Knostic
topics:
  - Security
  - Models
translationKey: cloudflare-glm-5-3-workers-ai-kv-cache-exposure
image: /images/news/cloudflare-glm-5-3-workers-ai-kv-cache-exposure-2026-10-28.jpg
imageAlt: "Deyron Labs graphic: Cloudflare Workers AI GLM-5.3 KV cache exposure, 155 responses affected, 27 August to 9 September 2026, per Cloudflare's 26 October 2026 post"
sources:
  - title: "Cross-request KV cache exposure in the GLM-5.3 Workers AI model, and our remediation with SGLang (Cloudflare)"
    url: "https://blog.cloudflare.com/kv-cache-exposure-remediation/"
    publisher: "Cloudflare"
    primary: true
---

## What happened

On 26 October 2026 Cloudflare published a post-mortem on a bug in its hosted version of the GLM-5.3 model (`@cf/zai-org/glm-5.3`) on Workers AI. In the post's words, "a configuration mismatch in GLM 5.3 on Workers AI triggered an SGLang bug that exposed KV cache pages across requests." Cloudflare says a researcher reported the issue on 8 September 2026 and that it took the model offline on 9 September before restoring it that evening. Cloudflare says it found no evidence of deliberate exploitation.

## Key details

- **Scope (per Cloudflare):** only GLM-5.3 on Workers AI was affected, from its launch on 27 August until 9 September. Cloudflare counts 155 affected responses, all to prompts longer than 681,280 tokens.
- **Cause 1, configuration:** the model was deployed with a 1,048,576-token context window, but the prefill KV pool held only 681,280 tokens.
- **Cause 2, software:** in the SGLang inference engine, over-length requests were marked rejected but not caught in disaggregated prefill/decode mode, so the decode step read stale KV cache pages from earlier requests and still returned HTTP 200. Cloudflare says pages are not zeroed between requests.
- **Fixes:** Cloudflare raised the prefill KV pool to about 2.04 million tokens, contributed an upstream SGLang patch that retires rejected requests before any KV transfer, and says fixes are in SGLang v0.5.20 to v0.5.22. It also added a per-deployment check of KV pool size against context length.
- **Advice to operators:** check KV pool size against context length on every node and upgrade to SGLang v0.5.22 or later.
- **Note on sources:** the model is made by Z.ai; the fault described is in Cloudflare's deployment and the open-source SGLang engine, not in the model's weights. Figures here are Cloudflare's own and were read from its post on 28 October 2026.

## Why it matters

Self-hosted and hosted inference stacks reuse large memory caches to be fast, and this incident shows that a mismatch between a configured context length and the memory actually reserved can leak one customer's prompt data into another's response without any error. Anyone running long-context models on SGLang or similar engines has a concrete check to run. The reported impact is small and Cloudflare describes no malicious use, but the content of the 155 responses is not public, so the real-world sensitivity of what leaked cannot be assessed from the post.

> Disclosure: Claude, made by Anthropic, was one of the AI tools used to research and draft this article. Details come from Cloudflare's post, read on 28 October 2026.
