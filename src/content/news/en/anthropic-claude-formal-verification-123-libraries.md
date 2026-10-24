---
title: "Anthropic says Claude wrote machine-checked proofs that code from 123 open-source libraries cannot crash"
summary: "Anthropic's Frontier Red Team and Theorem report that Claude turned fuzz tests for 123 open-source libraries into formal specifications and proved them with the Rocq proof checker, finding hundreds of bugs on the way. Anthropic stresses that 'formally verified' does not mean 'bug-free' and that the proofs are costly and narrow."
seoTitle: "Claude proves 123 libraries cannot crash"
seoDescription: "Anthropic reports Claude formally verified 239 entry points in 123 open-source libraries using Rocq, finding hundreds of bugs (post dated 22 October 2026)."
lang: en
publishedAt: 2026-10-24T06:00:00Z
entities:
  - Anthropic
  - Claude
  - Theorem
  - Rocq
  - OSS-Fuzz
topics:
  - Research
  - Coding
  - Security
translationKey: anthropic-claude-formal-verification-123-libraries
image: /images/news/anthropic-claude-formal-verification-123-libraries-2026-10-24.jpg
imageAlt: "Deyron Labs graphic: Anthropic formal verification; 123 libraries, 239 entry points, hundreds of bugs found, per Anthropic's 22 October 2026 post"
sources:
  - title: "Formal verification with Claude (Anthropic research)"
    url: "https://www.anthropic.com/research/formal-verification"
    publisher: "Anthropic"
    primary: true
---

## What happened

Anthropic published a research post on 22 October 2026 (last modified 23 October) describing work by its Frontier Red Team with the company Theorem. According to Anthropic, Claude wrote formal proofs that compiled programs cannot crash under specified conditions, and a proof checker verified each one.

## Key details

- **Method:** per Anthropic, the team converted existing fuzz tests (developer-written entry points that search for crashing inputs) into specifications about RISC-V assembly code. Claude then proved those specifications, and the Rocq proof checker verified every proof. Where Claude found bugs, it patched them, regenerated the specification and proved the new version.
- **Scale (Anthropic's figures):** 123 open-source libraries and 239 entry points, with proofs covering inputs up to 64 MB. A typical proof is about 600,000 lines of Rocq, roughly 180 million lines in total, for binaries with a median length of about 18,000 instructions.
- **Bugs:** Anthropic reports hundreds of bugs surfaced during the proof attempts, including some it says fuzzers would be unlikely to find. It also describes a logic bug that had been latent for over a decade.
- **Other case studies:** Anthropic says Claude proved the Linux kernel's zlib implementation matches the RFC 1950 specification, and built a Python interpreter in Rust that matched CPython output on 99.95% of 1.7 million random programs.
- **Efficiency:** on 36 small verification tasks, Anthropic says Opus 5.5 proved half using about 40% fewer tokens than Opus 5, and letting agents reuse each other's proofs cut token use by 17%.
- **Limits stated by Anthropic:** "formally verified" does not mean "bug-free"; bugs can remain in the specification, the machine model or the trusted tools. The proofs assume a single-threaded static RISC-V binary linked against musl libc, while most people run x86 or ARM builds with glibc. AddressSanitizer does not catch every memory-safety bug, dead code and caller misuse are not covered, and proofs can take hundreds of millions of tokens, so cost is a major barrier.

## Why it matters

If the results hold up, they show a model producing proofs that a separate checker can validate, which is a stronger kind of evidence than test coverage alone. The claims are Anthropic's own and have not been independently reproduced, and the stated assumptions and token costs mean this is not yet a drop-in way to certify the software most people run.

> Disclosure: Claude, made by Anthropic, was one of the AI tools used to research and draft this article, and this article is about Claude's work. Details come from Anthropic's post, read on 24 October 2026.
