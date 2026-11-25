---
title: "Sarvam launches Dictate and Extract APIs: dictation at ₹0.50 a minute, document extraction from ₹1 a page"
summary: "Sarvam AI released two APIs this week: Dictate (speech recognition plus editing, ₹0.50 per minute) and Extract (structured JSON from documents up to 500 pages, ₹1 or ₹2.50 per page). Benchmarks are Sarvam's own runs and comparisons use its own test sets."
seoTitle: "Sarvam Dictate and Extract APIs launched"
seoDescription: "Sarvam AI launched Dictate (₹0.50 per minute) and Extract (from ₹1 per page) on 23-24 Nov 2026; benchmark figures come from Sarvam's own runs."
lang: en
publishedAt: 2026-11-25T07:10:00Z
entities:
  - Sarvam AI
  - Sarvam Dictate
  - Sarvam Extract
topics:
  - Products
  - Pricing
image: /images/news/sarvam-dictate-extract-apis.jpg
imageAlt: "Deyron Labs graphic: Sarvam Dictate at 0.50 rupees per minute and Sarvam Extract at 1 or 2.50 rupees per page, with Sarvam's own benchmarks"
translationKey: sarvam-dictate-extract-apis
sources:
  - title: "Introducing Sarvam Dictate"
    url: "https://www.sarvam.ai/blogs/sarvam-dictate/"
    publisher: "Sarvam AI"
    primary: true
  - title: "Introducing Sarvam Extract"
    url: "https://www.sarvam.ai/blogs/extract-api/"
    publisher: "Sarvam AI"
    primary: true
---

## What happened

Indian AI company Sarvam published two product posts: Sarvam Dictate on 23 November 2026 and Sarvam Extract on 24 November 2026. Both are APIs. We read both Sarvam posts on 25 November 2026. All benchmark numbers below come from Sarvam's own tests; we did not reproduce them.

## Key details

- **Dictate:** one call does speech recognition and editing, returning intended text in English and 22 Indian languages. Sarvam says Saaras v4 transcribes and a version of Sarvam 105B trained for dictation edits the result. Price: ₹0.50 per minute ($0.33 per hour). Available via API at /v2/dictate; a jobs endpoint handles audio over 30 seconds. The response includes the raw transcript, the edited text and applied vocabulary corrections; vocabularies of up to 1,000 entries are supported.
- **Dictate results (Sarvam's test set from its own Kivi app, judged by three models from other providers):** share of characters needing edits was 4.2% for Dictate versus 7.0% for Gemini 3.5 Transcribe and 5.3% for AssemblyAI Dictation on 2,691 English dictations; 8.8% versus 15.5% for Gemini across 1,370 dictations in 18 Indian languages. Sarvam says it plans to release an evaluation set.
- **Extract:** returns structured JSON from documents with a source page, bounding box and confidence per value; handles up to 500 pages; English and 22 Indian languages; available to users in India and the US, with on-premises options for enterprises. Basic mode costs ₹1 per page ($10 per 1,000 pages) and scored 94.4 on ExtractBench (370 documents); Advanced adds a second pass, costs ₹2.50 per page and scored 95.4. Sarvam lists LlamaExtract Agentic Plus at 96.2 for ₹7.12 per page and Reducto Deep Extract at 96.1 for ₹6.03.
- **Caveats stated by Sarvam:** the Extract scorer was adjusted for empty object groups (unmodified scores 95.33 Advanced, 94.36 Basic); results are from Sarvam's own runs; known remaining errors include dropped or added words and missing rows in long tables. Only successfully processed pages are billed, and new accounts get free credits.

## Why it matters

Both products compete on price and on Indian-language coverage, where Sarvam argues general models are weaker. Developers handling Hindi, Marathi or Hinglish audio, or long Indian-language documents, now have a priced alternative to test. Because the comparisons use Sarvam's own data and settings, an independent test on your own documents is the sensible next step.

> Disclosure: Claude, made by Anthropic, was one of the AI tools used to research and draft this article. Sarvam AI is not affiliated with Deyron Labs.
