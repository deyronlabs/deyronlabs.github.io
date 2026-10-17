---
title: "DeepSeek updates V4.1-Flash to the 1017 snapshot, with unchanged API prices and its own search engine"
summary: "DeepSeek's API changelog for 17 October 2026 says the deepseek-flash model now points to V4.1-Flash-1017, which it says cuts task runtime and output length. Prices and API calls are unchanged. DeepSeek lists 77.0 on DeepSWE v1.1; we found no open weights for this snapshot yet."
seoTitle: "DeepSeek V4.1-Flash-1017: same price, faster"
seoDescription: "DeepSeek updated deepseek-flash to V4.1-Flash-1017 on 17 October 2026: unchanged pricing, 77.0 on DeepSWE v1.1 (its own figure) and a new search engine."
lang: en
publishedAt: 2026-10-17T20:00:00Z
entities:
  - DeepSeek
  - DeepSeek-V4.1-Flash
  - DeepSeek-V4.1-Flash-1017
  - DeepSeek Harness
topics:
  - Models
  - China
translationKey: deepseek-v4-1-flash-1017-update
sources:
  - title: "DeepSeek API docs: updates, entry of 2026-10-17 (DeepSeek-V4.1-Flash-1017)"
    url: "https://api-docs.deepseek.com/updates"
    publisher: "DeepSeek"
    primary: true
  - title: "deepseek-ai models on Hugging Face (listing checked 17 October 2026)"
    url: "https://huggingface.co/api/models?author=deepseek-ai&sort=createdAt&direction=-1&limit=5"
    publisher: "Hugging Face"
    primary: true
---

## What happened

On 17 October 2026, DeepSeek's API changelog added an entry for **DeepSeek-V4.1-Flash-1017**. The `deepseek-flash` model name now points to this upgraded version, and the models in DeepSeek's web chat and app were updated too. The previous V4.1-Flash launched on 10 September 2026.

DeepSeek says the API calling method and pricing remain unchanged.

## Key details

- **What DeepSeek claims:** compared with the previous V4.1, the update reduces task runtime and output length, so tasks cost less and finish faster. The changelog recommends DeepSeek Harness 0.2.1-rc.1 or later.
- **Benchmarks (DeepSeek's own figures, no independent evaluation found):** 77.0 on DeepSWE v1.1, 42.6 on Humanity's Last Exam without tools, 42.3 on Terminal-Bench 4.0, 68.2 on NL2Repo-Bench and 72.1 on Apex Bench v1.1. The changelog gives no scores for the previous version, so it does not show how large the improvement is.
- **Search:** web and API search now run on DeepSeek's own search engine, which DeepSeek says indexes hundreds of billions of pages and filters SEO spam and low-quality AI-generated content. Some press reports give a price for the search API; we did not find it in the changelog and do not repeat it.
- **Weights:** the earlier V4.1-Flash is on Hugging Face under an MIT license tag. When we checked the `deepseek-ai` listing on 17 October, no 1017 repository had appeared yet, although some press reports say the weights are out. We treat open weights for this snapshot as unconfirmed.

## Why it matters

For developers already calling `deepseek-flash`, the model behind the name changed without any change to code or price, so results and output length may shift on their own. The benchmark numbers are DeepSeek's and should be checked against independent tests before anyone treats them as a ranking. The open-weights question is worth rechecking in the coming days.
