---
title: "DeepSeek opens its full app feature set to developers: web search, file input, URL reading and a safety check in one API"
summary: "On 13 November 2026 DeepSeek's API changelog announced the full suite of the DeepSeek app's chat features for developers. The deepseek-flash model gains web search, deep-thinking search, file input, URL reading and a model-safety parameter, plus standalone Search and Fetch, OCR, ASR and TTS APIs. No prices are given in the entry."
seoTitle: "DeepSeek API adds web search, file input, TTS"
seoDescription: "DeepSeek's 13 Nov 2026 changelog opens web search, file input, URL reading, OCR, ASR and TTS to developers; prices are on its pricing page."
lang: en
publishedAt: 2026-11-14T07:10:00Z
entities:
  - DeepSeek
  - deepseek-flash
  - DeepSeek-V4.1-Flash
topics:
  - APIs
  - Agents
  - DeepSeek
translationKey: deepseek-full-app-api-suite
image: /images/news/deepseek-full-app-api-suite-2026-11-13.jpg
imageAlt: "Deyron Labs graphic: DeepSeek API: full app feature set, 13 Nov 2026; Web search, deep-thinking search, file input, URL reading; Model-safety check parameter; Standalone Search and Fetch, OCR, ASR, TTS APIs; Prices not in the entry; see pricing page"
sources:
  - title: "DeepSeek API change log: Releasing the full suite of application APIs"
    url: "https://api-docs.deepseek.com/updates/"
    publisher: "DeepSeek, 13 November 2026"
    primary: true
---

## What happened

DeepSeek's API change log has an entry dated 13 November 2026, "Releasing the full suite of application APIs". It opens to developers the chat features of the DeepSeek app. The documentation's landing page now shows a banner listing web search, file input, URL reading, model safety, ASR, TTS and more.

## Key details

From the change log, read on 14 November 2026. We have not tested the APIs.

- **On the deepseek-flash model**, in the Messages, Responses and Chat Completions APIs: web search (with thinking off, using a deepseek_web_search tool, with cited answers); deep-thinking search (thinking on, searching and reading links over several reasoning steps); file input (PDFs, Office files, images and others); URL reading (a deepseek_read_url tool); and a model-safety check parameter that reviews input and output and returns a refusal marker.
- **Standalone APIs listed:** Search and Fetch, OCR, ASR and TTS.
- **Demo client:** DeepSeek also open-sourced a demo chat client that can import DeepSeek chat history.
- **Model behind it:** the docs name `deepseek-flash`, served by DeepSeek-V4.1-Flash-1017, and `deepseek-v4-pro`. Earlier entries show Search and Fetch opened on 17 October (see our earlier article on its $0.75 per 1,000 pricing).
- **Not stated in the entry:** prices (it points to the pricing page), a license, or deprecations.

## Why it matters

Until now a developer who wanted DeepSeek's app experience, with search, file reading and speech, had to assemble it from separate tools. A single API with those features lowers that work and puts DeepSeek closer to the all-in-one platforms from US labs.

It is a product expansion, not a new model, so the details to check are the per-feature prices on DeepSeek's pricing page and how well web search and file reading perform on your own tasks.

> Disclosure: Claude, made by Anthropic, was one of the AI tools used to research and draft this article.