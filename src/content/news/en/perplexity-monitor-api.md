---
title: "Perplexity launches Monitor API, which watches the web or up to 10 pages and sends webhooks on changes"
summary: "On 16 November 2026 Perplexity introduced Monitor API, which checks the web or specified pages on a schedule and sends a signed webhook with a confidence score when it finds a relevant update. Perplexity lists $1 per 1,000 successful runs for web monitors and says it is available today in the API."
seoTitle: "Perplexity Monitor API: web alerts by webhook"
seoDescription: "Perplexity launched Monitor API on 16 Nov 2026: scheduled web and page monitors with webhooks, priced at $1 per 1,000 runs or URL fetches."
lang: en
publishedAt: 2026-11-17T06:50:00Z
entities:
  - Perplexity
  - Monitor API
  - Perplexity Search API
topics:
  - Agents
  - Products
  - Pricing
translationKey: perplexity-monitor-api
image: /images/news/perplexity-monitor-api-2026-11-17.jpg
imageAlt: "Deyron Labs graphic: Perplexity Monitor API; web and page monitors; webhook alerts; $1 per 1,000 runs; Perplexity blog, 16 November 2026"
sources:
  - title: "Introducing Perplexity's Monitor API"
    url: "https://www.perplexity.ai/hub/blog/introducing-perplexitys-monitor-api"
    publisher: "Perplexity Research, 16 November 2026"
    primary: true
---

## What happened

On 16 November 2026 Perplexity published "Introducing Perplexity's Monitor API". The post describes an API that checks the web on a schedule and sends a webhook when it finds a relevant update. Perplexity says it is "available today" through the API and the API Console, using the same API key as its Search, Context and Agent APIs.

## Key details

- **Two modes:** "Monitor the web" tracks a topic or query using Perplexity Search; "Monitor pages" watches up to 10 specified pages and returns a text diff when they change.
- **Filtering:** according to Perplexity, each web-monitor update passes four checks (relevance, source legitimacy, new information and freshness), and page monitors are checked for whether a change matters to the stated goal. Every update carries a confidence score.
- **Schedules and delivery:** runs can be set to every 15 minutes, hourly, daily, weekly or a custom cron. Webhooks are signed and retried automatically, and monitors can be paused, resumed or run on demand.
- **Pricing (as listed by Perplexity):** $1 per 1,000 successful runs for web monitors, and $1 per 1,000 URLs fetched for page monitors.
- **Self-reported evaluation:** Perplexity says it tested 60 topics over eight hours each against other Search API providers and that Monitor API delivered the most fresh, relevant results. We have not seen the data behind this comparison.
- **Not stated:** a licence, a free tier, rate limits and default threshold values.

## Why it matters

Monitoring is a common building block for agents and alerting tools, and until now it usually meant polling a search or scraping API and writing your own change detection. A single priced endpoint with signed webhooks and a confidence score lowers that work, though the quality of the relevance and freshness checks is Perplexity's own claim.

Teams considering it should test it on their own topics and pages before relying on it, and compare the per-run price against how often they would need to poll.

> Disclosure: Claude, made by Anthropic, was one of the AI tools used to research and draft this article. Perplexity is not affiliated with Deyron Labs; all claims are Perplexity's own.
