---
title: "ByteDance's Seedance 2.5 is fully available by API on BytePlus, with 4K video at $0.914 per second"
summary: "BytePlus, ByteDance's international platform, lists Dreamina Seedance 2.5 and Seedance 2.5 flash as fully available through its ModelArk API, with 4K output priced at $0.914 per second for the full model. TechNode reported a separate 4K opening on ByteDance's Volcano Engine on 16 November, with a price in yuan we could not confirm."
seoTitle: "Seedance 2.5 API: 4K video at $0.914 a second"
seoDescription: "BytePlus lists Seedance 2.5 as fully available by API in Nov 2026: 4K costs $0.914 per second, 1080p $0.569; the flash model stops at 720p."
lang: en
publishedAt: 2026-11-18T18:50:00Z
entities:
  - ByteDance
  - BytePlus
  - ModelArk
  - Seedance 2.5
  - Volcano Engine
topics:
  - Models
  - Pricing
  - China
translationKey: bytedance-seedance-2-5-4k-api
image: /images/news/bytedance-seedance-2-5-4k-api-2026-11-16.jpg
imageAlt: "Deyron Labs graphic: ByteDance Seedance 2.5 API on BytePlus ModelArk, November 2026; 4K at 0.914 dollars per second, 1080p at 0.569, 720p at 0.231, 480p at 0.103; Flash model stops at 720p"
sources:
  - title: "Model pricing"
    url: "https://docs.byteplus.com/en/docs/modelark/model-pricing"
    publisher: "BytePlus ModelArk documentation, updated 16 November 2026"
    primary: true
  - title: "Create a video generation task API"
    url: "https://docs.byteplus.com/en/docs/modelark/create-video-generation-task-api"
    publisher: "BytePlus ModelArk documentation, updated 16 November 2026"
    primary: true
  - title: "ByteDance opens Seedance 2.5's 4K video generation API to developers"
    url: "https://technode.com/2026/11/17/bytedance-opens-seedance-2-5s-4k-video-generation-api-to-developers/"
    publisher: "TechNode, 17 November 2026"
    primary: false
---

## What happened

BytePlus, the international cloud platform of ByteDance, states in its ModelArk documentation that "Dreamina Seedance 2.5 and Dreamina Seedance 2.5 flash" are "now fully available" through its video generation API, and a banner on the page says the official Seedance 2.5 API is live. The pages we read were last updated on 16 November 2026, and we read them on 18 November. TechNode reported on 17 November that ByteDance's Volcano Engine opened the 4K version of Seedance 2.5 to developers on Monday 16 November, after testing with 20 studios. We could not read a Volcano Engine page, so that part is TechNode's report.

## Key details

- **Prices on BytePlus (USD, 16:9, a 5-second clip, no video input):** Seedance 2.5 costs $0.514 at 480p ($0.103 per second), $1.156 at 720p ($0.231), $2.843 at 1080p ($0.569) and $4.568 at 4K ($0.914).
- **Flash model:** Seedance 2.5 flash costs $0.34 at 480p ($0.07 per second) and $0.76 at 720p ($0.15). BytePlus lists 1080p and 4K as not supported for it.
- **Billing:** only successfully generated videos are billed, and the price is a per-token rate multiplied by tokens. When the input includes video there is a minimum token count. A "Draft" mode runs at 480p only.
- **Model IDs in the documentation example:** dreamina-seedance-2-5-260628 for the full model and dreamina-seedance-2-5-flash-261115 for flash.
- **TechNode's additional claims, not confirmed by the BytePlus pages:** 10-bit color, a low-resolution preview step before the 4K render, and a Volcano Engine price of about 6.03 yuan per second, which TechNode attributes to the Chinese site AIHub. We have not converted it to dollars, since it is a different platform and currency.
- **Not stated in the pages we read:** licence or weights (this is a closed API model), availability by region, rate limits and benchmark results.

## Why it matters

For anyone budgeting AI video, the useful number is the price ladder: on BytePlus's list, moving from 1080p to 4K raises the per-second price from $0.569 to $0.914, and the cheaper flash model does not go above 720p. A 4K five-second clip at the listed rate is $4.568. The Volcano Engine details are reported, not confirmed, so comparisons between ByteDance's China and international prices should wait for the company's own listing. Quality at 4K has not been independently assessed in anything we read.

> Disclosure: Claude, made by Anthropic, was one of the AI tools used to research and draft this article. ByteDance is not affiliated with Deyron Labs; prices are BytePlus's own, as listed on the dates above.
