---
title: "NVIDIA releases Nemotron 3.5 Transcribe, an open speech-to-text model for 40 languages, with the Granary v2 dataset"
summary: "On 28 October 2026 NVIDIA published Nemotron 3.5 Transcribe, a speech-to-text model with about 4 billion active parameters that handles recordings up to an hour in 40 languages, plus the Granary v2 dataset. The model card lists the OpenMDW-1.1 license and permits commercial use. NVIDIA's own pages disagree on whether the model has 30 or 34 billion parameters in total."
seoTitle: "NVIDIA Nemotron 3.5 Transcribe: 40 languages"
seoDescription: "NVIDIA released Nemotron 3.5 Transcribe on 28 Oct 2026: open speech-to-text for 40 languages, hour-long audio, OpenMDW-1.1 license."
lang: en
publishedAt: 2026-10-29T06:45:00Z
entities:
  - NVIDIA
  - Nemotron 3.5 Transcribe
  - Granary v2
  - Hugging Face
topics:
  - Models
  - Open-weight
translationKey: nvidia-nemotron-3-5-transcribe
image: /images/news/nvidia-nemotron-3-5-transcribe-2026-10-29.jpg
imageAlt: "Deyron Labs graphic: NVIDIA Nemotron 3.5 Transcribe released 28 October 2026; 40 languages, up to one hour of audio, OpenMDW-1.1 license; NVIDIA lists both 30B and 34B total parameters"
sources:
  - title: "NVIDIA Nemotron 3.5 Transcribe and Granary v2: Intelligent Multilingual Transcription You Can Prompt and Adapt"
    url: "https://huggingface.co/blog/nvidia/nemotron-transcribe-granary"
    publisher: "NVIDIA on Hugging Face (28 October 2026)"
    primary: true
  - title: "NVIDIA-Nemotron-3.5-Transcribe-30B-A4B model card"
    url: "https://huggingface.co/nvidia/NVIDIA-Nemotron-3.5-Transcribe-30B-A4B"
    publisher: "NVIDIA on Hugging Face"
    primary: true
---

## What happened

On 28 October 2026 NVIDIA released Nemotron 3.5 Transcribe, a speech-to-text model, together with a second version of its Granary speech dataset. NVIDIA published a blog post on Hugging Face and a model card, and the model card gives a release date of 28 October 2026 on build.nvidia.com, GitHub (NeMo Speech), Hugging Face and NGC.

The model transcribes recorded audio, not live streams in the descriptions we read, and NVIDIA says it can be prompted, for example to follow instructions about formatting or to attribute speakers.

## Key details

Figures below are NVIDIA's, read from its blog post and model card on 29 October 2026. We have not run the model.

- **Languages:** NVIDIA says 40. The model card groups them into leading, production-ready and supported tiers; English, German, French, Spanish, Hindi and Korean are in the top tier, while Arabic, Mandarin Chinese and Vietnamese are in the third. The card's table lists 41 rows, and one, Norwegian, shows no speech recognition, which may explain the count of 40.
- **Audio:** recordings up to one hour, a 65,536-token context, word-level timestamps, up to eight speakers distinguished, and translation between English and 31 of the 40 languages, according to NVIDIA.
- **Size:** the blog says only about 4 billion of 30 billion parameters are active. The model card's table says 34 billion total parameters, 4.3 billion active, including the audio encoder. NVIDIA's pages therefore disagree on the total, and the model is named "30B-A4B".
- **License:** the card lists OpenMDW-1.1 and says the model is ready for commercial or non-commercial use. We did not read the license text itself.
- **Benchmarks (NVIDIA's, captured 12 October 2026):** a mean word error rate of 4.71 on its Open ASR English set against 4.94 for the next listed model, and a mean speaker-attributed error rate of 15.80 on multi-speaker audio against 16.83 for the next. NVIDIA describes these as the best published results in its tables.
- **Running it:** NVIDIA says it fits on one H100 80 GB GPU, runs with vLLM, SGLang-Omni and NeMo Speech, and is offered by hosted providers Baseten, DeepInfra and Simplismart.
- **Dataset:** Granary v2 is listed at 463,062 hours across 48 languages and 16 source corpora.

## Why it matters

Open, commercially usable transcription that handles long recordings, many speakers and 40 languages in one model is useful for meeting, podcast and call workflows that today often depend on paid APIs. The license and the single-GPU requirement are the details to check first.

The comparisons are NVIDIA's own tables, chosen and run by the vendor, so independent tests on your own audio matter more than the headline error rates. The inconsistent parameter counts are minor but worth knowing before you plan memory for a deployment.

> Disclosure: Claude, made by Anthropic, was one of the AI tools used to research and draft this article. Figures are NVIDIA's, taken from its 28 October 2026 blog post and model card.
