---
title: "OpenAI releases GPT-Rosalind-6, a biology model with fewer refusals, to approved customers only"
summary: "OpenAI's system card addendum, published 30 October 2026, describes GPT-Rosalind-6, a model for biology, drug discovery and translational medicine that uses the same weights as GPT-6 Astra. It is offered only to approved scientists, institutes, companies and government partners, with fewer refusals on dual-use biology questions."
seoTitle: "OpenAI GPT-Rosalind-6: biology, approved users"
seoDescription: "OpenAI's GPT-Rosalind-6 (30 Oct 2026) is a biology and drug-discovery model with fewer refusals, limited to approved customers."
lang: en
publishedAt: 2026-10-31T17:26:00Z
entities:
  - OpenAI
  - GPT-Rosalind-6
  - GPT-Rosalind-5.5
  - GPT-6 Astra
topics:
  - Models
  - Safety
  - Science
translationKey: openai-gpt-rosalind-6-trusted-access-biology
image: /images/news/openai-gpt-rosalind-6-trusted-access-biology-2026-10-30.jpg
imageAlt: "Deyron Labs graphic: OpenAI GPT-Rosalind-6 for biology, same weights as GPT-6 Astra, approved customers only; MedChemBench v7 49.6% vs 28.9% for Rosalind-5.5, reported by OpenAI"
sources:
  - title: "GPT-Rosalind-6 System Card Addendum"
    url: "https://deploymentsafety.openai.com/gpt-rosalind-6"
    publisher: "OpenAI Deployment Safety Hub"
    primary: true
  - title: "GPT-6 Astra system card"
    url: "https://deploymentsafety.openai.com/gpt-6-astra"
    publisher: "OpenAI Deployment Safety Hub"
    primary: false
---

## What happened

On 30 October 2026 OpenAI published a system card addendum for GPT-Rosalind-6, which it describes as "a frontier reasoning model for biology, drug discovery, and translational medicine." The addendum says the model uses the same weights as GPT-6 Astra, OpenAI's flagship reasoning model, and that no additional training data or post-training was added.

OpenAI offers it as GPT-Rosalind-6 Research to qualified scientists, research institutes, companies and government partners. The page says it is "available only to approved customers." Its stated trade-off is fewer refusals on dual-use biological questions in exchange for restricted access.

## Key details

All figures below are OpenAI's own, from the addendum, at the highest reasoning budget, and have not been independently reproduced.

- **Access:** applicants are reviewed on a legitimate life-sciences mission, a credible use case, governance, and the ability to control access. Non-government applicants go through business verification and compliance screening; select government entities have a trusted-access pathway for approved biosecurity, biosafety, public-health preparedness and biodefense work. OpenAI says approved enterprises must apply least-privilege access and use qualified human review before outputs inform experiments, publications or consequential decisions. It says the page does not broaden eligibility beyond earlier announcements such as the Rosalind Academic Plan.
- **Reported benchmarks, GPT-Rosalind-6 vs GPT-Rosalind-5.5:** MedChemBench v7 49.6% vs 28.9%; GeneBench Pro v13 single-attempt success 37.7% vs 16.7%; LifeSciBench Gold average 61.3% vs 44.0%.
- **Refusals:** on OpenAI's biorisk knowledge test the refusal rate is 9.4% for Rosalind-6, 1.8% for Rosalind-5.5 and 29.2% for GPT-6 Astra, according to the addendum.
- **Risk ratings:** OpenAI says it is treating the launch as High capability in the Biological and Chemical domain, below the Critical threshold, and that none of four Critical bio evaluations met its indicative threshold. It also says it treats the model as Critical in Cybersecurity and below High in AI Self-Improvement, relying on the GPT-6 Astra system card for those two ratings.
- **Safeguards:** the model keeps GPT-6 Astra's standard cyber safeguards, including real-time blocking, and OpenAI says it still trains refusals for requests that would meaningfully enable severe biological weaponization.
- **Evaluation inputs named by OpenAI:** Dyno Therapeutics, Gryphon Scientific, SecureBio and FutureHouse datasets or collaborations.

## Why it matters

This is a general-purpose frontier model released with a different access policy: the weights are the same as the flagship, but a vetted group gets looser behavior on sensitive biology. For readers who use AI tools, nothing changes today, because there is no public sign-up path. The signal is the model: labs are starting to split one underlying model into public and credential-gated versions, with the gate, not extra training, carrying the safety case.

Two things remain unverified. The benchmark gains come from OpenAI's own evaluations, and the Critical cybersecurity rating shows that the model's risk profile is inherited from GPT-6 Astra even though the product is aimed at life scientists. Independent evaluation and details of how access decisions are made would be the next things to watch.

> Disclosure: Claude, made by Anthropic, was used to research and draft this article. Anthropic is a competitor of OpenAI. All facts come from OpenAI's addendum, read on 31 October 2026.
