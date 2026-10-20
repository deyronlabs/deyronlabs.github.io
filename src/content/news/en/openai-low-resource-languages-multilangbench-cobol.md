---
title: "OpenAI reports GPT-6 Astra passes 87.4% of a SQLite-from-scratch test across 20 languages, COBOL included"
summary: "On 19 October 2026 OpenAI published two evaluations of coding in low-resource languages such as COBOL and Fortran. OpenAI says GPT-6 Astra averages 87.4% on MultiLangBench, up from 26.8% for GPT-5.6 Sol, and GPT-6.1 Sol reaches 86.6% on a COBOL migration test. The results are OpenAI's own."
seoTitle: "OpenAI GPT-6 Astra: 87.4% on MultiLangBench"
seoDescription: "OpenAI says GPT-6 Astra passes 87.4% of MultiLangBench tests across 20 languages and GPT-6.1 Sol 86.6% on a COBOL migration eval. Results are OpenAI's own."
lang: en
publishedAt: 2026-10-20T07:00:00Z
entities:
  - OpenAI
  - GPT-6 Astra
  - GPT-6.1 Sol
  - GPT-6 Luna
  - GPT-5.6 Sol
  - MultiLangBench
  - COBOL
topics:
  - Models
  - Research
  - Coding
translationKey: openai-low-resource-languages-multilangbench-cobol
image: /images/news/openai-low-resource-languages-multilangbench-cobol-2026-10-19.jpg
imageAlt: "Deyron Labs graphic: OpenAI reports GPT-6 Astra averages 87.4% on MultiLangBench across 20 languages, up from 26.8% for GPT-5.6 Sol, and GPT-6.1 Sol reaches 86.6% on a COBOL migration test; results are OpenAI's own"
sources:
  - title: "Advancing coding in low-resource programming languages"
    url: "https://openai.com/index/low-resource-programming-languages"
    publisher: "OpenAI"
    primary: true
  - title: "openai/MultiLangBench"
    url: "https://github.com/openai/MultiLangBench"
    publisher: "GitHub"
    primary: true
---

## What happened

On 19 October 2026, OpenAI published "Advancing coding in low-resource programming languages". The post says its latest models have improved at writing and migrating code in languages such as COBOL, Fortran and Visual Basic, and introduces two evaluations to show it: MultiLangBench and a COBOL migration evaluation. All scores in the post are OpenAI's own and have not been independently reproduced.

MultiLangBench asks a model to build a SQLite-compatible database engine from scratch in a specified programming language, across 20 languages. The candidate program receives an initial database and a SQL query and must produce a modified database. The COBOL migration evaluation asks models to migrate COBOL programs to C++, Java, Kotlin, Python or Rust, and counts a migration as successful only if all tests pass.

## Key details

- **MultiLangBench, GPT-6 Astra:** at maximum reasoning effort OpenAI reports an average test pass rate of 87.4% across the 20 languages, against 26.8% for GPT-5.6 Sol. Astra scores above 83% in 19 of the 20 languages, and COBOL is the hardest at 72%.
- **Per-language gains (GPT-5.6 Sol to GPT-6 Astra):** COBOL 10.9% to 72.1%, OCaml 25.6% to 85.8%, Fortran 21.4% to 83.5%, Visual Basic 27.5% to 89.4%.
- **GPT-6 Luna:** OpenAI reports 40.3% at maximum reasoning effort, above GPT-5.6 Sol, at an estimated average API cost of $0.77 per sample against $3.48 for GPT-5.6 Sol (about 78% lower).
- **COBOL migration, GPT-6.1 Sol:** 86.6% accuracy at low reasoning effort, against 5.4% for GPT-5.6 Sol at the same setting, at about 61% of the API cost. At higher reasoning effort OpenAI reports 97.9%, which it says nearly saturates the evaluation.
- **What is released:** OpenAI says it is releasing the MultiLangBench setup, test suite and per-language results on GitHub. The repository README describes tests derived from SQLite's TCL tests (about 24,000 of roughly 51,000 converted) and lists an Apache-2.0 license. The post does not say the COBOL migration evaluation is released.
- **Caveat from OpenAI:** the post says applying such migration to production software still requires expert review and testing against the system's business rules.

## Why it matters

COBOL still runs core banking and payments systems, and the post cites it as supporting more than 40% of online banking systems and 80% of in-person credit card transactions. A model that can migrate COBOL programs with passing tests would matter to the teams who maintain them, but these are OpenAI's own benchmarks, built and scored by OpenAI, and a jump from 5.4% to 86.6% should be checked by outside groups before anyone relies on it.

The practical point for readers is that MultiLangBench is public. Other labs and independent testers can run it on their own models, which is how the 87.4% figure can be confirmed or challenged. A model that rebuilds a database engine from documentation is not the same as one that safely migrates an undocumented bank system, which is why OpenAI's own advice is expert review.

> Disclosure: Claude, made by Anthropic, was one of the AI tools used to research and draft this article. Anthropic is a competitor of OpenAI. Claims about the results are OpenAI's own unless stated otherwise.
