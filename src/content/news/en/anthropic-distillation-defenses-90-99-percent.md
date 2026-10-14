---
title: "Anthropic says new defenses cut data harvested by distillation attacks by 90 to 99%, and accuses Zhipu and Moonshot"
summary: "On 12 October 2026 Anthropic said new safeguards on Claude's reasoning cut the data harvested by distillers by around 90 to 99% and that it has banned tens of thousands of accounts. It also alleges that Zhipu (Z.ai) distilled US models' cyber capabilities and that some Kimi requests were forwarded to Claude. These are Anthropic's own claims; neither company has responded in the sources we read."
seoTitle: "Anthropic: distillation harvest cut 90-99%"
seoDescription: "Anthropic says new safeguards cut data harvested by distillation attacks by about 90 to 99% (12 Oct 2026); its claims about Zhipu are unconfirmed."
lang: en
publishedAt: 2026-10-14T06:30:00Z
entities:
  - Anthropic
  - Claude
  - Zhipu AI
  - Z.ai
  - Moonshot AI
  - Kimi
  - GLM-5.3
topics:
  - Safety
  - Policy
  - China
translationKey: anthropic-distillation-defenses-90-99-percent
image: /images/news/anthropic-distillation-defenses-90-99-percent-2026-10-12.jpg
imageAlt: "Deyron Labs graphic: Anthropic says new defenses cut data harvested by distillers by around 90 to 99 percent and banned tens of thousands of accounts; allegations against Zhipu and Moonshot are Anthropic's own claims"
sources:
  - title: "Strengthening our defenses against distillation attacks"
    url: "https://www.anthropic.com/research/distillation-defenses"
    publisher: "Anthropic"
    primary: true
  - title: "Detecting and preventing distillation attacks (February 2026, earlier post)"
    url: "https://www.anthropic.com/news/detecting-and-preventing-distillation-attacks"
    publisher: "Anthropic"
    primary: true
  - title: "Anthropic says new safeguards sharply reduce AI distillation attacks"
    url: "https://tech.yahoo.com/ai/claude/articles/anthropic-says-safeguards-sharply-reduce-010959967.html"
    publisher: "Reuters, via Yahoo Tech"
    primary: false
---

## What happened

On 12 October 2026 Anthropic published a research post, "Strengthening our defenses against distillation attacks". Distillation here means training a model on another model's outputs; Anthropic uses "distillation attacks" for large-scale, unauthorized copying of Claude's capabilities, often through fraudulent accounts and proxy networks.

Anthropic says its new defenses reduced the data harvested by distillers by "around 90 to 99%". The post also makes allegations about two Chinese labs, Zhipu AI (known abroad as Z.ai) and Moonshot AI. Reuters reported that Z.ai did not immediately respond to a request for comment. We did not find a response from either company in the sources we read.

## Key details

Everything below is Anthropic's own account, from its post. We have not seen the underlying data, and no outside party has confirmed it.

- **Measured effect:** early evidence suggests the methods reduced harvested data by around 90 to 99%. On Anthropic's own platform, the post says extracted reasoning tokens are "10 to 100 times lower" than before.
- **Classifier:** a two-stage classifier aimed at reasoning extraction, with a stated false positive rate below 0.1%, meaning it can wrongly block fewer than 1 in 1,000 benign requests.
- **Bans:** Anthropic says it has banned "tens of thousands of accounts" associated with distillation, often within two hours of a campaign starting.
- **Account rules:** a feature called preserved thinking, introduced with Claude Fable 5.1 and Claude Opus 5.5, stops API accounts created on or after 31 August 2026 from editing Claude's prior context, which makes it harder for proxy networks to repeatedly probe protected reasoning.
- **Billing:** since 24 September, Anthropic says it charges for requests its safeguards block before Claude responds, in specific areas including distillation.
- **Zhipu allegation:** Anthropic says Zhipu distilled the cyber capabilities of leading US models while developing GLM-5.3. It says Zhipu's attempt to distill Claude Fable 5 was degraded by Anthropic's cyber safeguards, and that Zhipu reportedly switched to an older Claude model and another lab's model. Anthropic also says the US Center for AI Standards and Innovation (CAISI) assessed GLM-5.3 as the most cyber-capable open-weights model released to date; we have not read the CAISI assessment.
- **Moonshot allegation:** Anthropic reports a case in which requests to Moonshot's Kimi models were "secretly forwarded to Claude" as part of distillation efforts.
- **Limits:** Anthropic says it does not yet know how long these gains will last and that the approach involves trade-offs for it and its customers.

An earlier Anthropic post from February 2026 named DeepSeek, Moonshot and MiniMax in a similar campaign, citing over 16 million exchanges through about 24,000 fraudulent accounts. The new post builds on that one.

## Why it matters

For people who build on Claude's API, two changes are concrete: newer accounts cannot edit Claude's prior context, and blocked requests can be billed. Legitimate users should not hit either often given the stated false positive rate, but it is a rate Anthropic measured itself.

For everyone else, this is one lab describing how it protects its models and naming competitors. The allegations against Zhipu and Moonshot are claims by a party with a commercial interest; they are not findings by a court or an independent auditor. Treat the 90 to 99% figure the same way until someone outside Anthropic measures it.

> Disclosure: Claude, made by Anthropic, was one of the AI tools used to research and draft this article, and this story is about Anthropic. Figures and allegations are Anthropic's own, taken from its 12 October 2026 post; we have not independently verified them.
