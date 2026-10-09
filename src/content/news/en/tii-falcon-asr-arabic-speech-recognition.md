---
title: "TII releases Falcon-ASR, a 1.6B speech recognition model for Arabic, including Emirati, plus four other languages"
summary: "On 7 October 2026 the UAE's Technology Innovation Institute published Falcon-ASR, a 1.6 billion-parameter speech recognition model for Arabic with a focus on Emirati, plus English, French, Spanish and Portuguese in the same weights. TII reports a 20.92% average word error rate on six Arabic test sets; the post names no license."
seoTitle: "TII Falcon-ASR: speech recognition for Arabic"
seoDescription: "On 7 October 2026 the UAE's Technology Innovation Institute published Falcon-ASR, a 1.6 billion-parameter speech recognition model for Arabic with a…"
lang: en
publishedAt: 2026-10-09T05:30:00Z
entities:
  - Technology Innovation Institute
  - Falcon-ASR
  - Hugging Face
topics:
  - Models
  - Speech
  - Middle East
translationKey: tii-falcon-asr-arabic-speech-recognition
image: /images/news/tii-falcon-asr-arabic-speech-recognition-2026-10-09.jpg
imageAlt: "Deyron Labs graphic: TII releases Falcon-ASR, a 1.6B speech recognition model for Arabic including Emirati; results are TII's own and no license is stated"
sources:
  - title: "Introducing Falcon ASR"
    url: "https://huggingface.co/blog/tiiuae/falcon-asr"
    publisher: "Technology Innovation Institute (Hugging Face blog)"
    primary: true
---

## What happened

On 7 October 2026, the Technology Innovation Institute (TII) in Abu Dhabi published "Introducing Falcon ASR" on the Hugging Face blog. It describes Falcon-ASR as a 1.6 billion-parameter speech recognition model for Arabic, with a focus on Emirati. The same weights also transcribe English, French, Spanish and Portuguese, and the post says no language flag is required.

## Key details

All results below are TII's own.

- **Arabic:** an average word error rate (WER) of 20.92% and character error rate of 8.79% across six test sets of the Open Universal Arabic ASR Leaderboard. TII says the best published competitor it compared, Audar-ASR-V1-Turbo, scored 23.17% WER, so Falcon-ASR is "2.25 percentage points better".
- **Emirati:** 22.73% WER and 10.19% CER on an internal TII evaluation, with Qwen3-Omni-30B-A3B-Instruct next at 26.80% WER. Because this evaluation is internal, it cannot be checked externally.
- **English:** a mean WER of 5.74% across seven Open ASR Leaderboard test sets, from 1.75% on LibriSpeech clean to 11.86% on Earnings-22.
- **Not in the post:** a license and inference speed or latency figures.

## Why it matters

Dialect coverage is a known weak point for speech recognition. A model that targets Emirati Arabic and reports leaderboard-based comparisons for standard Arabic gives developers in the region a new option to test.

The strongest claim, about Emirati, rests on an internal evaluation, and the missing license means commercial use is unclear until the model card is checked.

> Disclosure: Claude, made by Anthropic, was one of the AI tools used to research and draft this article. Claims and results are TII's own.
