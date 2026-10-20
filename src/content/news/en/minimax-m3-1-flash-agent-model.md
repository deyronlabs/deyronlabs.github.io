---
title: "MiniMax launches M3.1 Flash, an agent-focused model at $0.15 per million input tokens, with weights promised later"
summary: "MiniMax says M3.1 Flash is nearly three times faster online than its predecessor and 70% cheaper to use on agentic tasks. It costs $0.15 per million input and $0.60 per million output tokens, and the company says weights will be released later, without a date."
seoTitle: "MiniMax M3.1 Flash: $0.15 per 1M input tokens"
seoDescription: "MiniMax's M3.1 Flash agent model, announced 19 October 2026, costs $0.15 per million input tokens; the company says weights will follow later."
lang: en
publishedAt: 2026-10-20T17:00:00Z
entities:
  - MiniMax
  - MiniMax M3.1 Flash
  - MiniMax Code
topics:
  - Models
  - Pricing
  - Agents
  - China
translationKey: minimax-m3-1-flash
image: /images/news/minimax-m3-1-flash-agent-model-2026-10-19.jpg
imageAlt: "Deyron Labs graphic: MiniMax M3.1 Flash costs $0.15 per million input and $0.60 per million output tokens, is about three times faster online, and its weights are promised for later"
sources:
  - title: "MiniMax M3.1 Flash"
    url: "https://www.minimax.io/blog/minimax-m31f"
    publisher: "MiniMax"
    primary: true
  - title: "TLDR AI, 20 October 2026 (newsletter, secondary)"
    url: "https://tldr.tech/ai"
    publisher: "TLDR"
    primary: false
---

## What happened

MiniMax, the Chinese AI lab, published an announcement dated 19 October 2026 for **M3.1 Flash**, a model it describes as a step up in agentic tasks, coding, computer use and cybersecurity. The company says the model is available through the MiniMax API, its "M Plan" subscription and MiniMax Code, and that "model weights will be released later". No release date for the weights is given.

## Key details

- **Speed (MiniMax):** online inference is "nearly three times faster" than the previous model, with output of 200+ tokens per second in everyday use and a median of 170+.
- **Cost (MiniMax):** the company says overall usage cost on agentic tasks is 70% lower than its predecessor. API pricing is flat per million tokens: $0.15 for input, $0.60 for output and $0.015 for cached input.
- **Benchmarks, all reported by MiniMax and not independently verified:** BankerToolBench 76.2; DeepSWE v1.1 73.7%, which MiniMax says puts it alongside top models; OSWorld V2 61.7 and Agents' Last Exam 29.6, both described as first among Chinese models; CyberGym 82%. AutomationBench-AA is described as "among the top performers" without a score. The announcement does not state a context window.
- **Testing history:** MiniMax says an early version ran anonymously as "Space Bunny" and processed more than 200 trillion tokens.
- **Still to come:** a higher-capability "Pro" model is planned, with no date.
- **Licence and weights:** none published yet, so the licence terms are unknown.

## Why it matters

For developers building coding or computer-use agents, the announced price puts a capable-sounding model at a fraction of typical frontier-model rates, and the speed figures matter for long agent loops where latency adds up. The caveats are significant: every score comes from MiniMax, the weights and licence are not yet available, and "first among Chinese models" is the company's own ranking. Teams should wait for independent evaluations and the weights release before treating the numbers as settled.

> Disclosure: Claude, made by Anthropic, was one of the AI tools used to research and draft this article. Anthropic is a competitor of MiniMax. Prices and benchmark figures are MiniMax's own and were read from its announcement on 20 October 2026.
