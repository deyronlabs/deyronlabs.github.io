---
title: "Anthropic mathematician posts unreviewed claim of a Riemann Hypothesis proof made with Claude, with a Lean formalization"
summary: "A four-page note on Levent Alpöge's website says the author, working with Claude, has found a proof of the Riemann Hypothesis and formalized it in Lean. Nothing has been peer reviewed, no paper has been posted, and independent checking of the Lean archive is not yet confirmed. Anthropic, the maker of Claude, is a conflict of interest here."
seoTitle: "Riemann Hypothesis proof claimed with Claude"
seoDescription: "Anthropic mathematician Levent Alpöge posted a four-page note on 20 Nov 2026 claiming a Riemann Hypothesis proof made with Claude; it is unreviewed."
lang: en
publishedAt: 2026-11-20T20:26:00Z
entities:
  - Anthropic
  - Claude
  - Levent Alpöge
  - Riemann Hypothesis
  - Lean
  - Mathlib
topics:
  - Research
  - Models
translationKey: anthropic-mathematician-riemann-hypothesis-claim
image: /images/news/anthropic-mathematician-riemann-hypothesis-claim-2026-11-20.jpg
imageAlt: "Deyron Labs graphic: a four-page note posted on 20 November 2026 claims a Riemann Hypothesis proof made with Claude and a Lean formalization; not peer reviewed, not independently verified"
sources:
  - title: "Note posted on alpo.ge (four-page PDF, unsigned; hosted on the personal site attributed to Levent Alpöge by the outlets below; read 20 November 2026)"
    url: "https://alpo.ge/remark.pdf"
    publisher: "alpo.ge"
    primary: true
  - title: "Claimed Riemann Hypothesis Proof Made With Claude Appears On Anthropic Mathematician Levent Alpöge's Website"
    url: "https://officechai.com/ai/claimed-riemann-hypothesis-proof-made-with-claude-appears-on-anthropic-mathematician-levent-alpoges-website/"
    publisher: "OfficeChai, 20 November 2026"
    primary: false
  - title: "Claude helped prove 167-year-old Riemann hypothesis, researcher claims"
    url: "https://interestingengineering.com/ai-robotics/anthropic-167-year-old-riemann-hypothesis-claude"
    publisher: "Interesting Engineering, 20 November 2026"
    primary: false
---

## What happened

On 20 November 2026 a four-page note appeared on alpo.ge, the personal website that OfficeChai and Interesting Engineering attribute to Anthropic mathematician Levent Alpöge. It opens: "I believe I have, working with Claude, discovered a proof of the Riemann Hypothesis." The note is unsigned and we could not confirm its authorship from the PDF itself; the attribution rests on where it is hosted and on those two outlets.

This is a claim, not an established result. There is no paper, no arXiv posting and no peer review. We read the note; we did not download or build the Lean archive it points to.

## Key details

Everything below is from the note unless another source is named.

- **The claim:** a proof of the Riemann Hypothesis, with the author saying the method "easily extends much further" to the Generalized Riemann Hypothesis and, he expects, the Extended Riemann Hypothesis.
- **Formal check:** the author says he and Claude "formalized the arguments without assumptions" in Lean and that the formalization is finished. The Lean files are offered as 14 compressed parts on alpo.ge. The note gives no archive size, build instructions or list of axioms used.
- **Claude's role, as the author describes it:** he guided the setup, and Claude "far outpaced" him near the end. The key idea he credits to Claude is a chain of theta lifts whose suggested length was the square root of X for a sum of length X. The note also says the informal draft grew to over 250,000 pages.
- **Caveats in the note:** the argument is "incredibly long at the moment"; it may contain "strange suboptimal choices"; the author says he has little mastery of automorphic forms on higher-rank groups; and parts where Claude is the expert are paraphrased from a summary that "might make zero sense", with the Lean meant to settle the details.
- **Timing and Anthropic:** the note says the timing is "horrible", that the author is "unilaterally responsible", and that an "obvious cynical view, to do with the timing, but it is false". Anthropic's initial public offering priced on 18 November. We found no official Anthropic statement on the note.
- **Verification so far:** Interesting Engineering reports, without naming the project, that an independent effort confirmed the downloaded files match the posted archive and that the main theorem statements compile against Mathlib. We could not confirm that independently. OfficeChai says nobody outside the author's circle has yet confirmed that the archive builds in full or that its final statement says what the Riemann Hypothesis says.
- **Reactions:** the note thanks a number of mathematicians by name. Being thanked is not a review, and we found no named mathematician's public assessment of this claim.
- **Prize rules:** Interesting Engineering notes the Clay Millennium Prize requires publication in an approved peer-reviewed outlet and years of scrutiny, so the problem remains officially unsolved.

## Why it matters

If the Lean files build, contain only standard axioms and state the Riemann Hypothesis faithfully, the claim could be checked by machine rather than by trusting a long human argument. Each of those three conditions is still open today. Until independent mathematicians and Lean experts report back, this is best read as an unreviewed claim from an Anthropic employee about work done with Anthropic's own model.

For readers who use AI tools for research, the practical point is the checking process: what to watch next is whether outside groups rebuild the archive, audit the definitions in it, and publish a readable write-up.

> Disclosure: this article is about a claim involving Claude and an Anthropic employee. Anthropic, the maker of Claude, which was one of the AI tools used to research and draft this article, is a conflict of interest here. Facts come from the note on alpo.ge and two secondary reports, read on 20 November 2026; we have not verified the mathematics.
