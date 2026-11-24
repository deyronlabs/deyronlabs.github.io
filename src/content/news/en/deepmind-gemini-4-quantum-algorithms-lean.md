---
title: "Google DeepMind says teams of Gemini 4 agents found cheaper quantum algorithms, with each result proven in Lean"
summary: "Google DeepMind and Google Quantum AI report that agent teams built on Gemini 4 improved published quantum algorithms, including an 11.8x lower computing cost for a fusion-related circuit, and proved each result in the Lean theorem prover. The figures are the authors' own."
seoTitle: "DeepMind Gemini 4 agents cut quantum costs 11.8x"
seoDescription: "Google DeepMind says Gemini 4 agent teams cut a fusion-related quantum circuit's cost 11.8x and proved each result in Lean (post of 23 Nov 2026)."
lang: en
publishedAt: 2026-11-24T18:05:00Z
entities:
  - Google DeepMind
  - Google Quantum AI
  - Gemini 4
  - Lean
  - arXiv
topics:
  - Research
  - Science
  - Google
image: /images/news/deepmind-gemini-4-quantum-algorithms-lean.jpg
imageAlt: "Deyron Labs graphic: Google DeepMind says Gemini 4 agents cut a fusion-related quantum circuit's cost 11.8x, memory from 5,650 to 4,338 qubits, with each result proven in Lean"
translationKey: deepmind-gemini-4-quantum-algorithms-lean
sources:
  - title: "Finding faster quantum algorithms with agents and formal verification"
    url: "https://deepmind.google/blog/finding-faster-quantum-algorithms-with-agents-and-formal-verification/"
    publisher: "Google DeepMind, 23 November 2026"
    primary: true
  - title: "Discovering formally verified quantum programs with AI (arXiv 2611.09822)"
    url: "https://arxiv.org/abs/2611.09822"
    publisher: "arXiv"
    primary: true
  - title: "formal-quantum-computation (Lean library)"
    url: "https://github.com/google-deepmind/formal-quantum-computation"
    publisher: "Google DeepMind, GitHub"
    primary: false
---

## What happened

On 23 November 2026 Google DeepMind published a post, written with Google Quantum AI, saying that teams of Gemini 4 agents improved well-known quantum algorithms and proved each result with Lean, a formal theorem prover. The accompanying paper, "Discovering formally verified quantum programs with AI" (arXiv 2611.09822), was first submitted on 6 November 2026 and last revised on 16 November. We read the blog post and the arXiv abstract on 24 November 2026; we did not read the full paper.

## Key details

All figures below are the authors' own, from the blog post unless noted.

- **Fusion-related circuit:** the agent teams cut the required computing cost, a metric combining qubits and operations, by 11.8x, and reduced memory from 5,650 to 4,338 error-corrected qubits. The arXiv abstract rounds this to 12x.
- **Photochemistry:** a light-sensitive molecule simulation made 8x cheaper.
- **Drug metabolism (Cytochrome P450):** a 2.5x improvement, with memory reduced from 481 to 333 qubits.
- **Grover's algorithm:** a 2.57x speedup for one specific implementation. **Quantum arithmetic (arcsin routine):** a 290x speedup.
- **Method:** independent agent teams per problem; ideas were verified in Lean before entering a shared notebook, and the agents met in a virtual conference every four hours, according to the post.
- **Availability:** the Lean library, problem specifications and verified solutions are open-sourced on GitHub; the arXiv paper is under a CC BY 4.0 license. The blog post does not state the code license.
- **Limits the post states:** running these algorithms in full scientific simulations would still need more resources than the first error-corrected quantum computers are likely to offer, and the large circuits cannot be tested on classical computers or today's small quantum processors, which is why proofs are used.
- **Not confirmed here:** independent replication, and exactly which statements the Lean proofs cover beyond the post's wording that each result was proven.

## Why it matters

The result is a concrete example of AI agents producing research output that comes with machine-checkable proofs, a pattern also seen this week in AI-written mathematics ([VP vs VNP claims](/en/news/anthropic-openai-vp-vnp-proofs/)), though here the verification target is the correctness and cost of programs. The practical caveat is that the savings apply to future error-corrected hardware, not to anything users can run today. Watch for independent checks of the Lean library and for whether the cost figures hold under other cost models.

> Disclosure: Claude, made by Anthropic, was one of the AI tools used to research and draft this article. Google DeepMind and Google are not affiliated with Deyron Labs.
