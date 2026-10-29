---
title: "Google announces Gemini 4 Carbon, ranked #1 on the Artificial Analysis index, but only cyber defenders can use it yet"
summary: "On 28 October 2026 Google announced Gemini 4 Carbon, which it calls its strongest model, with a score of 59 on Artificial Analysis Intelligence Index v5.0 and 88.2% on SEC-bench Pro. Access starts with a subset of cyber defenders through the Fairwind Program; developers, businesses and consumers have no date yet. All results are Google's own."
seoTitle: "Gemini 4 Carbon: Google's new frontier model"
seoDescription: "Google announced Gemini 4 Carbon on 28 Oct 2026, scoring 59 on Artificial Analysis v5.0; access is limited to cyber defenders for now."
lang: en
publishedAt: 2026-10-29T06:40:00Z
entities:
  - Google
  - Google DeepMind
  - Gemini 4 Carbon
  - Gemini 4 Argon
  - Fairwind Program
  - Artificial Analysis
topics:
  - Models
  - Security
  - Pricing
translationKey: google-gemini-4-carbon
image: /images/news/google-gemini-4-carbon-2026-10-29.jpg
imageAlt: "Deyron Labs graphic: Gemini 4 Carbon announced 28 October 2026; 59 on Artificial Analysis v5.0, 88.2% on SEC-bench Pro, access limited to cyber defenders; results are Google's own"
sources:
  - title: "Gemini 4 Carbon: our next frontier model"
    url: "https://blog.google/innovation-and-ai/models-and-research/gemini-models/introducing-gemini-4-carbon/"
    publisher: "Google (Koray Kavukcuoglu, 28 October 2026)"
    primary: true
  - title: "Fairwind Program"
    url: "https://deepmind.google/fairwind-program/"
    publisher: "Google DeepMind"
    primary: true
---

## What happened

On 28 October 2026 Google published "Gemini 4 Carbon: our next frontier model", written by Koray Kavukcuoglu, SVP at Google DeepMind and Google's Chief AI Architect. Google calls Carbon "our strongest model with state-of-the-art cybersecurity and long horizon capabilities" and says it builds on Gemini 4 Argon, which it launched two weeks earlier.

Carbon is not generally available. Google says it will make the model available "to a subset of cyber defenders" this week and will "gradually phase access to additional trusted partners" through the Fairwind Program. Availability to developers, businesses and consumers is listed as coming soon, with no date, while Google gathers feedback and iterates on guardrails.

## Key details

All figures below are Google's, read from its announcement on 29 October 2026. We have not run the model, and the announcement's main benchmark table is an image whose numbers we could not read, so we cite only figures that appear in the text.

- **Overall ranking:** Google says Carbon "ranks #1 on the recently updated v5.0 of Artificial Analysis Intelligence Index at 59".
- **Security benchmarks:** 88.2% on SEC-bench Pro (finding vulnerabilities), which Google calls state-of-the-art; 54.8% on ExploitGym (exploitation), also called a new state-of-the-art; and 71.0% on CWE-bench (patching), measured on Collinear's leaderboard. Google says the external benchmarks were run without guardrails.
- **Prompt injection:** On Gray Swan's indirect prompt-injection test Google reports a 0.0% attack success rate for Carbon, against 0.7% for Argon.
- **Coding and reliability:** Google reports +89 Elo points on WebDev Arena to #4 (1768), and says that on Terminal-Bench 4.0 successful cheating fell to 0.0%. It also says high-severity misalignment alerts in internal live coding dropped by almost 80%, and that Carbon cuts unsupported claims by about 2x versus Argon.
- **Price:** Google says Carbon will launch at the same introductory price as Argon, $2 per million input tokens and $10 per million output tokens, with cached input 95% cheaper. A footnote gives $4 and $20 once the introductory period ends; the post does not give an end date for Carbon.
- **Safety process:** Google says it is "actively engaged in the U.S. government's voluntary process for pre-release model testing" and that Carbon uses the same multi-layered safety stack as Argon. Google's post links a safety report, which we did not open.

Google's Fairwind Program page, which we also read, describes the programme as giving trusted partners early access for defensive work, with priority for governments, critical-infrastructure operators and core technology platforms, and rules against sharing or reselling access. That page, as we read it, names Gemini 4 Argon rather than Carbon, so the exact Carbon terms are not documented there yet.

## Why it matters

For most people the practical point is that Carbon cannot be used yet. Gating a model with strong vulnerability-finding and exploitation scores behind a vetted programme is a deliberate choice about dual-use risk, and it means the performance claims cannot be independently tested by the wider public for now.

The other open question is price and timing. Argon's introductory prices end on 30 November, and Google has not said when Carbon will reach the API or how long its own introductory price will last. Independent evaluations of Carbon have not appeared in the sources we checked, so the rankings and benchmark figures should be read as Google's claims.

> Disclosure: Claude, made by Anthropic, was one of the AI tools used to research and draft this article, and Anthropic competes with Google. Figures are Google's own, taken from its 28 October 2026 announcement and its Fairwind Program page.
