---
title: "OpenAI publishes new math results from an internal model, with Lean proofs for many"
summary: "On 6 October 2026 OpenAI released a set of mathematical results produced by an internal frontier model, with reasoning summaries and many proofs formalized in Lean. OpenAI says the average result took about three hours of ChatGPT Pro thinking. The results come from OpenAI and have not been independently reviewed."
seoTitle: "OpenAI publishes new math results, Lean proofs"
seoDescription: "OpenAI published math results from an internal model, many with Lean proofs, about three hours of ChatGPT Pro thinking each. Not independently reviewed."
lang: en
publishedAt: 2026-10-08T07:00:00Z
entities:
  - OpenAI
  - ChatGPT Pro
  - Lean
  - Institute for Advanced Study
  - Advisory Group on Mathematics and Artificial Intelligence
topics:
  - Research
  - Mathematics
translationKey: openai-publishes-math-results
image: /images/news/openai-math-results-2026-10-06.jpg
imageAlt: "Deyron Labs graphic: OpenAI published new math results from an internal model, many with Lean formalizations, not yet independently reviewed"
sources:
  - title: "Sharing AI progress in mathematics"
    url: "https://openai.com/index/sharing-ai-progress-in-mathematics"
    publisher: "OpenAI"
    primary: true
  - title: "openai/math repository"
    url: "https://github.com/openai/math"
    publisher: "GitHub"
    primary: true
  - title: "Recommendations of the Advisory Group on Mathematics and Artificial Intelligence"
    url: "https://agmai.org/general-sep29/"
    publisher: "Institute for Advanced Study"
---

## What happened

On 6 October 2026, OpenAI published "Sharing AI progress in mathematics". It says it is releasing "a broad range of new mathematical results produced by an internal frontier model". The results are in a public GitHub repository, `openai/math`, with protocols for paper revisions and citations. OpenAI says it consulted the Advisory Group on Mathematics and Artificial Intelligence at the Institute for Advanced Study and used that group's public recommendations to guide how the results are shared.

OpenAI does not name the model, and says it is working to release it responsibly while it keeps evaluating internal frontier models in mathematics and other sciences.

## Key details

- **Formal checking:** many proofs are shared as formalizations in Lean, a language in which a computer checks each proof step. OpenAI says it will add more formalizations over time.
- **Compute:** OpenAI says the average result used the equivalent of roughly three hours of ChatGPT Pro thinking.
- **Transparency material:** the repository includes 10 summaries of the model's reasoning, estimates of compute in ChatGPT Pro usage and statistics on attempted problems. The announcement page itself gives no count of results or attempted problems, so those numbers are in the repository, which we have not audited.
- **Community follow-up:** OpenAI says it will fund workshops, conferences and special programs on understanding major AI-produced results, with details "in the near future". It is also exploring community-hosted alternatives to GitHub that meet the advisory group's guidelines.
- **What is not stated:** the announcement does not say how many open problems were solved, which areas are covered, or whether mathematicians outside OpenAI have reviewed the results.

## Why it matters

The notable part is the method of release rather than any single result. Publishing proofs with Lean formalizations means a reader can verify that a proof is correct without trusting OpenAI, which is the standard that AI-generated mathematics needs to meet. A Lean check confirms that a proof follows from its stated assumptions. It does not confirm that the statement formalized is the one a mathematician cares about, which is where outside review matters.

For readers outside mathematics, the claim to watch is the compute figure. About three hours of ChatGPT Pro thinking per result suggests the work is within reach of a paid product, but OpenAI says the model behind the results is internal, so nobody else can reproduce it yet.

> Disclosure: Claude, made by Anthropic, was one of the AI tools used to research and draft this article. Anthropic is a competitor of OpenAI. Claims about the results are OpenAI's own unless stated otherwise.
