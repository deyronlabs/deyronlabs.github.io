---
title: "Gradium releases Phonon TTS, tiny on-device text-to-speech models with open weights on Hugging Face"
summary: "On 5 November 2026 Gradium published Phonon TTS on Hugging Face: two text-to-speech models of about 65 MB and 75 MB that run on-device, in five languages with more than 100 built-in voices. The English 31M model is Apache 2.0; the 40M multilingual model is non-commercial. The benchmark rankings are cited by Gradium from the Open TTS Leaderboard."
seoTitle: "Gradium Phonon TTS: 31M on-device open model"
seoDescription: "Gradium released Phonon TTS on 5 Nov 2026: 65-75 MB on-device speech models in five languages; the 31M English model is Apache 2.0."
lang: en
publishedAt: 2026-11-07T07:00:00Z
entities:
  - Gradium
  - Phonon TTS
  - Hugging Face
  - Open TTS Leaderboard
  - Pocket TTS
topics:
  - Models
  - Open-weight
  - Audio
translationKey: gradium-phonon-tts-on-device-open-weights
image: /images/news/gradium-phonon-tts-2026-11-05.jpg
imageAlt: "Deyron Labs graphic: Gradium Phonon TTS, two on-device speech models of 65-75 MB, five languages, 100+ voices, 31M English model under Apache 2.0, 28 ms to first audio as reported by Gradium"
sources:
  - title: "A Closer Look at Phonon TTS. Launching High-Quality On-Device Speech That Tops the Benchmarks."
    url: "https://huggingface.co/blog/phonon-tts"
    publisher: "Hugging Face blog (Gradium)"
    primary: true
---

## What happened

On 5 November 2026 Gradium published **Phonon TTS** in a post on the Hugging Face blog, calling it its first open release. Phonon is a family of text-to-speech models small enough to run on a device: the post says they come in two sizes, about 65 MB and 75 MB. The weights are on Hugging Face (for example `gradium/phonon-31m-en`), there is a browser demo in a Hugging Face Space, and support is in Transformers, which the post says starts at v5.21.

We read the Hugging Face post on 7 November 2026. The post is written by the Gradium team, so the claims below are Gradium's own.

## Key details

- **Models:** Phonon 31M is English-only. Phonon 40M covers English, French, German, Spanish and Portuguese. The post gives about 30.8 million parameters for the 31M model and 10.3 million for its audio tokenizer; it does not give a parameter count for the 40M model, nor which file size belongs to which model.
- **Voices:** more than 100 built-in voices. Custom voices go through voice cloning or voice design in Gradium Studio, its own product.
- **License:** Phonon 31M is Apache 2.0, so it can be used in commercial products. Phonon 40M is under a non-commercial license. For the other models the post says commercial use is priced by number of users, not by how much speech is generated; no price is given.
- **Benchmarks (Open TTS Leaderboard, as cited by Gradium):** Phonon ranks first for intelligibility in German and Spanish and in the top three in every language Gradium evaluated, “next to models up to 100 times its size”. On a CPU streaming test, 95th-percentile time to first audio is 28 ms for Phonon 31M (English) and 38 ms for Phonon 40M (English), against 165 ms for Pocket TTS. The post does not say who ran the measurements or on what hardware.
- **Adoption:** Gradium says the model was downloaded more than 200,000 times in its first two weeks; the post does not name which model that count refers to.
- **Not stated:** the license text beyond the labels above, a price for commercial use, and independent test results.

## Why it matters

Speech models this small can run locally, without sending text to a cloud service, which matters for offline apps, privacy-sensitive products and cheap voice features on ordinary hardware. An Apache 2.0 English model is the practical part: developers can ship it commercially. The multilingual model is free only for non-commercial use, so anyone planning a product in French, German, Spanish or Portuguese should check the terms and the user-based pricing first.

Treat the rankings as a starting point. The post is the maker's own, it does not explain who produced the latency figures, and leaderboard results depend on which languages and metrics are shown. Listening tests on your own text and device are still the real check.

> Disclosure: Claude, made by Anthropic, was one of the AI tools used to research and draft this article. Gradium is not affiliated with Deyron Labs; all performance claims are Gradium's own.
