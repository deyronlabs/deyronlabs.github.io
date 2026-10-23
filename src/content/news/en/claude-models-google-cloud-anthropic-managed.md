---
title: "Anthropic launches Claude Models on Google Cloud, a Claude API run by Anthropic and billed through Google Cloud"
summary: "Claude's release notes list Claude Models on Google Cloud (Anthropic managed) on 22 October 2026: the Claude API, operated by Anthropic, reached through a Google Cloud project with Google Cloud IAM for access and Google Cloud Marketplace for billing. Fast mode for Claude Opus 5.5 is supported. SDK clients are in beta."
seoTitle: "Claude Models on Google Cloud, run by Anthropic"
seoDescription: "Anthropic's Claude API is now reachable through Google Cloud projects, billed via Marketplace, with Opus 5.5 fast mode, per 22 October 2026 release notes."
lang: en
publishedAt: 2026-10-23T18:40:00Z
entities:
  - Anthropic
  - Google Cloud
  - Claude Opus 5.5
topics:
  - Products
  - Agents
translationKey: claude-models-google-cloud-anthropic-managed
image: /images/news/claude-models-google-cloud-anthropic-managed-2026-10-23.jpg
imageAlt: "Deyron Labs graphic: Claude Models on Google Cloud (Anthropic managed), billed through Google Cloud Marketplace, Google Cloud IAM access, no API keys, SDK clients in beta"
sources:
  - title: "Claude Models on Google Cloud (Anthropic managed)"
    url: "https://platform.claude.com/docs/en/build-with-claude/claude-models-on-google-cloud/anthropic-managed"
    publisher: "Anthropic"
    primary: true
  - title: "Claude Platform release notes"
    url: "https://platform.claude.com/docs/en/release-notes/overview"
    publisher: "Anthropic"
    primary: true
  - title: "Fast mode"
    url: "https://platform.claude.com/docs/en/build-with-claude/fast-mode"
    publisher: "Anthropic"
    primary: true
---

## What happened

Anthropic's Claude Platform release notes list "Claude Models on Google Cloud (Anthropic managed)" under 22 October 2026. Anthropic's documentation describes it as "the Claude API, run by Anthropic and reached through your Google Cloud project". Anthropic makes Claude, the AI tool that helped draft this article, so please read this as a company describing its own product. The documentation page itself carries no date, so the launch date comes from the release notes.

## Key details

All details are from Anthropic's documentation, checked on 23 October 2026.

- **Billing and access:** usage is billed through Google Cloud Marketplace; Anthropic meters usage and reports it to Google Cloud in Claude Consumption Units. Access is controlled with Google Cloud IAM, with three roles (viewer, user, admin); only the admin role on the project opens the Claude Console.
- **Authentication:** Google OAuth 2.0 bearer tokens. The page states it "doesn't use API keys".
- **Setup:** it creates a new Anthropic organization, separate from existing ones; an existing organization cannot be converted.
- **Operated by Anthropic:** Anthropic manages rate limits and is the data processor. Zero Data Retention is available on request.
- **Supported features:** fast mode for Claude Opus 5.5, prompt caching, extended thinking, Batches, Files, Agent Skills, Managed Agents and customer-managed encryption keys (Google Cloud KMS). API keys, MCP tunnels and some self-hosted features are not supported.
- **Status:** SDK clients for this offering are in beta. Data location stays "global", with a per-request `inference_geo: "us"` option for US-only inference.
- **Fast mode context:** on the standard Claude API, Anthropic lists fast mode for Opus 5.5 at up to 2.5x output tokens per second, priced at $8 per million input and $40 per million output tokens. Pricing for the Google Cloud offering is not stated on the page.

## Why it matters

Companies that already buy and govern cloud services through Google Cloud can now use Claude under their existing project, IAM and Marketplace billing without a separate payment relationship. The trade-offs listed in the documentation, such as no API keys and a new, separate Anthropic organization, matter for teams planning migrations from the regular API.

> Disclosure: Claude, made by Anthropic, was one of the AI tools used to research and draft this article, and Anthropic is the subject of the story. All facts are attributed to Anthropic's documentation.
