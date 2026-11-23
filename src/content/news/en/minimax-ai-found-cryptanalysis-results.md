---
title: "MiniMax publishes cryptanalysis results it says its internal AI model found, with code under Apache 2.0"
summary: "MiniMax's Cyber Team released papers and code on 20 November 2026 describing attacks on experimental cryptographic schemes that it says were found mainly by an internal AI model. Reported results include 94 recovered keys in a public McEliece challenge. MiniMax says nothing here breaks mainstream standards such as AES, RSA or SHA-256."
seoTitle: "MiniMax AI-found cryptanalysis results"
seoDescription: "MiniMax released cryptanalysis papers and Apache 2.0 code on 20 Nov 2026 that it says an internal AI model found, incl. 94 McEliece challenge keys."
lang: en
publishedAt: 2026-11-23T17:49:00Z
entities:
  - MiniMax
  - MiniMax Cyber Team
  - TII McEliece challenge
  - ARADI
  - HAWK
topics:
  - Research
  - Security
  - China
translationKey: minimax-ai-found-cryptanalysis-results
image: /images/news/minimax-ai-found-cryptanalysis-results-2026-11-23.jpg
imageAlt: "Deyron Labs graphic: MiniMax cryptanalysis results released 20 Nov 2026; 94 McEliece challenge keys recovered, 55 with no prior solution; up to 43,400x speedup; reported by MiniMax; no attack on AES, RSA or SHA-256"
sources:
  - title: "MiniMax-AI/Research: cryptography results (README)"
    url: "https://github.com/MiniMax-AI/Research"
    publisher: "GitHub, MiniMax; Apache License 2.0"
    primary: true
  - title: "MiniMax publishes AI-discovered cryptographic attacks with papers and code"
    url: "https://technode.com/2026/11/23/minimax-publishes-ai-discovered-cryptographic-attacks-with-papers-and-code/"
    publisher: "TechNode, 23 November 2026"
    primary: false
---

## What happened

MiniMax, the Chinese AI lab, published a GitHub repository of research projects "from MiniMax internal models". Its only section so far covers cryptography. According to the README, a first release dated 20 November 2026 contains cryptanalysis results from the MiniMax Cyber Team's auto-cryptanalysis project, and a second release dated 23 October 2026 contains counterexamples to two conjectures about Boolean functions. MiniMax says the results were "primarily discovered by our internal model". TechNode reported the work on 23 November 2026.

We read the repository's README on 23 November. We have not read the linked papers or run the code, and we cannot judge the mathematics ourselves.

## Key details

All numbers below are MiniMax's own and have not been independently reproduced.

- **TII McEliece challenge:** 94 Track-2 private keys recovered, including 55 "first-blood" solutions, meaning instances with no previously published solution, and speedups of up to 43,400x.
- **ARADI (a block cipher designed by the US National Security Agency):** key recovery up to 8 rounds in at most 16 seconds, a 2^54.8 attack on 9 rounds, and improved attacks on 10 to 12 rounds.
- **Signature and hash schemes:** secret-key recovery on HAWK-256 in 30.9 minutes (a 690x speedup) and reduced security estimates for the HAWK variants; passive secret-key recovery on SBC-VOLE in 0.06 seconds; collisions on Blender-256 in 0.73 seconds and Waterfall variants within 1 second.
- **Other targets:** a forgery on the CAESAR competition winner COLM0 with two encryption queries, and attacks on all nine LOCKER parameter sets and on the 2019 ROLLO-I-128 submission.
- **October release:** explicit counterexamples to the bent-sum conjecture (even n of at least 8) and the derivative conjecture (even n of at least 10), with proofs MiniMax says were verified in Lean 4 (arXiv:2610.32239).
- **License and contact:** Apache License 2.0; the repository lists cyber@minimax.io.
- **Scope:** per TechNode, MiniMax says the work concerns specific research designs, historical competition candidates and challenge parameters, and does not establish attacks on mainstream standards such as AES, RSA or SHA-256. MiniMax says its research team organized and verified the model's findings.
- **Not confirmed:** how much of the work was autonomous versus human-directed, the compute used, and whether outside cryptographers have checked the claims. We did not find independent commentary.

## Why it matters

Most of the targets are experimental or competition designs rather than deployed standards, so the immediate effect on everyday security is limited. The notable part is the method: a lab reports that a general AI model produced attacks that beat existing implementations on public challenges and on a published design, and released code others can run.

If outside researchers reproduce the results, they would be an example of AI systems contributing to security research on cryptographic designs. Until then, treat the speedups and "first solutions" as claims by MiniMax, and watch for third-party verification of the 94 recovered keys and for responses from the designers of the affected schemes.

> Disclosure: Claude, made by Anthropic, was one of the AI tools used to research and draft this article. MiniMax is not affiliated with Deyron Labs. All results are MiniMax's own and unverified by us.
