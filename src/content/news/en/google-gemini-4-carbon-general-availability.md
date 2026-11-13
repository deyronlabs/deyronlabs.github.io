---
title: "Google makes Gemini 4 Carbon generally available at $2/$10 per million tokens, rising to $4/$20 on 1 December"
summary: "On 10 November 2026 Google made Gemini 4 Carbon (gemini-4-carbon) generally available, two weeks after limiting it to cyber defenders. It is open to paying API developers, enterprises and Google AI Ultra subscribers at an introductory $2 per million input tokens and $10 per million output tokens through 30 November, then $4 and $20. All benchmark and safety figures are Google's own."
seoTitle: "Gemini 4 Carbon is GA: $2/$10 until 30 Nov"
seoDescription: "Google made Gemini 4 Carbon generally available on 10 Nov 2026: $2/$10 per 1M tokens until 30 Nov, then $4/$20. Results are Google's own."
lang: en
publishedAt: 2026-11-11T18:42:00Z
entities:
  - Google
  - Google DeepMind
  - Gemini 4 Carbon
  - Gemini 4 Argon
  - Google Antigravity
  - Gemini API
  - Fairwind Program
topics:
  - Models
  - Pricing
  - Google
translationKey: google-gemini-4-carbon-general-availability
image: /images/news/google-gemini-4-carbon-general-availability-2026-11-10.jpg
video: "https://www.youtube.com/shorts/5hQpVyXaNO4"
videoPublishedAt: 2026-11-13
imageAlt: "Deyron Labs graphic: Gemini 4 Carbon generally available from 10 November 2026; $2 input and $10 output per million tokens through 30 November, then $4 and $20; results are Google's own"
sources:
  - title: "Gemini 4 Carbon is now available"
    url: "https://blog.google/innovation-and-ai/models-and-research/gemini-models/gemini-4-carbon-now-available/"
    publisher: "Google (Koray Kavukcuoglu, 10 November 2026)"
    primary: true
  - title: "Gemini 4 Carbon and /swarm"
    url: "https://antigravity.google/blog/gemini-4-carbon-in-google-antigravity/"
    publisher: "Google Antigravity team, 10 November 2026"
    primary: true
  - title: "Gemini 4 Carbon: our next frontier model"
    url: "https://blog.google/innovation-and-ai/models-and-research/gemini-models/introducing-gemini-4-carbon/"
    publisher: "Google, 28 October 2026"
    primary: true
---

## What happened

On 10 November 2026 (16:00 UTC) Google published "Gemini 4 Carbon is now available", by Koray Kavukcuoglu, and made Carbon generally available for developers, enterprises, scientists and consumers. Two weeks earlier, on 28 October, Carbon had been released only to a set of cybersecurity defenders through Google's Fairwind Program. The API model ID is `gemini-4-carbon`.

Google's post says Carbon is available to all paying developers and enterprises through the Gemini API (Google AI Studio and Android Studio) and through Gemini for business. Google AI Ultra subscribers get it in Google Antigravity, the Gemini app and AI Mode in Search. Cyber-specific use continues through Fairwind on a rolling basis.

## Key details

All figures below are Google's, read from its 10 November announcements on 11 November 2026. We have not run the model, and we did not open the model card or the safety report that the post links.

- **Price:** an introductory $2 per million input tokens and $10 per million output tokens, the same as Gemini 4 Argon. A footnote says $4 and $20 apply after the introductory period ends on 30 November 2026. The post states no long-context tier.
- **Benchmarks (vendor-reported):** Google says Carbon ranks #1 on CursorBench 4.0, Perplexity's WANDR and Zapier AutomationBench at "more than 2X lower cost per task" than the next best external model, and #2 on Artificial Analysis's Multimodal Knowledge Agent benchmark at more than 6X lower average cost per task than the top model. It says Carbon matches the best model on Hebbia's financial agentic benchmark and leads SEC-bench Pro, ExploitGym and CWE-bench v1, without giving numbers for those in the post.
- **Reliability and safety (Google's tests):** a 92% pass rate on a 375-task honesty benchmark versus 70% for Argon; in simulated attack environments Carbon blocked 99% of attack trajectories, with a per-attempt breach rate of 0.8% versus 3.1% for Argon; on Gray Swan's automated cyberattack test the success rate was 2.17% versus 9.86% for Argon. Trajectory Labs, a third party Google cites, reported no new universal jailbreaks across 132 hours and more than 13,000 requests.
- **Not for every job:** Google says Argon "remains the ideal choice for the majority" of software engineering and knowledge work, and that Carbon uses more tokens.
- **Antigravity:** Google's Antigravity team says Carbon is rolling out there to AI Ultra subscribers in the app, CLI and IDE extensions, alongside `/swarm`, a multi-agent mode in preview. It warns that swarms "consume quota much faster than a standard chat". Scientists can apply for six months of free access to Argon and Carbon at the highest usage tier.

## Why it matters

The practical change is access: a model that was limited to vetted security teams since 28 October is now an ordinary paid API model, at the same introductory price as Argon but with a higher token appetite. The cost-per-task claims are Google's and compare against Google's own choice of "next best" competitor, so a per-task cost test on your own workload is the safer way to decide between Carbon and the cheaper Argon.

The date to watch is 30 November: both models' introductory prices are scheduled to double on 1 December. We did not find Carbon in Google's public pricing page or API changelog when we checked on 11 November, so confirm the price in AI Studio before budgeting. Independent evaluations of Carbon were not available in the sources we checked.

> Disclosure: Claude, made by Anthropic, was one of the AI tools used to research and draft this article, and Anthropic competes with Google. Figures are Google's own, from its 10 November 2026 announcements.
