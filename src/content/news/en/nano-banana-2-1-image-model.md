---
title: "Google releases Nano Banana 2.1 and cuts its image API prices by up to half"
summary: "Google released Nano Banana 2.1, an image generation and editing model built on Gemini 3.6 Flash, on 6 October 2026. Its API price is $0.0336 per 1K image, about half the $0.067 of Nano Banana 2 at 1K and 2K, and about a quarter lower at 4K. The quality scores come from Google's own model card."
seoTitle: "Nano Banana 2.1 launches, image API prices cut"
seoDescription: "Google released Nano Banana 2.1, an image generation and editing model built on Gemini 3.6 Flash, on 6 October 2026."
lang: en
publishedAt: 2026-10-07T15:25:00Z
entities:
  - Google
  - Google DeepMind
  - Nano Banana 2.1
  - Nano Banana 2
  - Gemini 3.6 Flash
  - Google AI Studio
  - Google Flow
  - Google Stitch
topics:
  - Models
  - Image generation
  - Pricing
translationKey: nano-banana-2-1-image-model
video: "https://www.youtube.com/shorts/mvlga-asVzI"
videoPublishedAt: 2026-10-07
image: /images/news/nano-banana-2-1-2026-10-06.jpg
imageAlt: "Deyron Labs graphic: Nano Banana 2.1 costs about half as much per image as Nano Banana 2, and its scores come from Google's own model card"
sources:
  - title: "Nano Banana 2.1 model card"
    url: "https://deepmind.google/models/model-cards/nano-banana-2-1/"
    publisher: "Google DeepMind"
    primary: true
  - title: "Gemini API release notes"
    url: "https://ai.google.dev/gemini-api/docs/changelog"
    publisher: "Google"
    primary: true
  - title: "Gemini API pricing"
    url: "https://ai.google.dev/gemini-api/docs/pricing"
    publisher: "Google"
    primary: true
  - title: "Nano Banana 2.1 Now In Google AI Mode In Search"
    url: "https://www.seroundtable.com/nano-banana-21-google-ai-mode-42246.html"
    publisher: "Search Engine Roundtable"
---

## What happened

On 6 October 2026, Google released Nano Banana 2.1, the successor to Nano Banana 2 (the model Google lists in its API as `gemini-3.1-flash-image`). It generates and edits images from text and image prompts. Google's model card says it is based on Gemini 3.6 Flash and accepts a context window of up to 1 million tokens.

The Gemini API release notes list the new model as generally available under the ID `gemini-nano-banana-2.1`, with 1K, 2K and 4K output and wide aspect ratios such as 1:4, 4:1, 1:8 and 8:1. Google describes improvements in visual quality, prompt adherence, character consistency across turns and text rendering.

## Key details

- **Price (Gemini API, per image):** $0.0336 at 1K, $0.0504 at 2K and $0.113 at 4K. Batch prices are half of the 1K and 2K rates ($0.0168 and $0.0252) and $0.0567 at 4K. The pricing page lists no free tier.
- **Compared with Nano Banana 2:** that model's listed prices are $0.067 at 1K, $0.101 at 2K and $0.151 at 4K. By our arithmetic the new prices are about 50% lower at 1K and 2K and about 25% lower at 4K, not 50% across the board.
- **Where it runs:** Google's model card lists the Gemini app, Google AI Studio, the Gemini API, Google Search AI Mode, Google Ads, Google Flow and Google Stitch. Search Engine Roundtable reports that in AI Mode it is reached through a banana icon under the search box, citing a Google announcement.
- **Quality scores, as reported by Google:** the model card lists an overall text-to-image preference score of 1050 Elo in Thinking mode versus 990 for Nano Banana 2, and a multi-character consistency score of 1106 versus 978.
- **Limitations Google lists:** small text renders poorly, characters are not always consistent between input and output, the model sometimes confuses spatial positions, and 3D reasoning and world knowledge are limited. Its knowledge cutoff is March 2026, with some areas older.
- **Safety:** Google says the model met its child safety launch thresholds and reached no Tracked or Critical Capability Levels in its frontier safety assessment.
- **Old model:** the release notes mark Nano Banana 2 as deprecated and say no shutdown date has been announced. One third-party blog cites 29 October as a deadline. We could not confirm that date in Google's documentation.

## Why it matters

The price cut is the clearest change. If you generate images through the API at 1K or 2K, the same job now costs roughly half as much, and Google did not raise the price to pay for a better model. At 4K the saving is smaller, so check the arithmetic against your own mix of resolutions.

The quality claims need more caution. The Elo scores come from Google's model card, and we found no independent evaluation at the time of writing. A 60-point gap in preference scores suggests a visible gain, but it says little about your own prompts. Run a few of your real prompts through both models before you migrate.

The reach of the release is also notable. Putting the model in AI Mode, Ads, Flow and Stitch means many people will meet it inside Google products before they ever call the API. The listed weaknesses, especially small text and spatial placement, are exactly the things people check first in a logo, a diagram or an ad.

> Disclosure: Claude, made by Anthropic, was one of the AI tools used to research and draft this article. Performance and pricing claims are Google's own unless stated otherwise.
