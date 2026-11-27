---
title: "OpenAI posts a manuscript claiming the square matrix multiplication exponent is 9/4, with a partial Lean formalization"
summary: "OpenAI published a manuscript dated 24 November 2026 in its openai/math GitHub repository, titled 'The matrix multiplication exponent is nine fourths'. The README says it proves a matching lower bound of n^(9/4) for formal arithmetic circuits, with a Lean formalization that covers division-free circuits. No authors or AI role are stated, and no independent review has been reported."
seoTitle: "OpenAI claims matrix multiplication exponent 9/4"
seoDescription: "OpenAI's 24 Nov 2026 manuscript claims a 9/4 exponent for square matrix multiplication in formal circuits; Lean covers division-free circuits only."
lang: en
publishedAt: 2026-11-25T20:40:00Z
updatedAt: 2026-11-27T10:00:00Z
entities:
  - OpenAI
  - Lean
  - Matrix multiplication
  - Fourier transform
topics:
  - Research
  - Models
translationKey: openai-matmul-exponent-nine-fourths
image: /images/news/openai-matmul-exponent-nine-fourths.jpg
imageAlt: "Deyron Labs graphic: OpenAI's 24 November 2026 manuscript claims the square matrix multiplication exponent is 9/4 for formal arithmetic circuits; the Lean formalization covers division-free circuits; no independent review"
sources:
  - title: "The matrix multiplication exponent is nine fourths (README, November 24, 2026 edition; paper PDF not read)"
    url: "https://github.com/openai/math/blob/main/preprints/The-matrix-multiplication-exponent-is-nine-fourths-November-24-2026/README.md"
    publisher: "OpenAI (GitHub openai/math), read 25 November 2026"
    primary: true
  - title: "The logarithmic exponent of finite Fourier transforms (README, November 24, 2026 edition; paper PDF not read)"
    url: "https://github.com/openai/math/blob/main/preprints/The-logarithmic-exponent-of-finite-Fourier-transforms-November-24-2026/README.md"
    publisher: "OpenAI (GitHub openai/math), read 26 November 2026"
    primary: true
---

## What happened

OpenAI added a set of mathematics manuscripts and Lean formalizations to its `openai/math` repository on GitHub on 24 November 2026. One of them is titled **"The matrix multiplication exponent is nine fourths"**. Its README, labeled "OpenAI · November 24, 2026 edition", states: "The exponent of square matrix multiplication is 9/4 over every field."

We read the README on 25 November 2026. We did not read the 1 MB paper PDF, which GitHub showed only as a wrapper. Everything below is what OpenAI's README says; we have not checked the mathematics, and no independent review has been reported.

Update, 27 November 2026: the same repository drop includes a second manuscript, "The logarithmic exponent of finite Fourier transforms". We read its README on 26 November 2026 and added the details below; we have not read the PDF or checked the mathematics.

## Key details

- **Update, second manuscript (Fourier transforms):** the README states that for a finite abelian group of order N, the minimum number of binary linear gates needed for the Fourier transform is N(log N)^(1/2+o(1)). It requires the field to contain a primitive root of unity of order equal to the group's exponent, with N invertible, and says the result holds for the forward and inverse transform and for J independent inputs. It says the same "logarithmic exponent" applies to formal polynomial multiplication over any field. The Lean development includes both the upper and lower bounds, for single transforms and batches; we did not read the PDF or the "formalization scope" sections.
- **Not in that README:** authors, any AI role, or expert reactions. Newsletter reports of expert reactions were not verified by us.

- **The claim, as the README words it:** the paper "proves the matching lower bound for formal arithmetic circuits". For every side length n ≥ 2, such a circuit needs at least ⌈n^(9/4)/2⌉ non-scalar multiplication or division gates. The README also says the geometric border rank of the square matrix multiplication tensor is at least n^(9/4), and that its asymptotic rank over the base field equals n^(9/4).
- **Companion paper:** the README mentions a companion paper on tensor geometry.
- **Lean formalization:** the formalization "proves the square exponent 9/4 for division-free circuits computing formal polynomial identities over every field", and its scope document says the dual and rectangular exponents are also formalized. The README does not say the Lean code covers the full statement in the abstract, so the formalized part appears narrower than the headline claim.
- **Who and how:** the README names no individual authors, only "OpenAI", and does not say what role AI models played in obtaining the result.
- **What is unclear:** the README does not explain how an exponent of 9/4 for formal circuits relates to the usual algorithmic exponent for matrix multiplication, so we do not draw that connection here.
- **Context:** the same repository drop includes other November 24 manuscripts. Earlier in the week, Anthropic and OpenAI each posted claimed VP ≠ VNP proofs with Lean code (see our earlier article).

## Why it matters

Matrix multiplication sits under most of machine learning, so any claim about its fundamental cost draws attention. This one concerns a lower bound for a specific model, formal arithmetic circuits, not a faster algorithm, and nothing in the README changes how matrices are multiplied in practice.

It is also the second AI-lab mathematics release this week that comes with Lean code but no independent verification. Until mathematicians review the paper and the scope of the Lean proof is clear, it should be read as OpenAI's claim, not an established result.

> Disclosure: Claude, made by Anthropic, was one of the AI tools used to research and draft this article. OpenAI is a competitor of Anthropic; all claims described are OpenAI's own and unverified by us.
