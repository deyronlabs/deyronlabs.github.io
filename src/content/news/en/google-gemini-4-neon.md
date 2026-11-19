---
title: "Google launches Gemini 4 Neon at $3/$15 per million tokens, with a 1 million token context window"
summary: "On 18 November 2026 Google released Gemini 4 Neon (gemini-4-neon), a model it positions between Gemini 4 Carbon and Hydrogen, in the Gemini API, Gemini for business, Google Antigravity and the Gemini app. Google lists $3 per million input tokens, $0.15 cached and $15 output, with a 1 million token context window. All benchmark and safety figures are Google's own or cited by Google."
seoTitle: "Gemini 4 Neon launches at $3/$15 per 1M tokens"
seoDescription: "Google released Gemini 4 Neon on 18 Nov 2026: $3 input and $15 output per 1M tokens, 1M-token context. Benchmark results are Google's own."
lang: en
publishedAt: 2026-11-19T08:30:00Z
entities:
  - Google
  - Google DeepMind
  - Gemini 4 Neon
  - Gemini 4 Carbon
  - Gemini 4 Hydrogen
  - Google Antigravity
  - Gemini API
  - Fairwind Program
topics:
  - Models
  - Pricing
  - Google
translationKey: google-gemini-4-neon
image: /images/news/google-gemini-4-neon-2026-11-18.jpg
imageAlt: "Deyron Labs graphic: Gemini 4 Neon released 18 November 2026; $3 input, $0.15 cached input and $15 output per million tokens; 1 million token context; results are Google's own"
sources:
  - title: "Introducing Gemini 4 Neon"
    url: "https://blog.google/innovation-and-ai/models-and-research/gemini-models/introducing-gemini-4-neon/"
    publisher: "Google (Koray Kavukcuoglu, 18 November 2026)"
    primary: true
  - title: "Gemini 4 Neon model card (linked from Google's post; not opened by us)"
    url: "https://storage.googleapis.com/deepmind-media/Model-Cards/Gemini-4-Neon-Model-Card.pdf"
    publisher: "Google DeepMind"
    primary: true
  - title: "Google makes Gemini 4 Carbon generally available at $2/$10 per million tokens, rising to $4/$20 on 1 December"
    url: "https://deyronlabs.com/en/news/google-gemini-4-carbon-general-availability/"
    publisher: "Deyron Labs"
---

## What happened

On 18 November 2026 (21:00 UTC) Google published "Introducing Gemini 4 Neon", by Koray Kavukcuoglu, and began rolling the model out. Google describes Neon as bringing "frontier-level intelligence" with fast end-to-end task completion across software engineering, knowledge work and science, at a lower cost. It sits between Gemini 4 Carbon, which Google positions for the hardest long-horizon projects, and Gemini 4 Hydrogen, which it positions for fast everyday execution.

Google says Neon is available in the Gemini API (Google AI Studio and Android Studio, paid tier; model string `gemini-4-neon`), in Gemini for business, in Google Antigravity and in the Gemini app for Google AI Pro and Ultra subscribers. Access for cyber defenders through the Fairwind Program is to begin "over the next few days" via the Cloud account team.

## Key details

All figures below are Google's, read from its 18 November post on 19 November 2026. We have not run the model, and we did not open the model card or the safety post that Google links.

- **Price and context:** $3 per million input tokens, $0.15 per million cached input tokens (Google calls this a 95% discount) and $15 per million output tokens, with a 1 million token context window. For comparison, Carbon's introductory price was $2 and $10, rising to $4 and $20 on 1 December, according to Google's 10 November announcement as we reported it.
- **Thinking levels and cost:** Google says Neon has four thinking levels. At the default "high" level it costs 32% less per task than Carbon, and at "xhigh" it costs "36%+" less per task than competing models at their highest setting.
- **Rankings Google cites:** #3 on the Artificial Analysis Intelligence Index (score 61 at xhigh), #2 on the Vals Index (70.9%), #2 on Arena's Agent Arena Index (1336), and #1 on Zapier AutomationBench (56.3%) and on Andon Labs' Vending-Bench 2. Google also cites 58.6 on the Artificial Analysis Coding Agent Index (#1) and 65.2% on Terminal-Bench 4.1. These are the vendor's presentation of third-party and in-house results, not our measurements.
- **Security results (Google-reported):** 90.5% on SEC-bench Pro and 76% on the hard tier of AutoBaxBench, both described by Google as state of the art.
- **Safety figures (Google's tests):** a 0.09% misaligned-action rate on Google's agentic safety suite, a 99.2% pass rate on its agent honesty evaluation and 0.0% attack success on the Gray Swan indirect prompt injection benchmark at the highest thinking level. Google says under-service fell 43%–56% and overreach 15%–35% versus Carbon.
- **Orchestration:** in Antigravity, Google says Neon can act as an orchestrator that directs parallel Hydrogen subagents. Its demos (a Blender lab bench, a ski simulator, a 100,000-cell spreadsheet) are demonstrations, not benchmarks.
- **Not stated in the post:** licence or usage terms beyond the hosted-service availability above, and the model card and safety documents were not opened by us.

## Why it matters

Neon fills the middle of Google's Gemini 4 line: a model priced above Carbon's introductory rate but, by Google's account, cheaper per task because it uses fewer tokens at the same effort. That claim, and the ranking of third in an independent index, are the parts to test on your own workload before changing models: per-task cost depends on how many tokens your tasks need, not on the per-token price alone.

The date to watch is 1 December, when Carbon's introductory pricing is scheduled to double; that is when the Neon-versus-Carbon cost comparison becomes concrete. Independent evaluations beyond the third-party rankings Google cites were not available in the sources we checked.

> Disclosure: Claude, made by Anthropic, was one of the AI tools used to research and draft this article, and Anthropic competes with Google. Figures are Google's own, from its 18 November 2026 announcement.
