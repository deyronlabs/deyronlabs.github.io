---
title: "Anthropic releases Claude Fable 5.2: up to 30% faster, $8/$40 per million tokens, with a restricted Mythos 5.2"
summary: "Anthropic released Claude Fable 5.2 on 9 November 2026 at $8 per million input tokens and $40 per million output tokens, down from $10 and $50 for Fable 5.1, and says it generates output up to 30% faster. Anthropic's own benchmarks show gains over 5.1; independent results are not yet available. Mythos 5.2 is the same model, limited to verified organizations."
seoTitle: "Claude Fable 5.2: 30% faster, $8/$40 per 1M"
seoDescription: "Anthropic released Claude Fable 5.2 on 9 Nov 2026: up to 30% faster than 5.1 at $8/$40 per 1M tokens; Mythos 5.2 is restricted to verified orgs."
lang: en
publishedAt: 2026-11-09T18:30:00Z
updatedAt: 2026-11-09T21:00:00Z
entities:
  - Anthropic
  - Claude
  - Claude Fable 5.2
  - Claude Mythos 5.2
  - Claude Fable 5.1
topics:
  - Models
  - Pricing
  - Safety
translationKey: claude-fable-5-2
image: /images/news/claude-fable-5-2-2026-11-09.jpg
imageAlt: "Deyron Labs graphic: Claude Fable 5.2, released 9 November 2026, costs $8 input and $40 output per million tokens versus $10 and $50 for Fable 5.1, with a 1M-token context window"
sources:
  - title: "Introducing Claude Fable 5.2 and Claude Mythos 5.2"
    url: "https://www.anthropic.com/claude-fable-and-mythos-5-2"
    publisher: "Anthropic"
    primary: true
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
---

## What happened

On 9 November 2026 Anthropic announced Claude Fable 5.2 and Claude Mythos 5.2, and its Claude Platform documentation lists Claude Fable 5.2 (API ID `claude-fable-5-2`) as released the same day. Anthropic says the two are "the same underlying model": Fable has strong safeguards for cybersecurity and biology and is available to all users, while Mythos 5.2 is offered through Anthropic's Cyber Verification Program and Life Sciences Verification Program to verified organizations. We read the announcement, the model overview, the release notes and a support article about launch offers on 9 November 2026. Anthropic's system card is a PDF whose text we could not extract, so nothing below comes from it. Anthropic is the subject of this story and every performance claim is Anthropic's own.

## Key details

- **Speed and price:** Anthropic says the models generate output "up to 30% faster" than Fable 5.1 and Mythos 5.1 and cost $8 per million input tokens and $40 per million output tokens. The platform release notes give Fable 5.1 and Mythos 5.1 as $10 and $50, so the cut is 20% on both. Cache reads are $0.20 per million tokens and the Batch API carries a 50% discount, per the overview page.
- **Fast mode:** an optional mode with up to 2.5x faster generation at $16 and $80 per million tokens, available in Claude Code, Claude Platform, Google Cloud and Microsoft Foundry. Fast mode for Mythos is limited to organizations in the verification programs.
- **Specifications:** 1M-token context window, 128K max output tokens, text and image input, text output. Adaptive thinking is always on and the default effort is high. The documented knowledge cutoff is June 2026.
- **Availability:** Anthropic says it is available "on all platforms, including Amazon Web Services, Google Cloud, and Microsoft Azure". Pro plans and standard Team seats get Fable up to 50% of weekly limits through 16 November 2026, plus one to three limit resets for eligible subscribers, per the support article. The Free plan is not eligible.
- **Benchmarks, as reported by Anthropic (safeguards on, highest available effort unless noted):** FrontierCode 2.0, 49.1% at Xhigh effort against 32.4% for Fable 5.1, 45.5% for Opus 5.5, 42.8% for GPT-6 Astra and 41.1% for Gemini 4 Carbon (at medium effort). FrontierSWE v2, 69.9% against 56.3% for 5.1. OSWorld 2.1 (offline, partial), 89.3% against 83.5%. Humanity's Last Exam with tools, 74.2% against 65.6%. RoboDojo Sim, 64.9% against 27.6%, run internally by Anthropic. On AutomationBench Anthropic lists 51.4% for Fable 5.2 and 53.9% for Gemini 4 Carbon. The methodology is in the system card, which we could not read, and none of these results has been independently verified.
- **Safety, per Anthropic:** it rates the risk as "low" and says Fable 5.2 blocks about 55% fewer requests than Fable 5.1 (60% fewer for cyber, 40% for biology). Anthropic lists external testing by UK AISI, Frontier Design and METR, and notes that those organizations did not review the announcement or system card. Anthropic also says the models express suspicion that they are being evaluated more often than recent models.
- **Developer changes, from the release notes:** 5.2 enforces the prefix check on every account and uses a new computer-use toolset (`computer_toolset_20260801`); a request that declares the older `computer_20251124` tool returns a 400 error. The model requires 30-day data retention and is not available under zero data retention unless Anthropic authorizes it.

## Why it matters

For teams already paying for Fable 5.1, the documented change is a 20% lower list price with the same context and output limits, plus a speed gain Anthropic puts at up to 30%. Whether the quality gains in Anthropic's benchmark table hold up outside its own tests is open: independent evaluations were not available when we checked, and the one competitor comparison where Fable 5.2 trails, AutomationBench, is a reminder that results vary by task. The developer notes matter for anyone migrating, since the toolset change and always-on adaptive thinking can break existing requests. Most users will work with Fable 5.2, as Mythos 5.2 stays limited to verified organizations.

> Disclosure: Claude, made by Anthropic, was one of the AI tools used to research and draft this article, and Anthropic is the subject of this story. All claims about the models are Anthropic's, from its own announcement and documentation, unless stated otherwise.
