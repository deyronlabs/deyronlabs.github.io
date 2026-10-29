---
title: "ElevenLabs introduces Cue, a forced-alignment model for character-level audio timing"
summary: "On 28 October 2026 ElevenLabs described Cue, a forced-alignment model that places each character of a transcript on the audio timeline, now behind its speech-to-text and available through a Forced Alignment API. ElevenLabs reports an average timing error of 179 ms on full recordings against 283 ms or more for open-source tools. The figures are the company's own."
seoTitle: "ElevenLabs Cue: character-level audio timing"
seoDescription: "ElevenLabs said on 28 Oct 2026 that its Cue aligner averages 179 ms timing error on real recordings; the figures are the company's own."
lang: en
publishedAt: 2026-10-29T17:30:00Z
entities:
  - "ElevenLabs"
  - "Cue"
  - "Forced Alignment API"
  - "Scribe"
topics:
  - Voice
  - Products
translationKey: elevenlabs-cue-forced-alignment-model
image: /images/news/elevenlabs-cue-forced-alignment-model-2026-10-29.jpg
imageAlt: "Deyron Labs graphic: ElevenLabs Cue forced-alignment model announced 28 October 2026; company reports 179 ms average timing error on full recordings"
sources:
  - title: "Forced alignment with Cue: Character-level audio timing"
    url: "https://elevenlabs.io/blog/cue-aligner"
    publisher: "ElevenLabs (28 October 2026)"
    primary: true
---

## What happened

On 28 October 2026 ElevenLabs published a blog post introducing Cue, a forced-alignment model. Forced alignment takes an existing transcript and finds when each word, or here each character, is spoken in the audio. ElevenLabs says Cue already sits behind every speech-to-text transcription on its platform and can be used on its own through its Forced Alignment API.

## Key details

All figures below come from the ElevenLabs post, read on 29 October 2026. They are the company's own benchmarks and we have not reproduced them.

- **Accuracy claim:** on real-world recordings, ElevenLabs says Cue is more accurate than every aligner it tested, in all 29 languages of its benchmark. Average timing error on full recordings is 179 ms, against 283 ms to more than 6,000 ms for open-source tools.
- **Noisy English audio:** 57 ms average error, against 65 ms to 920 ms for the other tools.
- **Songs:** on a subset of the JamendoLyrics dataset in English, French, Spanish and German, 92.7% of words fall within 0.3 seconds, against 82.0% for the next best tool.
- **Speed:** ElevenLabs says one hour of audio is aligned in around half a second on its production GPU, against nearly two seconds for Qwen3-ForcedAligner.
- **Inconsistencies on the page:** the introduction says an hour of audio takes "less than a second" while the body says about half a second, and the page refers both to 29 benchmark languages and to "more than 90" languages.

## Why it matters

Precise word timing is what makes subtitles, karaoke-style captions and audio editing line up with speech, so a more accurate aligner mainly helps anyone who builds captions from generated or recorded voice. The numbers are the vendor's, and the benchmark covers 29 languages, so results in other languages or on other audio are untested.

> Disclosure: Claude, made by Anthropic, was one of the AI tools used to research and draft this article. Deyron Labs uses ElevenLabs to generate voiceovers for its videos, so readers should weigh this coverage with that in mind. Details come from ElevenLabs' 28 October 2026 post, read on 29 October 2026.
