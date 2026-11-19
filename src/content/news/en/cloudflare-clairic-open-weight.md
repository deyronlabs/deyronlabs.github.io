---
title: "Cloudflare releases open-weight Clairic (27B) and Clairic-flash (9B) extraction models under Apache-2.0, from $0.10 per million input tokens"
summary: "On 18 November 2026 Cloudflare published an updated Clairic and a smaller Clairic-flash (9B), open-weight models that extract text from text, images and PDFs, on Workers AI and Hugging Face under Apache-2.0. Input tokens cost $0.24 and $0.10 per million, with a $0.10 promotion until 1 December. The evaluations are Cloudflare's own."
seoTitle: "Cloudflare Clairic: open-weight extraction models"
seoDescription: "Cloudflare released open-weight Clairic (27B) and Clairic-flash (9B) on 18 Nov 2026 under Apache-2.0; input is $0.24 and $0.10 per 1M tokens."
lang: en
publishedAt: 2026-11-19T10:50:00Z
entities:
  - Cloudflare
  - Clairic
  - Clairic-flash
  - Workers AI
  - Hugging Face
  - Qwen
topics:
  - Models
  - Open weights
  - Pricing
translationKey: cloudflare-clairic-open-weight
image: /images/news/cloudflare-clairic-open-weight-2026-11-18.jpg
imageAlt: "Deyron Labs graphic: Cloudflare open-weight Clairic 27B at $0.24 and Clairic-flash 9B at $0.10 per million input tokens, both Apache-2.0; $0.10 promotion until 1 December 2026; evaluations are Cloudflare's own"
sources:
  - title: "Open Clairic (Cloudflare blog)"
    url: "https://blog.cloudflare.com/open-clairic/"
    publisher: "Cloudflare (Alex Reneau, Michelle Chen, Kevin Flansburg, 18 November 2026)"
    primary: true
  - title: "Cloudflare/clairic and Cloudflare/clairic-flash model repositories"
    url: "https://huggingface.co/Cloudflare/clairic"
    publisher: "Hugging Face"
    primary: true
---

## What happened

On 18 November 2026 Cloudflare published "Open Clairic" on its blog: an updated Clairic and a new, smaller Clairic-flash (9B), released as open-weight models for extracting text from text, images and PDFs. The post is by Alex Reneau, Michelle Chen and Kevin Flansburg. Cloudflare calls itself a "neolab" and describes the work as coming from its "Workers AI superintelligence" team. We read the post in full on 19 November 2026.

## Key details

- **Availability:** hosted on Cloudflare Workers AI as `@cf/cloudflare/clairic` and `@cf/cloudflare/clairic-flash`, with weights on Hugging Face.
- **Licence and base models:** Hugging Face lists `Cloudflare/clairic` (base `Qwen/Qwen3.8-27B`) and `Cloudflare/clairic-flash` (base `Qwen/Qwen3.5-9B`), both under Apache-2.0. The repositories are listed as created on 16 October 2026 and had 15 and 11 likes and 7 downloads when we checked.
- **Input:** text, images and PDFs, with up to four images or pages per request.
- **Price:** $0.24 per million input tokens for the 27B model and $0.10 for the 9B model. Cloudflare runs a promotion at $0.10 per million input tokens for both until 1 December 2026. Only input tokens are billed.
- **Evaluations (Cloudflare's own, self-reported):** Cloudflare calls its results directional, for example 335 out of 336 on "fresh text fields", and compares the models with Liquid AI D1.2 plus OCR and with ScaleDown Extract. There are no public benchmarks. Cloudflare reports p50 latency under one second on its own infrastructure.
- **Not stated:** the training code is not published, and the evaluations are not independent.

## Why it matters

Document extraction is a routine job for many applications, and this release gives developers a permissively licensed, self-hostable option alongside a hosted price. The honest limit is evidence: all quality claims come from Cloudflare's internal tests, so anyone considering it should run their own documents through it first. The $0.10 promotional price ends on 1 December, after which the 27B model moves to $0.24 per million input tokens.

> Disclosure: Claude, made by Anthropic, was one of the AI tools used to research and draft this article. Cloudflare is not affiliated with Deyron Labs; figures are Cloudflare's own, from its 18 November 2026 post.
