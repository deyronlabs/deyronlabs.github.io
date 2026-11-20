---
title: "DeepSeek drops separate fees for web searches and page fetches that its models run server-side, TechNode reports"
summary: "DeepSeek's documentation says web searches, image searches and page fetches that a model runs through its server-side tools are not billed separately, only the tokens are. TechNode reported on 19 November 2026 that the change took effect on 18 November. The standalone Search and Fetch APIs keep their $0.75 per 1,000 successful requests fee."
seoTitle: "DeepSeek drops separate web search fees"
seoDescription: "DeepSeek's docs say model-run web searches and page fetches bill only tokens; TechNode reports the change took effect 18 Nov 2026."
lang: en
publishedAt: 2026-11-20T14:00:00Z
entities:
  - DeepSeek
  - TechNode
topics:
  - Pricing
  - Agents
  - China
translationKey: deepseek-web-search-fee-removal
image: /images/news/deepseek-web-search-fee-removal-2026-11-20.jpg
imageAlt: "Deyron Labs graphic: DeepSeek no longer bills model-run web search and page fetch separately, only tokens; reported effective 18 Nov 2026; standalone Search and Fetch APIs stay at $0.75 per 1,000 requests; no 18 Nov changelog entry"
sources:
  - title: "DeepSeek API docs: Search and Fetch guide (read 20 November 2026)"
    url: "https://api-docs.deepseek.com/guides/search"
    publisher: "DeepSeek"
    primary: true
  - title: "DeepSeek API docs: change log (latest entry 13 November 2026, read 20 November 2026)"
    url: "https://api-docs.deepseek.com/updates/"
    publisher: "DeepSeek"
    primary: true
  - title: "DeepSeek drops separate fees for model-triggered web searches (TechNode, 19 November 2026)"
    url: "https://technode.com/2026/11/19/deepseek-drops-separate-fees-for-model-triggered-web-searches/"
    publisher: "TechNode"
    primary: false
---

## What happened

DeepSeek's Search and Fetch guide, which we read on 20 November 2026, says that when a model uses DeepSeek's server-side tools to search the web, search for images or fetch a page, those calls are not billed separately. Only the tokens are charged. TechNode reported on 19 November that DeepSeek removed the separate fees and that the change took effect on 18 November.

## Key details

- **What is no longer billed separately (DeepSeek's guide):** web searches, image searches and page fetches that the model triggers through its server-side tools; the cost is the tokens used.
- **What still costs per request:** the standalone Search and Fetch APIs stay at $0.75 per 1,000 successful requests, the rate DeepSeek's guide lists and the one we covered in an earlier article.
- **Date:** 18 November 2026 comes only from TechNode. DeepSeek's change log, whose latest entry is dated 13 November, has no entry for 18 November, and the old pricing page address now redirects to the change log. We did not read DeepSeek's Models & Pricing page.
- **Figures:** neither source gives a token price for the searches or an estimate of savings.

## Why it matters

Agents that let a model search and read pages previously carried a per-request charge on top of tokens. If the guide is read correctly, that line item is gone for model-run searches, so costs for search-heavy agent runs depend on how many tokens the results consume. The effective date rests on one secondary report, so anyone budgeting against it should check DeepSeek's pricing page and their own billing.

> Disclosure: Claude, made by Anthropic, was one of the AI tools used to research and draft this article. DeepSeek documentation was read on 20 November 2026; the 18 November date is TechNode's.
