---
title: "Anthropic releases Claude Fable 5.2 at $8/$40 per million tokens, down from $10/$50, plus a restricted Mythos 5.2"
summary: "Anthropic's platform documentation lists Claude Fable 5.2 as released on 9 November 2026, priced at $8 per million input tokens and $40 per million output tokens, against $10 and $50 for Fable 5.1. It keeps a 1M-token context window and 128K max output. Mythos 5.2 shares its specifications but is limited to verified organizations. We could not read the announcement or system card, so benchmarks are not covered."
seoTitle: "Claude Fable 5.2 released: $8/$40 per 1M tokens"
seoDescription: "Anthropic's docs list Claude Fable 5.2 as released 9 Nov 2026 at $8/$40 per 1M tokens (Fable 5.1: $10/$50), 1M context; Mythos 5.2 is restricted."
lang: en
publishedAt: 2026-11-09T18:30:00Z
entities:
  - Anthropic
  - Claude
  - Claude Fable 5.2
  - Claude Mythos 5.2
  - Claude Fable 5.1
topics:
  - Models
  - Pricing
translationKey: claude-fable-5-2
image: /images/news/claude-fable-5-2-2026-11-09.jpg
imageAlt: "Deyron Labs graphic: Claude Fable 5.2, released 9 November 2026, costs $8 input and $40 output per million tokens versus $10 and $50 for Fable 5.1, with a 1M-token context window"
sources:
  - title: "Claude Fable 5.2 model overview (Claude Platform docs)"
    url: "https://platform.claude.com/docs/en/models/fable-5-2/overview"
    publisher: "Anthropic"
    primary: true
  - title: "Claude Platform release notes (9 November 2026 entry)"
    url: "https://platform.claude.com/docs/en/release-notes/overview"
    publisher: "Anthropic"
    primary: true
  - title: "Claude Fable 5.2 launch offers"
    url: "https://support.claude.com/en/articles/17506494-claude-fable-5-2-launch-offers"
    publisher: "Anthropic"
    primary: true
  - title: "Anthropic releases Claude Fable 5.2 and Claude Mythos 5.2 ahead of IPO"
    url: "https://www.cnbc.com/2026/11/09/anthropic-claude-fable-5-2-mythos-5-2.html"
    publisher: "CNBC"
    primary: false
---

## What happened

Anthropic's Claude Platform documentation lists Claude Fable 5.2 (API ID `claude-fable-5-2`) as released on 9 November 2026, with the status "Active (latest)". The release notes for the same date also name Claude Mythos 5.2. We read the model overview page, the release notes and a support article about launch offers on 9 November 2026. We could not read Anthropic's announcement page or the system card, and CNBC's report of the launch failed to load for us, so this article covers only what the documentation states.

## Key details

- **Price:** $8 per million input tokens and $40 per million output tokens. The release notes give Fable 5.1 and Mythos 5.1 as $10 and $50. Cache reads are $0.20 per million tokens, and the Batch API carries a 50% discount, per the overview page.
- **Specifications:** 1M-token context window, 128K max output tokens, text and image input, text output. Adaptive thinking is always on and cannot be turned off; the default effort is high. The documented knowledge cutoff is June 2026, and Anthropic says the model will not be retired sooner than 9 November 2027.
- **Where it runs:** the docs list the Claude API, Claude Models on Google Cloud (in both Google-managed and Anthropic-managed forms), Microsoft Foundry and Claude Platform on AWS.
- **Fast mode:** the release notes describe a fast mode on the Claude API with up to 2.5x higher output tokens per second at $16 and $80 per million tokens.
- **Mythos 5.2:** the docs say it shares Fable 5.2's specifications and pricing, but offers "the same capabilities only to organizations verified through Anthropic's verification programs, such as the Cyber Verification Program."
- **Developer changes:** per the release notes, 5.2 enforces the prefix check on every account and uses a new computer-use toolset (`computer_toolset_20260801`); a request that declares the older `computer_20251124` tool returns a 400 error. The docs also note that the model requires 30-day data retention and is not available under zero data retention unless Anthropic authorizes it.
- **Launch offers:** Anthropic's support article says Pro plans and standard Team seats get all Fable models for one week, up to 50% of weekly usage limits, from launch through 16 November 2026, plus one Fable limit reset. Max, Ultra and premium seats get one to three resets depending on subscription length. The Free plan is not eligible.
- **Not stated in what we read:** benchmark results, safety evaluations, differences in answer quality against Fable 5.1, and which claude.ai plans include 5.2 beyond the launch offers.

## Why it matters

For teams already paying for Fable 5.1, the documented change is a 20% lower list price on both input and output tokens, with the same context and output limits. Whether 5.2 is better is not something Anthropic's documentation answers, and independent evaluations were not available when we checked. The developer notes matter for anyone migrating: the toolset change and the always-on adaptive thinking can break existing requests. Access to Mythos 5.2 stays limited to verified organizations, so most users will work with Fable 5.2.

> Disclosure: Claude, made by Anthropic, was one of the AI tools used to research and draft this article, and Anthropic is the subject of this story. All claims about the models are Anthropic's, from its own documentation, unless stated otherwise.
