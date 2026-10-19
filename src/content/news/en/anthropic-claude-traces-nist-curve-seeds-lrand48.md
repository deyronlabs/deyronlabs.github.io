---
title: "Anthropic says Claude traced NIST elliptic-curve seeds to a 1990s random number generator in under 30 minutes"
summary: "In a post dated 16 October 2026, Anthropic's Frontier Red Team says Claude worked out how the seeds of several NIST elliptic curves were generated, using the C library's lrand48 generator seeded with a Unix timestamp. Anthropic says this is not a cryptographic break and makes backdoors much less plausible; some curve parameters remain unexplained."
seoTitle: "Claude traces NIST curve seeds to lrand48"
seoDescription: "Anthropic's 16 October 2026 post says Claude found how NIST P-curve seeds were made in under 30 minutes; it says this is not a break of ECDSA."
lang: en
publishedAt: 2026-10-19T05:42:00Z
entities:
  - Anthropic
  - Claude
  - NIST
  - Internet Security Research Group
topics:
  - Research
  - Security
translationKey: anthropic-claude-traces-nist-curve-seeds-lrand48
image: /images/news/anthropic-claude-ecdsa-curve-origins-2026-10-16.jpg
imageAlt: "Deyron Labs graphic: Anthropic says Claude traced NIST elliptic-curve seeds to lrand48 in under 30 minutes, not a cryptographic break, a $36,864 bounty donated"
sources:
  - title: "Claude reveals ECDSA curve origins"
    url: "https://www.anthropic.com/research/ecdsa-curve-origins"
    publisher: "Anthropic Frontier Red Team"
    primary: true
---

## What happened

On 16 October 2026, Anthropic's Frontier Red Team published "Claude reveals ECDSA curve origins". It says Claude determined how the seeds for several standard NIST elliptic curves were generated, a question that has fed speculation about hidden backdoors for years. Anthropic makes Claude, the AI tool that helped draft this article, so please read this as a company reporting on its own model's work.

## Key details

All claims below are Anthropic's own, from its post. We have not independently reproduced them.

- **Finding:** the seeds for the NIST P-192, P-224, P-256, P-384 and P-521 curves came from the C library's `lrand48` random number generator seeded with a Unix timestamp, not from hashing a phrase. Anthropic says the rumored humorous-passphrase origin was wrong.
- **Speed and method:** Anthropic says Claude found this "in under half an hour". It guessed which 1990s pseudorandom generator was used, scanned the published seeds for that generator's pattern, and used the LLL lattice-reduction algorithm to recover the generator state for the prime-curve seeds.
- **Base points:** Claude also explained the base points for six curves (P-192 and five ANSI X9.62 example curves), which come from the random number generator in FreeLIP.
- **Bounty:** a $36,864 bounty offered for finding the seeds will be donated to the Internet Security Research Group.
- **What it is not:** Anthropic writes that this "is not a cryptographic break, new attack, or weakness in the ECDSA curves", and says the findings make backdoors "much less plausible".
- **Still unexplained:** the base points for P-224, P-256, P-384, P-521 and the NIST binary curves; the seed for B-163; and why some viable candidate seeds were skipped.

Checked against the primary page on 19 October 2026.

## Why it matters

Standard curves are used widely in everyday encryption and signatures, and doubts about where their constants came from have lasted decades. Anthropic's account, if it holds up, gives a mundane origin for the seeds and removes one basis for backdoor suspicion.

It does not settle the matter. Several parameters are still unexplained, the result rests on one company's description, and independent cryptographers have yet to weigh in on this page. Nothing in the post changes how existing curves should be used.

> Disclosure: Claude, made by Anthropic, was one of the AI tools used to research and draft this article, and this article is about Anthropic. Claims are Anthropic's own and have not been independently verified.
