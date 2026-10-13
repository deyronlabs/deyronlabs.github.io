---
title: "NVIDIA opens Vera Rubin rack designs and MGX 1.2 to the Open Compute Project at its 2026 summit"
summary: "On 12 October 2026 NVIDIA said it is contributing Vera Rubin rack and compute-tray designs and an MGX 1.2 specification, covering racks up to 250kW, to the Open Compute Project. It also named partner plans from Meta, Cisco, Google and Visionbay; most items have no stated release dates or licenses."
seoTitle: "NVIDIA opens Vera Rubin rack designs to OCP"
seoDescription: "NVIDIA contributes Vera Rubin rack designs and MGX 1.2 (racks up to 250kW) to OCP on 12 Oct 2026; Meta, Cisco, Google named; no dates or licenses given."
lang: en
publishedAt: 2026-10-13T05:50:00Z
entities:
  - NVIDIA
  - Open Compute Project
  - Vera Rubin
  - MGX
  - Meta
  - Cisco
  - Google
  - Visionbay
topics:
  - Infrastructure
  - Hardware
  - Open standards
translationKey: nvidia-opens-vera-rubin-designs-ocp-2026
image: /images/news/nvidia-opens-vera-rubin-designs-ocp-2026-2026-10-12.jpg
imageAlt: "Deyron Labs graphic: NVIDIA contributes Vera Rubin rack designs and MGX 1.2, racks up to 250kW, to the Open Compute Project; no release dates or licenses stated"
sources:
  - title: "OCP Global Summit: Amid Ecosystem Adoption, NVIDIA Opens Vera Rubin Architecture to Help Scale AI Factories Worldwide"
    url: "https://blogs.nvidia.com/blog/ocp-global-summit-vera-rubin-scale-ai-factories/"
    publisher: "NVIDIA Blog"
    primary: true
---

## What happened

On 12 October 2026, at the Open Compute Project (OCP) Global Summit, NVIDIA published a blog post saying it is opening parts of its Vera Rubin data-center architecture to the OCP community. The contributions are Vera Rubin rack and compute-tray designs, delivered through NVIDIA's MGX architecture, and an updated MGX 1.2 specification.

NVIDIA also named related work from partners. Meta is adopting NVIDIA's Spectrum-6 Ethernet switches, Cisco is working on a new optical module form factor, Google plans to support a networking protocol in future NVIDIA hardware, and Visionbay introduced a data-center design built around 800V DC power.

## Key details

Everything below is NVIDIA's own description, from its blog post. We have not seen the underlying specifications.

- **MGX 1.2:** NVIDIA says the specification "extends the open architecture for AI factories" and adds rack-scale liquid cooling, a liquid-cooled 5,000A busbar and native 19-inch equipment support. It says the architecture "supports rack deployments up to 250kW".
- **Vera CPU rack:** a separate rack design specification aimed at agentic AI workloads such as tool calling, orchestration and sandboxed execution.
- **Software:** NVIDIA says it is open-sourcing DSX OS components for network configuration, cluster validation, rack management and bare-metal provisioning. The post points readers to a "DSX AI Factory Github page", but the link in the post leads to a Vera CPU product page, so we could not confirm where the code lives.
- **Facility specifications:** an Open Data Center Specification v0.7, published with AMD, Google and Meta, described as "a unified blueprint for next-generation AI factory facility design". A separate OCP Grid Resilience Specification, with Google, Meta and Microsoft, targets "restoring to near-full load within less than two seconds" after grid disturbances.
- **Networking:** Meta is adopting Spectrum-6 102.4Tb/s switches; NVIDIA says Spectrum-6 "delivers twice the switching capacity and per-lane bandwidth of Spectrum-4". Cisco is co-developing USFP, which NVIDIA says "will provide a path to 400Gb/s-per-lane networking". Google's Falcon Transport support is described as planned for future ConnectX-10 and BlueField products.
- **Not stated:** the post gives no release dates for the specifications or software, no licenses, and no figures behind its "tokens-per-watt" efficiency claims. Several partner items are described as plans, not shipping products.

## Why it matters

AI data centers are now limited as much by power delivery, cooling and networking as by chips. Publishing rack and facility designs through a shared standards body lets server makers and operators build to the same dimensions and power limits, which can lower the cost of building a site for AI hardware.

For people who use AI tools rather than build data centers, the effect is indirect and not immediate: nothing here changes what a model can do today. Open specifications are also not the same as open licenses, and NVIDIA has not yet said under what terms the designs and software can be used, so the practical impact depends on details still to come.

> Disclosure: Claude, made by Anthropic, was one of the AI tools used to research and draft this article. Figures are NVIDIA's own, taken from its 12 October 2026 blog post.
