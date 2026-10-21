---
title: "Mistral releases Voxtral 3: speech-to-text in 50+ languages, a text-to-speech model and a voice agent SDK"
summary: "Mistral AI's Voxtral 3 family covers batch and realtime transcription in 50+ languages, a text-to-speech model and a voice agent SDK. Prices start at $0.0035 per minute for transcription; the page does not state a licence or say whether weights are published."
seoTitle: "Mistral Voxtral 3: speech from $0.0035/min"
seoDescription: "Mistral's Voxtral 3 speech and voice-agent family, posted 20 October 2026, transcribes 50+ languages from $0.0035 per minute via an EU-hosted API."
lang: en
publishedAt: 2026-10-21T06:00:00Z
entities:
  - Mistral AI
  - Voxtral 3
  - LiveKit
topics:
  - Models
  - Pricing
  - Products
  - Europe
translationKey: mistral-voxtral-3
image: /images/news/mistral-voxtral-3-voice-agent-sdk-2026-10-20.jpg
imageAlt: "Deyron Labs graphic: Mistral Voxtral 3 transcribes 50+ languages, costs $0.004 per minute for the Small Transcribe model and offers realtime transcription under 500 milliseconds"
sources:
  - title: "Voxtral 3: Voice Agent SDK & Speech Models in 50+ Languages"
    url: "https://mistral.ai/news/voxtral-3/"
    publisher: "Mistral AI"
    primary: true
---

## What happened

Mistral AI, the French AI lab, published **Voxtral 3**, a set of speech models plus a voice agent SDK. The announcement page carries no visible publication date; its feed entry is timestamped 20 October 2026. Mistral says the models are available through its EU-hosted API, with European, US and global endpoints, or for self-deployment on a customer's own infrastructure.

## Key details

- **Transcription:** Voxtral Small Transcribe 3 is described by Mistral as its highest-accuracy transcription model, with 50+ languages (including the 24 official EU languages), speaker diarization and context biasing. Price: $0.0040 per minute. Voxtral Mini Transcribe 3 is the cheaper batch model at $0.0035 per minute.
- **Realtime:** a realtime transcription model with "sub-500ms" latency, priced at $0.008 per minute. The page is inconsistent on its language count (40+ on the product card, "over 35" in the text).
- **Text to speech:** a Mini TTS model, priced at $13 per million characters, with 35+ languages and 50+ dialects according to Mistral. Voice cloning needs 30+ minutes of sample audio.
- **Voice agent SDK:** built on LiveKit, using Mistral Small 4 for reasoning. The voice agent API costs $0.04 per minute with Mistral Small 4 and $0.08 per minute with any other reasoning model.
- **Claims not independently verified:** Mistral says Voxtral outperforms Whisper, Scribe v2 and Gemini 3.5 Transcribe. We did not reproduce its charts, and no independent evaluation was available when this was written.
- **Not stated:** the page gives no licence and no Hugging Face link, so it is unclear whether any weights are published. On-premises or private-cloud deployment requires contacting Mistral.

## Why it matters

Per-minute prices this low make large-scale transcription cheap for teams that need European data hosting, and bundling transcription, speech synthesis and an agent SDK targets companies building phone and support assistants. The open questions are practical ones: whether the weights and licence will be published, and whether the accuracy lead holds up in independent tests on a team's own audio.

> Disclosure: Claude, made by Anthropic, was one of the AI tools used to research and draft this article. Anthropic is not involved in this announcement. Prices and performance claims are Mistral's own, read from its announcement on 21 October 2026.
