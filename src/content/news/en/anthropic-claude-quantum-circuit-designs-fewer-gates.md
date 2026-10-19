---
title: "Anthropic says Claude designed quantum circuits with up to 17x fewer gates than the best published ones"
summary: "In a post dated 16 October 2026, Anthropic reports that Claude, working in a closed loop with an automated evaluator, found designs for eight quantum circuit tasks that beat published ones, including a 12x gate cut in a decoder step first built by Google researchers. The results are Anthropic's own and the full paper is on arXiv."
seoTitle: "Claude quantum circuits: up to 17x fewer gates"
seoDescription: "Anthropic's 16 October 2026 post says Claude found quantum circuit designs with up to 17x fewer gates, including a 12x cut for a Google decoder step."
lang: en
publishedAt: 2026-10-19T07:10:00Z
entities:
  - Anthropic
  - Claude
  - Google Quantum AI
topics:
  - Research
  - Science
translationKey: anthropic-claude-quantum-circuit-designs-fewer-gates
image: /images/news/anthropic-claude-quantum-circuits-2026-10-16.jpg
imageAlt: "Deyron Labs graphic: Anthropic says Claude designed quantum circuits with 17x fewer gates and a decoder step with 12x fewer gates than Google's earlier construction"
sources:
  - title: "Designing more efficient quantum circuits with Claude"
    url: "https://www.anthropic.com/research/designing-efficient-quantum-circuits"
    publisher: "Anthropic"
    primary: true
  - title: "Anthropic paper on arXiv (2610.22367), linked from the post"
    url: "https://arxiv.org/abs/2610.22367"
    publisher: "arXiv"
    primary: false
---

## What happened

Anthropic published "Designing more efficient quantum circuits with Claude" on 16 October 2026 (the page shows a last-modified date of 17 October). It says Claude, using a model it calls Claude Mythos 5, found designs for several quantum circuits that improve on the best published ones, "in some cases by an order of magnitude or more". Anthropic makes Claude, the AI tool that helped draft this article, so please read this as a company reporting on its own model.

## Key details

All figures below are Anthropic's own, from its post. The full paper is listed there as arXiv 2610.22367; we have not reviewed it.

- **Setup:** Claude was given plain-language specifications for eight circuits (chemistry, optimization, physics simulation and number theory) and an automated evaluator. The evaluator checks correctness, then scores each design by qubits multiplied by gates, a proxy for runtime.
- **Elliptic-curve point addition:** Claude worked for 53 hours with minimal human input and produced a new reversible implementation plus a family of designs. One design uses 12% more qubits but 17x fewer gates than the smallest previous design.
- **Decoder step (Reed-Solomon, Berlekamp-Massey):** Claude's design cut gates 12x compared with Google's previous construction, making the most expensive step of decoded quantum interferometry "a little over an order of magnitude cheaper". Where a worst-case reserve would need 665 qubits, the design reserves 19, and about one run in 10,000 needs more, which Anthropic says is within the error rate the task allows.
- **Verification described:** the evaluator checks every circuit. For one design Claude validated a formula with large numerical simulations and formalized the claim in Lean; for the decoder it ran 403 million sample decodings.
- **Context on FeMoco:** the post notes that estimates for simulating the FeMoco molecule fell from about 50 trillion Toffoli gates in 2017 to about 340 million, and says most of that came from algorithmic advances, not from Claude.
- **Caveats Anthropic lists:** Claude tended to prefer well-known approaches and sometimes over-checked its results; human input was limited to the brief and occasional prompts; circuit design is one part of a useful quantum computer, and error correction and hardware control remain separate problems.
- **Authors:** led by Andi Gu in Anthropic's STEM Fellows Program, in collaboration with researchers at Harvard and QuEra Computing.

Checked against the primary page on 19 October 2026.

## Why it matters

This is a concrete example of an AI model doing search-and-verify work in a technical field, with a checker that rejects wrong answers. That structure, a clear score plus an automatic correctness test, is what made the results measurable.

It does not mean useful quantum computers are closer. The gains are in gate counts for specific circuits, mostly on paper, and they have not been independently reproduced. The post itself says circuit design is only one piece of the problem.

> Disclosure: Claude, made by Anthropic, was one of the AI tools used to research and draft this article, and this article is about Anthropic. Figures are Anthropic's own and have not been independently verified.
