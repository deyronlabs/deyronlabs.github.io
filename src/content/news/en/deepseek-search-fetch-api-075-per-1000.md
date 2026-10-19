---
title: "DeepSeek opens Search and Fetch APIs at $0.75 per 1,000 requests, free via Claude Code and Codex until 1 Nov"
summary: "DeepSeek's API documentation now lists two web tools, Search and Fetch, built on its in-house search engine and priced at $0.75 per 1,000 successful requests each. Server-side calls made through DeepSeek Harness, Claude Code or Codex are free until billing starts at 00:00 Beijing time on 1 November 2026."
seoTitle: "DeepSeek Search and Fetch API: $0.75 per 1,000"
seoDescription: "DeepSeek's docs list Search and Fetch APIs at $0.75 per 1,000 successful requests, with Claude Code and Codex calls free until 1 November 2026."
lang: en
publishedAt: 2026-10-19T17:00:00Z
entities:
  - DeepSeek
  - DeepSeek Harness
  - Claude Code
  - Codex
topics:
  - Pricing
  - Agents
  - China
translationKey: deepseek-search-fetch-api
image: /images/news/deepseek-search-fetch-api-2026-10-19.jpg
imageAlt: "Deyron Labs graphic: DeepSeek Search and Fetch APIs cost $0.75 per 1,000 successful requests each; calls through Claude Code, Codex and DeepSeek Harness are free until 1 November 2026"
sources:
  - title: "DeepSeek API docs: Search and Fetch guide"
    url: "https://api-docs.deepseek.com/guides/search"
    publisher: "DeepSeek"
    primary: true
  - title: "DeepSeek API docs: Models & Pricing"
    url: "https://api-docs.deepseek.com/quick_start/pricing"
    publisher: "DeepSeek"
    primary: true
  - title: "DeepSeek API docs: news of 2026-10-17 (V4.1-Flash-1017 and Search/Fetch)"
    url: "https://api-docs.deepseek.com/news/news261017"
    publisher: "DeepSeek"
    primary: true
---

## What happened

DeepSeek's API documentation now describes two raw JSON endpoints for giving agents live web access: **Search**, which returns structured web results for a query, and **Fetch**, which returns the content of one web page as Markdown. A banner on the docs site reads "Search / Fetch API is now available", and the company's 17 October 2026 news item on the V4.1-Flash-1017 update says both are open to all users. The docs do not carry a separate launch date for the tools.

## Key details

- **Price (DeepSeek's docs):** $0.75 per 1,000 successful requests for each of Search and Fetch. Billing is per request, not per token or per result. Only HTTP 200 responses that return results or page content are billed; failed, empty and timed-out requests are not, and the `count` setting does not change the price. The Chinese-language guide lists the same rate as 5 yuan per 1,000.
- **Free period:** server-side tool calls made through DeepSeek Harness, Claude Code or Codex are currently free. Per-request billing starts at 00:00 Beijing time on 1 November 2026 (16:00 UTC on 31 October). Calls made directly to the endpoints are not covered by that note.
- **Endpoints:** `POST https://api.deepseek.com/v1/tools/search` and `/v1/tools/fetch`, with bearer-token authentication. Search accepts queries of 1 to 128 characters and returns 1 to 50 results (default 10); each result carries a date, an `authority` score from 0 to 4 and a `rerank_score` from 0 to 3, as defined by DeepSeek. Fetch takes an HTTP or HTTPS URL of up to 8,192 characters.
- **Search engine:** DeepSeek says the tools run on its own search engine. The news item says it handles "hundreds of millions" of requests a day; the docs give no index size, coverage or freshness figures, and no uptime commitment.
- **Fetch limits:** Fetch depends on the target site's availability and access policies, and returns 403 or 404 when a page cannot be retrieved.
- **Rate limits:** the English and Chinese versions of the guide list different per-account limits when we read them on 19 October, so we do not quote a figure.

## Why it matters

Web search is a per-request cost on top of model tokens for any agent that browses, and DeepSeek has put a flat price on it, with a short free window for people already using Claude Code or Codex through its API. Whether the tools are worth using depends on result quality and coverage, which DeepSeek's documentation does not quantify and which we have not tested. Developers should also note that the price and the free-period terms can change: the pricing page says DeepSeek reserves the right to adjust prices.

> Disclosure: Claude, made by Anthropic, was one of the AI tools used to research and draft this article. Claude Code is an Anthropic product and is named here only because DeepSeek's documentation names it. Prices and limits are DeepSeek's own and were read from its documentation on 19 October 2026.
