---
title: "Google launches Gemini Decisions API and Decision 1, a model that scores options for $0.10 per million input tokens"
summary: "On 11 November 2026 Google launched the Gemini Decisions API, powered by a new model, Gemini Decision 1, that answers up to 1,000 yes/no, choice and rubric-scoring questions in one pass with a confidence from 0 to 1. Google lists $0.10 per million input tokens, free output, a 256K-token input limit and text, image, audio, video and PDF input. Speed and cost comparisons are Google's own."
seoTitle: "Gemini Decision 1: $0.10 per million tokens"
seoDescription: "Google launched the Gemini Decisions API on 11 Nov 2026: Gemini Decision 1 scores options for $0.10 per 1M input tokens, with free output."
lang: en
publishedAt: 2026-11-12T07:30:00Z
entities:
  - Google
  - Google DeepMind
  - Gemini Decisions API
  - Gemini Decision 1
  - Google AI Studio
  - OpenRouter
topics:
  - Models
  - Agents
  - Pricing
  - Google
translationKey: google-gemini-decisions-api-decision-1
image: /images/news/google-gemini-decisions-api-decision-1-2026-11-11.jpg
imageAlt: "Deyron Labs graphic: Google Gemini Decisions API and Gemini Decision 1 launched 11 November 2026; $0.10 per million input tokens, free output, up to 1,000 questions per pass, 256K-token input; comparisons are Google's own"
sources:
  - title: "Gemini Decisions API"
    url: "https://blog.google/innovation-and-ai/technology/developers-tools/gemini-decisions-api/"
    publisher: "Google DeepMind (Min Choi and Felix Yu), 11 November 2026"
    primary: true
  - title: "Gemini Decisions API (link post)"
    url: "https://simonwillison.net/2026/Nov/11/gemini-decisions-api/"
    publisher: "Simon Willison, 11 November 2026"
    primary: false
---

## What happened

On 11 November 2026 (18:00 UTC) Google published "Gemini Decisions API", written by Min Choi and Felix Yu of Google DeepMind. The API is powered by a new model, Gemini Decision 1 (model ID `gemini-decision-1`), and is available through the Gemini API in Google AI Studio. Instead of writing text, the model answers fixed questions about its input and returns a confidence between 0 and 1 for each answer.

## Key details

Figures are Google's unless stated otherwise, read from its post on 12 November 2026. We have not run the model.

- **What it does:** Google says a single pass can evaluate up to 1,000 yes/no, choice and rubric-scoring questions. Choice questions take 2 to 255 options, and score questions use an ordered rubric.
- **Inputs:** up to 256K tokens across text, images, audio, video and PDFs.
- **Speed:** Google states 150 to 250 ms end to end, with a median of 50 to 100 ms of model compute.
- **Price:** $0.10 per million input tokens and $0 for output tokens, with a free tier in AI Studio for prototyping. Google says this is nearly 5x cheaper across a shared benchmark suite than Gemini 3.5 Flash-Lite with the Interactions API, and that its Gemini Notebook product sees up to 40% lower latency with it.
- **Availability:** AI Studio, the API docs and a playground, OpenRouter (`google/gemini-decision-1`), and integrations with LangChain, Vercel AI SDK, LiteLLM, Pydantic AI, Pipecat and LiveKit. Google says support in Gemini in Google Cloud is "coming soon".
- **Third-party note:** developer Simon Willison, in a hands-on post, reported that Gemini returned graded probabilities (for example 0.9234 for "robot") where a rival decision model returned only 1.0 or 0.0. This is one informal test, not a benchmark.
- **Not stated in the sources we read:** parameter count, license, a model card, and numeric benchmark scores (the benchmark charts in Google's post are images).

## Why it matters

Google is the latest of several vendors to ship a "decision model": a small, cheap model for routing, classification, checking and workflow control rather than for chat. Microsoft announced Decision-1 on 9 October at $0.042 per million input tokens, and OpenAI has a Decisions API (both covered earlier on this site), so the choice for developers now includes three large providers with similar designs. Google's version is distinguished by audio, video and PDF input and by confidence scores that are graded rather than 0 or 1.

The speed and cost comparisons are Google's, against a Google baseline, so test it on your own routing or grading task and measure accuracy, not only price. The model card and the licence terms are the things to look for before building on it.

> Disclosure: Claude, made by Anthropic, was one of the AI tools used to research and draft this article, and Anthropic competes with Google. Figures are Google's own, from its 11 November 2026 announcement.
