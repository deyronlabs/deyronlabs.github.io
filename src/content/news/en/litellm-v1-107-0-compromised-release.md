---
title: "LiteLLM says its v1.107.0 release was compromised and carried credential-stealing malware"
summary: "LiteLLM said on 21 October 2026 that its release pipeline was compromised and pushed v1.107.0 to PyPI and Docker with malware that steals credentials and loads remote-code-execution tools. The PyPI package was live for about 1 hour 43 minutes. LiteLLM advises pinning to 1.106.2 or earlier; its investigation is ongoing."
seoTitle: "LiteLLM v1.107.0 compromised: PyPI and Docker"
seoDescription: "LiteLLM said its v1.107.0 release, live on PyPI for about 1h43m on 21 October 2026, carried credential-stealing malware; pin to 1.106.2."
lang: en
publishedAt: 2026-10-22T17:10:00Z
entities:
  - LiteLLM
  - PyPI
topics:
  - Security
  - Agents
translationKey: litellm-v1-107-0-compromised-release
image: /images/news/litellm-v1-107-0-compromised-release-2026-10-22.jpg
imageAlt: "Deyron Labs graphic: LiteLLM v1.107.0 compromised, PyPI package live 11:39 to 13:23 UTC on 21 October 2026, pin to 1.106.2"
sources:
  - title: "Contained: Oct 21, 2026 LiteLLM release v1.107.0 Compromised"
    url: "https://docs.litellm.ai/blog/security-incident-oct-21-2026"
    publisher: "LiteLLM"
    primary: true
---

## What happened

LiteLLM, an open-source gateway many teams use to call different AI model providers through one interface, published a security notice on 21 October 2026. It says its release pipeline was compromised and pushed version 1.107.0 to PyPI and its Docker registry, and that this version "contained compiled malware which steals credentials and loads remote-code execution tools". The notice is marked "Incident contained, investigation in progress" and was last updated at 16:00 UTC on 21 October.

## Key details

All details are from LiteLLM's own notice, checked on 22 October 2026. The investigation is ongoing, so they may change.

- **Affected artifacts:** PyPI `litellm==1.107.0`, live from 11:39:51 to 13:23 UTC; Docker Hub `v1.107.0`, `latest`, `main-latest` and `main-stable`, from 11:46:56 to 14:20 UTC. GHCR tags were unavailable by 13:51 UTC.
- **What to do (LiteLLM):** "please pin your version to 1.106.2 or any explicit version published prior to now."
- **Not affected:** LiteLLM says customers running its private enterprise release were not impacted.
- **Timeline inconsistency:** the overview says the compromise began "at 4:00 AM PST October 21", which is 12:00 UTC, while the UTC timeline starts at 10:08:29 UTC and the PyPI upload is at 11:39:51. The notice does not reconcile these.
- **Credit and next steps:** LiteLLM credits a researcher for helping detect the incident, and mentions an embargoed fix whose disclosure date is scheduled for 27 October. The notice gives no CVE number and no count of affected installs.

## Why it matters

Gateways like LiteLLM sit next to API keys for several AI providers, which is why a credential-stealing release is more serious than a bug in a typical library. Anyone who installed or pulled the affected version, including through an unpinned `latest` Docker tag, during the windows above should check which version they ran.

Because the malware is described as stealing credentials, treating keys and secrets in an affected environment as exposed and rotating them is a reasonable precaution; that is our reading, not an instruction from LiteLLM, whose notice only gives the pinning advice. Pinning exact versions and verifying release artifacts are the standard defences against this kind of supply-chain incident.

> Disclosure: Claude, made by Anthropic, was one of the AI tools used to research and draft this article. All facts are attributed to LiteLLM's notice and have not been independently verified.
