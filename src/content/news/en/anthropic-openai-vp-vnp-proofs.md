---
title: "Anthropic and OpenAI each post a claimed VP ≠ VNP proof with Lean 4 code that no human has checked"
summary: "On 23 November 2026 Anthropic posted a paper and Lean 4 formalization claiming VP is a proper subset of VNP over every field, saying an internal Claude model found the result and that no human mathematician has checked the proof. OpenAI posted its own preprint, 'VP and VNP are different', the same day. Neither claim has been independently verified, and neither settles P vs NP."
seoTitle: "Anthropic, OpenAI claim VP ≠ VNP proofs"
seoDescription: "Anthropic and OpenAI each posted claimed VP versus VNP separation proofs with Lean 4 code on 23 Nov 2026; neither is human-checked or settles P vs NP."
lang: en
publishedAt: 2026-11-24T12:00:00Z
entities:
  - Anthropic
  - OpenAI
  - Claude
  - Lean 4
  - VP vs VNP
topics:
  - Research
  - Models
translationKey: anthropic-openai-vp-vnp-proofs
image: /images/news/anthropic-openai-vp-vnp-proofs-2026-11-24.jpg
imageAlt: "Deyron Labs graphic: Anthropic and OpenAI claim VP does not equal VNP proofs with Lean 4 formalizations; Anthropic says no human mathematician has checked its proof; neither settles P vs NP"
sources:
  - title: "vp-vnp: VP ≠ VNP over Every Field (README, paper and Lean 4 formalization; paper PDF not read)"
    url: "https://github.com/anthropics/formal-math/tree/main/vp-vnp"
    publisher: "Anthropic (GitHub anthropics/formal-math), read 24 November 2026"
    primary: true
  - title: "VP and VNP are different, November 23, 2026 edition (README; paper PDF not read)"
    url: "https://github.com/openai/math/tree/main/preprints/VP-and-VNP-are-different-November-23-2026"
    publisher: "OpenAI (GitHub openai/math), read 24 November 2026"
    primary: true
  - title: "Hacker News discussion of the Anthropic repository"
    url: "https://news.ycombinator.com/item?id=50620102"
    publisher: "Hacker News, 23 November 2026"
    primary: false
---

## What happened

On 23 November 2026, around 22:00 UTC, Anthropic published a research folder, `vp-vnp`, in its `anthropics/formal-math` repository on GitHub. It contains a paper titled "VP ≠ VNP over Every Field", credited to "Claude (Anthropic)", and a Lean 4 formalization. A few hours later OpenAI posted its own preprint, "VP and VNP are different", in its `openai/math` repository.

VP and VNP are classes from algebraic complexity theory (Valiant's framework): roughly, families of polynomials that small arithmetic circuits can compute, versus polynomials whose coefficients can be computed efficiently. Whether they are equal is a central open problem. We read both READMEs; we did not read either paper PDF.

## Key details

- **Anthropic's claim:** for every field, circuits for the Hamiltonian cycle polynomial, and for the permanent outside characteristic 2, need more than m^(c (log m)^(1/3)) gates for all large m, which the README says shows VP is a proper subset of VNP. The README states that this "does not settle P vs NP".
- **Who made it (Anthropic):** the README says the result "was discovered by an internal research Claude model", that the paper and the Lean formalization "were written by AI models, and no human mathematician has checked the proof". It calls the folder a research artifact that is not maintained.
- **Machine checking (Anthropic):** the README says the Lean project builds with `lake build`, that the proof uses only standard axioms, and that the repository's CI runs a Comparator check with a second kernel (nanoda). It also says no machine checks that the main statement file says what the paper claims.
- **OpenAI's claim:** the README states a border arithmetic circuit size lower bound of exp(Ω((log n)^(5/4))) for an explicit VNP family over every field, transferred to the directed Hamiltonian cycle polynomial and to the permanent outside characteristic two, and says a Lean proof of the exact VP–VNP separation is in the repository. The page we read does not say who or what produced the proof or whether people have checked it.
- **Different bounds:** the two READMEs state different lower bounds and different circuit models. We have not compared the papers, and we do not know how the two results relate.
- **Not found:** no post about this on Anthropic's news page on 24 November, and no OpenAI statement that we could read.

## Why it matters

If either proof holds up, it would be a major result in complexity theory, and both labs say AI models were central to producing it. That is also why the caveats matter: Anthropic itself says no human has checked its proof, and a Lean formalization only helps if its statements faithfully capture the mathematical claim, which the Anthropic README says is not machine-checked.

The posts follow an earlier unreviewed Claude-assisted claim we covered, a Riemann Hypothesis note posted on 20 November. Independent review by complexity theorists, and any statement from either lab, are what to watch next. Until then, treat both as claims, not established results.

> Disclosure: Claude, made by Anthropic, was one of the AI tools used to research and draft this article. Anthropic is one of the two labs making these claims, and OpenAI is its competitor. Details come from both labs' repository READMEs, read on 24 November 2026.
