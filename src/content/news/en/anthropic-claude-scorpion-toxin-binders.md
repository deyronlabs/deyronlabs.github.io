---
title: "Anthropic says Claude designed protein binders for scorpion toxins; 17 of 211 tested designs met its criteria"
summary: "Anthropic reports that an internal Claude research model worked largely autonomously for 64 hours to design minibinders against five scorpion neurotoxins. Two outside labs tested 211 designs and 17 met Anthropic's binding criteria. Anthropic says it has not tested neutralization in cells or animals and does not claim an antivenom."
seoTitle: "Claude designs scorpion-toxin binders"
seoDescription: "Anthropic reported on 20 October 2026 that Claude designed protein binders for scorpion toxins; 17 of 211 lab-tested designs bound, no antivenom claim."
lang: en
publishedAt: 2026-10-21T16:35:00Z
entities:
  - Anthropic
  - Claude
  - Adaptyv Bio
  - Twist Bioscience
  - Citrini Research
topics:
  - Science
  - Research
  - Models
translationKey: anthropic-claude-scorpion-toxin-binders
image: /images/news/anthropic-claude-scorpion-toxin-binders-2026-10-21.jpg
imageAlt: "Deyron Labs graphic: Claude designed scorpion-toxin binders; 318,484 designs generated, 211 lab-tested, 17 met Anthropic's binding criteria, no antivenom claim"
sources:
  - title: "How Claude designed protein binders against scorpion neurotoxins"
    url: "https://www.anthropic.com/research/claude-scorpion-toxin-binder-design"
    publisher: "Anthropic"
    primary: true
---

## What happened

On 20 October 2026 Anthropic published a research post describing how an internal research Claude model, working inside "Claude Science," designed protein minibinders against scorpion neurotoxins. Anthropic says the model worked mainly autonomously, directed by one prompt and four follow-ups developed with the investment research firm Citrini Research, and that Adaptyv Bio and Twist Bioscience tested 211 of the designs.

## Key details

- **Campaign:** over 64 hours, Claude used 12 design tools to generate 318,484 designs and co-folded and screened 553,052 design-toxin pairs, using on the order of 10,000 GPU hours, according to Anthropic. It produced a final list of 180 designs; 31 more were added with its help, for 211 in total.
- **Targets:** five toxins from four scorpion species (Cn2, Ts1, AaH I, AaH II and LqhIII). Anthropic cites 1.2 million or more scorpion stings and more than 3,250 deaths a year.
- **Lab results:** Anthropic says 17 of 211 designs met its criteria for a binder: a hit at both labs in every replicate, every KD at or below 1 µM, and no signal against a control protein. By toxin: 7 for Cn2, 4 for AaH II, 4 for AaH I and 2 for LqhIII. Each binds a single toxin; no multi-toxin design met the criteria for more than one.
- **Strongest binders:** two Cn2 designs showed affinities in the "single-digit nanomolar range" at both labs, and competition experiments suggest they bind near the site of an antibody reported to neutralize Cn2 in mice.
- **Baseline:** 11 of the 60 single-toxin designs were binders (18%), which Anthropic calls consistent with typical protein-design campaigns.
- **Limits stated by Anthropic:** binding was shown only against recombinant toxins; designs were not tested for neutralization in vitro or in live animals. "We do not claim to have produced an antivenom."
- **Release and review:** Anthropic is releasing all 211 designs and their data. Two outside researchers quoted on the page called it a promising first step.

## Why it matters

The result shows an AI model running a long design-and-select loop with limited human direction, with outside labs checking the output. Hit rates and what the designs do against real venom are the open questions; Anthropic itself lists neutralization tests and animal studies as next steps. These are the developer's own findings and have not yet been independently replicated.

> Disclosure: Claude, made by Anthropic, was one of the AI tools used to research and draft this article, and the research it covers is Anthropic's own. Details come from Anthropic's post of 20 October 2026, read on 21 October 2026; the technical report and dataset were not reviewed.
