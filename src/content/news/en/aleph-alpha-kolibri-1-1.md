---
title: "Aleph Alpha releases Kolibri 1.1, an Apache 2.0 English-German MoE with 75B total and 3B active parameters"
summary: "Aleph Alpha released Kolibri 1.1 on 23 November 2026, seven weeks after Kolibri 1.0. The company says the Apache 2.0 model scores 73.2 overall versus 66.6 for 1.0 and uses 3.4 times less GPU time per task. All figures are self-reported."
seoTitle: "Aleph Alpha Kolibri 1.1: 75B MoE, Apache 2.0"
seoDescription: "Aleph Alpha released Kolibri 1.1 on 23 Nov 2026: a 75B/3B-active English-German MoE with 1M context under Apache 2.0; benchmarks are self-reported."
lang: en
publishedAt: 2026-11-24T07:30:00Z
entities:
  - Aleph Alpha
  - Kolibri 1.1
  - Qwen3.8 Flash Next
topics:
  - Models
  - Open-weight
  - Europe
translationKey: aleph-alpha-kolibri-1-1
image: /images/news/aleph-alpha-kolibri-1-1-2026-11-24.jpg
imageAlt: "Deyron Labs graphic: Aleph Alpha Kolibri 1.1, 75B total and 3B active parameters, Apache 2.0, overall score 73.2 versus 66.6 for Kolibri 1.0, self-reported, 23 Nov 2026"
sources:
  - title: "Kolibri 1.1: More Efficient. More Capable."
    url: "https://aleph-alpha.com/en/blog/kolibri-1-1/"
    publisher: "Aleph Alpha, 23 November 2026"
    primary: true
---

## What happened

On 23 November 2026 Aleph Alpha, the German AI company, published Kolibri 1.1, seven weeks after Kolibri 1.0. The company says the model weights are on Hugging Face under the Apache 2.0 license. We read Aleph Alpha's announcement; every number below comes from it and is reported by the company, not independently tested.

Kolibri is described as an English-German mixture-of-experts model with 75 billion total and 3 billion active parameters, a context window of up to 1 million tokens, and a sparse-attention architecture.

## Key details

- **Overall score (Aleph Alpha's table):** 73.2 for Kolibri 1.1 versus 66.6 for 1.0.
- **Efficiency (company):** 0.208 GPU-hours per 1,000 tasks versus 0.718 for 1.0, which Aleph Alpha describes as 3.4 times less GPU time per task, and 41% fewer output tokens per task. Decode throughput at 1 million tokens of context is up to 14 times that of 1.0 on four B300 GPUs.
- **Benchmarks, 1.0 to 1.1 (company):** SWE-bench Verified 64.0 to 70.4; Terminal-Bench 2.1 25.8 to 35.6; GPQA Diamond 84.7 to 87.1; BrowseComp 31.9 to 34.8; AA-Omniscience Index -35.5 to -14.8.
- **Stated limits:** in the same table Qwen3.8 Flash Next scores higher overall (80.1), and the τ³-bench banking score fell from 38.7 to 28.6.
- **Not confirmed here:** independent evaluations, results outside Aleph Alpha's own tests, and the model card details on Hugging Face, which we did not read.

## Why it matters

Kolibri 1.1 is a European open-weight model with a small active-parameter count, so its main claim is cost: the company says it needs far less GPU time per task than its predecessor while scoring higher. That matters mostly to teams that want to self-host under a permissive license.

The company's own table also shows it trailing a larger competing model overall and regressing on one benchmark, so the strongest claims remain to be tested by third parties. Watch for independent benchmark runs and community results on long-context workloads.

> Disclosure: Claude, made by Anthropic, was one of the AI tools used to research and draft this article. Aleph Alpha is not affiliated with Deyron Labs.
